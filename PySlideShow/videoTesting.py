#!/usr/local/bin/python3

import cv2
import argparse
import os
# Importing Image class from PIL module
from PIL import Image


# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-ext", "--extension", required=False, default='png', help="extension name. default is 'png'.")
ap.add_argument("-o", "--output", required=False, default='output.mp4', help="output video file")
args = vars(ap.parse_args())

# Arguments
dir_path = './dataset/homosexual'
ext = args['extension']
output = args['output']

images = []
for f in os.listdir(dir_path):
    if f.endswith(ext):
        images.append(f)

# Determine the width and height from the first image
image_path = os.path.join(dir_path, images[0])
frame = cv2.imread(image_path)

height, width, channels = frame.shape

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use lower case

for image in images:
    image_path = os.path.join(dir_path, image)
    im1 =Image.open(image_path)
    im1 = im1.resize( (width, height))
    im1.save(image_path)


out = cv2.VideoWriter(output, fourcc, 20.0, (width, height))
for image in images:
    image_path = os.path.join(dir_path, image)
    for j in range(20*5):
        frame = cv2.imread(image_path)
        out.write(frame) # Write out frame to video


# Release everything if job is finished
out.release()
cv2.destroyAllWindows()

print("The output video is {}".format(output))
