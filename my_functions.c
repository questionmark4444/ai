#define STB_IMAGE_IMPLEMENTATION
#include "stb_image.h"

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

// Function to check the similarity of RGB values
float rgb_checker(unsigned char *pixel, unsigned char *testpixel) {
    int x;
    float score_add = 0;
    for (x = 0; x < 3; x++) {
        if (pixel[x] == testpixel[x]) {
            score_add += 1.0 / 3.0;
        }
    }
    return roundf(score_add);
}
