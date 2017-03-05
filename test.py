import glob
from PIL import Image
from images2gif import *

images = glob.glob('patches/*.png')
ff_images = sorted(images, key= lambda x: int(x[8:-8]))
im_arr = []
for imName in ff_images:
    im = np.array(Image.open(imName))
    im_arr.append(im)
writeGif('output.gif',im_arr, duration=0.2, dither=0)

'''
im = np.zeros((200,200), dtype=np.uint8)
im[10:30,:] = 100
im[:,80:120] = 255
im[-50:-40,:] = 50

images = [im*1.0, im*0.8, im*0.6, im*0.4, im*0]
writeGif('tmp/lala3.gif',images, duration=0.2, dither=0)
'''