#!/bin/env python3

"""Basic tkinter playground to tinker with the ways of calling
different widgets inside a tkinter canvas.
"""

from tkinter import (
  Entry,
  Tk,
  Frame, Canvas, Button,
  StringVar,
  E
)

from os import get_terminal_size

class PopUpEntry:
  def __init__(self, root_frame: Canvas):
    self.root = root_frame
    self.width = self.root.winfo_width()
    self.height = self.root.winfo_height()
    self.frame = Frame(self.root, width=self.width, height=self.height)
    self.content = StringVar(self.frame)
    self.entry_widget = Entry(self.frame, background="red", width=50)
    self.entry_id = canvas.create_window(size[0], size[1], window=self.frame, anchor=E)
    self.submit_button = Button(self.frame, text="Submit", command=lambda: self.close())

    print("Current size inside child window:", self.width, self.height, self.entry_widget.winfo_width())

    self.frame.grid(column=0, row=0)
    self.entry_widget.grid(column=0, row=0)
    self.submit_button.grid(column=1, row=0)

    self.toplevel = root_frame.create_window(root_frame.winfo_width() // 2, (10/100)*root_frame.winfo_height(), window=self.frame, anchor="center")
    self.root.update()


  def close(self):
    self.root.delete(self.toplevel)
    self.root.popup_entry_var = self.content.get()

DEBUG = False

if __name__ == "__main__":

  size = (600, 400)
  root = Tk()
  frame = Frame(root, width=400, height=400)
  canvas = Canvas(frame, width=300, height=300, bg="black")
  popup = Button(frame, text="Pop me!", command=lambda: PopUpEntry(canvas))
  infos = Button(frame, text="Get Current size!", command=lambda: print("Canvas size:", canvas.winfo_width(), canvas.winfo_height()))

  if DEBUG:
    canvas_frame = Frame(canvas, background="green", width=100, height=100)
    entry_widget = Entry(canvas_frame, background="red", width=50)
    entry_btn = Button(canvas_frame, width=50, text="Click me!", command=lambda: print("Canvas Widget Clicked!"))
    frame_id = canvas.create_window(size[0], size[1], window=canvas_frame, anchor="center")


  root.geometry(f"{size[0]}x{size[1]}")
  frame.grid(column=0, row=0)
  canvas.grid(column=0, row=0)
  popup.grid(column=1, row=0)
  infos.grid(column=1, row=1)

  if DEBUG:
    canvas_frame.grid(column=0, row=0)
    entry_widget.grid(column=0, row=0)
    entry_btn.grid(column=0, row=1)

  tsx, tsy = get_terminal_size()

  root.mainloop()