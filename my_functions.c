#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Function to check the similarity of RGB values
float rgb_checker(unsigned char *pixel, unsigned char *testpixel) {
    int add_score = 0;
    for (int x = 0; x < 101; x++) {
        add_score += ((int)(roundf((pixel[x])*0.2) == roundf((testpixel[x])*0.2)));
    }
    return add_score;
}
