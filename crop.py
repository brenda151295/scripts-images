
from PIL import Image
import os 
import glob

FILE = "images"
HEIGHT = 512
WIDTH = 512
FORMAT = ".jpg"

def crop(path, input, height, width, k):
    im = Image.open(input)
    imgwidth, imgheight = im.size
    name = input.split('/')[-1]
    os.mkdir(path)
    os.mkdir(os.path.join(path, name))
    for i in range(0,imgheight,height):
        for j in range(0,imgwidth,width):
            box = (j,i,j+width,i+height)
            a = im.crop(box)
            a.save(os.path.join(path,name,"IMG-%s %s" % (k,FORMAT)))
            k +=1


filelist = os.listdir(FILE)
for fichier in filelist[:]:
    if not(fichier.endswith(FORMAT)):
        filelist.remove(fichier)

for file in filelist:
    file = os.path.join(FILE, file)
    print file
    crop("crop",file,HEIGHT,WIDTH,1)