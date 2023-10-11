#libraries
from ctypes import *
import ctypes
import csv
import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import time


#variable to record how long this will take to load c functions
RecordStart1 = time.time()


#import c functions
c_file = "./my_functions.so"
rgb = CDLL(c_file)


#other variable to record how long this will take to load c functions
Recordend1 = time.time() - RecordStart1


#input classes and number of images from user
loop = True
while loop:
    try: #in case the images could not be found
        number_images = int(input("number of images of each class: "))
        print("") #new line
        if (number_of_images < 1):  #restart loop with error
            print(0/0)
        print("what is the first class of images")
        print("(this will look for a folder with the name of that class and png images with ascending number names)")
        class1 = input(" : ")
        class2 = input("what is the second class of images: ")
        print("") #new line

        #variable to record how long this will take to load and process images
        RecordStart2 = time.time()

        #import images
        class1_data = [cv2.imread(cv2.samples.findFile(f"training_set/{class1}/{x+1}.png")) for x in range(number_images)]
        class2_data = [cv2.imread(cv2.samples.findFile(f"training_set/{class2}/{x+1}.png")) for x in range(number_images)]

        #process data
        newclass1_data = [[[rgb.rgb_processor((ctypes.c_int * 3)(*class1_data[y][x][i])) for i in range(100)] for x in range(100)] for y in range(number_images)]
        newclass2_data = [[[rgb.rgb_processor((ctypes.c_int * 3)(*class2_data[y][x][i])) for i in range(100)] for x in range(100)] for y in range(number_images)]

        #save data in excel files
        for x in range(number_images):
            with open((f'temp/{class1}{x+1}.csv'), 'w') as f:
                csv.writer(f).writerows(newclass1_data[x])
            with open((f'temp/{class2}{x+1}.csv'), 'w') as f:
                csv.writer(f).writerows(newclass2_data[x])

        #other variable to record how long this will take to load and process images
        Recordend2 = time.time() - RecordStart2
        minutes = int((Recordend1 + Recordend2) / 60 * 100) / 100
        print(f"this took {minutes} minutes")  #print amount of minutes it took with 2 decimal places
        loop = False
    except:
        print("sorry something went wrong")
        print("(please write the names of the folders correctly and name the images correctly)")
        print("\n")
