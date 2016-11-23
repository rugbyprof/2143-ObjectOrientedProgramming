from PIL import Image
import urllib, cStringIO
import random

def random_color():
    return (random.randint(255),random.randint(255),random.randint(255))

def blur(img,blur_power=3):
    width = img.size[0]
    height = img.size[1]

    r = 0
    g = 0
    b = 0
    d = 2*blur_power * 2*blur_power
    for x in range(blur_power,width-blur_power):
        for y in range(blur_power,height-blur_power):
            for i in range(-blur_power,blur_power):
                for j in range(-blur_power,blur_power):
                    pix = img.getpixel((x+i,y+j))
                    r += pix[0]
                    g += pix[1]
                    b += pix[2]
            img.putpixel((x,y),(int(r/d),int(g/d),int(b/d)))
            r = 0
            g = 0
            b = 0

url = 'https://s-media-cache-ak0.pinimg.com/564x/b1/64/2a/b1642af1ba8b662e19e6d7a701a2522f.jpg'
file = cStringIO.StringIO(urllib.urlopen(url).read())
img = Image.open(file)
img = img.convert("L")
width = img.size[0]
height = img.size[1]

for x in range(width):
    for y in range(height):
        print(img.getpixel((x,y)))

img.save('puppy.jpg')
