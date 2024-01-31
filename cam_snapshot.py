import numpy as np
import cv2 as cv
from datetime import datetime
import time
from glob import glob
import os

FOLDER = '/home/garamizo/Datasets/Plant-Timelapse'
ADDRESS_CAMERA = 'rtsp://root:pass@192.168.1.123:554/live/ch0'

# quit if there is a picture already taken today, closer to noon
now = datetime.now()
targetDt = datetime(now.year, now.month, now.day, 12, 0, 0, 0)

for path in glob(f'{FOLDER}/{now.strftime("%d%m%Y_*.png")}'):
	dt = datetime.strptime(path.split('/')[-1], '%d%m%Y_%H%M%S.png')
	
	if abs(dt - targetDt) < abs(now - targetDt):
		print(f'Picture {path} is better match')
		exit()

print('New picture is closer to target time')

# quit if camera fails (e.g. no connection)
cap = cv.VideoCapture(ADDRESS_CAMERA)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
    
# sample multiple times to "warm up" camera
for i in range(10):
	ret, frame = cap.read()
	
if not ret:
	print("Can't receive frame (stream end?). Exiting ...")
else:
	now = datetime.now()
	
	# delete old pictures
	for path in glob(f'{FOLDER}/{now.strftime("%d%m%Y_*.png")}'):
		print(f'Deleting {path}')
		os.remove(path)

	dt_string = now.strftime("%d%m%Y_%H%M%S")
	cv.imwrite(f'{FOLDER}/{dt_string}.png', frame)
	print(f'Saved to {FOLDER}/{dt_string}.png')

cap.release()

