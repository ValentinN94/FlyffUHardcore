import os
from time import time
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QThread, QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView
from windowcapture import WindowCapture
from vision import Vision

# Create a worker class that subclasses QObject for running the 'overwatch' function in a separate thread.
class OverwatchWorker(QObject):
    finished = pyqtSignal(bool)

    def run(self):
        script_directory = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_directory, 'images', 'new_char_original.PNG')

        wincap = WindowCapture('FlyffHarcore')
        new_char = Vision(image_path)

        loop_time = time()
        wincap.start()
        while True:
            if wincap.screenshot is None:
                continue

            points = new_char.find(wincap.screenshot)

            print('FPS {}'.format(1 / (time() - loop_time)))
            loop_time = time()

            if points:
                self.finished.emit(True)
                return

        self.finished.emit(False)

# Create the main application window using QMainWindow.
class WebBrowser(QMainWindow):
    def __init__(self):
        super(WebBrowser, self).__init__()

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://universe.flyff.com/play"))
        self.setCentralWidget(self.browser)
        self.browser.loadFinished.connect(self.on_load_finished)

    # Slot that is called when the web page finishes loading.
    @pyqtSlot(bool)
    def on_load_finished(self, ok):
        if ok:
            # Create a custom QMessageBox with a "Continue" button
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle('Overwatch')
            msg_box.setText('Your movements will be recorded for the HardcoreUFlyff Challenge. Do you agree?')

            continue_button = msg_box.addButton('New Character', QMessageBox.AcceptRole)
            msg_box.addButton(QMessageBox.Yes)
            msg_box.addButton(QMessageBox.No)

            reply = msg_box.exec()

            if reply == QMessageBox.AcceptRole:
                self.run_overwatch()
            else:
                print("User does not want to continue.")
        else:
            print("Page failed to load.")

    # Method to set up and start the new thread for running the 'overwatch' function.
    def run_overwatch(self):
        self.overwatch_thread = QThread()
        self.overwatch_worker = OverwatchWorker()
        self.overwatch_worker.moveToThread(self.overwatch_thread)
        self.overwatch_thread.started.connect(self.overwatch_worker.run)
        self.overwatch_worker.finished.connect(self.on_overwatch_finished)
        self.overwatch_thread.start()

    # Slot to handle the result from the 'overwatch' function.
    @pyqtSlot(bool)
    def on_overwatch_finished(self, success):
        if success:
            print("Overwatch finished successfully.")
        else:
            print("Overwatch failed.")
        self.overwatch_thread.quit()
        self.overwatch_thread.wait()

app = QApplication([])
window = WebBrowser()
window.setWindowTitle('FlyffHarcore')
window.show()
app.exec_()
