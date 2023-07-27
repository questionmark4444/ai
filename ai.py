def rgb_checker(pixel, testpixel, score):
    x = 0
    while x < 3:
        if pixel[x] == testpixel[x]:
            score += 1
        x += 1
    return score

def pixel_checker(row, testrow, score):
    x = 0
    while x < 11:
        score += rgb_checker(row[x], testrow[x], score)
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
testhmm1 = test[0]
cat1hmm1 = cat[0][0]
cat2hmm1 = cat[1][0]
cat3hmm1 = cat[2][0]
cat4hmm1 = cat[3][0]
cat5hmm1 = cat[4][0]
cat6hmm1 = cat[5][0]
cat7hmm1 = cat[6][0]
cat8hmm1 = cat[7][0]
cat9hmm1 = cat[8][0]
cat10hmm1 = cat[9][0]
dog1hmm1 = dog[0][0]
dog2hmm1 = dog[1][0]
dog3hmm1 = dog[2][0]
dog4hmm1 = dog[3][0]
dog5hmm1 = dog[4][0]
dog6hmm1 = dog[5][0]
dog7hmm1 = dog[6][0]
dog8hmm1 = dog[7][0]
dog9hmm1 = dog[8][0]
dog10hmm1 = dog[9][0]
catidea = 0
catidea = pixel_checker(cat1hmm1, testhmm1, catidea)
catidea = pixel_checker(cat2hmm1, testhmm1, catidea)
catidea = pixel_checker(cat3hmm1, testhmm1, catidea)
catidea = pixel_checker(cat4hmm1, testhmm1, catidea)
catidea = pixel_checker(cat5hmm1, testhmm1, catidea)
catidea = pixel_checker(cat6hmm1, testhmm1, catidea)
catidea = pixel_checker(cat7hmm1, testhmm1, catidea)
catidea = pixel_checker(cat8hmm1, testhmm1, catidea)
catidea = pixel_checker(cat9hmm1, testhmm1, catidea)
catidea = pixel_checker(cat10hmm1, testhmm1, catidea)
dogidea = 0
dogidea = pixel_checker(dog1hmm1, testhmm1, dogidea)
dogidea = pixel_checker(dog2hmm1, testhmm1, dogidea)
dogidea = pixel_checker(dog3hmm1, testhmm1, dogidea)
dogidea = pixel_checker(dog4hmm1, testhmm1, dogidea)
dogidea = pixel_checker(dog5hmm1, testhmm1, dogidea)
dogidea = pixel_checker(dog6hmm1, testhmm1, dogidea)
dogidea = pixel_checker(dog7hmm1, testhmm1, dogidea)
dogidea = pixel_checker(dog8hmm1, testhmm1, dogidea)
dogidea = pixel_checker(dog9hmm1, testhmm1, dogidea)
dogidea = pixel_checker(dog10hmm1, testhmm1, dogidea)
if catidea >= dogidea:
    time.sleep(1)
    print('cat')
if dogidea >= catidea:
    time.sleep(1)
    print('dog')
if catidea == dogidea:
    time.sleep(1)
    print('ĂŻÂżÂ˝sĂâ~ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝>ĂŻÂżÂ˝ĂŻÂżÂ˝ĂâĂŻÂżÂ˝ĂÂ˘dĂŻÂżÂ˝{ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ĂÂťĂÂľĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝1ĂĹĄĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝ĂŻÂżÂ˝')
print(str(catidea) + ' ' + str(dogidea))
