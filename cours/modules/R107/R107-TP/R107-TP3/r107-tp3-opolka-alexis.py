#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###/////////////////////////////////////////////////////////////////////////
###
### Imports
###
###/////////////////////////////////////////////////////////////////////////
import r107_tp2_lib as tp_lib
import sys, os

###/////////////////////////////////////////////////////////////////////////
###
### Défi 1 - Pokemon Nombres Commun
###
###/////////////////////////////////////////////////////////////////////////

def lureMewtwo():
  # base: z || 2 = x,y où x+y = 11
  r = []
  for i in range(29, 1000): # Want every number under 1,000
    units = i % 10
    stack = i % 100
    dozens = stack // 10
    hundreds = i // 100
    sum = units+dozens+hundreds
    if sum == 11:
      r.append(i)

    #print(i, hundreds, dozens, units, sum, True if sum == 11 else False)

  return r

def lureOssatueur():
  # base: 7*x
  r = []
  i = 0
  curr_nbr = 0
  while 7*(i+1) < 1000: # Want evry number under 1,000
    i += 1
    curr_nbr = 7*i
    r.append(curr_nbr)
  return r

def lureThemAll(debug=False):
  ### A simple function used to compile the action of the two
  ### above
  lures_of_ossatueur = lureOssatueur()
  lures_of_mewtwo = lureMewtwo()
  r = []

  if debug:
    print(f"Tab 1 (Ossatueur): {lures_of_ossatueur}\n\nTab2 (Mewtwo): {lures_of_mewtwo}")

  for lure1 in lures_of_ossatueur:
    for lure2 in lures_of_mewtwo:
      if lure1 == lure2: ### We're required to return the numbers used to lure Ossatueur and Mewtwo
        r.append(lure1)

  return r

###/////////////////////////////////////////////////////////////////////////
###
### Défi 2 - Chiffres Préferés
###
###/////////////////////////////////////////////////////////////////////////

def chiffresPreferes(nbr):
  snbr = str(nbr) # Used to go through the number after, Switched from the dividing method to the str one
  curr_found = []
  for char in snbr:
    if char == "1" or char == "6": # Required to have either 1 or 6 in the number
      curr_found.append(snbr)
  return True if len(curr_found) > 0 else False

def findChiffresPreferes(start, end):
  l = [i for i in range(start, end+1)]
  r = []
  for nbr in l:
    if chiffresPreferes(nbr): # If the number has either 1 or 6
      r.append(nbr) # Add it to the final list we'll return

  return (r, len(r))

###/////////////////////////////////////////////////////////////////////////
###
### Défi 3 - Mirroir Ajout
###
###/////////////////////////////////////////////////////////////////////////

def getPalindrome(number: int | list | tuple, steps: int=0):
  ### Get a number, return it and see if it's a Palindrome
  ### If not add it to the start number and make a recursive call with the sum

  if isinstance(number, int):
    number_list = [int(nbr) for nbr in str(number)]
    number_str = str(number)
    number_reversed = [number_list[i] for i in range(len(number_list)-1, -1, -1)]
    number_reversed_str = "".join([str(nbr) for nbr in number_reversed])
    number_reversed_int = int(number_reversed_str)
    result_number = number_reversed_int + number

    ### print(True if number_str == number_reversed_str else False, number_list, number_reversed, number, number_reversed_int, result_number)

    ### Recursive calls instructions
    if number_str != number_reversed_str:
      result_number, steps = getPalindrome(result_number, steps+1)
      return (result_number, steps)
    else:
      return (number, steps)

  ### The case where we get a sequence (list, tuple) as parameters and we need to return
  ### the list of Palidromes and the steps required to get it from the number given

  elif isinstance(number, (list, tuple)):
    results = []

    for curr_nbr in number:
      curr_steps = 0
      curr_nbr_str = str(curr_nbr)
      curr_nbr_reversed = [int(curr_nbr_str[i]) for i in range(len(curr_nbr_str)-1, -1, -1)]
      curr_nbr_reversed_str = "".join([str(nbre) for nbre in curr_nbr_reversed])
      curr_nbr_reversed_int = int(curr_nbr_reversed_str)
      curr_result_nbr = curr_nbr_reversed_int + curr_nbr

      if curr_nbr_str != curr_nbr_reversed_str:
        curr_result_nbr, curr_steps = getPalindrome(curr_result_nbr, curr_steps+1)

        ### Loses some speed at execution but is able to return the specific type
        ### that was given - helps to gain an identical I/O object type.
        ### It can be said that the result is a list, indeed but I do think
        ### that making a list is better than a tuple when we are working with
        ### and the important data is stored in tuples so we don't really care
        ### if the order of results stays the same or not.

        if isinstance(number, tuple):
          results.append((curr_result_nbr, curr_steps))
        else:
          results.append([curr_result_nbr, curr_steps])

      else:
        if isinstance(number, tuple):
          results.append((curr_nbr, curr_steps))
        else:
          results.append([curr_nbr, curr_steps])

    return results

