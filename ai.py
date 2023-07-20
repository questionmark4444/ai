import numpy as np
import cv2
import glob
import os
import sys
import time
cat1 = cv2.imread(cv2.samples.findFile('training_set/cats/1.png'))
cat2 = cv2.imread(cv2.samples.findFile('training_set/cats/2.png'))
cat3 = cv2.imread(cv2.samples.findFile('training_set/cats/3.png'))
cat4 = cv2.imread(cv2.samples.findFile('training_set/cats/4.png'))
cat5 = cv2.imread(cv2.samples.findFile('training_set/cats/5.png'))
cat6 = cv2.imread(cv2.samples.findFile('training_set/cats/6.png'))
cat7 = cv2.imread(cv2.samples.findFile('training_set/cats/7.png'))
cat8 = cv2.imread(cv2.samples.findFile('training_set/cats/8.png'))
cat9 = cv2.imread(cv2.samples.findFile('training_set/cats/9.png'))
cat10 = cv2.imread(cv2.samples.findFile('training_set/cats/10.png'))
dog1 = cv2.imread(cv2.samples.findFile('training_set/dogs/1.png'))
dog2 = cv2.imread(cv2.samples.findFile('training_set/dogs/2.png'))
dog3 = cv2.imread(cv2.samples.findFile('training_set/dogs/3.png'))
dog4 = cv2.imread(cv2.samples.findFile('training_set/dogs/4.png'))
dog5 = cv2.imread(cv2.samples.findFile('training_set/dogs/5.png'))
dog6 = cv2.imread(cv2.samples.findFile('training_set/dogs/6.png'))
dog7 = cv2.imread(cv2.samples.findFile('training_set/dogs/7.png'))
dog8 = cv2.imread(cv2.samples.findFile('training_set/dogs/8.png'))
dog9 = cv2.imread(cv2.samples.findFile('training_set/dogs/9.png'))
dog10 = cv2.imread(cv2.samples.findFile('training_set/dogs/10.png'))
test = cv2.imread(cv2.samples.findFile('test_set/cats/test.png'))
testhmm1 = test[0]
testhmm1_1 = testhmm1[0]
testhmm1_1_1 = testhmm1_1[0]
testhmm1_1_2 = testhmm1_1[1]
testhmm1_1_3 = testhmm1_1[2]
testhmm1_2 = testhmm1[1]
testhmm1_2_1 = testhmm1_2[0]
testhmm1_2_2 = testhmm1_2[1]
testhmm1_2_3 = testhmm1_2[2]
testhmm1_3 = testhmm1[2]
testhmm1_3_1 = testhmm1_3[0]
testhmm1_3_2 = testhmm1_3[1]
testhmm1_3_3 = testhmm1_3[2]
testhmm1_4 = testhmm1[3]
testhmm1_4_1 = testhmm1_4[0]
testhmm1_4_2 = testhmm1_4[1]
testhmm1_4_3 = testhmm1_4[2]
testhmm1_5 = testhmm1[4]
testhmm1_5_1 = testhmm1_5[0]
testhmm1_5_2 = testhmm1_5[1]
testhmm1_5_3 = testhmm1_5[2]
testhmm1_6 = testhmm1[5]
testhmm1_6_1 = testhmm1_6[0]
testhmm1_6_2 = testhmm1_6[1]
testhmm1_6_3 = testhmm1_6[2]
testhmm1_7 = testhmm1[6]
testhmm1_7_1 = testhmm1_7[0]
testhmm1_7_2 = testhmm1_7[1]
testhmm1_7_3 = testhmm1_7[2]
testhmm1_8 = testhmm1[7]
testhmm1_8_1 = testhmm1_8[0]
testhmm1_8_2 = testhmm1_8[1]
testhmm1_8_3 = testhmm1_8[2]
testhmm1_9 = testhmm1[8]
testhmm1_9_1 = testhmm1_9[0]
testhmm1_9_2 = testhmm1_9[1]
testhmm1_9_3 = testhmm1_9[2]
testhmm1_10 = testhmm1[9]
testhmm1_10_1 = testhmm1_10[0]
testhmm1_10_2 = testhmm1_10[1]
testhmm1_10_3 = testhmm1_10[2]
testhmm1_11 = testhmm1[10]
testhmm1_11_1 = testhmm1_11[0]
testhmm1_11_2 = testhmm1_11[1]
testhmm1_11_3 = testhmm1_11[2]
cat1hmm1 = cat1[0]
cat1hmm1_1 = cat1hmm1[0]
cat1hmm1_1_1 = cat1hmm1_1[0]
cat1hmm1_1_2 = cat1hmm1_1[1]
cat1hmm1_1_3 = cat1hmm1_1[2]
cat1hmm1_2 = cat1hmm1[1]
cat1hmm1_2_1 = cat1hmm1_2[0]
cat1hmm1_2_2 = cat1hmm1_2[1]
cat1hmm1_2_3 = cat1hmm1_2[2]
cat1hmm1_3 = cat1hmm1[2]
cat1hmm1_3_1 = cat1hmm1_3[0]
cat1hmm1_3_2 = cat1hmm1_3[1]
cat1hmm1_3_3 = cat1hmm1_3[2]
cat1hmm1_4 = cat1hmm1[3]
cat1hmm1_4_1 = cat1hmm1_4[0]
cat1hmm1_4_2 = cat1hmm1_4[1]
cat1hmm1_4_3 = cat1hmm1_4[2]
cat1hmm1_5 = cat1hmm1[4]
cat1hmm1_5_1 = cat1hmm1_5[0]
cat1hmm1_5_2 = cat1hmm1_5[1]
cat1hmm1_5_3 = cat1hmm1_5[2]
cat1hmm1_6 = cat1hmm1[5]
cat1hmm1_6_1 = cat1hmm1_6[0]
cat1hmm1_6_2 = cat1hmm1_6[1]
cat1hmm1_6_3 = cat1hmm1_6[2]
cat1hmm1_7 = cat1hmm1[6]
cat1hmm1_7_1 = cat1hmm1_7[0]
cat1hmm1_7_2 = cat1hmm1_7[1]
cat1hmm1_7_3 = cat1hmm1_7[2]
cat1hmm1_8 = cat1hmm1[7]
cat1hmm1_8_1 = cat1hmm1_8[0]
cat1hmm1_8_2 = cat1hmm1_8[1]
cat1hmm1_8_3 = cat1hmm1_8[2]
cat1hmm1_9 = cat1hmm1[8]
cat1hmm1_9_1 = cat1hmm1_9[0]
cat1hmm1_9_2 = cat1hmm1_9[1]
cat1hmm1_9_3 = cat1hmm1_9[2]
cat1hmm1_10 = cat1hmm1[9]
cat1hmm1_10_1 = cat1hmm1_10[0]
cat1hmm1_10_2 = cat1hmm1_10[1]
cat1hmm1_10_3 = cat1hmm1_10[2]
cat1hmm1_11 = cat1hmm1[10]
cat1hmm1_11_1 = cat1hmm1_11[0]
cat1hmm1_11_2 = cat1hmm1_11[1]
cat1hmm1_11_3 = cat1hmm1_11[2]
cat2hmm1 = cat2[0]
cat2hmm1_1 = cat2hmm1[0]
cat2hmm1_1_1 = cat2hmm1_1[0]
cat2hmm1_1_2 = cat2hmm1_1[1]
cat2hmm1_1_3 = cat2hmm1_1[2]
cat2hmm1_2 = cat2hmm1[1]
cat2hmm1_2_1 = cat2hmm1_2[0]
cat2hmm1_2_2 = cat2hmm1_2[1]
cat2hmm1_2_3 = cat2hmm1_2[2]
cat2hmm1_3 = cat2hmm1[2]
cat2hmm1_3_1 = cat2hmm1_3[0]
cat2hmm1_3_2 = cat2hmm1_3[1]
cat2hmm1_3_3 = cat2hmm1_3[2]
cat2hmm1_4 = cat2hmm1[3]
cat2hmm1_4_1 = cat2hmm1_4[0]
cat2hmm1_4_2 = cat2hmm1_4[1]
cat2hmm1_4_3 = cat2hmm1_4[2]
cat2hmm1_5 = cat2hmm1[4]
cat2hmm1_5_1 = cat2hmm1_5[0]
cat2hmm1_5_2 = cat2hmm1_5[1]
cat2hmm1_5_3 = cat2hmm1_5[2]
cat2hmm1_6 = cat2hmm1[5]
cat2hmm1_6_1 = cat2hmm1_6[0]
cat2hmm1_6_2 = cat2hmm1_6[1]
cat2hmm1_6_3 = cat2hmm1_6[2]
cat2hmm1_7 = cat2hmm1[6]
cat2hmm1_7_1 = cat2hmm1_7[0]
cat2hmm1_7_2 = cat2hmm1_7[1]
cat2hmm1_7_3 = cat2hmm1_7[2]
cat2hmm1_8 = cat2hmm1[7]
cat2hmm1_8_1 = cat2hmm1_8[0]
cat2hmm1_8_2 = cat2hmm1_8[1]
cat2hmm1_8_3 = cat2hmm1_8[2]
cat2hmm1_9 = cat2hmm1[8]
cat2hmm1_9_1 = cat2hmm1_9[0]
cat2hmm1_9_2 = cat2hmm1_9[1]
cat2hmm1_9_3 = cat2hmm1_9[2]
cat2hmm1_10 = cat2hmm1[9]
cat2hmm1_10_1 = cat2hmm1_10[0]
cat2hmm1_10_2 = cat2hmm1_10[1]
cat2hmm1_10_3 = cat2hmm1_10[2]
cat2hmm1_11 = cat2hmm1[10]
cat2hmm1_11_1 = cat2hmm1_11[0]
cat2hmm1_11_2 = cat2hmm1_11[1]
cat2hmm1_11_3 = cat2hmm1_11[2]
cat3hmm1 = cat3[0]
cat3hmm1_1 = cat3hmm1[0]
cat3hmm1_1_1 = cat3hmm1_1[0]
cat3hmm1_1_2 = cat3hmm1_1[1]
cat3hmm1_1_3 = cat3hmm1_1[2]
cat3hmm1_2 = cat3hmm1[1]
cat3hmm1_2_1 = cat3hmm1_2[0]
cat3hmm1_2_2 = cat3hmm1_2[1]
cat3hmm1_2_3 = cat3hmm1_2[2]
cat3hmm1_3 = cat3hmm1[2]
cat3hmm1_3_1 = cat3hmm1_3[0]
cat3hmm1_3_2 = cat3hmm1_3[1]
cat3hmm1_3_3 = cat3hmm1_3[2]
cat3hmm1_4 = cat3hmm1[3]
cat3hmm1_4_1 = cat3hmm1_4[0]
cat3hmm1_4_2 = cat3hmm1_4[1]
cat3hmm1_4_3 = cat3hmm1_4[2]
cat3hmm1_5 = cat3hmm1[4]
cat3hmm1_5_1 = cat3hmm1_5[0]
cat3hmm1_5_2 = cat3hmm1_5[1]
cat3hmm1_5_3 = cat3hmm1_5[2]
cat3hmm1_6 = cat3hmm1[5]
cat3hmm1_6_1 = cat3hmm1_6[0]
cat3hmm1_6_2 = cat3hmm1_6[1]
cat3hmm1_6_3 = cat3hmm1_6[2]
cat3hmm1_7 = cat3hmm1[6]
cat3hmm1_7_1 = cat3hmm1_7[0]
cat3hmm1_7_2 = cat3hmm1_7[1]
cat3hmm1_7_3 = cat3hmm1_7[2]
cat3hmm1_8 = cat3hmm1[7]
cat3hmm1_8_1 = cat3hmm1_8[0]
cat3hmm1_8_2 = cat3hmm1_8[1]
cat3hmm1_8_3 = cat3hmm1_8[2]
cat3hmm1_9 = cat3hmm1[8]
cat3hmm1_9_1 = cat3hmm1_9[0]
cat3hmm1_9_2 = cat3hmm1_9[1]
cat3hmm1_9_3 = cat3hmm1_9[2]
cat3hmm1_10 = cat3hmm1[9]
cat3hmm1_10_1 = cat3hmm1_10[0]
cat3hmm1_10_2 = cat3hmm1_10[1]
cat3hmm1_10_3 = cat3hmm1_10[2]
cat3hmm1_11 = cat3hmm1[10]
cat3hmm1_11_1 = cat3hmm1_11[0]
cat3hmm1_11_2 = cat3hmm1_11[1]
cat3hmm1_11_3 = cat3hmm1_11[2]
cat4hmm1 = cat4[0]
cat4hmm1_1 = cat4hmm1[0]
cat4hmm1_1_1 = cat4hmm1_1[0]
cat4hmm1_1_2 = cat4hmm1_1[1]
cat4hmm1_1_3 = cat4hmm1_1[2]
cat4hmm1_2 = cat4hmm1[1]
cat4hmm1_2_1 = cat4hmm1_2[0]
cat4hmm1_2_2 = cat4hmm1_2[1]
cat4hmm1_2_3 = cat4hmm1_2[2]
cat4hmm1_3 = cat4hmm1[2]
cat4hmm1_3_1 = cat4hmm1_3[0]
cat4hmm1_3_2 = cat4hmm1_3[1]
cat4hmm1_3_3 = cat4hmm1_3[2]
cat4hmm1_4 = cat4hmm1[3]
cat4hmm1_4_1 = cat4hmm1_4[0]
cat4hmm1_4_2 = cat4hmm1_4[1]
cat4hmm1_4_3 = cat4hmm1_4[2]
cat4hmm1_5 = cat4hmm1[4]
cat4hmm1_5_1 = cat4hmm1_5[0]
cat4hmm1_5_2 = cat4hmm1_5[1]
cat4hmm1_5_3 = cat4hmm1_5[2]
cat4hmm1_6 = cat4hmm1[5]
cat4hmm1_6_1 = cat4hmm1_6[0]
cat4hmm1_6_2 = cat4hmm1_6[1]
cat4hmm1_6_3 = cat4hmm1_6[2]
cat4hmm1_7 = cat4hmm1[6]
cat4hmm1_7_1 = cat4hmm1_7[0]
cat4hmm1_7_2 = cat4hmm1_7[1]
cat4hmm1_7_3 = cat4hmm1_7[2]
cat4hmm1_8 = cat4hmm1[7]
cat4hmm1_8_1 = cat4hmm1_8[0]
cat4hmm1_8_2 = cat4hmm1_8[1]
cat4hmm1_8_3 = cat4hmm1_8[2]
cat4hmm1_9 = cat4hmm1[8]
cat4hmm1_9_1 = cat4hmm1_9[0]
cat4hmm1_9_2 = cat4hmm1_9[1]
cat4hmm1_9_3 = cat4hmm1_9[2]
cat4hmm1_10 = cat4hmm1[9]
cat4hmm1_10_1 = cat4hmm1_10[0]
cat4hmm1_10_2 = cat4hmm1_10[1]
cat4hmm1_10_3 = cat4hmm1_10[2]
cat4hmm1_11 = cat4hmm1[10]
cat4hmm1_11_1 = cat4hmm1_11[0]
cat4hmm1_11_2 = cat4hmm1_11[1]
cat4hmm1_11_3 = cat4hmm1_11[2]
cat5hmm1 = cat5[0]
cat5hmm1_1 = cat5hmm1[0]
cat5hmm1_1_1 = cat5hmm1_1[0]
cat5hmm1_1_2 = cat5hmm1_1[1]
cat5hmm1_1_3 = cat5hmm1_1[2]
cat5hmm1_2 = cat5hmm1[1]
cat5hmm1_2_1 = cat5hmm1_2[0]
cat5hmm1_2_2 = cat5hmm1_2[1]
cat5hmm1_2_3 = cat5hmm1_2[2]
cat5hmm1_3 = cat5hmm1[2]
cat5hmm1_3_1 = cat5hmm1_3[0]
cat5hmm1_3_2 = cat5hmm1_3[1]
cat5hmm1_3_3 = cat5hmm1_3[2]
cat5hmm1_4 = cat5hmm1[3]
cat5hmm1_4_1 = cat5hmm1_4[0]
cat5hmm1_4_2 = cat5hmm1_4[1]
cat5hmm1_4_3 = cat5hmm1_4[2]
cat5hmm1_5 = cat5hmm1[4]
cat5hmm1_5_1 = cat5hmm1_5[0]
cat5hmm1_5_2 = cat5hmm1_5[1]
cat5hmm1_5_3 = cat5hmm1_5[2]
cat5hmm1_6 = cat5hmm1[5]
cat5hmm1_6_1 = cat5hmm1_6[0]
cat5hmm1_6_2 = cat5hmm1_6[1]
cat5hmm1_6_3 = cat5hmm1_6[2]
cat5hmm1_7 = cat5hmm1[6]
cat5hmm1_7_1 = cat5hmm1_7[0]
cat5hmm1_7_2 = cat5hmm1_7[1]
cat5hmm1_7_3 = cat5hmm1_7[2]
cat5hmm1_8 = cat5hmm1[7]
cat5hmm1_8_1 = cat5hmm1_8[0]
cat5hmm1_8_2 = cat5hmm1_8[1]
cat5hmm1_8_3 = cat5hmm1_8[2]
cat5hmm1_9 = cat5hmm1[8]
cat5hmm1_9_1 = cat5hmm1_9[0]
cat5hmm1_9_2 = cat5hmm1_9[1]
cat5hmm1_9_3 = cat5hmm1_9[2]
cat5hmm1_10 = cat5hmm1[9]
cat5hmm1_10_1 = cat5hmm1_10[0]
cat5hmm1_10_2 = cat5hmm1_10[1]
cat5hmm1_10_3 = cat5hmm1_10[2]
cat5hmm1_11 = cat5hmm1[10]
cat5hmm1_11_1 = cat5hmm1_11[0]
cat5hmm1_11_2 = cat5hmm1_11[1]
cat5hmm1_11_3 = cat5hmm1_11[2]
cat6hmm1 = cat6[0]
cat6hmm1_1 = cat6hmm1[0]
cat6hmm1_1_1 = cat6hmm1_1[0]
cat6hmm1_1_2 = cat6hmm1_1[1]
cat6hmm1_1_3 = cat6hmm1_1[2]
cat6hmm1_2 = cat6hmm1[1]
cat6hmm1_2_1 = cat6hmm1_2[0]
cat6hmm1_2_2 = cat6hmm1_2[1]
cat6hmm1_2_3 = cat6hmm1_2[2]
cat6hmm1_3 = cat6hmm1[2]
cat6hmm1_3_1 = cat6hmm1_3[0]
cat6hmm1_3_2 = cat6hmm1_3[1]
cat6hmm1_3_3 = cat6hmm1_3[2]
cat6hmm1_4 = cat6hmm1[3]
cat6hmm1_4_1 = cat6hmm1_4[0]
cat6hmm1_4_2 = cat6hmm1_4[1]
cat6hmm1_4_3 = cat6hmm1_4[2]
cat6hmm1_5 = cat6hmm1[4]
cat6hmm1_5_1 = cat6hmm1_5[0]
cat6hmm1_5_2 = cat6hmm1_5[1]
cat6hmm1_5_3 = cat6hmm1_5[2]
cat6hmm1_6 = cat6hmm1[5]
cat6hmm1_6_1 = cat6hmm1_2[0]
cat6hmm1_6_2 = cat6hmm1_2[1]
cat6hmm1_6_3 = cat6hmm1_2[2]
cat6hmm1_7 = cat6hmm1[6]
cat6hmm1_7_1 = cat6hmm1_7[0]
cat6hmm1_7_2 = cat6hmm1_7[1]
cat6hmm1_7_3 = cat6hmm1_7[2]
cat6hmm1_8 = cat6hmm1[7]
cat6hmm1_8_1 = cat6hmm1_8[0]
cat6hmm1_8_2 = cat6hmm1_8[1]
cat6hmm1_8_3 = cat6hmm1_8[2]
cat6hmm1_9 = cat6hmm1[8]
cat6hmm1_9_1 = cat6hmm1_9[0]
cat6hmm1_9_2 = cat6hmm1_9[1]
cat6hmm1_9_3 = cat6hmm1_9[2]
cat6hmm1_10 = cat6hmm1[9]
cat6hmm1_10_1 = cat6hmm1_10[0]
cat6hmm1_10_2 = cat6hmm1_10[1]
cat6hmm1_10_3 = cat6hmm1_10[2]
cat6hmm1_11 = cat6hmm1[10]
cat6hmm1_11_1 = cat6hmm1_11[0]
cat6hmm1_11_2 = cat6hmm1_11[1]
cat6hmm1_11_3 = cat6hmm1_11[2]
cat7hmm1 = cat7[0]
cat7hmm1_1 = cat7hmm1[0]
cat7hmm1_1_1 = cat7hmm1_1[0]
cat7hmm1_1_2 = cat7hmm1_1[1]
cat7hmm1_1_3 = cat7hmm1_1[2]
cat7hmm1_2 = cat7hmm1[1]
cat7hmm1_2_1 = cat7hmm1_2[0]
cat7hmm1_2_2 = cat7hmm1_2[1]
cat7hmm1_2_3 = cat7hmm1_2[2]
cat7hmm1_3 = cat7hmm1[2]
cat7hmm1_3_1 = cat7hmm1_3[0]
cat7hmm1_3_2 = cat7hmm1_3[1]
cat7hmm1_3_3 = cat7hmm1_3[2]
cat7hmm1_4 = cat7hmm1[3]
cat7hmm1_4_1 = cat7hmm1_4[0]
cat7hmm1_4_2 = cat7hmm1_4[1]
cat7hmm1_4_3 = cat7hmm1_4[2]
cat7hmm1_5 = cat7hmm1[4]
cat7hmm1_5_1 = cat7hmm1_5[0]
cat7hmm1_5_2 = cat7hmm1_5[1]
cat7hmm1_5_3 = cat7hmm1_5[2]
cat7hmm1_6 = cat7hmm1[5]
cat7hmm1_6_1 = cat7hmm1_2[0]
cat7hmm1_6_2 = cat7hmm1_2[1]
cat7hmm1_6_3 = cat7hmm1_2[2]
cat7hmm1_7 = cat7hmm1[6]
cat7hmm1_7_1 = cat7hmm1_7[0]
cat7hmm1_7_2 = cat7hmm1_7[1]
cat7hmm1_7_3 = cat7hmm1_7[2]
cat7hmm1_8 = cat7hmm1[7]
cat7hmm1_8_1 = cat7hmm1_8[0]
cat7hmm1_8_2 = cat7hmm1_8[1]
cat7hmm1_8_3 = cat7hmm1_8[2]
cat7hmm1_9 = cat7hmm1[8]
cat7hmm1_9_1 = cat7hmm1_9[0]
cat7hmm1_9_2 = cat7hmm1_9[1]
cat7hmm1_9_3 = cat7hmm1_9[2]
cat7hmm1_10 = cat7hmm1[9]
cat7hmm1_10_1 = cat7hmm1_10[0]
cat7hmm1_10_2 = cat7hmm1_10[1]
cat7hmm1_10_3 = cat7hmm1_10[2]
cat7hmm1_11 = cat7hmm1[10]
cat7hmm1_11_1 = cat7hmm1_11[0]
cat7hmm1_11_2 = cat7hmm1_11[1]
cat7hmm1_11_3 = cat7hmm1_11[2]
cat8hmm1 = cat8[0]
cat8hmm1_1 = cat8hmm1[0]
cat8hmm1_1_1 = cat8hmm1_1[0]
cat8hmm1_1_2 = cat8hmm1_1[1]
cat8hmm1_1_3 = cat8hmm1_1[2]
cat8hmm1_2 = cat8hmm1[1]
cat8hmm1_2_1 = cat8hmm1_2[0]
cat8hmm1_2_2 = cat8hmm1_2[1]
cat8hmm1_2_3 = cat8hmm1_2[2]
cat8hmm1_3 = cat8hmm1[2]
cat8hmm1_3_1 = cat8hmm1_3[0]
cat8hmm1_3_2 = cat8hmm1_3[1]
cat8hmm1_3_3 = cat8hmm1_3[2]
cat8hmm1_4 = cat8hmm1[3]
cat8hmm1_4_1 = cat8hmm1_4[0]
cat8hmm1_4_2 = cat8hmm1_4[1]
cat8hmm1_4_3 = cat8hmm1_4[2]
cat8hmm1_5 = cat8hmm1[4]
cat8hmm1_5_1 = cat8hmm1_5[0]
cat8hmm1_5_2 = cat8hmm1_5[1]
cat8hmm1_5_3 = cat8hmm1_5[2]
cat8hmm1_6 = cat8hmm1[5]
cat8hmm1_6_1 = cat8hmm1_2[0]
cat8hmm1_6_2 = cat8hmm1_2[1]
cat8hmm1_6_3 = cat8hmm1_2[2]
cat8hmm1_7 = cat8hmm1[6]
cat8hmm1_7_1 = cat8hmm1_7[0]
cat8hmm1_7_2 = cat8hmm1_7[1]
cat8hmm1_7_3 = cat8hmm1_7[2]
cat8hmm1_8 = cat8hmm1[7]
cat8hmm1_8_1 = cat8hmm1_8[0]
cat8hmm1_8_2 = cat8hmm1_8[1]
cat8hmm1_8_3 = cat8hmm1_8[2]
cat8hmm1_9 = cat8hmm1[8]
cat8hmm1_9_1 = cat8hmm1_9[0]
cat8hmm1_9_2 = cat8hmm1_9[1]
cat8hmm1_9_3 = cat8hmm1_9[2]
cat8hmm1_10 = cat8hmm1[9]
cat8hmm1_10_1 = cat8hmm1_10[0]
cat8hmm1_10_2 = cat8hmm1_10[1]
cat8hmm1_10_3 = cat8hmm1_10[2]
cat8hmm1_11 = cat8hmm1[10]
cat8hmm1_11_1 = cat8hmm1_11[0]
cat8hmm1_11_2 = cat8hmm1_11[1]
cat8hmm1_11_3 = cat8hmm1_11[2]
cat9hmm1 = cat9[0]
cat9hmm1_1 = cat9hmm1[0]
cat9hmm1_1_1 = cat9hmm1_1[0]
cat9hmm1_1_2 = cat9hmm1_1[1]
cat9hmm1_1_3 = cat9hmm1_1[2]
cat9hmm1_2 = cat9hmm1[1]
cat9hmm1_2_1 = cat9hmm1_2[0]
cat9hmm1_2_2 = cat9hmm1_2[1]
cat9hmm1_2_3 = cat9hmm1_2[2]
cat9hmm1_3 = cat9hmm1[2]
cat9hmm1_3_1 = cat9hmm1_3[0]
cat9hmm1_3_2 = cat9hmm1_3[1]
cat9hmm1_3_3 = cat9hmm1_3[2]
cat9hmm1_4 = cat9hmm1[3]
cat9hmm1_4_1 = cat9hmm1_4[0]
cat9hmm1_4_2 = cat9hmm1_4[1]
cat9hmm1_4_3 = cat9hmm1_4[2]
cat9hmm1_5 = cat9hmm1[4]
cat9hmm1_5_1 = cat9hmm1_5[0]
cat9hmm1_5_2 = cat9hmm1_5[1]
cat9hmm1_5_3 = cat9hmm1_5[2]
cat9hmm1_6 = cat9hmm1[5]
cat9hmm1_6_1 = cat9hmm1_2[0]
cat9hmm1_6_2 = cat9hmm1_2[1]
cat9hmm1_6_3 = cat9hmm1_2[2]
cat9hmm1_7 = cat9hmm1[6]
cat9hmm1_7_1 = cat9hmm1_7[0]
cat9hmm1_7_2 = cat9hmm1_7[1]
cat9hmm1_7_3 = cat9hmm1_7[2]
cat9hmm1_8 = cat9hmm1[7]
cat9hmm1_8_1 = cat9hmm1_8[0]
cat9hmm1_8_2 = cat9hmm1_8[1]
cat9hmm1_8_3 = cat9hmm1_8[2]
cat9hmm1_9 = cat9hmm1[8]
cat9hmm1_9_1 = cat9hmm1_9[0]
cat9hmm1_9_2 = cat9hmm1_9[1]
cat9hmm1_9_3 = cat9hmm1_9[2]
cat9hmm1_10 = cat9hmm1[9]
cat9hmm1_10_1 = cat9hmm1_10[0]
cat9hmm1_10_2 = cat9hmm1_10[1]
cat9hmm1_10_3 = cat9hmm1_10[2]
cat9hmm1_11 = cat9hmm1[10]
cat9hmm1_11_1 = cat9hmm1_11[0]
cat9hmm1_11_2 = cat9hmm1_11[1]
cat9hmm1_11_3 = cat9hmm1_11[2]
cat10hmm1 = cat10[0]
cat10hmm1_1 = cat10hmm1[0]
cat10hmm1_1_1 = cat10hmm1_1[0]
cat10hmm1_1_2 = cat10hmm1_1[1]
cat10hmm1_1_3 = cat10hmm1_1[2]
cat10hmm1_2 = cat10hmm1[1]
cat10hmm1_2_1 = cat10hmm1_2[0]
cat10hmm1_2_2 = cat10hmm1_2[1]
cat10hmm1_2_3 = cat10hmm1_2[2]
cat10hmm1_3 = cat10hmm1[2]
cat10hmm1_3_1 = cat10hmm1_3[0]
cat10hmm1_3_2 = cat10hmm1_3[1]
cat10hmm1_3_3 = cat10hmm1_3[2]
cat10hmm1_4 = cat10hmm1[3]
cat10hmm1_4_1 = cat10hmm1_4[0]
cat10hmm1_4_2 = cat10hmm1_4[1]
cat10hmm1_4_3 = cat10hmm1_4[2]
cat10hmm1_5 = cat10hmm1[4]
cat10hmm1_5_1 = cat10hmm1_5[0]
cat10hmm1_5_2 = cat10hmm1_5[1]
cat10hmm1_5_3 = cat10hmm1_5[2]
cat10hmm1_6 = cat10hmm1[5]
cat10hmm1_6_1 = cat10hmm1_2[0]
cat10hmm1_6_2 = cat10hmm1_2[1]
cat10hmm1_6_3 = cat10hmm1_2[2]
cat10hmm1_7 = cat10hmm1[6]
cat10hmm1_7_1 = cat10hmm1_7[0]
cat10hmm1_7_2 = cat10hmm1_7[1]
cat10hmm1_7_3 = cat10hmm1_7[2]
cat10hmm1_8 = cat10hmm1[7]
cat10hmm1_8_1 = cat10hmm1_8[0]
cat10hmm1_8_2 = cat10hmm1_8[1]
cat10hmm1_8_3 = cat10hmm1_8[2]
cat10hmm1_9 = cat10hmm1[8]
cat10hmm1_9_1 = cat10hmm1_9[0]
cat10hmm1_9_2 = cat10hmm1_9[1]
cat10hmm1_9_3 = cat10hmm1_9[2]
cat10hmm1_10 = cat10hmm1[9]
cat10hmm1_10_1 = cat10hmm1_10[0]
cat10hmm1_10_2 = cat10hmm1_10[1]
cat10hmm1_10_3 = cat10hmm1_10[2]
cat10hmm1_11 = cat10hmm1[10]
cat10hmm1_11_1 = cat10hmm1_11[0]
cat10hmm1_11_2 = cat10hmm1_11[1]
cat10hmm1_11_3 = cat10hmm1_11[2]
dog1hmm1 = dog1[0]
dog1hmm1_1 = dog1hmm1[0]
dog1hmm1_1_1 = dog1hmm1_1[0]
dog1hmm1_1_2 = dog1hmm1_1[1]
dog1hmm1_1_3 = dog1hmm1_1[2]
dog1hmm1_2 = dog1hmm1[1]
dog1hmm1_2_1 = dog1hmm1_2[0]
dog1hmm1_2_2 = dog1hmm1_2[1]
dog1hmm1_2_3 = dog1hmm1_2[2]
dog1hmm1_3 = dog1hmm1[2]
dog1hmm1_3_1 = dog1hmm1_3[0]
dog1hmm1_3_2 = dog1hmm1_3[1]
dog1hmm1_3_3 = dog1hmm1_3[2]
dog1hmm1_4 = dog1hmm1[3]
dog1hmm1_4_1 = dog1hmm1_4[0]
dog1hmm1_4_2 = dog1hmm1_4[1]
dog1hmm1_4_3 = dog1hmm1_4[2]
dog1hmm1_5 = dog1hmm1[4]
dog1hmm1_5_1 = dog1hmm1_5[0]
dog1hmm1_5_2 = dog1hmm1_5[1]
dog1hmm1_5_3 = dog1hmm1_5[2]
dog1hmm1_6 = dog1hmm1[5]
dog1hmm1_6_1 = dog1hmm1_2[0]
dog1hmm1_6_2 = dog1hmm1_2[1]
dog1hmm1_6_3 = dog1hmm1_2[2]
dog1hmm1_7 = dog1hmm1[6]
dog1hmm1_7_1 = dog1hmm1_7[0]
dog1hmm1_7_2 = dog1hmm1_7[1]
dog1hmm1_7_3 = dog1hmm1_7[2]
dog1hmm1_8 = dog1hmm1[7]
dog1hmm1_8_1 = dog1hmm1_8[0]
dog1hmm1_8_2 = dog1hmm1_8[1]
dog1hmm1_8_3 = dog1hmm1_8[2]
dog1hmm1_9 = dog1hmm1[8]
dog1hmm1_9_1 = dog1hmm1_9[0]
dog1hmm1_9_2 = dog1hmm1_9[1]
dog1hmm1_9_3 = dog1hmm1_9[2]
dog1hmm1_10 = dog1hmm1[9]
dog1hmm1_10_1 = dog1hmm1_10[0]
dog1hmm1_10_2 = dog1hmm1_10[1]
dog1hmm1_10_3 = dog1hmm1_10[2]
dog1hmm1_11 = dog1hmm1[10]
dog1hmm1_11_1 = dog1hmm1_11[0]
dog1hmm1_11_2 = dog1hmm1_11[1]
dog1hmm1_11_3 = dog1hmm1_11[2]
dog2hmm1 = dog2[0]
dog2hmm1_1 = dog2hmm1[0]
dog2hmm1_1_1 = dog2hmm1_1[0]
dog2hmm1_1_2 = dog2hmm1_1[1]
dog2hmm1_1_3 = dog2hmm1_1[2]
dog2hmm1_2 = dog2hmm1[1]
dog2hmm1_2_1 = dog2hmm1_2[0]
dog2hmm1_2_2 = dog2hmm1_2[1]
dog2hmm1_2_3 = dog2hmm1_2[2]
dog2hmm1_3 = dog2hmm1[2]
dog2hmm1_3_1 = dog2hmm1_3[0]
dog2hmm1_3_2 = dog2hmm1_3[1]
dog2hmm1_3_3 = dog2hmm1_3[2]
dog2hmm1_4 = dog2hmm1[3]
dog2hmm1_4_1 = dog2hmm1_4[0]
dog2hmm1_4_2 = dog2hmm1_4[1]
dog2hmm1_4_3 = dog2hmm1_4[2]
dog2hmm1_5 = dog2hmm1[4]
dog2hmm1_5_1 = dog2hmm1_5[0]
dog2hmm1_5_2 = dog2hmm1_5[1]
dog2hmm1_5_3 = dog2hmm1_5[2]
dog2hmm1_6 = dog2hmm1[5]
dog2hmm1_6_1 = dog2hmm1_2[0]
dog2hmm1_6_2 = dog2hmm1_2[1]
dog2hmm1_6_3 = dog2hmm1_2[2]
dog2hmm1_7 = dog2hmm1[6]
dog2hmm1_7_1 = dog2hmm1_7[0]
dog2hmm1_7_2 = dog2hmm1_7[1]
dog2hmm1_7_3 = dog2hmm1_7[2]
dog2hmm1_8 = dog2hmm1[7]
dog2hmm1_8_1 = dog2hmm1_8[0]
dog2hmm1_8_2 = dog2hmm1_8[1]
dog2hmm1_8_3 = dog2hmm1_8[2]
dog2hmm1_9 = dog2hmm1[8]
dog2hmm1_9_1 = dog2hmm1_9[0]
dog2hmm1_9_2 = dog2hmm1_9[1]
dog2hmm1_9_3 = dog2hmm1_9[2]
dog2hmm1_10 = dog2hmm1[9]
dog2hmm1_10_1 = dog2hmm1_10[0]
dog2hmm1_10_2 = dog2hmm1_10[1]
dog2hmm1_10_3 = dog2hmm1_10[2]
dog2hmm1_11 = dog2hmm1[10]
dog2hmm1_11_1 = dog2hmm1_11[0]
dog2hmm1_11_2 = dog2hmm1_11[1]
dog2hmm1_11_3 = dog2hmm1_11[2]
dog3hmm1 = dog3[0]
dog3hmm1_1 = dog3hmm1[0]
dog3hmm1_1_1 = dog3hmm1_1[0]
dog3hmm1_1_2 = dog3hmm1_1[1]
dog3hmm1_1_3 = dog3hmm1_1[2]
dog3hmm1_2 = dog3hmm1[1]
dog3hmm1_2_1 = dog3hmm1_2[0]
dog3hmm1_2_2 = dog3hmm1_2[1]
dog3hmm1_2_3 = dog3hmm1_2[2]
dog3hmm1_3 = dog3hmm1[2]
dog3hmm1_3_1 = dog3hmm1_3[0]
dog3hmm1_3_2 = dog3hmm1_3[1]
dog3hmm1_3_3 = dog3hmm1_3[2]
dog3hmm1_4 = dog3hmm1[3]
dog3hmm1_4_1 = dog3hmm1_4[0]
dog3hmm1_4_2 = dog3hmm1_4[1]
dog3hmm1_4_3 = dog3hmm1_4[2]
dog3hmm1_5 = dog3hmm1[4]
dog3hmm1_5_1 = dog3hmm1_5[0]
dog3hmm1_5_2 = dog3hmm1_5[1]
dog3hmm1_5_3 = dog3hmm1_5[2]
dog3hmm1_6 = dog3hmm1[5]
dog3hmm1_6_1 = dog3hmm1_2[0]
dog3hmm1_6_2 = dog3hmm1_2[1]
dog3hmm1_6_3 = dog3hmm1_2[2]
dog3hmm1_7 = dog3hmm1[6]
dog3hmm1_7_1 = dog3hmm1_7[0]
dog3hmm1_7_2 = dog3hmm1_7[1]
dog3hmm1_7_3 = dog3hmm1_7[2]
dog3hmm1_8 = dog3hmm1[7]
dog3hmm1_8_1 = dog3hmm1_8[0]
dog3hmm1_8_2 = dog3hmm1_8[1]
dog3hmm1_8_3 = dog3hmm1_8[2]
dog3hmm1_9 = dog3hmm1[8]
dog3hmm1_9_1 = dog3hmm1_9[0]
dog3hmm1_9_2 = dog3hmm1_9[1]
dog3hmm1_9_3 = dog3hmm1_9[2]
dog3hmm1_10 = dog3hmm1[9]
dog3hmm1_10_1 = dog3hmm1_10[0]
dog3hmm1_10_2 = dog3hmm1_10[1]
dog3hmm1_10_3 = dog3hmm1_10[2]
dog3hmm1_11 = dog3hmm1[10]
dog3hmm1_11_1 = dog3hmm1_11[0]
dog3hmm1_11_2 = dog3hmm1_11[1]
dog3hmm1_11_3 = dog3hmm1_11[2]
dog4hmm1 = dog4[0]
dog4hmm1_1 = dog4hmm1[0]
dog4hmm1_1_1 = dog4hmm1_1[0]
dog4hmm1_1_2 = dog4hmm1_1[1]
dog4hmm1_1_3 = dog4hmm1_1[2]
dog4hmm1_2 = dog4hmm1[1]
dog4hmm1_2_1 = dog4hmm1_2[0]
dog4hmm1_2_2 = dog4hmm1_2[1]
dog4hmm1_2_3 = dog4hmm1_2[2]
dog4hmm1_3 = dog4hmm1[2]
dog4hmm1_3_1 = dog4hmm1_3[0]
dog4hmm1_3_2 = dog4hmm1_3[1]
dog4hmm1_3_3 = dog4hmm1_3[2]
dog4hmm1_4 = dog4hmm1[3]
dog4hmm1_4_1 = dog4hmm1_4[0]
dog4hmm1_4_2 = dog4hmm1_4[1]
dog4hmm1_4_3 = dog4hmm1_4[2]
dog4hmm1_5 = dog4hmm1[4]
dog4hmm1_5_1 = dog4hmm1_5[0]
dog4hmm1_5_2 = dog4hmm1_5[1]
dog4hmm1_5_3 = dog4hmm1_5[2]
dog4hmm1_6 = dog4hmm1[5]
dog4hmm1_6_1 = dog4hmm1_2[0]
dog4hmm1_6_2 = dog4hmm1_2[1]
dog4hmm1_6_3 = dog4hmm1_2[2]
dog4hmm1_7 = dog4hmm1[6]
dog4hmm1_7_1 = dog4hmm1_7[0]
dog4hmm1_7_2 = dog4hmm1_7[1]
dog4hmm1_7_3 = dog4hmm1_7[2]
dog4hmm1_8 = dog4hmm1[7]
dog4hmm1_8_1 = dog4hmm1_8[0]
dog4hmm1_8_2 = dog4hmm1_8[1]
dog4hmm1_8_3 = dog4hmm1_8[2]
dog4hmm1_9 = dog4hmm1[8]
dog4hmm1_9_1 = dog4hmm1_9[0]
dog4hmm1_9_2 = dog4hmm1_9[1]
dog4hmm1_9_3 = dog4hmm1_9[2]
dog4hmm1_10 = dog4hmm1[9]
dog4hmm1_10_1 = dog4hmm1_10[0]
dog4hmm1_10_2 = dog4hmm1_10[1]
dog4hmm1_10_3 = dog4hmm1_10[2]
dog4hmm1_11 = dog4hmm1[10]
dog4hmm1_11_1 = dog4hmm1_11[0]
dog4hmm1_11_2 = dog4hmm1_11[1]
dog4hmm1_11_3 = dog4hmm1_11[2]
dog5hmm1 = dog5[0]
dog5hmm1_1 = dog5hmm1[0]
dog5hmm1_1_1 = dog5hmm1_1[0]
dog5hmm1_1_2 = dog5hmm1_1[1]
dog5hmm1_1_3 = dog5hmm1_1[2]
dog5hmm1_2 = dog5hmm1[1]
dog5hmm1_2_1 = dog5hmm1_2[0]
dog5hmm1_2_2 = dog5hmm1_2[1]
dog5hmm1_2_3 = dog5hmm1_2[2]
dog5hmm1_3 = dog5hmm1[2]
dog5hmm1_3_1 = dog5hmm1_3[0]
dog5hmm1_3_2 = dog5hmm1_3[1]
dog5hmm1_3_3 = dog5hmm1_3[2]
dog5hmm1_4 = dog5hmm1[3]
dog5hmm1_4_1 = dog5hmm1_4[0]
dog5hmm1_4_2 = dog5hmm1_4[1]
dog5hmm1_4_3 = dog5hmm1_4[2]
dog5hmm1_5 = dog5hmm1[4]
dog5hmm1_5_1 = dog5hmm1_5[0]
dog5hmm1_5_2 = dog5hmm1_5[1]
dog5hmm1_5_3 = dog5hmm1_5[2]
dog5hmm1_6 = dog5hmm1[5]
dog5hmm1_6_1 = dog5hmm1_2[0]
dog5hmm1_6_2 = dog5hmm1_2[1]
dog5hmm1_6_3 = dog5hmm1_2[2]
dog5hmm1_7 = dog5hmm1[6]
dog5hmm1_7_1 = dog5hmm1_7[0]
dog5hmm1_7_2 = dog5hmm1_7[1]
dog5hmm1_7_3 = dog5hmm1_7[2]
dog5hmm1_8 = dog5hmm1[7]
dog5hmm1_8_1 = dog5hmm1_8[0]
dog5hmm1_8_2 = dog5hmm1_8[1]
dog5hmm1_8_3 = dog5hmm1_8[2]
dog5hmm1_9 = dog5hmm1[8]
dog5hmm1_9_1 = dog5hmm1_9[0]
dog5hmm1_9_2 = dog5hmm1_9[1]
dog5hmm1_9_3 = dog5hmm1_9[2]
dog5hmm1_10 = dog5hmm1[9]
dog5hmm1_10_1 = dog5hmm1_10[0]
dog5hmm1_10_2 = dog5hmm1_10[1]
dog5hmm1_10_3 = dog5hmm1_10[2]
dog5hmm1_11 = dog5hmm1[10]
dog5hmm1_11_1 = dog5hmm1_11[0]
dog5hmm1_11_2 = dog5hmm1_11[1]
dog5hmm1_11_3 = dog5hmm1_11[2]
dog6hmm1 = dog6[0]
dog6hmm1_1 = dog6hmm1[0]
dog6hmm1_1_1 = dog6hmm1_1[0]
dog6hmm1_1_2 = dog6hmm1_1[1]
dog6hmm1_1_3 = dog6hmm1_1[2]
dog6hmm1_2 = dog6hmm1[1]
dog6hmm1_2_1 = dog6hmm1_2[0]
dog6hmm1_2_2 = dog6hmm1_2[1]
dog6hmm1_2_3 = dog6hmm1_2[2]
dog6hmm1_3 = dog6hmm1[2]
dog6hmm1_3_1 = dog6hmm1_3[0]
dog6hmm1_3_2 = dog6hmm1_3[1]
dog6hmm1_3_3 = dog6hmm1_3[2]
dog6hmm1_4 = dog6hmm1[3]
dog6hmm1_4_1 = dog6hmm1_4[0]
dog6hmm1_4_2 = dog6hmm1_4[1]
dog6hmm1_4_3 = dog6hmm1_4[2]
dog6hmm1_5 = dog6hmm1[4]
dog6hmm1_5_1 = dog6hmm1_5[0]
dog6hmm1_5_2 = dog6hmm1_5[1]
dog6hmm1_5_3 = dog6hmm1_5[2]
dog6hmm1_6 = dog6hmm1[5]
dog6hmm1_6_1 = dog6hmm1_2[0]
dog6hmm1_6_2 = dog6hmm1_2[1]
dog6hmm1_6_3 = dog6hmm1_2[2]
dog6hmm1_7 = dog6hmm1[6]
dog6hmm1_7_1 = dog6hmm1_7[0]
dog6hmm1_7_2 = dog6hmm1_7[1]
dog6hmm1_7_3 = dog6hmm1_7[2]
dog6hmm1_8 = dog6hmm1[7]
dog6hmm1_8_1 = dog6hmm1_8[0]
dog6hmm1_8_2 = dog6hmm1_8[1]
dog6hmm1_8_3 = dog6hmm1_8[2]
dog6hmm1_9 = dog6hmm1[8]
dog6hmm1_9_1 = dog6hmm1_9[0]
dog6hmm1_9_2 = dog6hmm1_9[1]
dog6hmm1_9_3 = dog6hmm1_9[2]
dog6hmm1_10 = dog6hmm1[9]
dog6hmm1_10_1 = dog6hmm1_10[0]
dog6hmm1_10_2 = dog6hmm1_10[1]
dog6hmm1_10_3 = dog6hmm1_10[2]
dog6hmm1_11 = dog6hmm1[10]
dog6hmm1_11_1 = dog6hmm1_11[0]
dog6hmm1_11_2 = dog6hmm1_11[1]
dog6hmm1_11_3 = dog6hmm1_11[2]
dog7hmm1 = dog7[0]
dog7hmm1_1 = dog7hmm1[0]
dog7hmm1_1_1 = dog7hmm1_1[0]
dog7hmm1_1_2 = dog7hmm1_1[1]
dog7hmm1_1_3 = dog7hmm1_1[2]
dog7hmm1_2 = dog7hmm1[1]
dog7hmm1_2_1 = dog7hmm1_2[0]
dog7hmm1_2_2 = dog7hmm1_2[1]
dog7hmm1_2_3 = dog7hmm1_2[2]
dog7hmm1_3 = dog7hmm1[2]
dog7hmm1_3_1 = dog7hmm1_3[0]
dog7hmm1_3_2 = dog7hmm1_3[1]
dog7hmm1_3_3 = dog7hmm1_3[2]
dog7hmm1_4 = dog7hmm1[3]
dog7hmm1_4_1 = dog7hmm1_4[0]
dog7hmm1_4_2 = dog7hmm1_4[1]
dog7hmm1_4_3 = dog7hmm1_4[2]
dog7hmm1_5 = dog7hmm1[4]
dog7hmm1_5_1 = dog7hmm1_5[0]
dog7hmm1_5_2 = dog7hmm1_5[1]
dog7hmm1_5_3 = dog7hmm1_5[2]
dog7hmm1_6 = dog7hmm1[5]
dog7hmm1_6_1 = dog7hmm1_2[0]
dog7hmm1_6_2 = dog7hmm1_2[1]
dog7hmm1_6_3 = dog7hmm1_2[2]
dog7hmm1_7 = dog7hmm1[6]
dog7hmm1_7_1 = dog7hmm1_7[0]
dog7hmm1_7_2 = dog7hmm1_7[1]
dog7hmm1_7_3 = dog7hmm1_7[2]
dog7hmm1_8 = dog7hmm1[7]
dog7hmm1_8_1 = dog7hmm1_8[0]
dog7hmm1_8_2 = dog7hmm1_8[1]
dog7hmm1_8_3 = dog7hmm1_8[2]
dog7hmm1_9 = dog7hmm1[8]
dog7hmm1_9_1 = dog7hmm1_9[0]
dog7hmm1_9_2 = dog7hmm1_9[1]
dog7hmm1_9_3 = dog7hmm1_9[2]
dog7hmm1_10 = dog7hmm1[9]
dog7hmm1_10_1 = dog7hmm1_10[0]
dog7hmm1_10_2 = dog7hmm1_10[1]
dog7hmm1_10_3 = dog7hmm1_10[2]
dog7hmm1_11 = dog7hmm1[10]
dog7hmm1_11_1 = dog7hmm1_11[0]
dog7hmm1_11_2 = dog7hmm1_11[1]
dog7hmm1_11_3 = dog7hmm1_11[2]
dog8hmm1 = dog8[0]
dog8hmm1_1 = dog8hmm1[0]
dog8hmm1_1_1 = dog8hmm1_1[0]
dog8hmm1_1_2 = dog8hmm1_1[1]
dog8hmm1_1_3 = dog8hmm1_1[2]
dog8hmm1_2 = dog8hmm1[1]
dog8hmm1_2_1 = dog8hmm1_2[0]
dog8hmm1_2_2 = dog8hmm1_2[1]
dog8hmm1_2_3 = dog8hmm1_2[2]
dog8hmm1_3 = dog8hmm1[2]
dog8hmm1_3_1 = dog8hmm1_3[0]
dog8hmm1_3_2 = dog8hmm1_3[1]
dog8hmm1_3_3 = dog8hmm1_3[2]
dog8hmm1_4 = dog8hmm1[3]
dog8hmm1_4_1 = dog8hmm1_4[0]
dog8hmm1_4_2 = dog8hmm1_4[1]
dog8hmm1_4_3 = dog8hmm1_4[2]
dog8hmm1_5 = dog8hmm1[4]
dog8hmm1_5_1 = dog8hmm1_5[0]
dog8hmm1_5_2 = dog8hmm1_5[1]
dog8hmm1_5_3 = dog8hmm1_5[2]
dog8hmm1_6 = dog8hmm1[5]
dog8hmm1_6_1 = dog8hmm1_2[0]
dog8hmm1_6_2 = dog8hmm1_2[1]
dog8hmm1_6_3 = dog8hmm1_2[2]
dog8hmm1_7 = dog8hmm1[6]
dog8hmm1_7_1 = dog8hmm1_7[0]
dog8hmm1_7_2 = dog8hmm1_7[1]
dog8hmm1_7_3 = dog8hmm1_7[2]
dog8hmm1_8 = dog8hmm1[7]
dog8hmm1_8_1 = dog8hmm1_8[0]
dog8hmm1_8_2 = dog8hmm1_8[1]
dog8hmm1_8_3 = dog8hmm1_8[2]
dog8hmm1_9 = dog8hmm1[8]
dog8hmm1_9_1 = dog8hmm1_9[0]
dog8hmm1_9_2 = dog8hmm1_9[1]
dog8hmm1_9_3 = dog8hmm1_9[2]
dog8hmm1_10 = dog8hmm1[9]
dog8hmm1_10_1 = dog8hmm1_10[0]
dog8hmm1_10_2 = dog8hmm1_10[1]
dog8hmm1_10_3 = dog8hmm1_10[2]
dog8hmm1_11 = dog8hmm1[10]
dog8hmm1_11_1 = dog8hmm1_11[0]
dog8hmm1_11_2 = dog8hmm1_11[1]
dog8hmm1_11_3 = dog8hmm1_11[2]
dog9hmm1 = dog9[0]
dog9hmm1_1 = dog9hmm1[0]
dog9hmm1_1_1 = dog9hmm1_1[0]
dog9hmm1_1_2 = dog9hmm1_1[1]
dog9hmm1_1_3 = dog9hmm1_1[2]
dog9hmm1_2 = dog9hmm1[1]
dog9hmm1_2_1 = dog9hmm1_2[0]
dog9hmm1_2_2 = dog9hmm1_2[1]
dog9hmm1_2_3 = dog9hmm1_2[2]
dog9hmm1_3 = dog9hmm1[2]
dog9hmm1_3_1 = dog9hmm1_3[0]
dog9hmm1_3_2 = dog9hmm1_3[1]
dog9hmm1_3_3 = dog9hmm1_3[2]
dog9hmm1_4 = dog9hmm1[3]
dog9hmm1_4_1 = dog9hmm1_4[0]
dog9hmm1_4_2 = dog9hmm1_4[1]
dog9hmm1_4_3 = dog9hmm1_4[2]
dog9hmm1_5 = dog9hmm1[4]
dog9hmm1_5_1 = dog9hmm1_5[0]
dog9hmm1_5_2 = dog9hmm1_5[1]
dog9hmm1_5_3 = dog9hmm1_5[2]
dog9hmm1_6 = dog9hmm1[5]
dog9hmm1_6_1 = dog9hmm1_2[0]
dog9hmm1_6_2 = dog9hmm1_2[1]
dog9hmm1_6_3 = dog9hmm1_2[2]
dog9hmm1_7 = dog9hmm1[6]
dog9hmm1_7_1 = dog9hmm1_7[0]
dog9hmm1_7_2 = dog9hmm1_7[1]
dog9hmm1_7_3 = dog9hmm1_7[2]
dog9hmm1_8 = dog9hmm1[7]
dog9hmm1_8_1 = dog9hmm1_8[0]
dog9hmm1_8_2 = dog9hmm1_8[1]
dog9hmm1_8_3 = dog9hmm1_8[2]
dog9hmm1_9 = dog9hmm1[8]
dog9hmm1_9_1 = dog9hmm1_9[0]
dog9hmm1_9_2 = dog9hmm1_9[1]
dog9hmm1_9_3 = dog9hmm1_9[2]
dog9hmm1_10 = dog9hmm1[9]
dog9hmm1_10_1 = dog9hmm1_10[0]
dog9hmm1_10_2 = dog9hmm1_10[1]
dog9hmm1_10_3 = dog9hmm1_10[2]
dog9hmm1_11 = dog9hmm1[10]
dog9hmm1_11_1 = dog9hmm1_11[0]
dog9hmm1_11_2 = dog9hmm1_11[1]
dog9hmm1_11_3 = dog9hmm1_11[2]
dog10hmm1 = dog10[0]
dog10hmm1_1 = dog10hmm1[0]
dog10hmm1_1_1 = dog10hmm1_1[0]
dog10hmm1_1_2 = dog10hmm1_1[1]
dog10hmm1_1_3 = dog10hmm1_1[2]
dog10hmm1_2 = dog10hmm1[1]
dog10hmm1_2_1 = dog10hmm1_2[0]
dog10hmm1_2_2 = dog10hmm1_2[1]
dog10hmm1_2_3 = dog10hmm1_2[2]
dog10hmm1_3 = dog10hmm1[2]
dog10hmm1_3_1 = dog10hmm1_3[0]
dog10hmm1_3_2 = dog10hmm1_3[1]
dog10hmm1_3_3 = dog10hmm1_3[2]
dog10hmm1_4 = dog10hmm1[3]
dog10hmm1_4_1 = dog10hmm1_4[0]
dog10hmm1_4_2 = dog10hmm1_4[1]
dog10hmm1_4_3 = dog10hmm1_4[2]
dog10hmm1_5 = dog10hmm1[4]
dog10hmm1_5_1 = dog10hmm1_5[0]
dog10hmm1_5_2 = dog10hmm1_5[1]
dog10hmm1_5_3 = dog10hmm1_5[2]
dog10hmm1_6 = dog10hmm1[5]
dog10hmm1_6_1 = dog10hmm1_2[0]
dog10hmm1_6_2 = dog10hmm1_2[1]
dog10hmm1_6_3 = dog10hmm1_2[2]
dog10hmm1_7 = dog10hmm1[6]
dog10hmm1_7_1 = dog10hmm1_7[0]
dog10hmm1_7_2 = dog10hmm1_7[1]
dog10hmm1_7_3 = dog10hmm1_7[2]
dog10hmm1_8 = dog10hmm1[7]
dog10hmm1_8_1 = dog10hmm1_8[0]
dog10hmm1_8_2 = dog10hmm1_8[1]
dog10hmm1_8_3 = dog10hmm1_8[2]
dog10hmm1_9 = dog10hmm1[8]
dog10hmm1_9_1 = dog10hmm1_9[0]
dog10hmm1_9_2 = dog10hmm1_9[1]
dog10hmm1_9_3 = dog10hmm1_9[2]
dog10hmm1_10 = dog10hmm1[9]
dog10hmm1_10_1 = dog10hmm1_10[0]
dog10hmm1_10_2 = dog10hmm1_10[1]
dog10hmm1_10_3 = dog10hmm1_10[2]
dog10hmm1_11 = dog10hmm1[10]
dog10hmm1_11_1 = dog10hmm1_11[0]
dog10hmm1_11_2 = dog10hmm1_11[1]
dog10hmm1_11_3 = dog10hmm1_11[2]
catidea = 0
if testhmm1_1_1 == cat1hmm1_1_1:
    catidea = catidea + 1
