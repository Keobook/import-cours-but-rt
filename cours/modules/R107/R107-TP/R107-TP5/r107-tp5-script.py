#!/bin/env python3

# %% [markdown]
# # R107-TP5 Opolka Alexis

# %%
### Put here the imports required
import os
try:
  import termcolor
except ModuleNotFoundError:
  import importlib
  try:
    os.system("pip3 install termcolor")
    importlib.import_module("termcolor")
  except Exception as err:
    print("An error occured while downloading a dependency: termcolor", err)
    exit(1)

from datetime import datetime


def printQuestion(content):
  print("")
  print(content)
  print("")

# %% [markdown]
# ## 1. Introduction :
#
# Soit la variable suivante:

# %%
g = [[1,2,3,], ["a", "b", "c"]]

# %% [markdown]
# ### 1. Quel est le contenu de g[0][1] ? de g[1][2] ?
printQuestion("1. Quel est le contenu de g[0][1] ? de g[1][2] ?")

# %%
print("Le contenu de g[0][1] est:", g[0][1])
print("Le contenu de g[1][2] est:", g[1][2])

# %% [markdown]
# ### 2. Comment afficher g sous la forme de 2 lignes de 3 valeurs séparées par des espaces ?
printQuestion("2. Comment afficher g sous la forme de 2 lignes de 3 valeurs séparées par des espaces ?")

# %%
for dataline in g:
  for data in dataline:
    print(data, end=" ")
  print("")

# %% [markdown]
# ### 3. Comment afficher g sous la forme de 3 lignes et 2 colonnes ?
printQuestion("3. Comment afficher g sous la forme de 3 lignes et 2 colonnes ?")

# %%
for x  in range(0, len(g[0])):
  for y in g:
    print(y[x], end=" ")
  print("")

# %% [markdown]
# ## 2.Bataille navale :
# 
# Le but du jeu est de « couler » tous les bateaux du joueur adverse. Chaque joueur possède les bateaux suivants :
# 
# - 1 PORTE_AVION (noté P) de taille 4
# - 2 CROISEURS (noté C) de taille 3
# - 3 TORPILLEURS (noté T) de taille 2
# - 4 SOUS_MARIN (noté S) de taille 1
# 
# Ils sont placés secrètement, sans se toucher, sur une grille carrée de 8 lignes par 10 colonnes (dans notre cas).
# Chaque joueur, à son tour, « fait feu » sur une case donnée de l'adversaire. S'il s'agit du morceau d'un bateau ennemi,
# l'adversaire indique « touché » et le joueur attaquant peut « tirer » une seconde fois. Quand tous les morceaux d’un
# bateau sont touchés, on doit dire « touché-coulé ». Si un joueur manque sa cible, on dit alors « dans l'eau » et le tour
# du joueur est terminé. Le joueur ayant coulé le premier, tous les bateaux de son adversaire a gagné la partie.
# 
# ### 1. Tester le jeu en ligne par exemple sur http://fr.battleship-game.org/.
# ### 2. On décide de représenter les morceaux de chaque bateau par une lettre et les cases vides par un tiret. Créer manuellement une liste de liste contenant les 8 lignes et les 10 colonnes de la grille suivante :
# 
# ![fig1-2](./src/fig1-2.png)

# %%
# - C C C - - - T T -
# - - - - - - - - - -
# C - - - - - - - - -
# C - P P P P - - - T
# C - - - - - - - - T
# - - S - T - - - - -
# - - - - T - - S - S
# - S - - - - - - - -

def createBoard(width: int, height: int)-> list:
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

