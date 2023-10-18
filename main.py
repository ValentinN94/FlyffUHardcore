from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://universe.flyff.com/play"))
        self.setCentralWidget(self.browser)

# This is needed on Linux manjaro for URL to load
# For other OS use the following line
# app = QApplication(sys.argv)
app = QApplication(['', '--no-sandbox'])
window = MainWindow()
window.setWindowTitle('FlyffHarcore')
window.show()

app.exec_()