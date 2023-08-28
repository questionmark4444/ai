#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Function to merge RGB values
float rgb_processor(unsigned char *row) {
    return (row[0]+row[1]+row[2])*0.33333333333;
}

// Function to check the similarity of RGB values
float rgb_checker(unsigned char *pixel, unsigned char *testpixel) {
    int add_score = 0;
    for (int x = 0; x < 101; ++x) {
        add_score += ((int)(roundf(pixel[x]*0.0196078431) == roundf(testpixel[x]*0.0196078431)));
    }
    return add_score;
}
