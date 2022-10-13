#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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



  ### 1st step: We do a dummy translation from the fourchelangue
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

  ### 2nd step: We do a check of each word of the known double-letter cases in our translation
  ### Caution: It means a user-script interaction is required on this version of the function
  for i in range(0, len(curr_phrase)):
    for letter in curr_phrase[i]:
      if letter in ("I", "J", "U", "V"):
        ### While the word is not correct test different combinations until we find the correct one
        while correct_word == False:
          x = input(f"Is this correct ?\n -> {curr_phrase[i]}")
          if x in ("y", "Y", "yes", "YES"):
            correct_word = True
          else:
            for y in range(0, len(char_hist[i]), 3):
              new_char = str(char_hist[i][y]) + str(char_hist[i][y+1]) + str(char_hist[i][y+2])
              print(new_char, alphabet[new_char] if len(alphabet[new_char]) == 1 else alphabet[new_char][0])




  return curr_phrase

###/////////////////////////////////////////////////////////////////////////
###
### Défi 5 - CodeCabine
###
###/////////////////////////////////////////////////////////////////////////



###/////////////////////////////////////////////////////////////////////////
###
### Affichage
###
###/////////////////////////////////////////////////////////////////////////

fourched_lang = translateToFourchelangue('BONJOUR HARRY')

print("Pokemon Nombres Commun:", lureThemAll())
print("Chiffres Préferés:", findChiffresPreferes(10, 56), end="\n\n")
print("Palindrome result:", getPalindrome(475))
print("Palindromes results:", getPalindrome((844, 970, 395, 287)))
print("The fourche langue of 'BONJOUR HARRY' is:", fourched_lang, "and it's", True if fourched_lang == "FFHFHHSSFHHHFHHFFFFSFHSHFFHFHFSFFSFSHF" else False, "to the example given.")
print("What Harry said in Fourchelangue probably is:", translateFromFourchelangue("FHSFHHSSFHSSHSHFFSSHFSFHSSSFHFHFSSFFFHHHSSFHHHHSSHHSSHFHSHFHHHHSSFHSSSHFSHHHSHSFFFSSFHSFSSFSFHFHSSFSHHHSHHHFHHFFFFSFHSHHFFHHFFFFSFHSSSFFHHFFFFSHHSSHSHFHFSFHSSSFFHHFFFFSHHSHFHFFSFFSFHHSSFFSHHSSSHSSFFHFHHHSSFHSHHFFHHFFFFFFFHHHHHFSFHSSSFFHHFFFFSHHSFHHSHSSHSFFFHHFSSHFSFHSSHHSSHHSSHSSSHFSHHSHHSFSFFHHHHHFSHHSHHHFSSSSFFHHFFHFFSSSHFSHHSHHSFSFHFHHHHHHSFSFSSHFSHHSSSHHHSHSFFSFHHFSFFSHSFFFFFSSHHSHHSHFFSSHFHHSHHHFHFSFSHHHSHFHFFSHFHFSHHHSFHHFSFHSSSHHHSHSSHSFHHFSFFHSHFHSHSHSSSFSSHHSSSFFHHFFFFSHHSFSSSSHSSFSSHFSFFHHSSFHHSHSHHFFFSFFFFSHHSSSFFHHFFFFSHHSSSFFHHFFFFSHHSFHHSHSSHSFFFHHFSSHFSFFHHSSFFSHHSSHHSSHFSHHSHFHFFFHHSFSFSSHFSH"))