test_board = [
  ["-", "C", "C", "C", "-", "-", "-", "T", "T", "-"],
  ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
  ["C", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
  ["C", "-", "P", "P", "P", "P", "-", "-", "-", "T"],
  ["C", "-", "-", "-", "-", "-", "-", "-", "-", "T"],
  ["-", "-", "S", "-", "T", "-", "-", "-", "-", "-"],
  ["-", "-", "-", "-", "T", "-", "-", "S", "-", "S"],
  ["-", "S", "-", "-", "-", "-", "-", "-", "-", "-",]
]

main_board = createBoard(10, 8)

# %% [markdown]
# ### 3. Créer ensuite une fonction qui affiche uniquement le contenu d’une grille (Voir fig. 1 : Version simple).
# 
# EN OPTION : Afficher la numérotation des lignes et des colonnes (Voir fig. 2). Pour les colonnes, on peut,
# soit utiliser une liste contenant les lettres ABCD..., soit afficher la lettre à partir de son code ASCII : la
# fonction ord(c) donne le code ASCII de la lettre c et la fonction chr(x) donne le caractère
# correspondant au code ASCII x.

# %%
def showBoard(board, show_index=False):
  global alphabet

  if show_index:
    for i in range(0, len(board[0])):
      ### If first letter, automatically add a space in order to re-caliber the ouput
      if i == 0:
        print(" ", end=" ")
      print(alphabet[i], end=" ")
    print("")
  for y in range(0, len(board)):
    for x in range(0, len(board[y])):
      if x == 0:
        print(y+1 if show_index else "", end=" ")
      print(board[y][x][0], end=" ")
    print("")

alphabet = [ "A", "B", "C", "D", "E",
    "F", "G", "H", "I", "J", "K", "L",
    "M", "N", "O", "P", "Q", "R", "S",
    "T", "U", "V", "W", "X", "Y", "Z"]

print("Only the Board:")
showBoard(test_board)
print("\nNow with the indexes:")
showBoard(test_board, True)

# %% [markdown]
# ### 4. Comment obtenir le contenu de la case « C4 » ? Faire une fonction qui transforme la chaîne passée en paramètre en coordonnées de la case dans la grille (i pour les lignes et j pour les colonnes).
# Pour la valeur C4, on doit obtenir i=3 et j=2. Tester ensuite votre fonction pour les cases « H7 » et « F6 ».
# 
# ```py
# cStr="C4"
# i,j=getCoordonnees(cStr)
# print("La case",cStr,"i =",i,"j =",j,"contient :",g[i][j])
# ```

# %%
def getCoordonnees(case_stringed):
  global alphabet
  x,y = case_stringed[0], int(case_stringed[1])
  ### We substract 1 to y because we start at 1
  return (y-1, alphabet.index(x))

cStr="C4"
cStr1="H7"
cStr2="F6"
i,j = getCoordonnees(cStr)
i1,j1 = getCoordonnees(cStr1)
i2,j2 = getCoordonnees(cStr2)
print("La case", cStr, "i =", i, "j =", j, "contient :", test_board[i][j])
print("La case", cStr1, "i =", i1, "j =", j1, "contient :", test_board[i1][j1])
print("La case", cStr2, "i =", i2, "j =", j2, "contient :", test_board[i2][j2])

# %% [markdown]
# ### 5. Comment noter les cases indiquées par l’adversaire dans la grille, @ quand un bateau est touché et * quand c’est dans l’eau.

# %%
def getAction(cell, board):
  """A simple function returning a str object
    following the type of action it has been.
    *A duplicate of getIfHit()*

    Args
    ----
      `cell`, str: A str object containing the cell with its indexes, example: C4
      `board`, list: A list object containing the board to be affected by this action
  """

  y,x = getCoordonnees(cell)
  if board[y][x] != "-":
    return "@"
  else:
    return "*"


def getIfHit(cell, board):
  y, x = getCoordonnees(cell)
  if board[y][x] != "-":
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

print("Action result of C4 hit:", getAction("C4", test_board))
print("Action result of F6 hit:", getAction("F6", test_board))

# %% [markdown]
# ### 6. Faire une boucle dans laquelle on entre une case au clavier, on modifie la grille et on la ré-affiche.

# %%
def getActionIntoAction(cell, board):
  y,x = getCoordonnees(cell)
  board[y][x] = getAction(cell, board)

def cleanNShow(board_in_question):
  if os.name == "posix":
    os.system("clear")
  else:
    os.system("cls")
  showBoard(board_in_question, True)


def cleanOutput():
  if os.name == "posix":
    os.system("clear")
  else:
    os.system("cls")


def liveModifications():
  try:
    while True:
      cleanNShow(test_board)
      key = input("Enter a cell of the board from above: ")
      showActionResult((key, test_board))
      getActionIntoAction(key, test_board)
  except KeyboardInterrupt:
    cleanOutput()
    print("Process Interrupted")
    return 0


# %% [markdown]
# ### 8. Comment déterminer quand tous les bateaux sont coulés ?

# %% [markdown]
# On scanne toutes les cases et on voit si on tombe sur une des lettres utilisées (P,C,T,S) pour afficher un des navires

# %%
def getAliveOrNot(player_board):
  stillAlive = False
  for line in player_board:
    for cell in line:
      if cell in ("P", "C", "T", "S"):
        if not stillAlive:
          stillAlive = True
  return stillAlive

getAliveOrNot(test_board)

# %% [markdown]
# ### 9. Comment afficher les coups de l’adversaire en couleur dans le terminal (rouge pour « touché » et bleu pour « dans l’eau ») voir par exemple le module termcolor (Si besoin : pip3 install termcolor).

# %% [markdown]
# On peut simplement utiliser une des fonctions définies au dessus, soit getIfHit() soit getAction(). Sur un soucis de practicalité (et de performances) on utilisera plus getIfHit() qui nous sort un boolean.

# %%
def showBoardColored(board, show_index=False):
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
      curr_cell = board[y][x][0]

      if x == 0:
        print(y+1 if show_index else "", end=" ")

      if not curr_cell in ("@", "*"):
        print(curr_cell, end=" ")
      else:
        if curr_cell == "@":
          print(termcolor.colored(curr_cell, "red"), end=" ")
        else:
          print(termcolor.colored(curr_cell, "blue"), end=" ")
    print("")


tested_board = [
    ["-", "C", "C", "C", "-", "-", "-", "T", "T", "-"],   # - C C C - - - T T -
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],   # - - - - - - - - - -
    ["C", "-", "*", "-", "-", "-", "-", "-", "-", "-"],   # C - - - - - - - - -
    ["C", "-", "@", "P", "P", "P", "-", "-", "-", "T"],   # C - P P P P - - - T
    ["C", "-", "-", "-", "-", "-", "-", "-", "-", "T"],   # C - - - - - - - - T
    ["-", "-", "S", "-", "T", "-", "-", "-", "-", "-"],   # - - S - T - - - - -
    ["-", "-", "-", "-", "T", "-", "-", "S", "-", "S"],   # - - - - T - - S - S
    ["-", "S", "-", "-", "-", "-", "-", "-", "-", "-", ]   # - S - - - - - - - -
]