if testhmm1_1_1 == cat2hmm1_1_1:
    catidea = catidea + 1
if testhmm1_1_1 == cat3hmm1_1_1:
    catidea = catidea + 1
if testhmm1_1_1 == cat4hmm1_1_1:
    catidea = catidea + 1
if testhmm1_1_1 == cat5hmm1_1_1:
    catidea = catidea + 1
if testhmm1_1_1 == cat6hmm1_1_1:
    catidea = catidea + 1
if testhmm1_1_1 == cat7hmm1_1_1:
    catidea = catidea + 1
if testhmm1_1_1 == cat8hmm1_1_1:
    catidea = catidea + 1
if testhmm1_1_1 == cat9hmm1_1_1:
    catidea = catidea + 1
if testhmm1_1_1 == cat10hmm1_1_1:
    catidea = catidea + 1
if testhmm1_1_2 == cat1hmm1_1_2:
    catidea = catidea + 1
if testhmm1_1_2 == cat2hmm1_1_2:
    catidea = catidea + 1
if testhmm1_1_2 == cat3hmm1_1_2:
    catidea = catidea + 1
if testhmm1_1_2 == cat4hmm1_1_2:
    catidea = catidea + 1
if testhmm1_1_2 == cat5hmm1_1_2:
    catidea = catidea + 1
