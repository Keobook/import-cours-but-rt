#!/bin/env python3

from io import BytesIO
from os import (
    get_terminal_size, PathLike, mkdir, system
)
import os
from tkinter import (
    Tk, ### Window Frames
    Canvas, Frame, Menu, Entry, Button, Scale, ### In-App Frames
    N, E, S, W,  ### The Constants related to the positioning
    Event as TkEvent, ### Tkinter Events
    StringVar, IntVar, ### Tkinter vars
    filedialog as TkFileDialog ### OS-dependant
)
from typing import Union, Callable, Tuple, List
from subprocess import call
from PIL import Image, EpsImagePlugin

### Internal imports
from network_equipment import NetworkEquipment
from network_link import NetworkLink
from utils import get_absolute_current_path


class NetApp(Tk):
    def __init__(self, name: str, base_size: Tuple[int, int], title: str = ""):
        """Create a Specific App for the Networks and Telecommunications
        using tkinter.

        Args:
            name (str): The displayed name of the app
            base_size (Tuple[int, int]): The default size of the window
            title (str, optional): The title of the window. Defaults to `name`.
        """
        super().__init__(name, name)

        self.name = name
        self.x_size = base_size[0]
        self.y_size = base_size[1]
        self.app_title = title

        if self.app_title == "":
            self.app_title = self.name

        ### The mouse coordinates
        self.mouse_coords = (0, 0)

        ### Ther term size
        self.term_size_x, self.term_size_y = get_terminal_size()

        self.equipments = {}
        self.equipment_nbr = 0
        self.reverse_equipments = {}

        self.mainframe = Frame(self, height=self.x_size, width=self.y_size)
        self.playground = Canvas(self.mainframe, bg="white", width=self.x_size, height=self.y_size)
        self.focused_tag = 0

        ### Let's define the menus
        self.master_menu = None
        self.rightclick_menu = None
        self.menus = {}
        self.__setMenuAndActions()
        self.__setRightClickMenuAndActions()

        ### Let's configure the callable
        self.popup: PopUpMessage = PopUpMessage
        self.popup_entry_var = ""

        ### Let's configure the link states
        self.current_link_state = "idle" ### Will either be 'idle' or 'active'
        self.current_link_root = 0
        self.link_binding = None
        self.escape_sequence = None
        self.is_link_fragmented = False
        ### ID-based dictionary, works the same way as self.reverse_equipments
        ### (i.e. It's only used to retrieve elements from IDs)
        self.links = {}

        ### Set the export-related variables
        self.temp_export_file = self.app_title + ".eps"
        self.final_export = self.app_title + ".png"

        ### Let's set the display
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.playground.grid(column=1, row=1, rowspan=self.y_size, columnspan=self.x_size)

        ### Bind some basics events to the root window
        self.bind("<Motion>", lambda event: self.__getMouseCoords(event))
        self.bind("<KeyPress-Control_L>", lambda _: self.__setLinkSegmentation(True))
        self.bind("<KeyPress-Control_R>", lambda _: self.__setLinkSegmentation(True))
        self.bind("<KeyRelease-Control_L>", lambda _: self.__setLinkSegmentation(False))
        self.bind("<KeyRelease-Control_R>", lambda _: self.__setLinkSegmentation(False))

    def __setLinkSegmentation(self, value: bool):
        print("IS_Fragmented is now:", value)
        self.is_link_fragmented = value

    def __getMouseCoords(self, event: TkEvent):
        self.mouse_coords = (event.x, event.y)

    def __setRightClickMenuAndActions(self):
        self.rightclick_menu = Menu(self, tearoff=0)
        self.rightclick_menu.add_command(label="Change Name", command=lambda: self.handleChangeOfEquipmentName())
        self.rightclick_menu.add_command(label="Change Icon", command=lambda: self.handleChangeOfEquipmentIcon())
        self.rightclick_menu.add_command(label="Create Link", command=lambda: self.handleLinkCreation())
        self.rightclick_menu.add_command(label="Change Ports", command=lambda: self.handleChangeOfEquipmentPorts())

    def __createNewMenu(self, title: str, return_title: bool = True) -> Union[Tuple[str, Menu], Menu]:
        """A private method to create a new menu and configure it internally.

        Args:
            title (str): The name to display, it should be pretty explicit.
            return_title (bool, optional): Specifies if you want to return the title. Defaults to True.

        Returns:
            Union[Tuple[str, Menu], Menu]: Returns either (title, Menu_Object) or Menu_Object
        """
        new_menu = Menu(self.master_menu, tearoff=0)

        self.menus[title] = {
            "name": title,
            "object": new_menu,
            "commands": {},
            "menus": {},
        }

        self.master_menu.add_cascade(label=title, menu=new_menu)

        if not return_title:
            return new_menu
        else:
            return (title, new_menu)

    def __createNewCommand(self, parent_menu: Tuple[str, Menu], title: str, command: Callable, return_title: bool = False) -> Union[None, str]:
        """A private method to create a New Command inside a parent menu and configure it internally.

        Args:
            parent_menu (Tuple[str, Menu]): The parent menu of the command (i.e. where you want the command to appear).
            title (str): The name of the command.
            command (Callable): The callable function
            return_title (bool, optional): `True` if you want this method to return the title. Defaults to False.

        Returns:
            Union[None, str]: Either return nothing or the title of the command.
        """
        parent_menu_label: str = parent_menu[0]
        parent_menu_object: Menu = parent_menu[1]

        parent_menu_object.add_command(label=title, command=command)

        ### Let's update the menus dictionary
        self.menus[parent_menu_label]["commands"].update({title: command})

        if not return_title:
            return None
        else:
            return title

    def __setMenuAndActions(self):
        """A private method to set the different menus and Actions of the Tkinter Window."""
        self.master_menu = Menu(self)
        self.config(menu=self.master_menu)

        ### File Menu
        file_menu = self.__createNewMenu("File")
        if os.name == "nt":
            self.__createNewCommand(file_menu, "Export into PNG", self.export_png)

        ### Edit Menu
        edit_menu = self.__createNewMenu("Edit")
        self.__createNewCommand(edit_menu, "Insert Switch", lambda: self.addEquipment("switch"))
        self.__createNewCommand(edit_menu, "Insert Router", lambda: self.addEquipment("router"))
        self.__createNewCommand(edit_menu, "Insert Laptop", lambda: self.addEquipment("pc"))
        self.__createNewCommand(edit_menu, "Insert Mobile", lambda: self.addEquipment("mobile"))

        ### While menus are nice, hotkeys are better!
        self.__createNetAppBindings()

    def __createNetAppBindings(self):
        self.bind("<a>", lambda _: self.addEquipment("switch"))
        self.bind("<e>", lambda _: self.addEquipment("router"))
        self.bind("<q>", lambda _: self.addEquipment("pc"))
        self.bind("<d>", lambda _: self.addEquipment("mobile"))

    def __deleteNetAppBindings(self):
        self.unbind("<a>")
        self.unbind("<e>")
        self.unbind("<q>")
        self.unbind("<d>")

    def __configureEquipment(self, equipment_tag: int) -> None:
        """A private method to configure the equipment with the given tag.

        Args:
            equipment_tag (int): The canvas `tagOrId` of the equipment
        """

        ### Create the bindings of the equipment
        self.__createBindingsOnEquipment(equipment_tag)

        ### Always set the last element on top
        self.playground.tag_raise(equipment_tag)

    def __createBindingsOnEquipment(self, equipment_tag: int) -> None:
        self.equipments[self.equipment_nbr]["bindings"].update(
            {
                "left-click": {
                    "id": self.playground.tag_bind(equipment_tag, "<Button-1>", lambda event: self.startDragFocus(event)),
                    "command": self.startDragFocus,
                },
                "left-click-motion": {
                    "id": self.playground.tag_bind(equipment_tag, "<B1-Motion>", lambda event: self.endDragFocus(event)),
                    "command": self.endDragFocus,
                },
                "double-left-click": {
                    "id": self.playground.tag_bind(equipment_tag, "<Double-Button-1>", lambda event: self.deleteItem(event)),
                    "command": self.deleteItem,
                },
                "right-click": {
                    "id": self.playground.tag_bind(equipment_tag, "<Button-3>", lambda event: self.popRightClickMenu(event)),
                    "command": self.popRightClickMenu,
                }
            }
        )

        ### For the simplicity of use, we're duplicating the entries
        self.equipments[equipment_tag]["bindings"] = self.equipments[self.equipment_nbr]["bindings"]

    def __deleteBindingsOfEquipment(self, equipment_tag: int) -> None:
        self.equipments[self.equipment_nbr]["bindings"].update(
            {
                "left-click": {
                    "id": self.playground.tag_unbind(equipment_tag, "<Button-1>"),
                    "command": self.startDragFocus,
                },
                "left-click-motion": {
                    "id": self.playground.tag_unbind(equipment_tag, "<B1-Motion>"),
                    "command": self.endDragFocus,
                },
                "double-left-click": {
                    "id": self.playground.tag_unbind(equipment_tag, "<Double-Button-1>"),
                    "command": self.deleteItem,
                },
                "right-click": {
                    "id": self.playground.tag_unbind(equipment_tag, "<Button-3>"),
                    "command": self.popRightClickMenu,
                }
            }
        )

        ### For the simplicity of use, we're duplicating the entries
        self.equipments[equipment_tag]["bindings"] = self.equipments[self.equipment_nbr]["bindings"]

    def __prepareDeletionOfEquipment(self, equipment_tag: int) -> None:
        """A private method to unconfigure the equipment with the given tag.

        Args:
            equipment_tag (int): The canvas `tagOrId` of the equipment
        """

        self.equipments[self.reverse_equipments[equipment_tag]] = None

        ### Always set the last element on the bottom layer
        self.playground.tag_lower(equipment_tag)

    def run(self):
        self.title(self.app_title)
        self.geometry(f"{self.x_size}x{self.y_size}")
        try:
            self.mainloop()
        except KeyboardInterrupt:
            self.destroy()

    def addEquipment(self, type) -> None:
        """Add the given equipment to the playground

        Args:
            type (str): Either `switch`, `router`, `pc`, `mobile`. (All entries are going to be lowercased)

        Raises:
            ValueError: You gave an unsupported type.
        """
        self.equipment_nbr += 1

        default_coords = (
            self.x_size // 2,
            self.y_size // 2,
        )  ### We're getting the center of the current window

        new_equipment = NetworkEquipment(type)
        canvas_tag = self.playground.create_image(
            default_coords, image=new_equipment.icon
        )
        equipment_label = self.playground.create_text(
            (default_coords[0], default_coords[1] + new_equipment.icon_size[1] // 2),
            text=new_equipment.name,
        )

        ### Update the main array with our internal equipment ID as key
        self.equipments.update(
            {
                self.equipment_nbr: {
                    "item": new_equipment,
                    "canvas_id": canvas_tag,
                    "bindings": {},
                    "dependencies": {"label": equipment_label, "links": []},
                }
            }
        )

        ### Create a duplicate entry with the same key as the reverse array
        ### It should only be used at a last resort for us to pick equipment
        ### data.
        self.equipments.update({
            canvas_tag: self.equipments[self.equipment_nbr]
        })

        ### Set a `reverse` array with the Canvas tag as key
        self.reverse_equipments.update({canvas_tag: self.equipment_nbr})

        self.__configureEquipment(canvas_tag)

    ### Drag & Drop
    def startDragFocus(self, event: TkEvent):
        x, y = event.x, event.y

        self.focused_tag = self.playground.find_closest(x, y)[0]

    def endDragFocus(self, event: TkEvent):
        widget: Canvas = event.widget
        x = event.x if widget.winfo_x() + event.x <= self.x_size else self.x_size
        y = event.y if widget.winfo_y() + event.y <= self.y_size else self.y_size

        ### We're dividing by 2 the icon size to find the difference
        ### between the mouse position and the center of the icon.
        difference_mouse_icon = NetworkEquipment.icon_size[0] // 2
        to_move_x = x - difference_mouse_icon
        to_move_y = y - difference_mouse_icon

        self.playground.moveto(
            self.focused_tag, to_move_x, to_move_y
        )

        ### After moving the icon, we need to go through its dependency list to move them
        self.updateEquipmentDependencies(self.focused_tag, x = x, y = y, difference=difference_mouse_icon)

    def updateEquipmentDependencies(self, equipment_id: int, x: int = 0, y:int = 0, difference: int = 0, state: str="update") -> None:
        """Updates the equipment dependencies, both links and labels.
        With the `state` parameter given to `deletion`, it can also delete the said equipment.

        Args:
            equipment_id (int): The selected equipment ID or Tag.
            x (int, optional): The x coordinate to update to. Defaults to 0.
            y (int, optional): The y coordiante to update to. Defaults to 0.
            difference (int, optional): If there is a difference to apply in the movement of the label. Defaults to 0.
            state (str, optional): Controls the behavior of the update, can be either `update` or `deletion`. Defaults to "update".
        """

        if state != "deletion":
            if equipment_id in self.reverse_equipments.keys():
                dependencies = self.equipments[self.reverse_equipments[equipment_id]]["dependencies"]
                dependent_label = dependencies["label"]

                self.playground.moveto(dependent_label, x - (difference // 2), y + difference)

                dependent_links: List[NetworkLink] = dependencies["links"]

                for i in range(0, len(dependent_links)):
                    link_object = dependent_links[i]

                    if link_object.start_equipment == equipment_id:
                        link_object.updateStartCoords(x, y)
                    elif link_object.end_equipment == equipment_id:
                        link_object.updateEndCoords(x, y)
                    else:
                        ### The current nearest tag is not one of the registered links
                        print("I'm in this else situation")

                    link_object.update(self.links)
            else:
                self.createCanvasEquipmentIDWarning(equipment_id)
        else: ### We're deleting the dependencies of the element
            print("Dependency:", equipment_id, self.reverse_equipments[equipment_id], self.equipments[self.reverse_equipments[equipment_id]], self.equipments)
            dependencies = self.equipments[self.reverse_equipments[equipment_id]]["dependencies"]
            dependent_label: int = dependencies["label"]

            self.playground.delete(dependent_label)

            dependent_links: List[NetworkLink] = dependencies["links"]

            for i in range(0, len(dependent_links)):
                link_object: NetworkLink = dependent_links[i]

                self.deleteLink(None, is_called_after_event_processing=True, link_id=link_object.tag)


    ### Double clicks
    def deleteItem(self, event: TkEvent):
        x, y = event.x, event.y

        selected_tag = self.playground.find_closest(x, y)[0]

        self.updateEquipmentDependencies(selected_tag, state="deletion")
        self.__prepareDeletionOfEquipment(selected_tag)
        self.playground.delete(selected_tag)

    def deleteLink(self, event: TkEvent, is_called_after_event_processing: bool = False, link_id: int = 0):

        if not is_called_after_event_processing:
            x, y = event.x, event.y

            selected_link: int = self.playground.find_closest(x, y)[0]
        else:
            selected_link: int = link_id

        current_link: NetworkLink = self.links[selected_link]

        if current_link.is_fragmented:
            current_link.cleanSegmentedLinkContent()
        else:
            current_link.cleanDiagonalLinkContent()

        ### We remove the link from the NetworkEquipment POV
        current_holder: NetworkEquipment = self.equipments[self.reverse_equipments[current_link.start_equipment]]["item"]
        current_holder.removeLink(current_link)

        ### We should remove the link from the other side, too
        remote_holder: NetworkEquipment = self.equipments[self.reverse_equipments[current_link.end_equipment]]["item"]
        remote_holder.removeLink(current_link)

        if not is_called_after_event_processing:

            self.current_link_state = "idle"
            self.rightclick_menu.entryconfigure(2, label="Create link", command = lambda: self.handleLinkCreation())
            self.current_link_root = 0

            ### We're unbinding the callback to the mouse movement
            self.playground.unbind("<Motion>", self.link_binding)
            self.unbind("<KeyPress-Escape>", self.escape_sequence)
        del current_link

    ### Right Clicks
    def popRightClickMenu(self, event: TkEvent):
        x, y = event.x_root, event.y_root

        if self.rightclick_menu is not None:
            self.rightclick_menu.tk_popup(x, y)

    def handleChangeOfEquipmentName(self):
        ### The user shouldn't have changed of active tag between
        ### the <KeyRelease> event and the call of this function
        ### so we should be able to safely use `self.focused_tag`.

        x, y = self.mouse_coords
        current_equipment = self.playground.find_closest(x, y)[0]

        self.popup(self, "entry", self.mouse_coords, self.__deleteNetAppBindings, self.__createNetAppBindings, lambda name: self.setEquipmentName(current_equipment, name))

        if self.popup_entry_var == "":
            self.popup_entry_var = "[EMPTY]"

        if self.focused_tag != 0:

            ### We are still checking in case he acted on another equipment
            ### than the last selected
            if self.focused_tag == current_equipment:
                self.setEquipmentName(self.focused_tag, self.popup_entry_var)
            else:
                ### The user changed equipment from the last interaction
                self.setEquipmentName(current_equipment, self.popup_entry_var)
        else:
            self.setEquipmentName(current_equipment, self.popup_entry_var)

    def handleChangeOfEquipmentIcon(self):
        ### The user shouldn't have changed of active tag between
        ### the <KeyRelease> event and the call of this function
        ### so we should be able to safely use `self.focused_tag`.

        x, y = self.mouse_coords
        equipment_tag = self.playground.find_closest(x, y)[0]

        try:
            icon_path = TkFileDialog.askopenfilename()

            if self.focused_tag != 0:
                if self.focused_tag == equipment_tag:
                    self.setEquipmentIcon(self.focused_tag, icon_path)
                else:
                    self.setEquipmentIcon(equipment_tag, icon_path)
            else:
                self.setEquipmentIcon(equipment_tag, icon_path)
        except Exception:
            pass

    def handleLinkCreation(self, ending: bool = False):
        ### The user shouldn't have changed of active tag between
        ### the <KeyRelease> event and the call of this function
        ### so we should be able to safely use `self.focused_tag`.

        x,y = self.mouse_coords
        equipment_tag = self.playground.find_closest(x, y)[0]

        ### We are still checking in case he acted on another equipment
        ### than the last selected
        if self.focused_tag == equipment_tag:
            self.setEquipmentsLink(self.focused_tag, ending)
        else:
            self.setEquipmentsLink(equipment_tag, ending)

    def handleChangeOfEquipmentPorts(self):
        x,y = self.mouse_coords
        equipment_tag = self.playground.find_closest(x, y)[0]
        equipment: NetworkEquipment = self.equipments[equipment_tag]["item"]

        self.popup(self, "int-entry", self.mouse_coords, equipment.links_max_nbr, self.__deleteNetAppBindings, self.__createNetAppBindings, lambda number: self.setEquipmentsPortsNumber(equipment_tag, number))

        ### We are still checking in case he acted on another equipment
        ### than the last selected
        if self.focused_tag == equipment_tag:
            self.setEquipmentsPortsNumber(self.focused_tag, self.popup_entry_var)
        else:
            self.setEquipmentsPortsNumber(equipment_tag, self.popup_entry_var)

    ### Hovers
    def highlightTag(self, event: TkEvent, fragmented: bool = False):
        x, y = event.x, event.y

        try:
            print(self.playground.find_closest(x, y)[0])
            if fragmented:
                link_obj: NetworkLink = self.links[self.playground.find_closest(x, y)[0]]
                for segment_id in link_obj.segments:
                    self.playground.itemconfigure(segment_id, fill="red")
            else:
                self.playground.itemconfigure(self.playground.find_closest(x, y)[0], fill="red")

        except KeyError as err:
            link_id: NetworkLink = self.playground.find_closest(x, y)[0]
            print(f"KeyError Exception on Highlight: {err}", link_id, True if link_id in self.links else False)
            print(f"\nself.links: \n{self.links}")
            print("-"*self.term_size_x)

    def unhighlightTag(self, event: TkEvent, fragmented: bool = False):
        x, y = event.x, event.y

        try:
            if fragmented:
                link_obj: NetworkLink = self.links[self.playground.find_closest(x, y)[0]]
                for segment_id in link_obj.segments:
                    self.playground.itemconfigure(segment_id, fill="black")
            else:
                self.playground.itemconfigure(self.playground.find_closest(x, y)[0], fill="black")
        except Exception as err:
            print(f"Exception on Unhighlight: {err}")

    ### Setters
    def setEquipmentName(self, equipment_tag: int, name: str):
        if name == "":
            name = "[EMPTY]"

        if equipment_tag not in self.reverse_equipments.keys():
            equipment_object: NetworkEquipment = self.equipments[equipment_tag]["item"]
        else:
            equipment_holder = self.reverse_equipments[equipment_tag]
            equipment_object: NetworkEquipment = self.equipments[equipment_holder]["item"]
        equipment_object.setName(name)

        equipment_label = self.equipments[equipment_holder]["dependencies"]["label"]

        self.playground.itemconfigure(equipment_label, text=equipment_object.name)

    def setEquipmentIcon(self, equipment_tag: int, new_icon: Union[str, PathLike]):
        equipment_holder = self.reverse_equipments[equipment_tag]
        equipment_object: NetworkEquipment = self.equipments[equipment_holder]["item"]
        equipment_object.setIcon(new_icon)

        self.playground.itemconfigure(equipment_tag, image=equipment_object.icon)

    def setEquipmentsLink(self, equipment_tag: int, ending: bool = False, panicked: bool = False):
        if equipment_tag not in self.reverse_equipments.keys():
            base: dict = self.equipments[self.reverse_equipments[equipment_tag]]
        else:
            base: dict = self.equipments[equipment_tag]
        equipment: NetworkEquipment = base["item"]
        links: dict = base["dependencies"]["links"]
        x, y = self.mouse_coords

        if self.current_link_state == "idle":
            print(f"Equipment {equipment.name}:", equipment.isOpenToLinkCreation(), equipment.getLinksNumber(True), equipment.links)
            if equipment.isOpenToLinkCreation():
                current_link = NetworkLink(x, y, self.playground, equipment_tag, self.is_link_fragmented)

                current_link.draw(self.links)
                links.append(current_link)

                ### We're adding this link to the links of the equipment
                equipment.addLink(current_link)

                self.current_link_state = "active"
                self.rightclick_menu.entryconfigure(2, label="Set link", command = lambda: self.handleLinkCreation(True))
                self.current_link_root = equipment_tag

                ### We're binding the callback to the mouse movement
                self.link_binding = self.playground.bind("<Motion>", lambda _: self.setEquipmentsLink(self.current_link_root))

                ### We're binding some other useful events
                current_link.addBinding("<Double-Button-1>", lambda event: self.deleteLink(event), lambda event: self.deleteLink(event, True))
                current_link.addBinding("<Enter>", lambda event: self.highlightTag(event), lambda event: self.highlightTag(event, True))
                current_link.addBinding("<Leave>", lambda event: self.unhighlightTag(event), lambda event: self.unhighlightTag(event, True))

                ### We're binding an escape sequence to the whole app to escape any started work
                ### We're binding to the root widget because it otherwise escapes the binding and is never
                ### sent to the playground.
                self.escape_sequence = self.bind("<KeyPress-Escape>", lambda _: self.setEquipmentsLink(self.current_link_root, panicked=True))
            else:
                self.createCanvasLinksWarning(equipment.name)


        elif self.current_link_state == "active":
            old_base: dict = self.equipments[self.reverse_equipments[self.current_link_root]]
            old_equipment: NetworkEquipment = old_base["item"]
            old_links: dict = old_base["dependencies"]["links"]
            old_links_object: NetworkLink = old_links[-1]
            x, y = old_links_object.start_coords
            x1, y1 = self.mouse_coords

            if not old_links_object.setEndCoords(x1, y1, equipment_tag):
                old_links_object.updateEndCoords(x1, y1)

            if not ending:
                old_links_object.updateFragmentationStatus(self.is_link_fragmented)
                old_links_object.update(self.links)
            else:
                end_equipment: NetworkEquipment = self.equipments[self.reverse_equipments[equipment_tag]]["item"]
                print(f"End-Equipment {end_equipment.name}:", end_equipment.isOpenToLinkCreation(), end_equipment.getLinksNumber(True), end_equipment.links)

                if end_equipment is not old_equipment:

                    if end_equipment.isOpenToLinkCreation():
                        end_equipment.addLink(old_links_object)
                        old_links_object.setEndCoords(x1, y1, equipment_tag, True)
                        old_links_object.updateFragmentationStatus(self.is_link_fragmented)
                        old_links_object.update(self.links)

                        links.append(old_links_object)

                        self.current_link_state = "idle"
                        self.rightclick_menu.entryconfigure(2, label="Create link", command = lambda: self.handleLinkCreation())
                        self.current_link_root = 0

                        ### We're unbinding the callback to the mouse movement
                        self.playground.unbind("<Motion>", self.link_binding)
                    else:
                        self.createCanvasLinksWarning(end_equipment.name)
                else:
                    self.createCanvasSingularLinksWarning(end_equipment.name)

        if panicked:
            links_obj: NetworkLink = links[-1]
            if links_obj.is_fragmented:
                links_obj.cleanSegmentedLinkContent()
            else:
                links_obj.cleanDiagonalLinkContent()

            self.current_link_state = "idle"
            self.rightclick_menu.entryconfigure(2, label="Create link", command = lambda: self.handleLinkCreation())
            self.current_link_root = 0

            ### We're unbinding the callback to the mouse movement
            self.playground.unbind("<Motion>", self.link_binding)
            self.unbind("<KeyPress-Escape>", self.escape_sequence)
            to_remove: NetworkLink = links.pop(-1)
            equipment.removeLink(to_remove)
            del links_obj

    def setEquipmentsPortsNumber(self, equipment_tag: int, ports_number: int):
        if equipment_tag not in self.reverse_equipments:
            equipment: NetworkEquipment = self.equipments[equipment_tag]["item"]
        else:
            equipment: NetworkEquipment = self.equipments[self.reverse_equipments[equipment_tag]]["item"]

        equipment.updateMaxLinks(ports_number)

    ### Internal PopUps Utils
    def createCanvasLinksWarning(self, equipment_name: str):
        CanvasPopUpWarning(self.playground, f"You have too many links on {equipment_name}!")

    def createCanvasSingularLinksWarning(self, equipment_name: str) -> None:
        CanvasPopUpWarning(self.playground, f"You can't simply link {equipment_name} on itself!")

    def createCanvasEquipmentIDWarning(self, equipment_id: int):
        ### First of all, get the name of the equipment
        equipment_with_issues: NetworkEquipment = self.equipments[equipment_id]["item"]
        CanvasPopUpWarning(self.playground, f"Sorry but an unexpected issue has been raised with {equipment_with_issues.name}!")


    ### Export area
    def export_png(self):

        abs_path = get_absolute_current_path()

        try:
            if EpsImagePlugin.gs_windows_binary is not None:
                eps = self.playground.postscript(colormode="color")
                img = Image.open(BytesIO(bytes(eps, 'ascii')))
                img.save(self.final_export)
            else:
                raise ValueError
        except OSError:
            ### We don't have the Ghostscript executable in our path
            ### We're then going to downloading it, configuring it and retry once again

            if not os.path.exists(f"{abs_path}bin/"):
                mkdir(f"{abs_path}bin/")

            system(f"cd {abs_path}bin/")

            if os.name == "nt":
                if not os.path.exists("./gs10021w64.exe"):
                    call("pwsh -Command Invoke-WebRequest https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs10021/gs10021w64.exe -OutFile ./gs10021w64.exe", shell=True)
                    call("./gs10021w64.exe")

                EpsImagePlugin.gs_windows_binary = "C:\\Program Files\\gs\\gs10.02.1\\bin\\gswin64c"

            self.export_png()

        self.createCanvasSuccessWarning("Current playground successfully exported into png!")

class PopUpMessage:
    def __init__(self, root_frame: NetApp, type: str, mouse_position: Tuple[int], *args, **kwargs):
        self.popup = None

        if type == "entry":
            self.popup = CanvasPopUpEntry(root_frame, root_frame.playground, mouse_position, *args, **kwargs)
        elif type == "int-entry":
            self.popup = CanvasPopUpIntEntry(root_frame, root_frame.playground, mouse_position, *args, **kwargs)

class CanvasPopUpWarning:
    def __init__(self, root_canvas: Canvas, text: str) -> None:
        text_to_disappear = root_canvas.create_text(root_canvas.winfo_width() // 2, (10/100)*root_canvas.winfo_height(), text=text, fill="red")
        root_canvas.after(1500, lambda: root_canvas.delete(text_to_disappear))


class CanvasPopUpEntry:
  def __init__(self, root_app: NetApp, root_frame: Canvas, mouse_position: Tuple[int, int], bindingsDown: Callable, bindingsUp: Callable, updateLabelName: Callable):
    self.app = root_app
    self.root = root_frame
    self.var_linked = root_app.popup_entry_var

    self.deleteBindings: Callable = bindingsDown
    self.createBindings: Callable = bindingsUp
    self.updateName: Callable = updateLabelName

    self.width = self.root.winfo_width()
    self.height = self.root.winfo_height()

    self.x_pos, self.y_pos = mouse_position

    self.frame = Frame(self.root, width=self.width, height=self.height)

    self.content = StringVar(self.frame)

    self.entry_widget = Entry(self.frame, textvariable=self.content, background="grey", width=50, takefocus=True)
    self.submit_button = Button(self.frame, text="Submit", command=lambda: self.close())

    print("Current size inside child window:", self.width, self.height, self.entry_widget.winfo_width())

    ### First of all, let's unbind the hotkeys to let the user type in the entry
    self.deleteBindings()

    self.frame.grid(column=0, row=0)
    self.entry_widget.grid(column=0, row=0)
    self.submit_button.grid(column=1, row=0)

    self.entry_widget.focus()

    self.toplevel = root_frame.create_window(self.x_pos, self.y_pos+10, window=self.frame, anchor="center")
    self.root.update()


  def close(self):
    ### We're exporting the value out of this object
    self.var_linked = self.content.get()
    self.updateName(self.var_linked)

    ### We're destroying the widgets
    self.entry_widget.destroy()
    self.submit_button.destroy()
    self.frame.destroy()

    ### We're deleting the StringVar
    del self.content

    ### We're deleting the canvas reference
    self.root.delete(self.toplevel)

    ### At the end, create the new hotkeys to let the user use them
    self.createBindings()

class CanvasPopUpIntEntry:
  def __init__(self, root_app: NetApp, root_frame: Canvas, mouse_position: Tuple[int, int], max: int, bindingsDown: Callable, bindingsUp: Callable, updatePortsNumber: Callable):
    self.app = root_app
    self.root = root_frame
    self.var_linked = root_app.popup_entry_var

    self.deleteBindings: Callable = bindingsDown
    self.createBindings: Callable = bindingsUp
    self.updateNumber: Callable = updatePortsNumber

    self.width = self.root.winfo_width()
    self.height = self.root.winfo_height()

    self.x_pos, self.y_pos = mouse_position

    self.frame = Frame(self.root, width=self.width, height=self.height)

    self.content = IntVar(self.frame)

    self.entry_widget = Scale(self.frame, from_=0, to=max, variable=self.content, background="grey", takefocus=True)
    self.submit_button = Button(self.frame, text="Submit", command=lambda: self.close())

    print("Current size inside child window:", self.width, self.height, self.entry_widget.winfo_width())

    ### First of all, let's unbind the hotkeys to let the user type in the entry
    self.deleteBindings()

    self.frame.grid(column=0, row=0)
    self.entry_widget.grid(column=0, row=0)
    self.submit_button.grid(column=1, row=0)

    self.entry_widget.focus()

    self.toplevel = root_frame.create_window(self.x_pos, self.y_pos+10, window=self.frame, anchor="center")
    self.root.update()


  def close(self):
    ### We're exporting the value out of this object
    self.var_linked = self.content.get()
    self.updateNumber(self.var_linked)

    ### We're destroying the widgets
    self.entry_widget.destroy()
    self.submit_button.destroy()
    self.frame.destroy()

    ### We're deleting the StringVar
    del self.content

    ### We're deleting the canvas reference
    self.root.delete(self.toplevel)

    ### At the end, create the new hotkeys to let the user use them
    self.createBindings()


if __name__ == "__main__":
    t = NetApp("Net-App", (800, 800))
    t.run()