showBoardColored(tested_board)

# %% [markdown]
# ### 10. Comment sauvegarder une grille dans un fichier ? Faire une fonction.

# %%
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

saveState(test_board)

# %% [markdown]
# ### 11. Comment lire un fichier de sauvegarde ? Faire une fonction.

# %%

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


new_state = loadState("save-2022-10-18.txt")
showBoard(new_state)


# %% [markdown]
# ## 3. Mise en place des bateaux :
#
# Dans cette partie, on désire pouvoir placer les bateaux sur une grille vide.
#
#

# %% [markdown]
# ### 1. Créer une fonction qui fabrique une grille vide.

# %%
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

def cleanBoard(board: list) -> list:
  """A function used to clean a board after using it or iterating with it"""

  for y in range(0, len(board)):
    for x in range(0, len(board[y])):
      if board[y][x] != "-":
        board[y][x] == "-"


# %% [markdown]
# ### 2. Comment placer le PORTE_AVION (noté P) de taille 4, en position B2 orienté en vertical pour obtenir la grille de la figure 3 ?
#
# ![fig3-4](./src/fig3-4.png)

# %%
ship_data = {
    "carrier": (4, "P"),
    "cruisers": (3, "C"),
    "torpedo-boat": (2, "T"),
    "submarine": (1, "S")
}

