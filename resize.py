import PIL
from PIL import Image
import os

FILE = "images"
WIDTH = 512
FORMAT = ".jpg"


def resize(path, name, mywidth):
	img = Image.open(name)
	name = name.split('/')[-1]
	wpercent = (mywidth/float(img.size[0]))
	hsize = int((float(img.size[1])*float(wpercent)))
	img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
	os.mkdir(path)
	img.save(os.path.join(path,name))

filelist = os.listdir(FILE)
for fichier in filelist[:]:
    if not(fichier.endswith(FORMAT)):
        filelist.remove(fichier)

for file in filelist:
    file = os.path.join(FILE, file)
    print file
    resize("resize",file,WIDTH)