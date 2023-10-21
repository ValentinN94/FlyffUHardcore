from time import time
import cv2 as cv
from windowcapture import WindowCapture
from vision import Vision

wincap = WindowCapture('FlyffHarcore')
# initialize the Vision class
vision_limestone = Vision('Capture.PNG')

loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    # display the processed image
    points = vision_limestone.find(screenshot, 0.8)


    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')