def placeShip(ship_name, start_cell, axis, board):
  global ship_data

  cases_to_place, letter_to_place = ship_data[ship_name]
  start_cell_y, start_cell_x = getCoordonnees(start_cell)
  if axis.lower() == "v":
    if start_cell_y+cases_to_place < len(board):
      for i in range(0, cases_to_place):
        board[start_cell_y+i][start_cell_x] = letter_to_place
    else:
      return IndexError("The cell is too much near the border to be placed vertically")
  elif axis.lower() == "h":
    if start_cell_x+cases_to_place < len(board[start_cell_y]):
      for i in range(0, cases_to_place):
        board[start_cell_y][start_cell_x+i] = letter_to_place
    else:
      return IndexError("The cell is too much near the border to be placed horizontally")
  else:
    return KeyError("We can't find any other axis than v or h")

my_board = createBoard(10, 8)
placeShip("carrier", "B2", "v", my_board)
showBoard(my_board, True)

# %% [markdown]
# ### 3. Que faut-il changer pour obtenir la figure 4, avec le bateau en horizontal ?

# %%
board2 = createBoard(10, 8)
placeShip("carrier", "B2", "h", board2)
showBoard(board2, True)

# %% [markdown]
# ### 4. Créer alors 2 fonctions (placeBateauHorizontal() et placeBateauVertical()) pour placer des bateaux sur une grille à partir de la position souhaitée, de la lettre représentant le bateau et de sa taille.

# %%
def placeBateauHorizontal(board, ship_name, start_cell):
  placeShip(ship_name, start_cell, "h", board)

def placeBateauVertical(board, ship_name, start_cell):
  placeShip(ship_name, start_cell, "v", board)

# %% [markdown]
# ### 5. Si au lieu de placer le PORTE_AVION en B2, on choisit la case H6. Pourquoi ne peut-on pas placer le bateau en horizontal ou en vertical ? Quel test faut-il faire ?
# Créer alors les fonctions verifHorizontal(grille,pos,taille) et verifVertical(grille,pos,taille).

# %%
t_board = createBoard(10, 8)
placeShip("carrier", "H6", "v", t_board)

# %%
def verifHorizontal(grille, pos, taille):
  """Une fonction pour vérifier si on peut placer un bateau horizontallement.

  Args
  ---
    `grille`, list: La grille de jeu
    `pos`, tuple | list: Un tuple/Une liste de deux éléments ayant les coords x et y de la cellule
    `taille`, int: Un entier qui donne la taille du bateau à placer

  Returns
  ---
    Boolean: True if it's ok, False otherwise
  """

  if pos[1]+taille < len(grille[pos[0]]):
    return True
  return False

def verifVertical(grille, pos, taille):
  """Une fonction pour vérifier si on peut placer un bateau horizontallement.

  Args
  ---
    `grille`, list: La grille de jeu
    `pos`, tuple | list: Un tuple/Une liste de deux éléments ayant les coords x et y de la cellule
    `taille`, int: Un entier qui donne la taille du bateau à placer

  Returns
  ---
    Boolean: True if it's ok, False otherwise
  """

  if pos[0]+taille < len(grille):
    return True
  return False

empty_board = createBoard(10, 8)
print(verifHorizontal(empty_board, getCoordonnees("F6"), ship_data["carrier"][0]), "<-- Should be True")
print(verifVertical(empty_board, getCoordonnees("H6"), ship_data["carrier"][0]), "<-- Should be False")

# %% [markdown]
# ### 6. Lorsque l’on doit placer les autres bateaux, il faut aussi vérifier que les bateaux ne se superposent pas et qu’ils ne se touchent pas également (Voir figures 1 et 2). Par exemple les grilles des figures 5 et 6 ci-dessous sont incorrectes :
# 
# ![fig5-6](./src/fig5-6.png)

