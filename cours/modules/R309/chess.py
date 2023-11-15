#!/bin/env python3

import json
from math import floor
import os
from tkinter import (
  Tk, Canvas,
  N, E, S, W,
  Event as TkEvent
)
from tkinter import ttk
from PIL import Image, ImageTk

### Classes
class ChessPiece:
  def __init__(self, name, relative_path):
    self.name = name
    self.path = absolute_path(relative_path)
    self.img = ImageTk.PhotoImage(Image.open(self.path, "r").resize((71, 71)))

  def getName(self):
    return self.name

class GridColor:
  def __init__(self, name, hexadecimal_value):
    self.name = name
    self.hex = hexadecimal_value

  def get_name(self):
    return self.name
  
  def get_color(self):
    return self.hex

class EventHandler:
  def __init__(self):
    self.old_coords = (0, 0)
    self.new_coords = (0, 0)
    self.current_tag = 0

  def makeDraggable(self, canvas_tag: int) -> int:
    """Simply update the canvas tag with a correct drag/drop event binding

    Args:
        canvas_tag (int): The <int> returned from a <canvas>.create_...(...) method.

    Returns:
        int: The given tag id returned for you to insert this function without any disruption.
    """
    maincanvas.tag_bind(canvas_tag, "<Button-1>", self.dragStart)
    maincanvas.tag_bind(canvas_tag, "<B1-Motion>", self.dragMotion)
    maincanvas.tag_raise(canvas_tag)

    return canvas_tag
  
  def dragStart(self, event: TkEvent):
    """_summary_

    Args:
        event (TkEvent): _description_
    """
    x,y = (floor(event.x/base_value), floor(event.y/base_value))

    self.old_coords = (x, y)

    ### Let's add the selected piece
    if self.current_tag == 0:
      self.current_tag = chessboard[f"{x}/{y}"][1][0]
    else:
      print("You're already holding a chess piece somewhere!")

  def dragMotion(self, event: TkEvent):
    """_summary_

    Args:
        event (TkEvent): _description_
    """
    x, y = event.x, event.y
    x2, y2 = self.old_coords

    distance_x = x - x2
    distance_y = y - y2

    print(f"coords=({x2}/{y2})/({x}/{y}), real=({event.x}/{event.y}), dist=({distance_x}, {distance_y})")

    maincanvas.moveto(self.current_tag, distance_x, 0)
    maincanvas.tag_raise(self.current_tag)

    self.current_tag = 0

### Functions
def absolute_path(relative_path):
  """A simple utility to transform relative to absolute path.

  Args:
      relative_path (str): The relative path we're trying to get.

  Returns:
      str: The absolute path of our target.
  """

  absolute_cwd = os.getcwd()
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

#### Scripting

## Events Handler
event = EventHandler()

### Window
window = Tk()
window.title("Chess Board")

### Frames
rootframe = ttk.Frame(window, padding="12 12 12 12")
rootframe.grid(column=0, row=0, sticky=(N, W, E, S))

### Canvas
base_value = 100
maincanvas = Canvas(rootframe, {
  "bg": "grey",
  "width": 800,
  "height": 800
})
maincanvas.grid(column=8, row=8, columnspan=base_value, rowspan=base_value)

black = GridColor("Black", "#000000")
grey = GridColor("Grey", "#686b6b")
white = GridColor("Wwhite", "#dfdfdf")

chessboard = {}

for y in range(0, 8):
  for x in range(0, 8):
    color = grey if (x+y)%2 else white
    chessboard[f"{x}/{y}"] = [
       (maincanvas.create_rectangle(
         x*base_value, base_value*y,
         (x+1)*base_value, (y+1)*base_value,
         fill=color.get_color(), width=0
         ),
         f" {color.get_name()} rectangle"),
       None]

### Images
blackqueen = ChessPiece("black queen", "src/queen.png")

chessboard["0/0"][1] = (event.makeDraggable(maincanvas.create_image(50, 50, image=blackqueen.img)), blackqueen.getName())

print(json.dumps(chessboard, indent=2))

window.mainloop()