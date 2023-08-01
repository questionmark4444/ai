from ctypes import *
import ctypes
c_file = "./my_functions.so"
rgb = CDLL(c_file)

def rgb_checker(pixel, testpixel):
    array = (ctypes.c_int * 3)(*pixel)
    testarray = (ctypes.c_int * 3)(*testpixel)
    score_add = rgb.rgb_checker(array, testarray)
    round(score_add)
    return score_add


def pixel_checker(row, testrow):
    x = 0
    score_add = 0
    while x < 99:
        score_add += rgb_checker(row[x], testrow[x])
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
while x < 41:
    cat += [cv2.imread(cv2.samples.findFile("training_set/cats/" + str(x) + ".png"))]
    dog += [cv2.imread(cv2.samples.findFile("training_set/dogs/" + str(x) + ".png"))]
    x += 1

test = cv2.imread(cv2.samples.findFile("test_set/cats/test.png"))
catidea = 0
catidea += row_checker(cat[0], test)
catidea += row_checker(cat[1], test)
catidea += row_checker(cat[2], test)
catidea += row_checker(cat[3], test)
catidea += row_checker(cat[4], test)
catidea += row_checker(cat[5], test)
catidea += row_checker(cat[6], test)
catidea += row_checker(cat[7], test)
catidea += row_checker(cat[8], test)
catidea += row_checker(cat[9], test)
dogidea = 0
dogidea += row_checker(dog[0], test)
dogidea += row_checker(dog[1], test)
dogidea += row_checker(dog[2], test)
dogidea += row_checker(dog[3], test)
dogidea += row_checker(dog[4], test)
dogidea += row_checker(dog[5], test)
dogidea += row_checker(dog[6], test)
dogidea += row_checker(dog[7], test)
dogidea += row_checker(dog[8], test)
dogidea += row_checker(dog[9], test)
if catidea >= dogidea:
    time.sleep(1)
    print('cat')
if dogidea >= catidea:
    time.sleep(1)
    print('dog')
if catidea == dogidea:
    time.sleep(1)
    print("error")
print("")
print(catidea)
print('\n')
print(dogidea)
