from ctypes import *
import ctypes
c_file = "./my_functions.so"
rgb = CDLL(c_file)

def pixel_checker(row, testrow):
    x = 0
    score_add = 0
    while x < 99:
        score_add += rgb.rgb_checker((ctypes.c_int * 3)(*row[x]), (ctypes.c_int * 3)(*testrow[x]))
        x += 1
    return score_add

def row_checker(image, testimage):
    x = 0
    score_add = 0
    while x < 99:
        score_add += pixel_checker(image[x], testimage[x])
        x += 1
    return score_add

# Importing libraries
import cv2

import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import time

x = 1
cat = []
dog = []
while x < 201:
    cat += [cv2.imread(cv2.samples.findFile("training_set/cats/" + str(x) + ".png"))]
    dog += [cv2.imread(cv2.samples.findFile("training_set/dogs/" + str(x) + ".png"))]
    x += 1

test = cv2.imread(cv2.samples.findFile(input("\nwhere is test image: ")))
catidea = 0
dogidea = 0
x = 0
while x < 200:
    catidea += row_checker(cat[x], test)
    dogidea += row_checker(dog[x], test)
    x += 1
if catidea >= dogidea:
    print('cat')
if dogidea >= catidea:
    print('dog')
if catidea == dogidea:
    print("error")
print("")
print(catidea)
print('\n')
print(dogidea)
