from typing import Iterator

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