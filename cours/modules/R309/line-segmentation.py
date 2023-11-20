#!/bin/env python3

"""Basic tkinter playground to tinker with an algorithm
  to dynamically segment a diagonal line into smaller x-only + y-only segments.
"""

from tkinter import (
  Tk,
  Frame, Canvas,
  Event as TkEvent
)
from os import (
  get_terminal_size,
)

link = []
term_size_x, term_size_y = get_terminal_size()
start_coords = []
current_links = []


def start_drawing(event: TkEvent):
  global current_links, start_coords
  x, y = event.x, event.y
  widget: Canvas = event.widget
  if current_links == []:
    for segment in segmented_line(x, y, x, y):
      x0, x1, y0, y1 = segment
      current_links.append(canvas.create_line(x0, y0, x1, y1))

    start_coords = [x, y]

def end_drawing(event: TkEvent):
  global current_links, start_coords
  x, y = event.x, event.y

  x0, y0 = start_coords
  i = 0

  if current_links == []:
    for segment in segmented_line(x0, y0, x, y):
      x0, x1, y0, y1 = segment
      current_links.append(canvas.create_line(x0, y0, x1, y1))
      i += 1

  else:
    for link_segment in current_links:
      canvas.delete(link_segment)

    for segment in segmented_line(x0, y0, x, y):
      x0, x1, y0, y1 = segment
      current_links.append(canvas.create_line(x0, y0, x1, y1))

      i += 1

def segmented_line(x0, y0, x1, y1):
  global CTRL_LINK_SPACING

  ### Compute the absolute distance between the origin and the destination
  dx: int = int(abs(x0 - x1))
  dy: int = int(abs(y0 - y1))

  ### Compute the theoric required number of segments from each absolute distance
  ### based on the global constant `CTRL_LINK_SPACING`
  nx = dx // CTRL_LINK_SPACING
  ny = dy // CTRL_LINK_SPACING

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

  print(f"\n{term_size_x*'-'}\n")

  print(f"DX: {dx}, DY: {dy}, X-Segments: {nx}, Y-Segments: {ny}, X-Segments-Length: {nx_length}, Y-Segments-Length: {ny_length}, Delta: {delta}")

  print(f"\n{term_size_x*'-'}")

  ### We create the list of the segments with a rotation of x then y
  for i in range(1, nx+1):
    fragmented_segment_on_x = []
    fragmented_segment_on_y = []
    base_x_segment = []
    base_y_segment = []

    # segments.append([x0 + nx_length*(i-1), x0 + (nx_length*i), y0 + (ny_length*(i-1)), y0 + (ny_length*(i-1))])

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

  print("The segments:\n\n", segments)
  return segments

CTRL_LINK_SPACING = 50
DEBUG = False

if __name__ == "__main__":
  root = Tk()
  frame = Frame(root, width=400, height=400)
  canvas = Canvas(frame, width=root.winfo_width(), height=root.winfo_height())

  frame.grid(column=0, row=0)
  canvas.grid(column=0, row=0)

  canvas.bind("<Button-1>", lambda event: start_drawing(event))
  canvas.bind("<B1-Motion>", lambda event: end_drawing(event))

  if DEBUG:

    canvas.create_rectangle(250, 250, 250, 250, fill="red", width=10)
    canvas.create_rectangle(150, 320, 150, 320, fill="red", width=10)

    for segment in segmented_line(250, 250, 150, 320):
      x0, x1, y0, y1 = segment
      canvas.create_line(x0, y0, x1, y1)

  root.bind("<Configure>", lambda event: canvas.configure(width=root.winfo_width(), height=root.winfo_height()))

  root.mainloop()