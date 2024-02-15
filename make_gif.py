# import numpy as np
import cv2
# from datetime import datetime
# import time
from glob import glob
import imageio
# import os

FOLDER = '/home/garamizo/Datasets/Plant-Timelapse'
DEST = '/home/garamizo/Software/Plant-Timelapse/html/images/video.gif'
height = 800

imgs = []
for path in sorted(glob(f'{FOLDER}/*.png')):
    print(path)
    img = cv2.imread(path)
    h, w, c = img.shape
    img = cv2.cvtColor(cv2.resize(img, (w*height//h, height)), cv2.COLOR_BGR2RGB) 
    imgs.append(img)

imgs.append(img.copy() * 0)
imageio.mimwrite(f'{DEST}', imgs, fps=2, loop=0)