###/////////////////////////////////////////////////////////////////////////
###
### Défi 4 - Fourchelangue
###
###/////////////////////////////////////////////////////////////////////////
def translateToFourchelangue(phrase):
    # HFH FFH SHS SHH SSH FHF FSS HFF  HHH SFS FFS FHS SSF
    #  A   B   C   D   E   F   G   H   IJ  K   L   M   N
    # FHH HHF SFF FSF FSH HHS  FFF SSS HFS SHF SFH
    #  O   P   Q   R   S   T   UV  W   X   Y   Z

    alphabet = {
    "A": "HFH", "B": "FFH", "C": "SHS", "D": "SHH", "E": "SSH", "F": "FHF", "G": "FSS",
    "H": "HFF", "I": "HHH", "J": "HHH", "K": "SFS", "L": "FFS", "M": "FHS", "N": "SSF",
    "O": "FHH", "P": "HHF", "Q": "SFF", "R": "FSF", "S": "FSH", "T": "HHS", "U": "FFF",
    "V": "FFF", "W": "SSS", "X": "HFS", "Y": "SHF", "Z": "SFH", " ": "HS"
    }
    phrase_in_fourchelangue = ""

    for char in phrase:
        phrase_in_fourchelangue += alphabet[char.upper()]

    return phrase_in_fourchelangue


### TODO: Finish this function which I surely have a problem of algorithm
def translateFromFourchelangue(fourche_phrase):

  #------------------------------------------------------------
  #  --- Fourchelangue dictionary ---
  #
  # HFH FFH SHS SHH SSH FHF FSS HFF  HHH SFS FFS FHS SSF
  #  A   B   C   D   E   F   G   H   IJ  K   L   M   N
  # FHH HHF SFF FSF FSH HHS  FFF SSS HFS SHF SFH
  #  O   P   Q   R   S   T   UV  W   X   Y   Z
  #-----------------------------------------------------------

  alphabet = {
  "HFH": "A", "FFH": "B", "SHS": "C", "SHH": "D", "SSH": "E", "FHF": "F", "FSS": "G",
  "HFF": "H", "HHH": ("I", "J"), "SFS": "K", "FFS": "L", "FHS": "M", "SSF": "N",
  "FHH": "O", "HHF": "P", "SFF": "Q", "FSF": "R", "FSH": "S", "HHS": "T", "FFF": ("U", "V"),
  "SSS": "W", "HFS": "X", "SHF": "Y", "SFH": "Z", "HS": " "
  }
  double_case_dict = {
    "I": "J", "J": "I",
    "U": "V", "V": "U"
  }

  translated_phrase = ""
  curr_phrase = []
  char_hist = []
  curr_word = ""
  curr_tl_char = ""
  chars_used = ""
  new_word = ""
  correct_word = False
  first_time_first_letter = False
  first_time_second_letter = False
  ### A little explanation of the values used:
  ### 0: None have been used, 1: only the first character has been used, 2: only the second character has been used,
  ### 3: If two double-letter cases are detected we did the first then the second, 4: We did the reverse of the third - the second then the first
  method_used = 0
  searched = False



  ### 1st step: We do a dummy translation from the fourchelangue
  method_used = 1
  for char in fourche_phrase:
    curr_tl_char += char

    if curr_tl_char in alphabet.keys():
      print(f"{curr_tl_char} -> {alphabet[curr_tl_char]}")

      if curr_tl_char == "HS":
        curr_phrase.append(curr_word)
        char_hist.append(chars_used)
        curr_word = ""
        curr_tl_char = ""
        chars_used = ""
      else:
        curr_word = curr_word + alphabet[curr_tl_char][0]
        chars_used += curr_tl_char
        curr_tl_char = ""


  ### Tenter à modifier par les mots
  ### 2nd step: We do a check of each word of the known double-letter cases in our translation
  ### Caution: It means a user-script interaction is required on this version of the function
  for i in range(0, len(curr_phrase)):
    next_index = 0
    searched = False
    double_case_letter = []
    list_word = [letter for letter in curr_phrase[i]]
    for index in range(0, len(curr_phrase[i])):
      if curr_phrase[i][index] in ("I", "J", "U", "V"):
        searched = True
        double_case_letter.append([index, curr_phrase[i][index]])

    if searched:
      clean_output()
      x = input(f"Is this correct '{curr_phrase[i]}' [Y/N]: ")
      if x.lower() == "y":
        continue
      else:
        if method_used == 1:
          method_used = 2

        for letter in double_case_letter:
          correct = False
          while not correct:
            x = input(f"Is this '{''.join(list_word)}' correct [Y/N]:")
            if x.lower() == "y":
              correct = True
            else:
              if list_word[letter[0]] == letter[1]:
                list_word[letter[0]] = double_case_dict[letter[1]]
              else:
                list_word[letter[0]] = letter[1]

        curr_phrase[i] = "".join(list_word)

  returnable_phrase = createStrFromList(curr_phrase)

  return returnable_phrase

