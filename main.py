from time import time
from windowcapture import WindowCapture
from vision import Vision
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
import os

script_directory = os.path.dirname(os.path.abspath(__file__))

image_path = os.path.join(script_directory, 'images', 'new_char_original.PNG')

def overwatch():
    # Your main script logic here
    wincap = WindowCapture('FlyffHarcore')
    # initialize the Vision class
    vision_limestone = Vision(image_path)

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
        if points:
            break

    return True