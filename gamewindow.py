from PyQt5.QtCore import pyqtSlot, QThread, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from src.threads.challenge import OverwatchWorker
from windowcapture import WindowCapture
import numpy as np



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
            top_left, bottom_right = self.overwatch_worker.points
            print(top_left, bottom_right)
        else:
            print("Overwatch failed.")
        self.overwatch_thread.quit()
        self.overwatch_thread.wait()

    @pyqtSlot(np.ndarray)
    def handle_screenshot_ready(self, screenshot):
        if screenshot:
            print('Screenshoot is here')



# Handle the captured screenshot here

app = QApplication([])
window = WebBrowser()
window.setWindowTitle('FlyffHarcore')
window.show()
app.exec_()