###/////////////////////////////////////////////////////////////////////////
###
### Défi 5 - CodeCabine
###
###/////////////////////////////////////////////////////////////////////////
def checkTheCheckList(number):
  checklist = {
    1: False,
    2: False,
    4: False,
    6: False,
    7: False
  }

  squared = number ** 2
  ssquared = str(squared)

  for snbr in  ssquared:
    nbr = int(snbr)
    if nbr in checklist.keys():
      if not checklist[nbr]:
        checklist[nbr] = True
    else:
      ### If we have a number that isn't in the checklist it means
      ### that it's not the number we're searching for so we don't need
      ### more processor ressource for that process and pass to the next one
      return False

  for value in checklist.values():
    ### If a value is set to False it means we don't use it in the squared
    ### number then it's not the number we're searching for.
    if value == False:
      return False

  return True

def codecabine(start_code, number_to_code_to_return):
  list_number = []
  x = 0
  ### From the number we know to a max number which is the sum
  ### of the start_code and 10,001 <- 10001 because we want to go to the 10,000th one.
  ### High probability of not taking much processor and/or RAM
  ### When dealing with "little" numbers (< 1,000,000) because we surely
  ### should find a squared number corresponding in a 10000+ iterations
  for number in range(start_code+1, start_code+10001):
    x += 1
    if len(list_number) < number_to_code_to_return:
      if checkTheCheckList(number):
        list_number.append((x, number))
    else:
      break

  return list_number

###/////////////////////////////////////////////////////////////////////////
###
### Défi 6 - Goldbach
###
###/////////////////////////////////////////////////////////////////////////
def goldbach(numbers_list, number_of_possibility=0):
  ### if number_of_possibility == 0 -> we want every couple possible
  r = []
  for number in numbers_list:
    premiers = tp_lib.getNonNullNbrs(tp_lib.methEratosthene(tp_lib.createListToMax(2, number), False))
    couples = []

    for x in range(len(premiers)-1, 0, -1):
      for y in range(x, 0, -1):
        if premiers[x] + premiers[y] == number:
          # print(f"NBR: {number}, X: ({x}, {premiers[x]}), Y: ({y}, {premiers[y]}), SUM: {premiers[x] + premiers[y]}, {True if premiers[x] + premiers[y] == number else False}, L: {premiers}")
          couples.append((premiers[x], premiers[y]))

    if number_of_possibility > 0:
      if number_of_possibility == 1:
        ### We delete the possibility of having multiples unused objects holding data
        ### Output: [(item1), (item2), (item3), etc.]
        r.append(couples[0])
      else:
        ### May be in some cases useless to have a list holding the couples
        ### but we do not make an exception in order to have an easier way go through
        ### it in possible later steps
        r.append(couples[:number_of_possibility])
    else:
      ### We want every case possible, go from zero to the length of the list
      ### -> Dynamically create a list
      r.append(couples[:len(couples)])

  return r

