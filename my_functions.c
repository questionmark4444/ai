#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Function to check the similarity of RGB values
float rgb_checker(unsigned char *pixel, unsigned char *testpixel) {
    int x;
    int score_add = 0;
    score_add += (roundf(pixel[0]/5) == roundf(testpixel[0]/5));
    score_add += (roundf(pixel[1]/5) == roundf(testpixel[1]/5));
    score_add += (roundf(pixel[2]/5) == roundf(testpixel[2]/5));
    return score_add;
}