# %%
def verifOtherShips(board, ship, start_cell, axis, debug=False):
  global ship_data
  test_board = board.copy() ### We copy the object as we're iterating with it, in order to not break the supposedly good structure
  shipd = ship_data[ship]

  ship_over = False
  ship_touchy = False

  if debug:
    print(f"DATA: board: {board}, ship: {ship}, start_cell: {start_cell}, axis: {axis}, shipd: {shipd}, (ship_over, ship_touchy): ({ship_over}, {ship_touchy})")

  ### The test of overlapping
  ### We suppose this test came as the last and as such, we're not verifying once again the size
  for i in range(0, shipd[0]):
    if axis == "v":
      if board[start_cell[0]+i][start_cell[1]][0] == "-":
        if debug:
          print(board[start_cell[0]+i][start_cell[1]])
        continue
      else:
        ship_over = True
        break
    elif axis == "h":
      if board[start_cell[0]][start_cell[1]+i][0] != "-":
        ship_over = True
        break

  ### The test of no-touch area
  ###
  ###
  ### V axis:
  ###
  ###     D E F         |           D E F     D E F     D E F     D E F
  ###   0 - - -      ---|----- x  0 - - -   0 - - -   0 * * *   0 - - -
  ###   1 - C -         |         1 * C -   1 - C *   1 - C -   1 - C -
  ###   2 - C -         |         2 * C -   2 - C *   2 - C -   2 - C -
  ###   3 - C -         |         3 * C -   3 - C *   3 - C -   3 - C -
  ###   4 - - -         y         4 - - -   4 - - -   4 - - -   4 * * *
  ###
  ###   Start: E1, End: E3
  ###     1st wave (D1->D3): Start.y + Start.x-1 -> End.y + End.x-1
  ###     2nd wave (F1->F3): Start.y + Start.x+1 -> End.y + End.x+1
  ###     3rd wave (D0->F0): Start.y-1 + Start.x-1 -> End.y-1 + End.x+1
  ###     4th wave (D4->F4): Start.y+1 + Start.x-1 -> End.y+1 + End.x+1
  ###
  ### H axis:                         1st wave      2nd wave      3rd wave      4th wave
  ###     D E F G H       |             D E F G H     D E F G H     D E F G H     D E F G H
  ###   0 - - - - -    ---|------- x  0 - - - - -   0 - - - - -   0 - - - - -   0 - - - - -
  ###   1 - P - - -       |           1 - P - - -   1 - P - - -   1 - P - - -   1 - P - - -
  ###   2 - P - - -       |           2 - * * * -   2 - P - - -   2 * P - - -   2 - P - - *
  ###   3 - C C C -       |           3 - C C C -   3 - C C C -   3 * C C C -   3 - C C C *
  ###   4 - P - - -       |           4 - P - - -   4 - * * * -   4 * P - - -   4 - P - - *
  ###   5 - - - - -       y           5 - - - - -   5 - - - - -   5 - - - - -   5 - - - - -
  ###
  ###  Start: E4, End: G4
  ###   1st wave (E3->G3): Start.y-1 + Start.x -> End.y-1 + End.x
  ###   2nd wave (E5->G5): Start.y+1 + Start.x -> End.y+1 + End.x
  ###   3rd wave (D3->D5): Start.y-1 + Start.x-1 -> End.y+1 + End.x-1
  ###   4th wave (H3->H5): Start.y-1 + Start.x+1 -> End.y+1 + End.x+1
  ###
  ###//////////////////////////////////////

  if ship_over:

    if axis == "v":
      ### Y-1
      for i in range(0, shipd[0]):
        if debug:
          print("I:", i, board[start_cell[0]+i][start_cell[1]-1], True if board[start_cell[0]+i][start_cell[1]-1][0] == "-" else False)
        if board[start_cell[0]+i][start_cell[1]-1][0] != "-":
          ship_touchy = True
          break

      ### Y+1
      for i in range(0, shipd[0]):
        if debug:
          print("I:", i, board[start_cell[0]+i][start_cell[1]+1], True if board[start_cell[0]+i][start_cell[1]+1][0] == "-" else False)
        if board[start_cell[0]+i][start_cell[1]+1][0] != "-":
          ship_touchy = True
          break

      ### X-1
      for i in range(0, 3):
        if debug:
          print("I:", i, board[start_cell[0]-1][start_cell[1]-1+i], True if board[start_cell[0]-1][start_cell[1]-1+i][0] == "-" else False)
        if board[start_cell[0]-1][start_cell[1]-1+i][0] != "-":
          ship_touchy = True
          break

      ### X+1
      for i in range(0, 3):
        if debug:
          print("I:", i, board[start_cell[0]+1][start_cell[1]+1+i], True if board[start_cell[0]+1][start_cell[1]+1+i][0] == "-" else False)
        if board[start_cell[0]+1][start_cell[1]+1+i][0] != "-":
          ship_touchy = True
          break


    elif axis == "h":
      ### X-1
      for i in range(0, 3):
        if debug:
          print("I:", i, board[start_cell[0]-1][start_cell[1]+i], True if board[start_cell[0]-1][start_cell[1]+i][0] == "-" else False)
        if board[start_cell[0]-1][start_cell[1]+i][0] != "-":
          ship_touchy = True
          break

      ### X+1
      for i in range(0, 3):
        if debug:
          print("I:", i, board[start_cell[0]+1][start_cell[1]+i], True if board[start_cell[0]+1][start_cell[1]+i][0] == "-" else False)
        if board[start_cell[0]+1][start_cell[1]+i][0] != "-":
          ship_touchy = True
          break

      ### Y-1
      for i in range(0, shipd[0]):
        if debug:
          print("I:", i, board[start_cell[0]-1+i][start_cell[1]-1], True if board[start_cell[0]-1+i][start_cell[1]-1][0] == "-" else False)
        if board[start_cell[0]+i][start_cell[1]-1][0] != "-":
          ship_touchy = True
          break

      ### X+1
      for i in range(0, shipd[0]):
        if debug:
          print("I:", i, board[start_cell[0]-1+i][start_cell[1]+1], True if board[start_cell[0]-1+i][start_cell[1]+1][0] == "-" else False)
        if board[start_cell[0]+i][start_cell[1]+1][0] != "-":
          ship_touchy = True
          break




  if debug:
    print(f"Ship_Over: {ship_over}, Ship_Touchy: {ship_touchy}")
  if ship_over: # If we're overlapping, ofc we're touching the ships
    return False

  if ship_touchy:
    return False

  return True

