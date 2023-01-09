#!/usr/bin/env python3
#coding=utf8

### This library was made during for an SAE (SAE-15)
### It simply contains three functions:
###
### - moyenne(): calculates the mean of a list of integers / float
### - sigma(): calculates the sigma of a list of integers / float
### - plot(): creates a graphical representation of data given in a list of integers / float

import math as m
import matplotlib.pyplot as plt

def moyenne(_list: list) -> int | float:
  """
  _list <list>: A list of elements from where we compte the mean returned
  """
  nbr = len(_list)
  _sum = 0
  for i in range(0, len(_list)):
    if isinstance(_list[i], (int, float)):
      _sum += _list[i]

  return _sum / nbr

def sigma(_list: list) -> int | float:
  """
  _list <list>: A list of elements from where we compute the sigma returned
  """
  ### 1/n∑(xi − moy(x))**2
  nbr = len(_list)
  _moyenne = moyenne(_list)
  _sum = 0

  for i in range(0, len(_list)):
    if isinstance(_list[i], (int, float)):
      _sum += (_list[i] - _moyenne)**2

  _sigma = m.sqrt((1/nbr) * _sum)

  return _sigma


def plot(_ylist: list, _xlist: list, _ylabel: str = None, _xlabel: str = None) -> None:
  """
  _ylist <list>: The list used on the Y axis of the plot
  _xlist <list>: The list used on the X axis of the plot
  _ylabel <str>: The label on the Y axis
  _xlabel <str>: The label on the X axis
  """
  fig, ax = plt.subplots()
  ax.plot(_xlist, _ylist)
  if not _xlabel == None:
    ax.set_xlabel(_xlabel)
  if not _ylabel == None:
    ax.set_ylabel(_ylabel)