if testhmm1_1_2 == cat6hmm1_1_2:
    catidea = catidea + 1
if testhmm1_1_2 == cat7hmm1_1_2:
    catidea = catidea + 1
if testhmm1_1_2 == cat8hmm1_1_2:
    catidea = catidea + 1
if testhmm1_1_2 == cat9hmm1_1_2:
    catidea = catidea + 1
if testhmm1_1_2 == cat10hmm1_1_2:
    catidea = catidea + 1
if testhmm1_1_3 == cat1hmm1_1_3:
    catidea = catidea + 1
if testhmm1_1_3 == cat2hmm1_1_3:
    catidea = catidea + 1
if testhmm1_1_3 == cat3hmm1_1_3:
    catidea = catidea + 1
if testhmm1_1_3 == cat4hmm1_1_3:
    catidea = catidea + 1
if testhmm1_1_3 == cat5hmm1_1_3:
    catidea = catidea + 1
if testhmm1_1_3 == cat6hmm1_1_3:
    catidea = catidea + 1
if testhmm1_1_3 == cat7hmm1_1_3:
    catidea = catidea + 1
if testhmm1_1_3 == cat8hmm1_1_3:
    catidea = catidea + 1
if testhmm1_1_3 == cat9hmm1_1_3:
    catidea = catidea + 1