my_board = createBoard(10, 8)
placeShip("carrier", "B2", "v", my_board)
showBoard(my_board, True)
#print("VérifBoard:", verifOtherShips(my_board, "submarine", getCoordonnees("F5"), "v"))
print("VérifBoard:", verifOtherShips(my_board, "cruisers", getCoordonnees("B4"), "h"))
placeShip("cruisers", "B4", "h", my_board)
showBoard(my_board, True)

# %%
def placeShip(ship_name, start_cell, axis, board):
  global ship_data

  cases_to_place, letter_to_place = ship_data[ship_name]
  start_cell_y, start_cell_x = getCoordonnees(start_cell)
  if axis.lower() == "v":
    if verifVertical(board, (start_cell_y, start_cell_x), cases_to_place):
      if verifOtherShips(board, ship_name, (start_cell_y, start_cell_x), axis):
        for i in range(0, cases_to_place):
          board[start_cell_y+i][start_cell_x] = letter_to_place
      else:
        return KeyError() # "Another ship is in proximity or over one of the cells used"
    else:
      return IndexError() # "The cell is too much near the border to be placed vertically"
  elif axis.lower() == "h":
    if verifHorizontal(board, (start_cell_y, start_cell_x), cases_to_place):
      if verifOtherShips(board, ship_name, (start_cell_y, start_cell_x), axis):
        for i in range(0, cases_to_place):
          board[start_cell_y][start_cell_x+i] = letter_to_place
      else:
        return KeyError() # "Another ship is in proximity or over one of the cells used"
    else:
      return IndexError() # "The cell is too much near the border to be placed horizontally"
  else:
    return KeyError("Unknown axis") # "We can't find any other axis than v or h"

  return True # We did achieve a placement

