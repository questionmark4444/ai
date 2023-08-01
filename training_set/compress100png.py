#compress images and resize to 100 by 100

from PIL import Image
import time

x = 1
while (x < 501) :
        #im1 = Image.open(f'dog.{x}.jpg')
        im1 = Image.open(f'dogs/{x}.png')
        im2 = im1.resize((100, 100))
        try:
                im2.save(f'dogs/{x}.png', optimize = True, quality=99)
        except:
                im2.save(f'dogs/{x}.png')
                print(x)
        time.sleep(0.1)
        x += 1