if testhmm1_1_3 == cat10hmm1_1_3:
    catidea = catidea + 1
if testhmm1_2_1 == cat1hmm1_2_1:
    catidea = catidea + 1
if testhmm1_2_1 == cat2hmm1_2_1:
    catidea = catidea + 1
if testhmm1_2_1 == cat3hmm1_2_1:
    catidea = catidea + 1
if testhmm1_2_1 == cat4hmm1_2_1:
    catidea = catidea + 1
if testhmm1_2_1 == cat5hmm1_2_1:
    catidea = catidea + 1
if testhmm1_2_1 == cat6hmm1_2_1:
    catidea = catidea + 1
if testhmm1_2_1 == cat7hmm1_2_1:
    catidea = catidea + 1
if testhmm1_2_1 == cat8hmm1_2_1:
    catidea = catidea + 1
if testhmm1_2_1 == cat9hmm1_2_1:
    catidea = catidea + 1
if testhmm1_2_1 == cat10hmm1_2_1:
    catidea = catidea + 1
if testhmm1_2_2 == cat1hmm1_2_2:
    catidea = catidea + 1
if testhmm1_2_2 == cat2hmm1_2_2:
    catidea = catidea + 1
if testhmm1_2_2 == cat3hmm1_2_2:
    catidea = catidea + 1
