from ctypes import *
import ctypes
import csv

import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import time

#import c functions
c_file = "./my_functions.so"
rgb = CDLL(c_file)

number_images = 5000

#import images
cat = [cv2.imread(cv2.samples.findFile("training_set/cats/" + str(x+1) + ".png")) for x in range(number_images)]
dog = [cv2.imread(cv2.samples.findFile("training_set/dogs/" + str(x+1) + ".png")) for x in range(number_images)]

#process data
newcat = [[[rgb.rgb_processor((ctypes.c_int * 3)(*cat[y][x][i])) for i in range(100)] for x in range(100)] for y in range(number_images)]
newdog = [[[rgb.rgb_processor((ctypes.c_int * 3)(*dog[y][x][i])) for i in range(100)] for x in range(100)] for y in range(number_images)]

#save data in excel files
for x in range(number_images):
    with open(('temp/cat' + str(x+1) + '.csv'), 'w') as f:
        csv.writer(f).writerows(newcat[x])
    with open(('temp/dog' + str(x+1) + '.csv'), 'w') as f:
        csv.writer(f).writerows(newdog[x])
