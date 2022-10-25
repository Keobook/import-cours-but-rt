#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###////////////////////////////////////////////////////////////////////////////////////:
###
### Imports
###
###////////////////////////////////////////////////////////////////////////////////////:

from os import (
  system,
  name as os_name
)
from importlib import import_module
from datetime import datetime

try:
  import termcolor
except ModuleNotFoundError:
  try:
    system("pip3 install termcolor")
    import_module("termcolor")
  except:
    print("An error occured while downloading a dependency: termcolor")
    exit(1)



###////////////////////////////////////////////////////////////////////////////////////:
###
### Functions definition
###
###////////////////////////////////////////////////////////////////////////////////////:

def createBoard(width: int, height: int) -> list:
  """A function used to create the board of any board game

    Arguments
    ---
      `width`:
        The width of the board, can only be an int
      `height`:
        The height of the board, can only be an int

    Output: a list with the len() of height and each cell has a len() of width
  """
  return [[["-"] for x in range(0, width)] for y in range(0, height)]


def showBoard(board, show_index=False):
  global alphabet

  if show_index:
    for i in range(0, len(board[0])):
      ### If first letter, automatically add a space in order to re-caliber the ouput
      if i == 0:
        print(" ", end="")
      print(alphabet[i], end=" ")
    print("")
  for y in range(0, len(board)):
    for x in range(0, len(board[y])):
      if x == 0:
        print(y+1 if show_index else "", end=" ")
      print(board[y][x][0], end=" ")
    print("")


def showBoardColored(board, show_index=False):
  global alphabet
  global letter_to_highlight

  if show_index:
    for i in range(0, len(board[0])):
      ### If first letter, automatically add a space in order to re-caliber the ouput
      if i == 0:
        print(" ", end="")
      print(alphabet[i], end=" ")
    print("")
  for y in range(0, len(board)):
    for x in range(0, len(board[y])):
      curr_cell = board[y][x][0]

      if x == 0:
        print(y+1 if show_index else "", end=" ")

      if not curr_cell in ("@", "*", letter_to_highlight[0]):
        print(curr_cell, end=" ")
      else:
        if curr_cell == "@":
          print(termcolor.colored(curr_cell, "red"), end=" ")
        elif curr_cell == "*":
          print(termcolor.colored(curr_cell, "blue"), end=" ")
        elif curr_cell == letter_to_highlight[0]:
          print(termcolor.colored(curr_cell, None, letter_to_highlight[1]), end=termcolor.colored(" ", None, letter_to_highlight[1]))
    print("")


def getCoordonnees(case_stringed):
  global alphabet
  x, y = case_stringed[0], int(case_stringed[1])
  ### We substract 1 to y because we start at 1
  return (y-1, alphabet.index(x))


def getAction(cell, board):
  """A simple function returning a str object
    following the type of action it has been.
    *A duplicate of getIfHit()*

    Args
    ----
      `cell`, str: A str object containing the cell with its indexes, example: C4
      `board`, list: A list object containing the board to be affected by this action
  """

  y, x = getCoordonnees(cell)
  if board[y][x] in data_type:
    return "@"
  else:
    return "*"


def getIfHit(cell, board):
  global data_type
  y, x = getCoordonnees(cell)
  if board[y][x] in data_type:
    return True
  else:
    return False


def showActionResult(action):
  """Prints the result of the action
  Args
  ----
    `action`, tuple: tuple containing (cell, board)
      `cell`, str: The cell you want to hit
      `board`, list: The board you want the action to be taken into account
  """
  if getIfHit(action[0], action[1]):
    print("It's a hit!")
  else:
    print("Oh no! You missed!")


def getActionIntoAction(cell, board):
  y, x = getCoordonnees(cell)
  board[y][x] = getAction(cell, board)


def cleanNShow(board_in_question, colored=False):
  if os_name == "posix":
    system("clear")
  else:
    system("cls")

  if colored:
    showBoardColored(board_in_question, True)
  else:
    showBoard(board_in_question, True)


def cleanOutput():
  if os_name == "posix":
    system("clear")
  else:
    system("cls")


def liveModifications(board, colored=False):
  try:
    while True:
      cleanNShow(board, colored)
      key = input("Enter a cell of the board from above: ")
      showActionResult((key, board))
      getActionIntoAction(key, board)
  except KeyboardInterrupt:
    cleanOutput()
    print("Process Interrupted")
    return 0


def getAliveOrNot(player_board):
  global data_type
  stillAlive = False
  for line in player_board:
    for cell in line:
      if cell in data_type:
        if not stillAlive:
          stillAlive = True
  return stillAlive


def createSaveState(board: list) -> str:
  save_str = ""
  for line in board:
    for column in line:
      save_str += column + "|"
    save_str += "\n"
  return save_str


def saveState(board: list) -> None:
  with open(f"save-{str(datetime.now())[:10]}.txt", "wt", encoding="utf-8") as fout:
    fout.write(createSaveState(board))


def loadState(save_file: str) -> list:
  board = []
  with open(save_file, "rt", encoding="utf-8") as fin:
    lines = fin.read().strip().split("\n")
    for line in lines:
      cell = line.strip().split("|")
      temp_line = []
      for data in cell:
        if data != "":
          temp_line.append(data)
      board.append(temp_line)

  return board


