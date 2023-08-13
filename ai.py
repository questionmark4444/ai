from ctypes import *
import ctypes
c_file = "./my_functions.so"
rgb = CDLL(c_file)

def rgb_processor(row):
    x = 0
    newvalue = 0
    newvalue1 = 0
    newvalue2 = 0
    newvalue3 = 0
    newrow = [0] * 100
    while x < 100:
        newvalue1 = row[x][0]/3
        newvalue2 = row[x][1]/3
        newvalue3 = row[x][2]/3
        newvalue = round(newvalue1+newvalue2+newvalue3)
        newrow[x] = newvalue
        x += 1
    return newrow

def pixel_checker(row, testrow):
    x = 0
    score_add = 0
    while x < 100:
        score_add += rgb.rgb_checker((ctypes.c_int * 100)(*row), (ctypes.c_int * 100)(*testrow))
        x += 1
    return score_add*0.2

def row_checker(image, testimage):
    x = 0
    score_add = 0
    newimage = [0] * 100
    newtestimage = [0] * 100
    while x < 100:
        newimage[x] = rgb_processor(image[x])
        newtestimage[x] = rgb_processor(testimage[x])
        x += 1
    x = 0
    while x < 100:
        score_add += pixel_checker(newimage[x], newtestimage[x])
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
cat = [[[[0, 0, 0]] * 100] * 100] * 600
dog = [[[[0, 0, 0]] * 100] * 100] * 600
while x < 801:
    cat += [cv2.imread(cv2.samples.findFile("training_set/cats/" + str(x) + ".png"))]
    dog += [cv2.imread(cv2.samples.findFile("training_set/dogs/" + str(x) + ".png"))]
    x += 1

test = cv2.imread(cv2.samples.findFile(input("\nwhere is test image: ")))
catidea = 0
dogidea = 0
x = 0
while x < 800:
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