if testhmm1_2_2 == cat4hmm1_2_2:
    catidea = catidea + 1
if testhmm1_2_2 == cat5hmm1_2_2:
    catidea = catidea + 1
if testhmm1_2_2 == cat6hmm1_2_2:
    catidea = catidea + 1
if testhmm1_2_2 == cat7hmm1_2_2:
    catidea = catidea + 1
if testhmm1_2_2 == cat8hmm1_2_2:
    catidea = catidea + 1
if testhmm1_2_2 == cat9hmm1_2_2:
    catidea = catidea + 1
if testhmm1_2_2 == cat10hmm1_2_2:
    catidea = catidea + 1
if testhmm1_2_3 == cat1hmm1_2_3:
    catidea = catidea + 1
if testhmm1_2_3 == cat2hmm1_2_3:
    catidea = catidea + 1
if testhmm1_2_3 == cat3hmm1_2_3:
    catidea = catidea + 1
if testhmm1_2_3 == cat4hmm1_2_3:
    catidea = catidea + 1
if testhmm1_2_3 == cat5hmm1_2_3:
    catidea = catidea + 1
if testhmm1_2_3 == cat6hmm1_2_3:
    catidea = catidea + 1
if testhmm1_2_3 == cat7hmm1_2_3:
    catidea = catidea + 1
if testhmm1_2_3 == cat8hmm1_2_3:
    catidea = catidea + 1
if testhmm1_2_3 == cat9hmm1_2_3:
    catidea = catidea + 1
if testhmm1_2_3 == cat10hmm1_2_3:
    catidea = catidea + 1
if testhmm1_3_1 == cat1hmm1_3_1:
    catidea = catidea + 1
if testhmm1_3_1 == cat2hmm1_3_1:
    catidea = catidea + 1
if testhmm1_3_1 == cat3hmm1_3_1:
    catidea = catidea + 1
if testhmm1_3_1 == cat4hmm1_3_1:
    catidea = catidea + 1
if testhmm1_3_1 == cat5hmm1_3_1:
    catidea = catidea + 1
if testhmm1_3_1 == cat6hmm1_3_1:
    catidea = catidea + 1
if testhmm1_3_1 == cat7hmm1_3_1:
    catidea = catidea + 1
if testhmm1_3_1 == cat8hmm1_3_1:
    catidea = catidea + 1
if testhmm1_3_1 == cat9hmm1_3_1:
    catidea = catidea + 1
if testhmm1_3_1 == cat10hmm1_3_1:
    catidea = catidea + 1
if testhmm1_3_2 == cat1hmm1_3_2:
    catidea = catidea + 1
if testhmm1_3_2 == cat2hmm1_3_2:
    catidea = catidea + 1
if testhmm1_3_2 == cat3hmm1_3_2:
    catidea = catidea + 1
if testhmm1_3_2 == cat4hmm1_3_2:
    catidea = catidea + 1
if testhmm1_3_2 == cat5hmm1_3_2:
    catidea = catidea + 1
if testhmm1_3_2 == cat6hmm1_3_2:
    catidea = catidea + 1
if testhmm1_3_2 == cat7hmm1_3_2:
    catidea = catidea + 1
if testhmm1_3_2 == cat8hmm1_3_2:
    catidea = catidea + 1
if testhmm1_3_2 == cat9hmm1_3_2:
    catidea = catidea + 1
if testhmm1_3_2 == cat10hmm1_3_2:
    catidea = catidea + 1
if testhmm1_3_3 == cat1hmm1_3_3:
    catidea = catidea + 1
if testhmm1_3_3 == cat2hmm1_3_3:
    catidea = catidea + 1
if testhmm1_3_3 == cat3hmm1_3_3:
    catidea = catidea + 1
if testhmm1_3_3 == cat4hmm1_3_3:
    catidea = catidea + 1
if testhmm1_3_3 == cat5hmm1_3_3:
    catidea = catidea + 1
if testhmm1_3_3 == cat6hmm1_3_3:
    catidea = catidea + 1
if testhmm1_3_3 == cat7hmm1_3_3:
    catidea = catidea + 1
if testhmm1_3_3 == cat8hmm1_3_3:
    catidea = catidea + 1
if testhmm1_3_3 == cat9hmm1_3_3:
    catidea = catidea + 1
if testhmm1_3_3 == cat10hmm1_3_3:
    catidea = catidea + 1
if testhmm1_4_1 == cat1hmm1_4_1:
    catidea = catidea + 1
if testhmm1_4_1 == cat2hmm1_4_1:
    catidea = catidea + 1
if testhmm1_4_1 == cat3hmm1_4_1:
    catidea = catidea + 1
if testhmm1_4_1 == cat4hmm1_4_1:
    catidea = catidea + 1
if testhmm1_4_1 == cat5hmm1_4_1:
    catidea = catidea + 1
if testhmm1_4_1 == cat6hmm1_4_1:
    catidea = catidea + 1
if testhmm1_4_1 == cat7hmm1_4_1:
    catidea = catidea + 1
if testhmm1_4_1 == cat8hmm1_4_1:
    catidea = catidea + 1
if testhmm1_4_1 == cat9hmm1_4_1:
    catidea = catidea + 1
if testhmm1_4_1 == cat10hmm1_4_1:
    catidea = catidea + 1
if testhmm1_4_2 == cat1hmm1_4_2:
    catidea = catidea + 1
if testhmm1_4_2 == cat2hmm1_4_2:
    catidea = catidea + 1
if testhmm1_4_2 == cat3hmm1_4_2:
    catidea = catidea + 1
if testhmm1_4_2 == cat4hmm1_4_2:
    catidea = catidea + 1
if testhmm1_4_2 == cat5hmm1_4_2:
    catidea = catidea + 1
if testhmm1_4_2 == cat6hmm1_4_2:
    catidea = catidea + 1
if testhmm1_4_2 == cat7hmm1_4_2:
    catidea = catidea + 1
if testhmm1_4_2 == cat8hmm1_4_2:
    catidea = catidea + 1
if testhmm1_4_2 == cat9hmm1_4_2:
    catidea = catidea + 1
if testhmm1_4_2 == cat10hmm1_4_2:
    catidea = catidea + 1
if testhmm1_4_3 == cat1hmm1_4_3:
    catidea = catidea + 1
if testhmm1_4_3 == cat2hmm1_4_3:
    catidea = catidea + 1
if testhmm1_4_3 == cat3hmm1_4_3:
    catidea = catidea + 1
if testhmm1_4_3 == cat4hmm1_4_3:
    catidea = catidea + 1
if testhmm1_4_3 == cat5hmm1_4_3:
    catidea = catidea + 1
if testhmm1_4_3 == cat6hmm1_4_3:
    catidea = catidea + 1
if testhmm1_4_3 == cat7hmm1_4_3:
    catidea = catidea + 1
if testhmm1_4_3 == cat8hmm1_4_3:
    catidea = catidea + 1
if testhmm1_4_3 == cat9hmm1_4_3:
    catidea = catidea + 1
if testhmm1_4_3 == cat10hmm1_4_3:
    catidea = catidea + 1
if testhmm1_5_1 == cat1hmm1_5_1:
    catidea = catidea + 1
if testhmm1_5_1 == cat2hmm1_5_1:
    catidea = catidea + 1
if testhmm1_5_1 == cat3hmm1_5_1:
    catidea = catidea + 1
if testhmm1_5_1 == cat4hmm1_5_1:
    catidea = catidea + 1
if testhmm1_5_1 == cat5hmm1_5_1:
    catidea = catidea + 1
if testhmm1_5_1 == cat6hmm1_5_1:
    catidea = catidea + 1
if testhmm1_5_1 == cat7hmm1_5_1:
    catidea = catidea + 1
if testhmm1_5_1 == cat8hmm1_5_1:
    catidea = catidea + 1
if testhmm1_5_1 == cat9hmm1_5_1:
    catidea = catidea + 1
if testhmm1_5_1 == cat10hmm1_5_1:
    catidea = catidea + 1
if testhmm1_5_2 == cat1hmm1_5_2:
    catidea = catidea + 1
if testhmm1_5_2 == cat2hmm1_5_2:
    catidea = catidea + 1
if testhmm1_5_2 == cat3hmm1_5_2:
    catidea = catidea + 1
if testhmm1_5_2 == cat4hmm1_5_2:
    catidea = catidea + 1
if testhmm1_5_2 == cat5hmm1_5_2:
    catidea = catidea + 1
if testhmm1_5_2 == cat6hmm1_5_2:
    catidea = catidea + 1
if testhmm1_5_2 == cat7hmm1_5_2:
    catidea = catidea + 1
if testhmm1_5_2 == cat8hmm1_5_2:
    catidea = catidea + 1
if testhmm1_5_2 == cat9hmm1_5_2:
    catidea = catidea + 1
if testhmm1_5_2 == cat10hmm1_5_2:
    catidea = catidea + 1
if testhmm1_5_3 == cat1hmm1_5_3:
    catidea = catidea + 1
if testhmm1_5_3 == cat2hmm1_5_3:
    catidea = catidea + 1
if testhmm1_5_3 == cat3hmm1_5_3:
    catidea = catidea + 1
if testhmm1_5_3 == cat4hmm1_5_3:
    catidea = catidea + 1
if testhmm1_5_3 == cat5hmm1_5_3:
    catidea = catidea + 1
if testhmm1_5_3 == cat6hmm1_5_3:
    catidea = catidea + 1
if testhmm1_5_3 == cat7hmm1_5_3:
    catidea = catidea + 1
if testhmm1_5_3 == cat8hmm1_5_3:
    catidea = catidea + 1
if testhmm1_5_3 == cat9hmm1_5_3:
    catidea = catidea + 1
if testhmm1_5_3 == cat10hmm1_5_3:
    catidea = catidea + 1
if testhmm1_6_1 == cat1hmm1_6_1:
    catidea = catidea + 1
if testhmm1_6_1 == cat2hmm1_6_1:
    catidea = catidea + 1
if testhmm1_6_1 == cat3hmm1_6_1:
    catidea = catidea + 1
if testhmm1_6_1 == cat4hmm1_6_1:
    catidea = catidea + 1
if testhmm1_6_1 == cat5hmm1_6_1:
    catidea = catidea + 1
if testhmm1_6_1 == cat6hmm1_6_1:
    catidea = catidea + 1
if testhmm1_6_1 == cat7hmm1_6_1:
    catidea = catidea + 1
if testhmm1_6_1 == cat8hmm1_6_1:
    catidea = catidea + 1
