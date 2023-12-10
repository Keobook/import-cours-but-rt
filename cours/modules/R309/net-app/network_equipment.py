from os import (
    system, PathLike
    )
from typing import Union
from network_link import NetworkLink
from utils import absolute_path
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