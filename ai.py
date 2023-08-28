from ctypes import *
import ctypes
import pandas as pd
import csv

#c functions
c_file = "./my_functions.so"
rgb = CDLL(c_file)

#compare test image with data
def row_checker(image, testimage):
    score_add = 0
    notsaved = bool(0)
    if notsaved:
        #compare images
        newimage = np.array([[rgb.rgb_processor((ctypes.c_int * 3)(*image[x][i])) for i in range(100)] for x in range(100)])
        newtestimage = np.array([[rgb.rgb_processor((ctypes.c_int * 3)(*testimage[x][i])) for i in range(100)] for x in range(100)])
        for x in range(100):
            score_add += rgb.rgb_checker((ctypes.c_int * 100)(*newimage[x]), (ctypes.c_int * 100)(*newtestimage[x]))
    else:
        #compare excel files
        image_array = np.array(image)  # Convert the list to a NumPy array
        image_uint8 = image_array.astype(np.uint8)
        score_add = np.sum(np.equal(image_uint8, testimage[:, :, 0]))
    return score_add

# Importing libraries
import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import time

#if values have been preprocessed and saved in excel files
saved = bool(1)
image_number = 5000
cat = []
dog = []
if saved:
    #open excel files
    for x in range(image_number):
        with open('temp/cat' + str(x+1) + '.csv', 'r') as f:
            cat += [list(csv.reader(f))]
        with open('temp/dog' + str(x+1) + '.csv', 'r') as f:
            dog += [list(csv.reader(f))]
else:
    #open images
    cat = [cv2.imread(cv2.samples.findFile("training_set/cats/" + str(x+1) + ".png")) for x in range(image_number)]
    dog = [cv2.imread(cv2.samples.findFile("training_set/dogs/" + str(x+1) + ".png")) for x in range(image_number)]
test = cv2.imread(cv2.samples.findFile(input("\nwhere is test image: ")))

x = 0
catidea = 0
dogidea = 0
#compare test image with data
for x in range(image_number):
    catidea += row_checker(cat[x], test)
    dogidea += row_checker(dog[x], test)
if catidea >= dogidea:
    print('cat')
if dogidea >= catidea:
    print('dog')
if catidea == dogidea:
    print("error")
print('\n')
print(catidea)
print('\n')
print(dogidea)
