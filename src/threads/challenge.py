import os
from time import time

from src.detection.vision import Vision
from PyQt5.QtCore import QObject, pyqtSignal
from windowcapture import WindowCapture
import cv2 as cv

class OverwatchWorker(QObject):
    finished = pyqtSignal(bool)

    def run(self):
        script_directory = os.path.dirname(os.path.abspath(__file__))
        src_directory = os.path.join(script_directory, os.path.pardir)
        main_directory = os.path.join(src_directory, os.path.pardir)
        os.chdir(main_directory)
        image_path = os.path.join(os.getcwd(), 'images', 'char_status', 'LVL_target.PNG')
        print(f"Full image path: {image_path}")

        wincap = WindowCapture('FlyffHarcore')
        new_char = Vision(image_path)

        loop_time = time()
        wincap.capture_and_emit_screenshot()
        counter = 0
        while True:

            self.points = new_char.find(wincap.get_screenshot())

            print('FPS {}'.format(1 / (time() - loop_time)))
            loop_time = time()
            cv.imwrite('result' + str(counter) + '.jpg', wincap.get_screenshot())
            if self.points:
                self.finished.emit(True)
                return

        self.finished.emit(False)