if testhmm1_6_1 == cat9hmm1_6_1:
    catidea = catidea + 1
if testhmm1_6_1 == cat10hmm1_6_1:
    catidea = catidea + 1
if testhmm1_6_2 == cat1hmm1_6_2:
    catidea = catidea + 1
if testhmm1_6_2 == cat2hmm1_6_2:
    catidea = catidea + 1
if testhmm1_6_2 == cat3hmm1_6_2:
    catidea = catidea + 1
if testhmm1_6_2 == cat4hmm1_6_2:
    catidea = catidea + 1
if testhmm1_6_2 == cat5hmm1_6_2:
    catidea = catidea + 1
if testhmm1_6_2 == cat6hmm1_6_2:
    catidea = catidea + 1
if testhmm1_6_2 == cat7hmm1_6_2:
    catidea = catidea + 1
if testhmm1_6_2 == cat8hmm1_6_2:
    catidea = catidea + 1
if testhmm1_6_2 == cat9hmm1_6_2:
    catidea = catidea + 1
if testhmm1_6_2 == cat10hmm1_6_2:
    catidea = catidea + 1
if testhmm1_6_3 == cat1hmm1_6_3:
    catidea = catidea + 1
if testhmm1_6_3 == cat2hmm1_6_3:
    catidea = catidea + 1
if testhmm1_6_3 == cat3hmm1_6_3:
    catidea = catidea + 1
if testhmm1_6_3 == cat4hmm1_6_3:
    catidea = catidea + 1
if testhmm1_6_3 == cat5hmm1_6_3:
    catidea = catidea + 1
if testhmm1_6_3 == cat6hmm1_6_3:
    catidea = catidea + 1
if testhmm1_6_3 == cat7hmm1_6_3:
    catidea = catidea + 1
if testhmm1_6_3 == cat8hmm1_6_3:
    catidea = catidea + 1
if testhmm1_6_3 == cat9hmm1_6_3:
    catidea = catidea + 1
if testhmm1_6_3 == cat10hmm1_6_3:
    catidea = catidea + 1
if testhmm1_7_1 == cat1hmm1_7_1:
    catidea = catidea + 1
if testhmm1_7_1 == cat2hmm1_7_1:
    catidea = catidea + 1
if testhmm1_7_1 == cat3hmm1_7_1:
    catidea = catidea + 1
if testhmm1_7_1 == cat4hmm1_7_1:
    catidea = catidea + 1
if testhmm1_7_1 == cat5hmm1_7_1:
    catidea = catidea + 1
if testhmm1_7_1 == cat6hmm1_7_1:
    catidea = catidea + 1
if testhmm1_7_1 == cat7hmm1_7_1:
    catidea = catidea + 1
if testhmm1_7_1 == cat8hmm1_7_1:
    catidea = catidea + 1
if testhmm1_7_1 == cat9hmm1_7_1:
    catidea = catidea + 1
if testhmm1_7_1 == cat10hmm1_7_1:
    catidea = catidea + 1
if testhmm1_7_2 == cat1hmm1_7_2:
    catidea = catidea + 1
if testhmm1_7_2 == cat2hmm1_7_2:
    catidea = catidea + 1
if testhmm1_7_2 == cat3hmm1_7_2:
    catidea = catidea + 1
if testhmm1_7_2 == cat4hmm1_7_2:
    catidea = catidea + 1
if testhmm1_7_2 == cat5hmm1_7_2:
    catidea = catidea + 1
if testhmm1_7_2 == cat6hmm1_7_2:
    catidea = catidea + 1
if testhmm1_7_2 == cat7hmm1_7_2:
    catidea = catidea + 1
if testhmm1_7_2 == cat8hmm1_7_2:
    catidea = catidea + 1
if testhmm1_7_2 == cat9hmm1_7_2:
    catidea = catidea + 1
if testhmm1_7_2 == cat10hmm1_7_2:
    catidea = catidea + 1
if testhmm1_7_3 == cat1hmm1_7_3:
    catidea = catidea + 1
if testhmm1_7_3 == cat2hmm1_7_3:
    catidea = catidea + 1
if testhmm1_7_3 == cat3hmm1_7_3:
    catidea = catidea + 1
if testhmm1_7_3 == cat4hmm1_7_3:
    catidea = catidea + 1
if testhmm1_7_3 == cat5hmm1_7_3:
    catidea = catidea + 1
if testhmm1_7_3 == cat6hmm1_7_3:
    catidea = catidea + 1
if testhmm1_7_3 == cat7hmm1_7_3:
    catidea = catidea + 1
if testhmm1_7_3 == cat8hmm1_7_3:
    catidea = catidea + 1
if testhmm1_7_3 == cat9hmm1_7_3:
    catidea = catidea + 1
if testhmm1_7_3 == cat10hmm1_7_3:
    catidea = catidea + 1
if testhmm1_8_1 == cat1hmm1_8_1:
    catidea = catidea + 1
if testhmm1_8_1 == cat2hmm1_8_1:
    catidea = catidea + 1
if testhmm1_8_1 == cat3hmm1_8_1:
    catidea = catidea + 1
if testhmm1_8_1 == cat4hmm1_8_1:
    catidea = catidea + 1
if testhmm1_8_1 == cat5hmm1_8_1:
    catidea = catidea + 1
if testhmm1_8_1 == cat6hmm1_8_1:
    catidea = catidea + 1
if testhmm1_8_1 == cat7hmm1_8_1:
    catidea = catidea + 1
if testhmm1_8_1 == cat8hmm1_8_1:
    catidea = catidea + 1
if testhmm1_8_1 == cat9hmm1_8_1:
    catidea = catidea + 1
if testhmm1_8_1 == cat10hmm1_8_1:
    catidea = catidea + 1
if testhmm1_8_2 == cat1hmm1_8_2:
    catidea = catidea + 1
if testhmm1_8_2 == cat2hmm1_8_2:
    catidea = catidea + 1
if testhmm1_8_2 == cat3hmm1_8_2:
    catidea = catidea + 1
if testhmm1_8_2 == cat4hmm1_8_2:
    catidea = catidea + 1
if testhmm1_8_2 == cat5hmm1_8_2:
    catidea = catidea + 1
if testhmm1_8_2 == cat6hmm1_8_2:
    catidea = catidea + 1
if testhmm1_8_2 == cat7hmm1_8_2:
    catidea = catidea + 1
if testhmm1_8_2 == cat8hmm1_8_2:
    catidea = catidea + 1
if testhmm1_8_2 == cat9hmm1_8_2:
    catidea = catidea + 1
if testhmm1_8_2 == cat10hmm1_8_2:
    catidea = catidea + 1
if testhmm1_8_3 == cat1hmm1_8_3:
    catidea = catidea + 1
if testhmm1_8_3 == cat2hmm1_8_3:
    catidea = catidea + 1
if testhmm1_8_3 == cat3hmm1_8_3:
    catidea = catidea + 1
if testhmm1_8_3 == cat4hmm1_8_3:
    catidea = catidea + 1
if testhmm1_8_3 == cat5hmm1_8_3:
    catidea = catidea + 1
if testhmm1_8_3 == cat6hmm1_8_3:
    catidea = catidea + 1
if testhmm1_8_3 == cat7hmm1_8_3:
    catidea = catidea + 1
if testhmm1_8_3 == cat8hmm1_8_3:
    catidea = catidea + 1
if testhmm1_8_3 == cat9hmm1_8_3:
    catidea = catidea + 1
if testhmm1_8_3 == cat10hmm1_8_3:
    catidea = catidea + 1
if testhmm1_9_1 == cat1hmm1_9_1:
    catidea = catidea + 1
if testhmm1_9_1 == cat2hmm1_9_1:
    catidea = catidea + 1
if testhmm1_9_1 == cat3hmm1_9_1:
    catidea = catidea + 1
if testhmm1_9_1 == cat4hmm1_9_1:
    catidea = catidea + 1
if testhmm1_9_1 == cat5hmm1_9_1:
    catidea = catidea + 1
if testhmm1_9_1 == cat6hmm1_9_1:
    catidea = catidea + 1
if testhmm1_9_1 == cat7hmm1_9_1:
    catidea = catidea + 1
if testhmm1_9_1 == cat8hmm1_9_1:
    catidea = catidea + 1
if testhmm1_9_1 == cat9hmm1_9_1:
    catidea = catidea + 1
if testhmm1_9_1 == cat10hmm1_9_1:
    catidea = catidea + 1
if testhmm1_9_2 == cat1hmm1_9_2:
    catidea = catidea + 1
if testhmm1_9_2 == cat2hmm1_9_2:
    catidea = catidea + 1
if testhmm1_9_2 == cat3hmm1_9_2:
    catidea = catidea + 1
if testhmm1_9_2 == cat4hmm1_9_2:
    catidea = catidea + 1
if testhmm1_9_2 == cat5hmm1_9_2:
    catidea = catidea + 1
if testhmm1_9_2 == cat6hmm1_9_2:
    catidea = catidea + 1
if testhmm1_9_2 == cat7hmm1_9_2:
    catidea = catidea + 1
if testhmm1_9_2 == cat8hmm1_9_2:
    catidea = catidea + 1
if testhmm1_9_2 == cat9hmm1_9_2:
    catidea = catidea + 1
if testhmm1_9_2 == cat10hmm1_9_2:
    catidea = catidea + 1
if testhmm1_9_3 == cat1hmm1_9_2:
    catidea = catidea + 1
if testhmm1_9_3 == cat2hmm1_9_2:
    catidea = catidea + 1
if testhmm1_9_3 == cat3hmm1_9_2:
    catidea = catidea + 1
if testhmm1_9_3 == cat4hmm1_9_2:
    catidea = catidea + 1
if testhmm1_9_3 == cat5hmm1_9_2:
    catidea = catidea + 1
if testhmm1_9_3 == cat6hmm1_9_2:
    catidea = catidea + 1
if testhmm1_9_3 == cat7hmm1_9_2:
    catidea = catidea + 1
if testhmm1_9_3 == cat8hmm1_9_2:
    catidea = catidea + 1
if testhmm1_9_3 == cat9hmm1_9_2:
    catidea = catidea + 1
if testhmm1_9_3 == cat10hmm1_9_2:
    catidea = catidea + 1
if testhmm1_10_1 == cat1hmm1_10_1:
    catidea = catidea + 1
if testhmm1_10_1 == cat2hmm1_10_1:
    catidea = catidea + 1
if testhmm1_10_1 == cat3hmm1_10_1:
    catidea = catidea + 1
if testhmm1_10_1 == cat4hmm1_10_1:
    catidea = catidea + 1
if testhmm1_10_1 == cat5hmm1_10_1:
    catidea = catidea + 1
if testhmm1_10_1 == cat6hmm1_10_1:
    catidea = catidea + 1
if testhmm1_10_1 == cat7hmm1_10_1:
    catidea = catidea + 1
if testhmm1_10_1 == cat8hmm1_10_1:
    catidea = catidea + 1
if testhmm1_10_1 == cat9hmm1_10_1:
    catidea = catidea + 1
if testhmm1_10_1 == cat10hmm1_10_1:
    catidea = catidea + 1
if testhmm1_10_2 == cat1hmm1_10_2:
    catidea = catidea + 1
if testhmm1_10_2 == cat2hmm1_10_2:
    catidea = catidea + 1
if testhmm1_10_2 == cat3hmm1_10_2:
    catidea = catidea + 1
if testhmm1_10_2 == cat4hmm1_10_2:
    catidea = catidea + 1
if testhmm1_10_2 == cat5hmm1_10_2:
    catidea = catidea + 1
if testhmm1_10_2 == cat6hmm1_10_2:
    catidea = catidea + 1
if testhmm1_10_2 == cat7hmm1_10_2:
    catidea = catidea + 1
if testhmm1_10_2 == cat8hmm1_10_2:
    catidea = catidea + 1
if testhmm1_10_2 == cat9hmm1_10_2:
    catidea = catidea + 1
if testhmm1_10_2 == cat10hmm1_10_2:
    catidea = catidea + 1
if testhmm1_10_3 == cat1hmm1_10_3:
    catidea = catidea + 1
if testhmm1_10_3 == cat2hmm1_10_3:
    catidea = catidea + 1
if testhmm1_10_3 == cat3hmm1_10_3:
    catidea = catidea + 1
if testhmm1_10_3 == cat4hmm1_10_3:
    catidea = catidea + 1
if testhmm1_10_3 == cat5hmm1_10_3:
    catidea = catidea + 1
if testhmm1_10_3 == cat6hmm1_10_3:
    catidea = catidea + 1
if testhmm1_10_3 == cat7hmm1_10_3:
    catidea = catidea + 1
if testhmm1_10_3 == cat8hmm1_10_3:
    catidea = catidea + 1
if testhmm1_10_3 == cat9hmm1_10_3:
    catidea = catidea + 1
if testhmm1_10_3 == cat10hmm1_10_3:
    catidea = catidea + 1
if testhmm1_11_1 == cat1hmm1_11_2:
    catidea = catidea + 1
if testhmm1_11_1 == cat2hmm1_11_2:
    catidea = catidea + 1
if testhmm1_11_1 == cat3hmm1_11_2:
    catidea = catidea + 1
if testhmm1_11_1 == cat4hmm1_11_2:
    catidea = catidea + 1
if testhmm1_11_1 == cat5hmm1_11_2:
    catidea = catidea + 1
if testhmm1_11_1 == cat6hmm1_11_2:
    catidea = catidea + 1
if testhmm1_11_1 == cat7hmm1_11_2:
    catidea = catidea + 1
if testhmm1_11_1 == cat8hmm1_11_2:
    catidea = catidea + 1
if testhmm1_11_1 == cat9hmm1_11_2:
    catidea = catidea + 1
if testhmm1_11_1 == cat10hmm1_11_2:
    catidea = catidea + 1
if testhmm1_11_2 == cat1hmm1_11_3:
    catidea = catidea + 1
if testhmm1_11_2 == cat2hmm1_11_3:
    catidea = catidea + 1
if testhmm1_11_2 == cat3hmm1_11_3:
    catidea = catidea + 1
if testhmm1_11_2 == cat4hmm1_11_3:
    catidea = catidea + 1
if testhmm1_11_2 == cat5hmm1_11_3:
    catidea = catidea + 1
if testhmm1_11_2 == cat6hmm1_11_3:
    catidea = catidea + 1
if testhmm1_11_2 == cat7hmm1_11_3:
    catidea = catidea + 1
if testhmm1_11_2 == cat8hmm1_11_3:
    catidea = catidea + 1
if testhmm1_11_2 == cat9hmm1_11_3:
    catidea = catidea + 1
