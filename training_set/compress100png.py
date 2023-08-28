#compress images and resize to 100 by 100

from PIL import Image
import time

x = 1
while (x < 5000) :
        im1 = Image.open(f'cats/{x}.png')
        im2 = Image.open(f'dogs/{x}.png')
        im3 = im1.resize((100, 100))
        im4 = im2.resize((100, 100))
        try:
                im3.save(f'cats/{x}.png', format="PNG", optimize = True, quality=99)
                im4.save(f'dogs/{x}.png', format="PNG", optimize = True, quality=99)
        except:
                im1.save(f'cats/{x}.png')
                im2.save(f'dogs/{x}.png')
                print(x)
        time.sleep(0.1)
        x += 1