my_board = createBoard(10, 8)
placeShip("carrier", "B2", "v", my_board)
showBoard(my_board, True)
print("VérifBoard:", verifOtherShips(my_board, "cruisers", getCoordonnees("B7"), "h"))
placeShip("cruisers", "B7", "h", my_board)
showBoard(my_board, True)

# %% [markdown]
# ### 7. Faire une boucle pour placer tous les bateaux sur la grille en demandant à chaque fois à l’utilisateur la position et l’orientation.

# %%
def startGame(ship_list):
  global game_board

  usable_data = [[ship, 0] for ship in ship_list]
  result = None

  for ship in usable_data:
    while ship[1] == 0:
      print(f"Please place a {ship[0].upper()} on the board:")
      showBoard(game_board, True)

      cell = input("Enter your cell here: ")
      axis = input("Enter the axis here [H/V]: ").lower()
      try:
        result = placeShip(ship[0], cell, axis, game_board)
        ship[1] = 1
      except IndexError or KeyError or KeyError("Unknown axis") as err:
        if err == KeyError("Unknown axis"):
          print("You can't put something else than H/h or V/v")
        else:
          print("Either the Axis or the Cell is wrong")
      cleanOutput()


ship_to_place = ["carrier", "cruisers", "cruisers", "torpedo-boat", "torpedo-boat", "torpedo-boat", "submarine", "submarine", "submarine", "submarine" ]
game_board = createBoard(10,8)

# %% [markdown]
# ### 8. Comment générer une grille avec un placement aléatoire (Voir module random et la fonction randint()) ?

# %%
from random import randint, choice


def startRandomisedGame(ship_list, gameboard):
  global alphabet

  placed = False
  randx = ""
  randy = 0
  axis = "h"

  for i in range(0, len(ship_list)):
    print(f"Ship n°{i}: {ship_list[i]}, {randy}{randx}, {axis} => {placed}, {ship_list}")


    while placed:
      randx = choice(alphabet[:9])
      randy = randint(0, 8)
      axis = choice(["h", "v"])

      placed = placeShip(ship_list[i], f"{randx}{randy}", axis, gameboard)

  print("See these ships, they're beautiful (and randomly placed):")
  showBoard(gameboard, True)

startRandomisedGame(ship_to_place, game_board)

# %% [markdown]
# ## 4. Programmation réseau :
# 
# Dans cette partie, on désire pouvoir jouer à distance entre 2 machines. On vous fourni un exemple de client/serveur
# réalisant un échange de textes entre 2 programmes.

# %% [markdown]
# ### 1. Tester les fichiers fournis : lancer en premier bnServer-base.py dans une console et bnClientbase.py dans une autre.
# 
# Modifier les message envoyés entre le client et le serveur.

# %% [markdown]
# ### 2. Adapter alors les 2 programmes pour réaliser une connexion distante entre 2 joueurs de bataille navale.
# 
# On pourra partir avec une grille sauvegardée en fichier des 2 cotés ou bien utiliser le système aléatoire de la question 3.8. Pour simplifier un peu le système, on ne fera uniquement qu’un 1 seul coup par joueur.\
# Le client jouera donc en premier en envoyant une position B3 par exemple et le serveur devra répondre en fonction de sa grille (TOUCHE ou bien DANS L’EAU). Ensuite ce sera au tour du serveur d’envoyer une position, etc... A chaque coup on devra afficher la grille personnelle et la grille de tir.

# %% [markdown]
# ### 3. Finaliser le jeu pour que quand un joueur touche un bateau, il puisse rejouer à nouveau.