if testhmm1_11_2 == cat10hmm1_11_3:
    catidea = catidea + 1
if testhmm1_11_3 == cat1hmm1_11_3:
    catidea = catidea + 1
if testhmm1_11_3 == cat2hmm1_11_3:
    catidea = catidea + 1
if testhmm1_11_3 == cat3hmm1_11_3:
    catidea = catidea + 1
if testhmm1_11_3 == cat4hmm1_11_3:
    catidea = catidea + 1
if testhmm1_11_3 == cat5hmm1_11_3:
    catidea = catidea + 1
if testhmm1_11_3 == cat6hmm1_11_3:
    catidea = catidea + 1
if testhmm1_11_3 == cat7hmm1_11_3:
    catidea = catidea + 1
if testhmm1_11_3 == cat8hmm1_11_3:
    catidea = catidea + 1
if testhmm1_11_3 == cat9hmm1_11_3:
    catidea = catidea + 1
if testhmm1_11_3 == cat10hmm1_11_3:
    catidea = catidea + 1
dogidea = 0
if testhmm1_1_1 == dog1hmm1_1_1:
    dogidea = dogidea + 1
if testhmm1_1_1 == dog2hmm1_1_1:
    dogidea = dogidea + 1
if testhmm1_1_1 == dog3hmm1_1_1:
    dogidea = dogidea + 1
if testhmm1_1_1 == dog4hmm1_1_1:
    dogidea = dogidea + 1
if testhmm1_1_1 == dog5hmm1_1_1:
    dogidea = dogidea + 1
if testhmm1_1_1 == dog6hmm1_1_1:
    dogidea = dogidea + 1
if testhmm1_1_1 == dog7hmm1_1_1:
    dogidea = dogidea + 1
if testhmm1_1_1 == dog8hmm1_1_1:
    dogidea = dogidea + 1
if testhmm1_1_1 == dog9hmm1_1_1:
    dogidea = dogidea + 1
if testhmm1_1_1 == dog10hmm1_1_1:
    dogidea = dogidea + 1
if testhmm1_1_2 == dog1hmm1_1_2:
    dogidea = dogidea + 1
if testhmm1_1_2 == dog2hmm1_1_2:
    dogidea = dogidea + 1
if testhmm1_1_2 == dog3hmm1_1_2:
    dogidea = dogidea + 1
if testhmm1_1_2 == dog4hmm1_1_2:
    dogidea = dogidea + 1
if testhmm1_1_2 == dog5hmm1_1_2:
    dogidea = dogidea + 1
if testhmm1_1_2 == dog6hmm1_1_2:
    dogidea = dogidea + 1
if testhmm1_1_2 == dog7hmm1_1_2:
    dogidea = dogidea + 1
if testhmm1_1_2 == dog8hmm1_1_2:
    dogidea = dogidea + 1
if testhmm1_1_2 == dog9hmm1_1_2:
    dogidea = dogidea + 1
if testhmm1_1_2 == dog10hmm1_1_2:
    dogidea = dogidea + 1
if testhmm1_1_3 == dog1hmm1_1_3:
    dogidea = dogidea + 1
if testhmm1_1_3 == dog2hmm1_1_3:
    dogidea = dogidea + 1
if testhmm1_1_3 == dog3hmm1_1_3:
    dogidea = dogidea + 1
if testhmm1_1_3 == dog4hmm1_1_3:
    dogidea = dogidea + 1
if testhmm1_1_3 == dog5hmm1_1_3:
    dogidea = dogidea + 1
if testhmm1_1_3 == dog6hmm1_1_3:
    dogidea = dogidea + 1
if testhmm1_1_3 == dog7hmm1_1_3:
    dogidea = dogidea + 1
if testhmm1_1_3 == dog8hmm1_1_3:
    dogidea = dogidea + 1
if testhmm1_1_3 == dog9hmm1_1_3:
    dogidea = dogidea + 1
if testhmm1_1_3 == dog10hmm1_1_3:
    dogidea = dogidea + 1
if testhmm1_2_1 == dog1hmm1_2_1:
    dogidea = dogidea + 1
if testhmm1_2_1 == dog2hmm1_2_1:
    dogidea = dogidea + 1
if testhmm1_2_1 == dog3hmm1_2_1:
    dogidea = dogidea + 1
if testhmm1_2_1 == dog4hmm1_2_1:
    dogidea = dogidea + 1
if testhmm1_2_1 == dog5hmm1_2_1:
    dogidea = dogidea + 1
if testhmm1_2_1 == dog6hmm1_2_1:
    dogidea = dogidea + 1
if testhmm1_2_1 == dog7hmm1_2_1:
    dogidea = dogidea + 1
if testhmm1_2_1 == dog8hmm1_2_1:
    dogidea = dogidea + 1
if testhmm1_2_1 == dog9hmm1_2_1:
    dogidea = dogidea + 1
if testhmm1_2_1 == dog10hmm1_2_1:
    dogidea = dogidea + 1
if testhmm1_2_2 == dog1hmm1_2_2:
    dogidea = dogidea + 1
if testhmm1_2_2 == dog2hmm1_2_2:
    dogidea = dogidea + 1
if testhmm1_2_2 == dog3hmm1_2_2:
    dogidea = dogidea + 1
if testhmm1_2_2 == dog4hmm1_2_2:
    dogidea = dogidea + 1
if testhmm1_2_2 == dog5hmm1_2_2:
    dogidea = dogidea + 1
if testhmm1_2_2 == dog6hmm1_2_2:
    dogidea = dogidea + 1
if testhmm1_2_2 == dog7hmm1_2_2:
    dogidea = dogidea + 1
if testhmm1_2_2 == dog8hmm1_2_2:
    dogidea = dogidea + 1
if testhmm1_2_2 == dog9hmm1_2_2:
    dogidea = dogidea + 1
if testhmm1_2_2 == dog10hmm1_2_2:
    dogidea = dogidea + 1
if testhmm1_2_3 == dog1hmm1_2_3:
    dogidea = dogidea + 1
if testhmm1_2_3 == dog2hmm1_2_3:
    dogidea = dogidea + 1
if testhmm1_2_3 == dog3hmm1_2_3:
    dogidea = dogidea + 1
if testhmm1_2_3 == dog4hmm1_2_3:
    dogidea = dogidea + 1
if testhmm1_2_3 == dog5hmm1_2_3:
    dogidea = dogidea + 1
if testhmm1_2_3 == dog6hmm1_2_3:
    dogidea = dogidea + 1
if testhmm1_2_3 == dog7hmm1_2_3:
    dogidea = dogidea + 1
if testhmm1_2_3 == dog8hmm1_2_3:
    dogidea = dogidea + 1
if testhmm1_2_3 == dog9hmm1_2_3:
    dogidea = dogidea + 1
if testhmm1_2_3 == dog10hmm1_2_3:
    dogidea = dogidea + 1
if testhmm1_3_1 == dog1hmm1_3_1:
    dogidea = dogidea + 1
if testhmm1_3_1 == dog2hmm1_3_1:
    dogidea = dogidea + 1
if testhmm1_3_1 == dog3hmm1_3_1:
    dogidea = dogidea + 1
if testhmm1_3_1 == dog4hmm1_3_1:
    dogidea = dogidea + 1
if testhmm1_3_1 == dog5hmm1_3_1:
    dogidea = dogidea + 1
if testhmm1_3_1 == dog6hmm1_3_1:
    dogidea = dogidea + 1
if testhmm1_3_1 == dog7hmm1_3_1:
    dogidea = dogidea + 1
if testhmm1_3_1 == dog8hmm1_3_1:
    dogidea = dogidea + 1
if testhmm1_3_1 == dog9hmm1_3_1:
    dogidea = dogidea + 1
if testhmm1_3_1 == dog10hmm1_3_1:
    dogidea = dogidea + 1
if testhmm1_3_2 == dog1hmm1_3_2:
    dogidea = dogidea + 1
if testhmm1_3_2 == dog2hmm1_3_2:
    dogidea = dogidea + 1
if testhmm1_3_2 == dog3hmm1_3_2:
    dogidea = dogidea + 1
if testhmm1_3_2 == dog4hmm1_3_2:
    dogidea = dogidea + 1
if testhmm1_3_2 == dog5hmm1_3_2:
    dogidea = dogidea + 1
if testhmm1_3_2 == dog6hmm1_3_2:
    dogidea = dogidea + 1
if testhmm1_3_2 == dog7hmm1_3_2:
    dogidea = dogidea + 1
if testhmm1_3_2 == dog8hmm1_3_2:
    dogidea = dogidea + 1
if testhmm1_3_2 == dog9hmm1_3_2:
    dogidea = dogidea + 1
if testhmm1_3_2 == dog10hmm1_3_2:
    dogidea = dogidea + 1
if testhmm1_3_3 == dog1hmm1_3_3:
    dogidea = dogidea + 1
if testhmm1_3_3 == dog2hmm1_3_3:
    dogidea = dogidea + 1
if testhmm1_3_3 == dog3hmm1_3_3:
    dogidea = dogidea + 1
if testhmm1_3_3 == dog4hmm1_3_3:
    dogidea = dogidea + 1
if testhmm1_3_3 == dog5hmm1_3_3:
    dogidea = dogidea + 1
if testhmm1_3_3 == dog6hmm1_3_3:
    dogidea = dogidea + 1
if testhmm1_3_3 == dog7hmm1_3_3:
    dogidea = dogidea + 1
if testhmm1_3_3 == dog8hmm1_3_3:
    dogidea = dogidea + 1
if testhmm1_3_3 == dog9hmm1_3_3:
    dogidea = dogidea + 1
if testhmm1_3_3 == dog10hmm1_3_3:
    dogidea = dogidea + 1
if testhmm1_4_1 == dog1hmm1_4_1:
    dogidea = dogidea + 1
if testhmm1_4_1 == dog2hmm1_4_1:
    dogidea = dogidea + 1
if testhmm1_4_1 == dog3hmm1_4_1:
    dogidea = dogidea + 1
if testhmm1_4_1 == dog4hmm1_4_1:
    dogidea = dogidea + 1
if testhmm1_4_1 == dog5hmm1_4_1:
    dogidea = dogidea + 1
if testhmm1_4_1 == dog6hmm1_4_1:
    dogidea = dogidea + 1
if testhmm1_4_1 == dog7hmm1_4_1:
    dogidea = dogidea + 1
if testhmm1_4_1 == dog8hmm1_4_1:
    dogidea = dogidea + 1
if testhmm1_4_1 == dog9hmm1_4_1:
    dogidea = dogidea + 1
if testhmm1_4_1 == dog10hmm1_4_1:
    dogidea = dogidea + 1
if testhmm1_4_2 == dog1hmm1_4_2:
    dogidea = dogidea + 1
if testhmm1_4_2 == dog2hmm1_4_2:
    dogidea = dogidea + 1
if testhmm1_4_2 == dog3hmm1_4_2:
    dogidea = dogidea + 1
if testhmm1_4_2 == dog4hmm1_4_2:
    dogidea = dogidea + 1
if testhmm1_4_2 == dog5hmm1_4_2:
    dogidea = dogidea + 1
if testhmm1_4_2 == dog6hmm1_4_2:
    dogidea = dogidea + 1
if testhmm1_4_2 == dog7hmm1_4_2:
    dogidea = dogidea + 1
if testhmm1_4_2 == dog8hmm1_4_2:
    dogidea = dogidea + 1
if testhmm1_4_2 == dog9hmm1_4_2:
    dogidea = dogidea + 1
if testhmm1_4_2 == dog10hmm1_4_2:
    dogidea = dogidea + 1
if testhmm1_4_3 == dog1hmm1_4_3:
    dogidea = dogidea + 1
if testhmm1_4_3 == dog2hmm1_4_3:
    dogidea = dogidea + 1
if testhmm1_4_3 == dog3hmm1_4_3:
    dogidea = dogidea + 1
if testhmm1_4_3 == dog4hmm1_4_3:
    dogidea = dogidea + 1
if testhmm1_4_3 == dog5hmm1_4_3:
    dogidea = dogidea + 1
if testhmm1_4_3 == dog6hmm1_4_3:
    dogidea = dogidea + 1
if testhmm1_4_3 == dog7hmm1_4_3:
    dogidea = dogidea + 1
if testhmm1_4_3 == dog8hmm1_4_3:
    dogidea = dogidea + 1
if testhmm1_4_3 == dog9hmm1_4_3:
    dogidea = dogidea + 1
if testhmm1_4_3 == dog10hmm1_4_3:
    dogidea = dogidea + 1
if testhmm1_5_1 == dog1hmm1_5_1:
    dogidea = dogidea + 1
if testhmm1_5_1 == dog2hmm1_5_1:
    dogidea = dogidea + 1
if testhmm1_5_1 == dog3hmm1_5_1:
    dogidea = dogidea + 1
if testhmm1_5_1 == dog4hmm1_5_1:
    dogidea = dogidea + 1
if testhmm1_5_1 == dog5hmm1_5_1:
    dogidea = dogidea + 1
if testhmm1_5_1 == dog6hmm1_5_1:
    dogidea = dogidea + 1
if testhmm1_5_1 == dog7hmm1_5_1:
    dogidea = dogidea + 1
if testhmm1_5_1 == dog8hmm1_5_1:
    dogidea = dogidea + 1
if testhmm1_5_1 == dog9hmm1_5_1:
    dogidea = dogidea + 1
if testhmm1_5_1 == dog10hmm1_5_1:
    dogidea = dogidea + 1
if testhmm1_5_2 == dog1hmm1_5_2:
    dogidea = dogidea + 1
if testhmm1_5_2 == dog2hmm1_5_2:
    dogidea = dogidea + 1
if testhmm1_5_2 == dog3hmm1_5_2:
    dogidea = dogidea + 1
if testhmm1_5_2 == dog4hmm1_5_2:
    dogidea = dogidea + 1
if testhmm1_5_2 == dog5hmm1_5_2:
    dogidea = dogidea + 1
if testhmm1_5_2 == dog6hmm1_5_2:
    dogidea = dogidea + 1
if testhmm1_5_2 == dog7hmm1_5_2:
    dogidea = dogidea + 1
if testhmm1_5_2 == dog8hmm1_5_2:
    dogidea = dogidea + 1
if testhmm1_5_2 == dog9hmm1_5_2:
    dogidea = dogidea + 1
if testhmm1_5_2 == dog10hmm1_5_2:
    dogidea = dogidea + 1
if testhmm1_5_3 == dog1hmm1_5_3:
    dogidea = dogidea + 1
if testhmm1_5_3 == dog1hmm1_5_3:
    dogidea = dogidea + 1
if testhmm1_5_3 == dog2hmm1_5_3:
    dogidea = dogidea + 1
