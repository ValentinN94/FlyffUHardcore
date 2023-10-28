import os
from time import time
from windowcapture import WindowCapture
from src.detection.vision import Vision
from PyQt5.QtCore import QObject, pyqtSignal

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
        wincap.start()
        while True:
            if wincap.screenshot is None:
                continue

            self.points = new_char.find(wincap.screenshot)

            print('FPS {}'.format(1 / (time() - loop_time)))
            loop_time = time()

            if self.points:
                self.finished.emit(True)
                return

        self.finished.emit(False)