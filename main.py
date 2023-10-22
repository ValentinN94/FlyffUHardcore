from time import time
import cv2 as cv
from windowcapture import WindowCapture
from vision import Vision
from gamewindow import WebBrowser, app

app.exec_()

wincap = WindowCapture('FlyffHarcore')
# initialize the Vision class
vision_limestone = Vision('Capture.PNG')

loop_time = time()
wincap.start()
while(True):

    #if we don't have a screenshot yet, don't run the code below this point yet
    if wincap.screenshot is None:
        continue

    # display the processed image
    points = vision_limestone.find(wincap.screenshot, 0.8)


    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

        # press 'q' with the output window focused to exit.
        # waits 1 ms every loop to process key presses
        # if cv.waitKey(1) == ord('q'):
        #     cv.destroyAllWindows()
        #     break