if testhmm1_5_3 == dog3hmm1_5_3:
    dogidea = dogidea + 1
if testhmm1_5_3 == dog4hmm1_5_3:
    dogidea = dogidea + 1
if testhmm1_5_3 == dog5hmm1_5_3:
    dogidea = dogidea + 1
if testhmm1_5_3 == dog6hmm1_5_3:
    dogidea = dogidea + 1
if testhmm1_5_3 == dog7hmm1_5_3:
    dogidea = dogidea + 1
if testhmm1_5_3 == dog8hmm1_5_3:
    dogidea = dogidea + 1
if testhmm1_5_3 == dog9hmm1_5_3:
    dogidea = dogidea + 1
if testhmm1_5_3 == dog10hmm1_5_3:
    dogidea = dogidea + 1
if testhmm1_6_1 == dog1hmm1_6_1:
    dogidea = dogidea + 1
if testhmm1_6_1 == dog2hmm1_6_1:
    dogidea = dogidea + 1
if testhmm1_6_1 == dog3hmm1_6_1:
    dogidea = dogidea + 1
if testhmm1_6_1 == dog4hmm1_6_1:
    dogidea = dogidea + 1
if testhmm1_6_1 == dog5hmm1_6_1:
    dogidea = dogidea + 1
if testhmm1_6_1 == dog6hmm1_6_1:
    dogidea = dogidea + 1
if testhmm1_6_1 == dog7hmm1_6_1:
    dogidea = dogidea + 1
if testhmm1_6_1 == dog8hmm1_6_1:
    dogidea = dogidea + 1
if testhmm1_6_1 == dog9hmm1_6_1:
    dogidea = dogidea + 1
if testhmm1_6_1 == dog10hmm1_6_1:
    dogidea = dogidea + 1
if testhmm1_6_2 == dog1hmm1_6_2:
    dogidea = dogidea + 1
if testhmm1_6_2 == dog2hmm1_6_2:
    dogidea = dogidea + 1
if testhmm1_6_2 == dog3hmm1_6_2:
    dogidea = dogidea + 1
if testhmm1_6_2 == dog4hmm1_6_2:
    dogidea = dogidea + 1
if testhmm1_6_2 == dog5hmm1_6_2:
    dogidea = dogidea + 1
if testhmm1_6_2 == dog6hmm1_6_2:
    dogidea = dogidea + 1
if testhmm1_6_2 == dog7hmm1_6_2:
    dogidea = dogidea + 1
if testhmm1_6_2 == dog8hmm1_6_2:
    dogidea = dogidea + 1
if testhmm1_6_2 == dog9hmm1_6_2:
    dogidea = dogidea + 1
if testhmm1_6_2 == dog10hmm1_6_2:
    dogidea = dogidea + 1
if testhmm1_6_3 == dog1hmm1_6_3:
    dogidea = dogidea + 1
if testhmm1_6_3 == dog2hmm1_6_3:
    dogidea = dogidea + 1
if testhmm1_6_3 == dog3hmm1_6_3:
    dogidea = dogidea + 1
if testhmm1_6_3 == dog4hmm1_6_3:
    dogidea = dogidea + 1
if testhmm1_6_3 == dog5hmm1_6_3:
    dogidea = dogidea + 1
if testhmm1_6_3 == dog6hmm1_6_3:
    dogidea = dogidea + 1
if testhmm1_6_3 == dog7hmm1_6_3:
    dogidea = dogidea + 1
if testhmm1_6_3 == dog8hmm1_6_3:
    dogidea = dogidea + 1
if testhmm1_6_3 == dog9hmm1_6_3:
    dogidea = dogidea + 1
if testhmm1_6_3 == dog10hmm1_6_3:
    dogidea = dogidea + 1
if testhmm1_7_1 == dog1hmm1_7_1:
    dogidea = dogidea + 1
if testhmm1_7_1 == dog2hmm1_7_1:
    dogidea = dogidea + 1
if testhmm1_7_1 == dog3hmm1_7_1:
    dogidea = dogidea + 1
if testhmm1_7_1 == dog4hmm1_7_1:
    dogidea = dogidea + 1
if testhmm1_7_1 == dog5hmm1_7_1:
    dogidea = dogidea + 1
if testhmm1_7_1 == dog6hmm1_7_1:
    dogidea = dogidea + 1
if testhmm1_7_1 == dog7hmm1_7_1:
    dogidea = dogidea + 1
if testhmm1_7_1 == dog8hmm1_7_1:
    dogidea = dogidea + 1
if testhmm1_7_1 == dog9hmm1_7_1:
    dogidea = dogidea + 1
if testhmm1_7_1 == dog10hmm1_7_1:
    dogidea = dogidea + 1
if testhmm1_7_2 == dog1hmm1_7_2:
    dogidea = dogidea + 1
if testhmm1_7_2 == dog2hmm1_7_2:
    dogidea = dogidea + 1
if testhmm1_7_2 == dog3hmm1_7_2:
    dogidea = dogidea + 1
if testhmm1_7_2 == dog4hmm1_7_2:
    dogidea = dogidea + 1
if testhmm1_7_2 == dog5hmm1_7_2:
    dogidea = dogidea + 1
if testhmm1_7_2 == dog6hmm1_7_2:
    dogidea = dogidea + 1
if testhmm1_7_2 == dog7hmm1_7_2:
    dogidea = dogidea + 1
if testhmm1_7_2 == dog8hmm1_7_2:
    dogidea = dogidea + 1
if testhmm1_7_2 == dog9hmm1_7_2:
    dogidea = dogidea + 1
if testhmm1_7_2 == dog10hmm1_7_2:
    dogidea = dogidea + 1
if testhmm1_7_3 == dog1hmm1_7_3:
    dogidea = dogidea + 1
if testhmm1_7_3 == dog2hmm1_7_3:
    dogidea = dogidea + 1
if testhmm1_7_3 == dog3hmm1_7_3:
    dogidea = dogidea + 1
if testhmm1_7_3 == dog4hmm1_7_3:
    dogidea = dogidea + 1
if testhmm1_7_3 == dog5hmm1_7_3:
    dogidea = dogidea + 1
if testhmm1_7_3 == dog6hmm1_7_3:
    dogidea = dogidea + 1
if testhmm1_7_3 == dog7hmm1_7_3:
    dogidea = dogidea + 1
if testhmm1_7_3 == dog8hmm1_7_3:
    dogidea = dogidea + 1
if testhmm1_7_3 == dog9hmm1_7_3:
    dogidea = dogidea + 1
if testhmm1_7_3 == dog10hmm1_7_3:
    dogidea = dogidea + 1
if testhmm1_8_1 == dog1hmm1_8_1:
    dogidea = dogidea + 1
if testhmm1_8_1 == dog2hmm1_8_1:
    dogidea = dogidea + 1
if testhmm1_8_1 == dog3hmm1_8_1:
    dogidea = dogidea + 1
if testhmm1_8_1 == dog4hmm1_8_1:
    dogidea = dogidea + 1
if testhmm1_8_1 == dog5hmm1_8_1:
    dogidea = dogidea + 1
if testhmm1_8_1 == dog6hmm1_8_1:
    dogidea = dogidea + 1
if testhmm1_8_1 == dog7hmm1_8_1:
    dogidea = dogidea + 1
if testhmm1_8_1 == dog8hmm1_8_1:
    dogidea = dogidea + 1
if testhmm1_8_1 == dog9hmm1_8_1:
    dogidea = dogidea + 1
if testhmm1_8_1 == dog10hmm1_8_1:
    dogidea = dogidea + 1
if testhmm1_8_2 == dog1hmm1_8_2:
    dogidea = dogidea + 1
if testhmm1_8_2 == dog2hmm1_8_2:
    dogidea = dogidea + 1
if testhmm1_8_2 == dog3hmm1_8_2:
    dogidea = dogidea + 1
if testhmm1_8_2 == dog4hmm1_8_2:
    dogidea = dogidea + 1
if testhmm1_8_2 == dog5hmm1_8_2:
    dogidea = dogidea + 1
if testhmm1_8_2 == dog6hmm1_8_2:
    dogidea = dogidea + 1
if testhmm1_8_2 == dog7hmm1_8_2:
    dogidea = dogidea + 1
if testhmm1_8_2 == dog8hmm1_8_2:
    dogidea = dogidea + 1
if testhmm1_8_2 == dog9hmm1_8_2:
    dogidea = dogidea + 1
if testhmm1_8_2 == dog10hmm1_8_2:
    dogidea = dogidea + 1
if testhmm1_8_3 == dog1hmm1_8_3:
    dogidea = dogidea + 1
if testhmm1_8_3 == dog2hmm1_8_3:
    dogidea = dogidea + 1
if testhmm1_8_3 == dog3hmm1_8_3:
    dogidea = dogidea + 1
if testhmm1_8_3 == dog4hmm1_8_3:
    dogidea = dogidea + 1
if testhmm1_8_3 == dog5hmm1_8_3:
    dogidea = dogidea + 1
if testhmm1_8_3 == dog6hmm1_8_3:
    dogidea = dogidea + 1
if testhmm1_8_3 == dog7hmm1_8_3:
    dogidea = dogidea + 1
if testhmm1_8_3 == dog8hmm1_8_3:
    dogidea = dogidea + 1
if testhmm1_8_3 == dog9hmm1_8_3:
    dogidea = dogidea + 1
if testhmm1_8_3 == dog10hmm1_8_3:
    dogidea = dogidea + 1
if testhmm1_9_1 == dog1hmm1_9_2:
    dogidea = dogidea + 1
if testhmm1_9_1 == dog2hmm1_9_2:
    dogidea = dogidea + 1
if testhmm1_9_1 == dog3hmm1_9_2:
    dogidea = dogidea + 1
if testhmm1_9_1 == dog4hmm1_9_2:
    dogidea = dogidea + 1
if testhmm1_9_1 == dog5hmm1_9_2:
    dogidea = dogidea + 1
if testhmm1_9_1 == dog6hmm1_9_2:
    dogidea = dogidea + 1
if testhmm1_9_1 == dog7hmm1_9_2:
    dogidea = dogidea + 1
if testhmm1_9_1 == dog8hmm1_9_2:
    dogidea = dogidea + 1
if testhmm1_9_1 == dog9hmm1_9_2:
    dogidea = dogidea + 1
if testhmm1_9_1 == dog10hmm1_9_2:
    dogidea = dogidea + 1
if testhmm1_9_2 == dog1hmm1_9_3:
    dogidea = dogidea + 1
if testhmm1_9_2 == dog2hmm1_9_3:
    dogidea = dogidea + 1
if testhmm1_9_2 == dog3hmm1_9_3:
    dogidea = dogidea + 1
if testhmm1_9_2 == dog4hmm1_9_3:
    dogidea = dogidea + 1
if testhmm1_9_2 == dog5hmm1_9_3:
    dogidea = dogidea + 1
if testhmm1_9_2 == dog6hmm1_9_3:
    dogidea = dogidea + 1
if testhmm1_9_2 == dog7hmm1_9_3:
    dogidea = dogidea + 1
if testhmm1_9_2 == dog8hmm1_9_3:
    dogidea = dogidea + 1
if testhmm1_9_2 == dog9hmm1_9_3:
    dogidea = dogidea + 1
if testhmm1_9_2 == dog10hmm1_9_3:
    dogidea = dogidea + 1
if testhmm1_9_3 == dog1hmm1_9_2:
    dogidea = dogidea + 1
if testhmm1_9_3 == dog2hmm1_9_2:
    dogidea = dogidea + 1
if testhmm1_9_3 == dog3hmm1_9_2:
    dogidea = dogidea + 1
if testhmm1_9_3 == dog4hmm1_9_2:
    dogidea = dogidea + 1
if testhmm1_9_3 == dog5hmm1_9_2:
    dogidea = dogidea + 1
if testhmm1_9_3 == dog6hmm1_9_2:
    dogidea = dogidea + 1
if testhmm1_9_3 == dog7hmm1_9_2:
    dogidea = dogidea + 1
if testhmm1_9_3 == dog8hmm1_9_2:
    dogidea = dogidea + 1
if testhmm1_9_3 == dog9hmm1_9_2:
    dogidea = dogidea + 1
if testhmm1_9_3 == dog10hmm1_9_2:
    dogidea = dogidea + 1
if testhmm1_10_1 == dog1hmm1_10_1:
    dogidea = dogidea + 1
if testhmm1_10_1 == dog2hmm1_10_1:
    dogidea = dogidea + 1
if testhmm1_10_1 == dog3hmm1_10_1:
    dogidea = dogidea + 1
if testhmm1_10_1 == dog4hmm1_10_1:
    dogidea = dogidea + 1
if testhmm1_10_1 == dog5hmm1_10_1:
    dogidea = dogidea + 1
if testhmm1_10_1 == dog6hmm1_10_1:
    dogidea = dogidea + 1
if testhmm1_10_1 == dog7hmm1_10_1:
    dogidea = dogidea + 1
if testhmm1_10_1 == dog8hmm1_10_1:
    dogidea = dogidea + 1
if testhmm1_10_1 == dog9hmm1_10_1:
    dogidea = dogidea + 1
if testhmm1_10_1 == dog10hmm1_10_1:
    dogidea = dogidea + 1
if testhmm1_10_2 == dog1hmm1_10_2:
    dogidea = dogidea + 1
if testhmm1_10_2 == dog2hmm1_10_2:
    dogidea = dogidea + 1
if testhmm1_10_2 == dog3hmm1_10_2:
    dogidea = dogidea + 1
if testhmm1_10_2 == dog4hmm1_10_2:
    dogidea = dogidea + 1
if testhmm1_10_2 == dog5hmm1_10_2:
    dogidea = dogidea + 1
if testhmm1_10_2 == dog6hmm1_10_2:
    dogidea = dogidea + 1
if testhmm1_10_2 == dog7hmm1_10_2:
    dogidea = dogidea + 1
if testhmm1_10_2 == dog8hmm1_10_2:
    dogidea = dogidea + 1
if testhmm1_10_2 == dog9hmm1_10_2:
    dogidea = dogidea + 1
if testhmm1_10_2 == dog10hmm1_10_2:
    dogidea = dogidea + 1
if catidea >= dogidea:
    time.sleep(1)
    print('cat')
if dogidea >= catidea:
    time.sleep(1)
    print('dog')
if catidea == dogidea:
    time.sleep(1)
    print('�sҔ~���\x1a�\x1f�����>\x10\x1e\x19�\x1f�ǒ�ۢd�\x0e{���\x1b�������\x10���ӻ͵���\x1c\x08�\x01 �\x7f\x05\x7f\x0e\x03\x15���1̚�����\x11')
print(str(catidea) + ' ' + str(dogidea))
