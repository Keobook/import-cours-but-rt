#!/bin/env python3

from os import PathLike
import os
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
        os.system("pip3 install Pillow")
    except Exception: ### Generic-based Exception
        os.system("python3 -m pip --upgrade pip")
        os.system("python3 -m pip install --upgrade Pillow")

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

        ### Let's set the display
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.playground.grid(column=1, row=1, rowspan=self.y_size, columnspan=self.x_size)

        ### Bind some basics events to the root window
        self.bind("<Motion>", lambda event: self.__getMouseCoords(event))

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
                },
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
        self.mainloop()

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
        # print(f"coords=({x}/{y})")

        self.focused_tag = self.playground.find_closest(x, y)[0]

    def endDragFocus(self, event: TkEvent):
        widget: Canvas = event.widget
        x = event.x if widget.winfo_x() + event.x <= self.x_size else self.x_size
        y = event.y if widget.winfo_y() + event.y <= self.y_size else self.y_size

        ### We're dividing by 2 the icon size to find the difference
        ### between the mouse position and the center of the icon.
        difference_mouse_icon = NetworkEquipment.icon_size[0] // 2

        self.playground.moveto(
            self.focused_tag, x - difference_mouse_icon, y - difference_mouse_icon
        )

        ### After moving the icon, we need to go through its dependency list to move them
        dependencies = self.equipments[self.reverse_equipments[self.focused_tag]]["dependencies"]
        dependent_label = dependencies["label"]

        self.playground.moveto(dependent_label, x - difference_mouse_icon // 2, y + difference_mouse_icon)

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

            x1, y1 = link_object.start_coords
            x2, y2 = link_object.end_coords

            self.playground.coords(link_object.tag, x1, y1, x2, y2)

    ### Double clicks
    def deleteItem(self, event: TkEvent):
        x, y = event.x, event.y

        selected_tag = self.playground.find_closest(x, y)[0]
        self.__prepareDeletionOfEquipment(selected_tag)
        self.playground.delete(selected_tag)

    def deleteLink(self, event: TkEvent):
        x, y = event.x, event.y

        selected_link = self.playground.find_closest(x, y)[0]
        self.playground.delete(selected_link)

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
    def highlightTag(self, event: TkEvent):
        x, y = event.x, event.y
        self.playground.itemconfigure(self.playground.find_closest(x, y)[0], fill="red")

    def unhighlightTag(self, event: TkEvent):
        x, y = event.x, event.y
        self.playground.itemconfigure(self.playground.find_closest(x, y)[0], fill="black")

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

    def setEquipmentsLink(self, equipment_tag: int, ending: bool = False):
        links: dict = self.equipments[self.reverse_equipments[equipment_tag]]["dependencies"]["links"]
        x, y = self.mouse_coords


        if self.current_link_state == "idle":
            ### We're creating the visual link
            link_id = self.playground.create_line(x, y, x, y)
            self.playground.tag_lower(link_id)

            links.append(NetworkLink(x, y, link_id, equipment_tag))

            self.current_link_state = "active"
            self.rightclick_menu.entryconfigure(2, label="Set link", command = lambda: self.handleLinkCreation(True))
            self.current_link_root = equipment_tag

            ### We're binding the callback to the mouse movement
            self.link_binding = self.playground.bind("<Motion>", lambda event: self.setEquipmentsLink(self.current_link_root))
            self.playground.bind("<Double-Button-1>", lambda event: self.deleteLink(event))
            self.playground.tag_bind(link_id, "<Enter>", lambda event: self.highlightTag(event))
            self.playground.tag_bind(link_id, "<Leave>", lambda event: self.unhighlightTag(event))

        elif self.current_link_state == "active":
            old_links: dict = self.equipments[self.reverse_equipments[self.current_link_root]]["dependencies"]["links"]
            old_links_object: NetworkLink = old_links[-1]
            x, y = old_links_object.start_coords
            x1, y1 = self.mouse_coords

            self.playground.coords(old_links_object.tag, x, y, x1, y1)

            if ending:

                old_links_object.setEndCoords(x1, y1, equipment_tag)

                links.append(old_links_object)

                self.current_link_state = "idle"
                self.rightclick_menu.entryconfigure(2, label="Create link", command = lambda: self.handleLinkCreation())
                self.current_link_root = 0

                ### We're unbinding the callback to the mouse movement
                self.playground.unbind("<Motion>", self.link_binding)

        else:
            ### TODO: Create an Escape sequence to erase the current draft link
            pass


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
    def __init__(self, x: int, y: int, canvas_tag: int, equipment_tag: int):
        self.start_coords = Coords(x, y)
        self.end_coords = None
        self.tag = canvas_tag
        self.start_equipment = equipment_tag
        self.end_equipment = None

    def setEndCoords(self, x: int, y: int, equipment_tag: int):
        self.end_coords = Coords(x, y)
        self.end_equipment = equipment_tag

    def updateStartCoords(self, x: int, y: int):
        self.start_coords.update(x, y)

    def updateEndCoords(self, x: int, y: int):
        self.end_coords.update(x, y)

class PopUpMessage:
    def __init__(self, root_frame: NetApp, type: str):
        self.popup = None
        if type == "entry":
            self.popup = PopUpEntry(root_frame)
        
        root_frame.wait_window(self.popup.toplevel)

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
    icon_size = (64, 64)
    ids = {key: 0 for key in supported_equipments}

    def __init__(self, type: str):
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
        self.icon_path = f"./src/icons/{self.equipment}.png"
        self.icon = ImageTk.PhotoImage(
            Image.open(self.icon_path, "r").resize(NetworkEquipment.icon_size)
        )

        ### We update its ID
        NetworkEquipment.ids[self.equipment] += 1

        self.name = f"{self.equipment}-{NetworkEquipment.ids[self.equipment]}"
        self.links_nbr = 0

    ### Setters
    def setName(self, new_name: str):
        self.name = new_name

    def setIcon(self, new_icon: Union[str, PathLike]):
        self.icon_path = new_icon
        self.icon = ImageTk.PhotoImage(Image.open(self.icon_path, "r").resize(NetworkEquipment.icon_size))

    ### Getters
    def getLinksNumber(self, getter = False):
        if not getter:
            self.links_nbr += 1
        return self.links_nbr

if __name__ == "__main__":
    t = NetApp("test-app", (800, 800))
    t.run()
