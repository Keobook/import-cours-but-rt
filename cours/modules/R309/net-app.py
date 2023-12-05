#!/bin/env python3

from os import (
    PathLike, system, get_terminal_size, getcwd
)
from tkinter import (
    Tk, Toplevel, ### Window Frames
    Canvas, Frame, Menu, Entry, Button, ### In-App Frames
    N, E, S, W,  ### The Constants related to the positioning
    Event as TkEvent, ### Tkinter Events
    StringVar, ### Tkinter vars
    filedialog as TkFileDialog ### OS-dependant
)
from typing import Iterator, Union, Callable, Tuple, List

### As PIL is now imported from its fork, Pillow
### We need to check if the current Python executable
try:
    from PIL import ImageTk, Image
except ImportError:
    try:
        system("pip3 install Pillow")
    except Exception: ### Generic-based Exception
        system("python3 -m pip --upgrade pip")
        system("python3 -m pip install --upgrade Pillow")

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
        self.popup = PopUpMessage
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
        self.__createNewCommand(file_menu, "Export into PNG", self.export_png)

        ### Edit Menu
        edit_menu = self.__createNewMenu("Edit")
        self.__createNewCommand(edit_menu, "Insert Switch", lambda: self.add_equipment("switch"))
        self.__createNewCommand(edit_menu, "Insert Router", lambda: self.add_equipment("router"))
        self.__createNewCommand(edit_menu, "Insert Laptop", lambda: self.add_equipment("pc"))
        self.__createNewCommand(edit_menu, "Insert Mobile", lambda: self.add_equipment("mobile"))

        ### While menus are nice, hotkeys are better!
        self.bind("<a>", lambda _: self.add_equipment("switch"))
        self.bind("<e>", lambda _: self.add_equipment("router"))
        self.bind("<q>", lambda _: self.add_equipment("pc"))
        self.bind("<d>", lambda _: self.add_equipment("mobile"))

    def __configureEquipment(self, equipment_tag: int) -> None:
        """A private method to configure the equipment with the given tag.

        Args:
            equipment_tag (int): The canvas `tagOrId` of the equipment
        """

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

        ### Always set the last element on top
        self.playground.tag_raise(equipment_tag)

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

    def add_equipment(self, type) -> None:
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

        self.reverse_equipments.update({canvas_tag: self.equipment_nbr})

        self.__configureEquipment(canvas_tag)

        with open("./entities.json", "wt", encoding="utf-8") as fout:
            fout.write(f"{self.equipments}")

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
        dependencies = self.equipments[self.reverse_equipments[self.focused_tag]]["dependencies"]
        dependent_label = dependencies["label"]

        self.playground.moveto(dependent_label, x - (difference_mouse_icon // 2), y + difference_mouse_icon)

        dependent_links: List[NetworkLink] = dependencies["links"]

        for i in range(0, len(dependent_links)):
            link_object = dependent_links[i]

            if link_object.start_equipment == self.focused_tag:
                link_object.updateStartCoords(x, y)
            elif link_object.end_equipment == self.focused_tag:
                link_object.updateEndCoords(x, y)
            else:
                ### The current nearest tag is not one of the registered links
                print("I'm in this else situation")

            link_object.update(self.links)

    ### Double clicks
    def deleteItem(self, event: TkEvent):
        x, y = event.x, event.y

        selected_tag = self.playground.find_closest(x, y)[0]
        self.__prepareDeletionOfEquipment(selected_tag)
        self.playground.delete(selected_tag)

        TODO: Remove both the text and the links

    def deleteLink(self, event: TkEvent, fragmented: bool = False):
        x, y = event.x, event.y

        selected_link = self.playground.find_closest(x, y)[0]

        # if fragmented:
        #     fragmented_link: NetworkLink = self.links[selected_link]
        #     for segment_id in fragmented_link.segments:
        #         self.playground.delete(segment_id)
        # else:
        #     self.playground.delete(selected_link)

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

    ### Right Clicks
    def popRightClickMenu(self, event: TkEvent):
        x, y = event.x_root, event.y_root

        if self.rightclick_menu is not None:
            self.rightclick_menu.tk_popup(x, y)

    def handleChangeOfEquipmentName(self):
        ### The user shouldn't have changed of active tag between
        ### the <KeyRelease> event and the call of this function
        ### so we should be able to safely use `self.focused_tag`.

        self.popup(self, "entry")

        if self.focused_tag != 0:
          self.setEquipmentName(self.focused_tag, self.popup_entry_var)
        else:
            ### Apparently, the user tried to rename before doing anything else
            ### We can try to get the closest element of where the mouse currently is

            x, y = self.mouse_coords

            self.setEquipmentName(self.playground.find_closest(x, y)[0], self.popup_entry_var)

    def handleChangeOfEquipmentIcon(self):
        ### The user shouldn't have changed of active tag between
        ### the <KeyRelease> event and the call of this function
        ### so we should be able to safely use `self.focused_tag`.

        icon_path = TkFileDialog.askopenfilename()

        if self.focused_tag != 0:
          self.setEquipmentIcon(self.focused_tag, icon_path)
        else:
            ### Apparently, the user tried to rename before doing anything else
            ### We can try to get the closest element of where the mouse currently is

            x, y = self.mouse_coords

            self.setEquipmentIcon(self.playground.find_closest(x, y)[0], icon_path)

    def handleLinkCreation(self, ending: bool = False):
        ### The user shouldn't have changed of active tag between
        ### the <KeyRelease> event and the call of this function
        ### so we should be able to safely use `self.focused_tag`.

        if not ending:
            if self.focused_tag != 0:
                self.setEquipmentsLink(self.focused_tag, ending)
            else:
                x, y = self.mouse_coords
                self.setEquipmentsLink(self.playground.find_closest(x, y)[0], ending)
        else:
            x, y = self.mouse_coords
            self.setEquipmentsLink(self.playground.find_closest(x, y)[0], ending)

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
    def setEquipmentName(self, equipment_tag: int, name: str ):
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
        base: dict = self.equipments[self.reverse_equipments[equipment_tag]]
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

    ### PopUps Utils
    def createCanvasLinksWarning(self, equipment_name: str):
        CanvasPopUpWarning(self.playground, f"You have too many links on {equipment_name}!")

    def createCanvasSingularLinksWarning(self, equipment_name: str) -> None:
        CanvasPopUpWarning(self.playground, f"You can't simply link {equipment_name} on itself!")

    ### Export area
    def export_png(self):
        print("Current playground exported into PNG!")

class Coords:
    def __init__(self, x = None, y = None):
        if isinstance(x, tuple):
            self.x = x[0]
            self.y = x[0]
            self.__list__ = [coord for coord in x]
        else:
            self.x = x
            self.y = y
            self.__list__ = [x, y]
        self.__current__ = -1

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __sub__(self, coords: tuple):
        x, y = coords
        return int(x - self.x), int(y - self.y)

    def __iter__(self) -> Iterator:
        """Returns a built-in iterator.

        Returns:
            Iterator: The iterator used for reading the coordinates
        """
        return self.__list__.__iter__()
    
    def update(self, x: int, y: int):
        self.x = x
        self.y = y
        self.__list__ = [x, y]

class NetworkLink:
    def __init__(self, x: int, y: int, canvas: Canvas, equipment_tag: int, fragmented: bool = False):
        self.start_coords = Coords(x, y)
        self.end_coords = None
        self.tag = None
        self.start_equipment = equipment_tag
        self.end_equipment = None

        self.canvas = canvas
        self.is_fragmented: bool = fragmented
        self.segments = []
        self.reverse_links_dict = None

        self.bindings = {}

        self.term_size_x, self.term_size_y = get_terminal_size()

        self.CTRL_LINK_SPACING = 30

    def setEndCoords(self, x: int, y: int, equipment_tag: int, force: bool = False):
        if not force:
            if self.end_coords is None:
                self.end_coords = Coords(x, y)
                self.end_equipment = equipment_tag
                return True
            else:
                return False
        else:
            self.end_coords = Coords(x, y)
            self.end_equipment = equipment_tag
            return True

    def updateStartCoords(self, x: int, y: int):
        self.start_coords.update(x, y)

    def updateEndCoords(self, x: int, y: int):
        self.end_coords.update(x, y)

    def addBinding(self, event_to_bind: str, non_fragmented_call: Callable, fragmented_call: Callable = None):
        if self.is_fragmented:
            segment_binding = []
            for segment_id in self.segments:
                segment_binding.append({
                    "id": self.canvas.tag_bind(segment_id, event_to_bind, fragmented_call),
                    "non-fragmented-call": non_fragmented_call,
                    "fragmented-call": fragmented_call,
                })
        else:
            segment_binding = [{
                "id": self.canvas.tag_bind(self.tag, event_to_bind, non_fragmented_call),
                "non-fragmented-call": non_fragmented_call,
                "fragmented-call": fragmented_call
            }]

        self.bindings.update({
            event_to_bind: segment_binding
        })

    def removeBinding(self, event_to_unbind: str):
        if self.is_fragmented:
            for i in range(0, len(self.segments)):
                segment_id = self.segments[i]
                segment_binding = self.bindings[event_to_unbind][0]["id"]

                self.canvas.tag_unbind(segment_id, segment_binding)
        else:
            if self.tag is not None:
                self.canvas.tag_unbind(self.tag, self.bindings[event_to_unbind])
            else:
                pass

    def segmented_line(self, x0, y0, x1, y1):

        ### Compute the absolute distance between the origin and the destination
        dx: int = int(abs(x0 - x1))
        dy: int = int(abs(y0 - y1))

        ### Compute the theoric required number of segments from each absolute distance
        ### based on the global constant `CTRL_LINK_SPACING`
        nx = dx // self.CTRL_LINK_SPACING
        ny = dy // self.CTRL_LINK_SPACING

        ### Delta is our decisive number of segments we're gonna create.
        ### We take the longest cut of either `nx` or `ny`.
        ### We then compute the length of the segments.
        delta = nx if nx > ny else ny
        if delta != 0:
            if delta == nx:
                ny = delta
                ny_length = dy // delta
                nx_length = dx // delta
            else:
                nx = delta
                nx_length = dx // delta
                ny_length = dy // delta
        else:
            nx_length = 0
            ny_length = 0

        segments = []

        print(f"\n{self.term_size_x*'-'}\n")

        print(f"DX: {dx}, DY: {dy}, X-Segments: {nx}, Y-Segments: {ny}, X-Segments-Length: {nx_length}, Y-Segments-Length: {ny_length}, Delta: {delta}")

        print(f"\n{self.term_size_x*'-'}\n")

        ### We create the list of the segments with a rotation of x then y
        for i in range(1, nx+1):
            fragmented_segment_on_x = []
            fragmented_segment_on_y = []
            base_x_segment = []
            base_y_segment = []

            ### We're fragmenting the creation of the segments
            ### of X and Y and the corresponding base segments

            if x1 < x0:
                fragmented_segment_on_x = [x0 - nx_length*(i-1), x0 - (nx_length*i)]
                base_x_segment = [x0 - nx_length*(i-1), x0 - nx_length*(i-1)]
                print(f"Turn n°{i}: x: {x0 - nx_length*(i-1)} -> {x0 - (nx_length*i)},", end=" ")
            else:
                fragmented_segment_on_x = [x0 + nx_length*(i-1), x0 + (nx_length*i)]
                base_x_segment = [x0 + nx_length*(i-1), x0 + nx_length*(i-1)]
                print(f"Turn n°{i}: x: {x0 + nx_length*(i-1)} -> {x0 + (nx_length*i)},", end=" ")

            if y1 < y0:
                fragmented_segment_on_y = [y0 - ny_length*(i-1), y0 - (ny_length*i)]
                base_y_segment = [y0 - ny_length*i, y0 - ny_length*i]
                print(f"y: {y0 - (ny_length*(i-1))} -> {y0 - (ny_length*i)}, old_coords: ({x0}/{y0}) -> ({x1}/{y1})")
            else:
                fragmented_segment_on_y = [y0 + ny_length*(i-1), y0 + (ny_length*i)]
                base_y_segment = [y0 + ny_length*i, y0 + ny_length*i]
                print(f"y: {y0 + (ny_length*(i-1))} -> {y0 + (ny_length*i)}, old_coords: ({x0}/{y0}) -> ({x1}/{y1})")

            segments.append(fragmented_segment_on_x + base_y_segment)
            segments.append(base_x_segment + fragmented_segment_on_y)

        return segments

    def draw(self, reverse_links_dict: dict) -> Union[int, list]:
        x0, y0 = self.start_coords
        if self.end_coords is not None:
            x1, y1 = self.end_coords
        else:
            x1, y1 = x0, y0

        if self.is_fragmented:
            ### We have multiple x-only or y-only segments
            ### from the start coordinates to the end coordinates
            for segment in self.segmented_line(x0, y0, x1, y1):
                x0, x1, y0, y1 = segment
                line_id = self.canvas.create_line(x0, y0, x1, y1)
                self.segments.append(line_id)
                self.canvas.tag_lower(line_id)

                for binding_key, binding_values in self.bindings.items():
                    self.canvas.tag_bind(line_id, binding_key, binding_values["fragmented-call"])

                if self.setOrUpdateReverseLinksDict(reverse_links_dict):
                    self.updateReverseLinksDict(line_id)

            to_return: list = self.segments
        else:
            ### We have one direct diagonal link
            self.tag = self.canvas.create_line(x0, y0, x1, y1)
            self.canvas.tag_lower(self.tag)

            for binding_key, binding_values in self.bindings.items():
                self.canvas.tag_bind(self.tag, binding_key, binding_values["non-fragmented-call"])

            if self.setOrUpdateReverseLinksDict(reverse_links_dict):
                self.updateReverseLinksDict(self.tag)

            to_return: int = self.tag

        return to_return

    def update(self, reverse_links_dict: dict) -> Union[int, list]:
        x0, y0 = self.start_coords
        x1, y1 = self.end_coords

        if self.is_fragmented:
            ### Cleaning the self.tag if we're moving from
            ### direct + diagonal link to direct + segmented link
            if self.tag is not None:
                self.cleanDiagonalLinkContent()

            ### Cleaning the self.segments and the current canvas IDs
            ### if we were already segmented
            if self.segments != []:
                self.cleanSegmentedLinkContent()

            ### We are regenerating the segments one by one
            for segment in self.segmented_line(x0, y0, x1, y1):
                x0, x1, y0, y1 = segment

                ### We're creating the line on the canvas then
                ### lowering the tag to not lock user input on the link object
                line_id = self.canvas.create_line(x0, y0, x1, y1)
                self.canvas.tag_lower(line_id)
                ### We're appending the line_id into the self.segments dictionnary
                self.segments.append(line_id)

                ### We're going through every binding element already created
                ### for links to create a homogeneous set of segments
                for binding_key, binding_values in self.bindings.items():
                    self.canvas.tag_bind(line_id, binding_key, binding_values[0]["fragmented-call"])

                if self.setOrUpdateReverseLinksDict(reverse_links_dict):
                    self.updateReverseLinksDict(line_id)

            to_return: list = self.segments

        else:
            ### Well, what a surprise, we were working with a segmented link
            ### Now, we need to clean the old link
            if self.segments != []:
                self.cleanSegmentedLinkContent()

                if self.tag is not None:
                    self.cleanDiagonalLinkContent()

                self.tag = self.canvas.create_line(x0, y0, x1, y1)
                self.canvas.tag_lower(self.tag)

                for binding_key, binding_values in self.bindings.items():
                    self.canvas.tag_bind(self.tag, binding_key, binding_values[0]["non-fragmented-call"])

                if self.setOrUpdateReverseLinksDict(reverse_links_dict):
                    self.updateReverseLinksDict(self.tag)

            elif self.tag is not None:
                ### In fact, we were already a diagonal link
                self.canvas.coords(self.tag, x0, y0, x1, y1)

            to_return: int = self.tag


        return to_return

    def updateFragmentationStatus(self, fragmentation_value: bool):
        self.is_fragmented = fragmentation_value

    def cleanDiagonalLinkContent(self) -> None:
        """A simple utility to clean the content of a diagonal link.

                CAUTION: The link should be verified before calling this function with:

                    ```py
                    if self.tag is not None:
                        self.cleanDiagonalLinkContent()
                    ```
        """
        self.canvas.delete(self.tag)
        self.deleteFromReverseLinksDict(self.tag)
        self.tag = None

    def cleanSegmentedLinkContent(self) -> None:
        """A simple utility to clean the content of a segmented link.
        """
        ### Firstly, we're unbinding all events from every element
        for event in self.bindings.keys():
            self.removeBinding(event)

        for segment_id in self.segments:
            self.canvas.delete(segment_id)

            ### We're cleaning the current (internal & external) list of segments
            ### Otherwise, we're risking load latency because of the size of the list
            self.segments.pop(self.segments.index(segment_id))
            self.deleteFromReverseLinksDict(segment_id)

    def setOrUpdateReverseLinksDict(self, reverse_dict: dict) -> bool:
        if self.reverse_links_dict is not None:
            if self.reverse_links_dict is not reverse_dict:
                self.reverse_links_dict = reverse_dict
        else:
            self.reverse_links_dict = reverse_dict

        return True

    def updateReverseLinksDict(self, line_id: Union[str, int]) -> None:
        self.reverse_links_dict.update({
            line_id: self
        })

    def deleteFromReverseLinksDict(self, line_id: Union[str, int]) -> None:
        if line_id in self.reverse_links_dict.keys():
            self.reverse_links_dict.pop(line_id)

class PopUpMessage:
    def __init__(self, root_frame: NetApp, type: str):
        self.popup = None
        if type == "entry":
            self.popup = PopUpEntry(root_frame)
        
        root_frame.wait_window(self.popup.toplevel)

class CanvasPopUpWarning:
    def __init__(self, root_canvas: Canvas, text: str) -> None:
        text_to_disappear = root_canvas.create_text(root_canvas.winfo_width() // 2, (10/100)*root_canvas.winfo_height(), text=text, fill="red")
        root_canvas.after(1500, lambda: root_canvas.delete(text_to_disappear))


class PopUpEntry:
    def __init__(self, root_frame: NetApp):
        self.root = root_frame
        self.toplevel = Toplevel(root_frame)
        self.content = StringVar(self.toplevel)
        self.entry = Entry(self.toplevel, textvariable=self.content, takefocus=True)
        self.submit_button = Button(self.toplevel, text="Submit", command=lambda: self.close())

        self.toplevel.grid(None, None)
        self.entry.grid(column=0, row=0)
        self.submit_button.grid(column=0, row=1)

    def close(self):
        self.toplevel.destroy()
        self.root.popup_entry_var = self.content.get()

class NetworkEquipment:
    supported_equipments = ["switch", "router", "pc", "mobile"]
    four_links = supported_equipments[:2]
    icon_size = (64, 64)
    ids = {key: 0 for key in supported_equipments}

    def __init__(self, type: str) -> None:
        """A simple class holding all the utils required to work
        with specific simulated network equipment inside a Tkinter Canvas.

        Args:
            type (str): Either `switch`, `router`, `pc`, `mobile`. (All entries are going to be lowercased)

        Raises:
            ValueError: You gave an unsupported type.
        """

        if type.lower() not in NetworkEquipment.supported_equipments:
            raise ValueError("Unsupported Network Equipment")
        
        self.equipment = type
        self.icon_path = self.__setIconPath(f"./src/icons/{self.equipment}.png")
        self.icon = ImageTk.PhotoImage(
            Image.open(self.icon_path, "r").resize(NetworkEquipment.icon_size)
        )

        ### We update its ID
        NetworkEquipment.ids[self.equipment] += 1

        self.name = f"{self.equipment}-{NetworkEquipment.ids[self.equipment]}"
        self.links_nbr = 0

        if self.equipment in NetworkEquipment.four_links:
            self.links_max_nbr = 4
        else:
            self.links_max_nbr = 1

        ### We're dynamically creating a list containing the NetworkLink elements
        self.links = [None for i in range(0, self.links_max_nbr)]

    ### Setters
    def setName(self, new_name: str) -> None:
        self.name = new_name

        return None

    def setIcon(self, new_icon: Union[str, PathLike]) -> None:
        self.icon_path = self.__setIconPath(new_icon)
        self.icon = ImageTk.PhotoImage(Image.open(self.icon_path, "r").resize(NetworkEquipment.icon_size))

        return None

    def __setIconPath(self, path: str) -> str:
        """Private setter for the icon path

        Args:
            path (str): The relative path of the icon

        Returns:
            str: The absolute equivalent of the relative path
        """
        return absolute_path(path)
    
    def addLink(self, link_object: NetworkLink) -> None:
        """Simple utility that adds links objects to the internal list.
        Should be used after:

        ```py
        if NetworkEquipment.isOpenToLinkCreation():
            NetworkEquipment.addLink(NetworkLink)
        ```

        Args:
            link_object (NetworkLink): The link object to add
        """

        self.links[self.links.index(None)] = link_object
        self.getLinksNumber()

        return None

    def removeLink(self, link_object: NetworkLink) -> None:
        """Simple utility that removes links objects to the internal list and decrements the counter.

        Args:
            link_object (NetworkLink): The link object to remove
        """

        self.links.pop(self.links.index(link_object))
        self.links.append(None)
        self.links_nbr -= 1

        return None

    ### Getters
    def getLinksNumber(self, getter: bool = False) -> int:
        if not getter:
            if self.links_nbr+1 <= self.links_max_nbr:
                self.links_nbr += 1
            else:
                return -1
        return self.links_nbr
    
    def isOpenToLinkCreation(self) -> bool:
        """Is this current Equipment can add new link connections?

        Returns:
            bool: Either `True` or `False`
        """
        if self.links_nbr < self.links_max_nbr:
            return True
        else:
            return False

def absolute_path(relative_path: str) -> str:
  """A simple utility function to transform relative to absolute path.

  Args:
      relative_path (str): The relative path we're trying to get.

  Returns:
      str: The absolute path of our target.
  """

  absolute_cwd = getcwd()
  current_path = "/cours/modules/R309/"

  if absolute_cwd.endswith("import-cours-but-rt"):
    ### We got the root of our current workspace, let's add the path from there
    ### to come to our relative path
    result = absolute_cwd + current_path + relative_path
  else:
    ### We should be deeper than the root of the workspace
    ### so we don't need to add anything else
    result = absolute_cwd + "/" + relative_path

  return result


if __name__ == "__main__":
    t = NetApp("test-app", (800, 800))
    t.run()