###/////////////////////////////////////////////////////////////////////////
###
### Utils
###
###/////////////////////////////////////////////////////////////////////////

def clean_output():
  if os.name == "posix":
    os.system("clear")
  else:
    os.system("cls")

def createStrFromList(liste):
  r = ""
  for elem in liste:
    r = r + " " + elem

  return r



###/////////////////////////////////////////////////////////////////////////
###
### Affichage
###
###/////////////////////////////////////////////////////////////////////////

fourched_lang = translateToFourchelangue('BONJOUR HARRY')
gb1 = (24, 6, 12, 16)
gb2 = (4878, 8704, 7320, 7618, 7964, 5356, 1152, 8566, 5396, 1152, 8566, 5396, 7678, 2818, 1060, 9306, 1362, 7912, 5948, 7974, 3122, 3362, 3620, 4058, 4710, 7210, 304, 6774, 738, 7644, 928, 2636, 4752, 8564, 2772, 5792, 5120, 2266, 6002, 9020, 8006, 8584, 5730, 5416, 2662, 728, 7050, 8098, 9018, 5806, 5618, 9866)

### Defi 1 - Pokemon nombes commun => Lure Mewtwo and Ossatueur
print("Pokemon Nombres Commun:", lureThemAll())

### Defi 2 - Chiffres Préferés
print("Chiffres Préferés:", findChiffresPreferes(10, 56), end="\n\n")

### Defi 3 - Palindrome
print("Palindrome result:", getPalindrome(475))
print("Palindromes results:", getPalindrome((844, 970, 395, 287)))

### Defi 4 - Fourche langue
print("The fourche langue of 'BONJOUR HARRY' is:", fourched_lang, "and it's", True if fourched_lang == "FFHFHHSSFHHHFHHFFFFSFHSHFFHFHFSFFSFSHF" else False, "to the example given.")
print("What Harry said in Fourchelangue probably is:", translateFromFourchelangue("FHSFHHSSFHSSHSHFFSSHFSFHSSSFHFHFSSFFFHHHSSFHHHHSSHHSSHFHSHFHHHHSSFHSSSHFSHHHSHSFFFSSFHSFSSFSFHFHSSFSHHHSHHHFHHFFFFSFHSHHFFHHFFFFSFHSSSFFHHFFFFSHHSSHSHFHFSFHSSSFFHHFFFFSHHSHFHFFSFFSFHHSSFFSHHSSSHSSFFHFHHHSSFHSHHFFHHFFFFFFFHHHHHFSFHSSSFFHHFFFFSHHSFHHSHSSHSFFFHHFSSHFSFHSSHHSSHHSSHSSSHFSHHSHHSFSFFHHHHHFSHHSHHHFSSSSFFHHFFHFFSSSHFSHHSHHSFSFHFHHHHHHSFSFSSHFSHHSSSHHHSHSFFSFHHFSFFSHSFFFFFSSHHSHHSHFFSSHFHHSHHHFHFSFSHHHSHFHFFSHFHFSHHHSFHHFSFHSSSHHHSHSSHSFHHFSFFHSHFHSHSHSSSFSSHHSSSFFHHFFFFSHHSFSSSSHSSFSSHFSFFHHSSFHHSHSHHFFFSFFFFSHHSSSFFHHFFFFSHHSSSFFHHFFFFSHHSFHHSHSSHSFFFHHFSSHFSFFHHSSFFSHHSSHHSSHFSHHSHFHFFFHHSFSFSSHFSH"))

### Defi 5 - Code Cabine
print("The next three codes are:", codecabine(64224, 3))

### Defi 6 - Goldbach
print(f"The goldbach of {gb1} is:", goldbach(gb1))
print(f"The goldbach of {gb2} is:", goldbach(gb2, 1))