def placeShip(ship_name, board, ships, clean_board=True):
  ship_data = {
      "carrier": (4, "P"),
      "cruisers": (3, "C"),
      "torpedo-boat": (2, "T"),
      "submarine": (1, "S")
  }
  cases_to_place = ship_data[ship_name]
  start_cell_y, start_cell_x = 0, 0
  old_start_cell_y, old_start_cell_x = 0, 0
  temp_board = board.copy()
  axis = "h"
  old_axis = "h"


  ### Always set the element on the up-left corner even if it's on already set ships
  hardWriteShipData(cases_to_place, temp_board, axis, (start_cell_y, start_cell_x))
  try:
    while True:
      cleanNShow(temp_board, True)
      #showBoard(temp_board, True)
      action = input("Enter either:\n- L: go to the left,\n- R: go to the right,\n- U: go to the top,\n- D: go to the bottom,\n- V: change axis to vertical,\n- H: change axis to horizontal\n- X: validate your choice\nEnter you choice: ").upper()
      if action == "L":
        if start_cell_x > 0:
          old_start_cell_x = start_cell_x
        else:
          old_start_cell_x = 0
        start_cell_x = start_cell_x-1 if start_cell_x-1 >= 0 else 0
        print(old_start_cell_x, start_cell_x)

      if action == "R":
        if start_cell_x < len(temp_board[0])-1:
          old_start_cell_x = start_cell_x
        else:
          old_start_cell_x = start_cell_x-1
        start_cell_x = start_cell_x+1 if start_cell_x+1 <= len(temp_board[0])-1 else len(temp_board[0])-1
        print(old_start_cell_x, start_cell_x)


      if action == "U":
        old_start_cell_y = start_cell_y
        start_cell_y = start_cell_y-1 if start_cell_y-1 >= 0 else 0

      if action == "D":
        old_start_cell_y = start_cell_y
        start_cell_y = start_cell_y+1 if start_cell_y+1 <= len(temp_board)-1 else len(temp_board)-1

      if action == "V":
        if axis != "v":
          axis = "v"

      if action == "H":
        if axis != "h":
          axis = "h"

      if action == "X":
        break

      temp_board = hardWriteShipData(cases_to_place, temp_board, axis, (start_cell_y, start_cell_x), False, (old_start_cell_y, old_start_cell_x), old_axis)

    ships += 1
    return temp_board, ships

  except KeyboardInterrupt:
    cleanOutput()
    print("Process Interrupted")
    return 0

def hardWriteShipData(data, board, axis, start_cell, clean_board=True, old_start_cell=0, old_axis=None):
  global letter_to_highlight
  number, letter = data
  max_x, max_y = len(board[0])-number, len(board)-number

  cboard = board
  if not clean_board:
    cboard = [[["-"] if board[y][x] == letter else board[y][x] for x in range(0, len(board[y])) ] for y in range(0, len(board))]

  cleanOutput()
  print(data, axis, start_cell, clean_board, old_start_cell, old_axis, True if start_cell[0]+number < max_y else False, True if start_cell[1]+number < max_x else False)


  for i in range(0, number):
    if axis == "v":
      if i+start_cell[0] < max_y:
        if letter_to_highlight[0] == letter:
          letter_to_highlight = ("#", "on_blue")

        if cboard[start_cell[0]+i][start_cell[1]] == "$":
          letter_to_highlight = (letter, "on_red")
          continue

        cboard[i+start_cell[0]][start_cell[1]] = letter
      else:
        try:
          cboard[i+start_cell[0]][start_cell[1]] = letter
        except IndexError:
          letter_to_highlight = (letter, "on_red")
    else:
      if i+start_cell[1] < max_x:
        if letter_to_highlight[0] == letter:
          letter_to_highlight = ("#", "on_blue")

          if cboard[start_cell[0]+i][start_cell[1]] == "$":
            letter_to_highlight = (letter, "on_red")
            continue

        cboard[start_cell[0]][i+start_cell[1]] = letter
      else:
        try:
          cboard[start_cell[0]][i+start_cell[1]] = letter
        except IndexError:
          letter_to_highlight = (letter, "on_red")

  return cboard

###////////////////////////////////////////////////////////////////////////////////////:
###
### Initiations of variables
###
###////////////////////////////////////////////////////////////////////////////////////:

alphabet = ["A", "B", "C", "D", "E",
            "F", "G", "H", "I", "J", "K", "L",
            "M", "N", "O", "P", "Q", "R", "S",
            "T", "U", "V", "W", "X", "Y", "Z"]

main_board = createBoard(10, 8)
data_type = ("P", "C", "T", "S")
letter_to_highlight = ("#", "on_blue")
#liveModifications(main_board, True)
ship_list = ["carrier", "cruisers", "cruisers", "torpedo-boat",
             "torpedo-boat", "torpedo-boat", "submarine", "submarine", "submarine", "submarine"]
ships = 0
while ships < 10:
  if ships == 0:
    main_board, ships = placeShip(ship_list[ships], main_board, ships)
  else:
    main_board, ships = placeShip(ship_list[ships], main_board, ships, False)
