def rgb_checker(pixel, testpixel, score):
    x = 0
    while x < 3:
        if pixel[x] == testpixel[x]:
            score += 1
        x += 1
    return score

def pixel_checker(row, testrow, score):
    x = 0
    while x < 99:
        score += rgb_checker(row[x], testrow[x], score)
        x += 1
    return score

def row_checker(image, testimage, score):
    x = 0
    while x < 99:
        score += pixel_checker(image[x], testimage[x], score)
        x += 1
    return score

import numpy as np
import cv2
import glob
import os
import sys
import time
x = 1
cat = []
dog = []
while x < 11:
    cat += [cv2.imread(cv2.samples.findFile("training_set/cats/" + str(x) + ".png"))]
    dog += [cv2.imread(cv2.samples.findFile("training_set/dogs/" + str(x) + ".png"))]
    x += 1
test = cv2.imread(cv2.samples.findFile("test_set/cats/test.png"))
catidea = 0
catidea = row_checker(cat[0], test, catidea)
catidea = row_checker(cat[1], test, catidea)
catidea = row_checker(cat[2], test, catidea)
catidea = row_checker(cat[3], test, catidea)
catidea = row_checker(cat[4], test, catidea)
catidea = row_checker(cat[5], test, catidea)
catidea = row_checker(cat[6], test, catidea)
catidea = row_checker(cat[7], test, catidea)
catidea = row_checker(cat[8], test, catidea)
catidea = row_checker(cat[9], test, catidea)
dogidea = 0
dogidea = row_checker(dog[0], test, dogidea)
dogidea = row_checker(dog[1], test, dogidea)
dogidea = row_checker(dog[2], test, dogidea)
dogidea = row_checker(dog[3], test, dogidea)
dogidea = row_checker(dog[4], test, dogidea)
dogidea = row_checker(dog[5], test, dogidea)
dogidea = row_checker(dog[6], test, dogidea)
dogidea = row_checker(dog[7], test, dogidea)
dogidea = row_checker(dog[8], test, dogidea)
dogidea = row_checker(dog[9], test, dogidea)
if catidea >= dogidea:
    time.sleep(1)
    print('cat')
if dogidea >= catidea:
    time.sleep(1)
    print('dog')
if catidea == dogidea:
    time.sleep(1)
    print('ĂŻÂżÂ˝sĂâ~ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝>ĂŻÂżÂ˝ĂŻÂżÂ˝ĂâĂŻÂżÂ˝ĂÂ˘dĂŻÂżÂ˝{ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ĂÂťĂÂľĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝1ĂĹĄĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝')
print("")
print(catidea)
print('\n')
print(dogidea))
