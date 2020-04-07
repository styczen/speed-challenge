#!/usr/bin/env python
import cv2
import pickle
import os

WIDTH = 640
HEIGHT = 480
TOP_LINE = 70
BOTTOM_LINE = 340

def get_frame(capture):
    frame_nr = capture.get(cv2.CAP_PROP_POS_FRAMES)
    ret, frame = capture.read()
    return ret, frame, int(frame_nr)

try:
    os.mkdir('images')
except FileExistsError:
    pass

# Load file with car speeds
with open('data/train.txt', 'r') as f:
    speeds = f.readlines()

# Create video capture to read frames of video
cap = cv2.VideoCapture('data/train.mp4')
nr_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

image_paths = [] 
speeds = [float(speed) for speed in speeds]

while True:
    ret, image, frame_nr = get_frame(cap)
    if not ret:
        print(f'\nDone')
        break

    print(f'{frame_nr + 1} / {nr_frames}', end='\r')

    # Crop image, save its relative path to list
    image_cropped = image[TOP_LINE:BOTTOM_LINE, ...]  
    image_rel_path = os.path.join('images', f'{frame_nr}.png')
    image_paths.append(image_rel_path) 

    # Save image to directory to PNG
    cv2.imwrite(image_rel_path, image_cropped)

# Save images to pickle
pickle.dump({'image_paths': image_paths, 'targets': speeds}, open('train.pickle', 'wb'))

cap.release()

