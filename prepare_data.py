#!/usr/bin/env python
import cv2
import pickle
import os
import sys

WIDTH = 640
HEIGHT = 480
# The goal is to get 320x240 image
TOP_LINE = 85
BOTTOM_LINE = 325
LEFT_LINE = 160
RIGHT_LINE = WIDTH - 160

DIR = os.path.join('data', 'images')

#def get_frame(capture):
#    frame_nr = capture.get(cv2.CAP_PROP_POS_FRAMES)
#    ret, frame = capture.read()
#    return ret, frame, int(frame_nr)

try:
    os.mkdir(DIR)
except FileExistsError:
    pass

# Load file with car speeds
with open(os.path.join('data', 'train.txt'), 'r') as f:
    speeds_lst = f.readlines()

# Create video capture to read frames of video
cap = cv2.VideoCapture(os.path.join('data', 'train.mp4'))
nr_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Check length validity of data.
if nr_frames != len(speeds_lst):
    print('Number of frames in a video does not match number of target speeds. Exiting...')
    sys.exit()

# Structures with data
images = []
speeds = {}

for frame_nr in range(len(speeds_lst)):
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_nr)
    ret, image = cap.read()
    
    if not ret:
        print('\nError reading frames.')
        break
   
    print(f'{frame_nr + 1} / {nr_frames}', end='\r')
    image_name = f'{frame_nr}.png'

    # Crop image
    image_cropped = image[TOP_LINE:BOTTOM_LINE, LEFT_LINE:RIGHT_LINE, :]  
   
    # Log
    images.append(image_name)
    speeds[image_name] = float(speeds_lst[frame_nr])

    # Save image to directory to PNG
    cv2.imwrite(os.path.join(DIR, image_name), image_cropped)

# Save dataset to pickle
pickle.dump({'x': images, 'y': speeds}, open(os.path.join('data', 'train.pickle'), 'wb'))

# Release VideoCapture
cap.release()

