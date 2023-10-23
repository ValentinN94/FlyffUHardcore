from time import time
from windowcapture import WindowCapture
from vision import Vision
import cv2 as cv

# Your main script logic here
wincap = WindowCapture('FlyffHarcore')
# initialize the Vision class
vision_limestone = Vision('new_char_gold.PNG')

loop_time = time()
wincap.start()
while (True):

    # if we don't have a screenshot yet, don't run the code below this point yet
    if wincap.screenshot is None:
        continue

    # display the processed image
    points = vision_limestone.find(wincap.screenshot)

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

