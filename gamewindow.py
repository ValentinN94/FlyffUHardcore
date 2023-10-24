from PyQt5.QtCore import QUrl, pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QAction
from PyQt5.QtWebEngineWidgets import QWebEngineView
from main import overwatch

class PopUpDialog(QMessageBox):
    def __init__(self):
        super(PopUpDialog, self).__init__()
        self.setWindowTitle("Popup Dialog")
        self.setText("This is a pop-up dialog.")
        self.addButton(QMessageBox.Ok)

class WebBrowser(QMainWindow):
    def __init__(self):
        super(WebBrowser, self).__init__()

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://universe.flyff.com/play"))
        self.setCentralWidget(self.browser)

        self.ftool = QAction("Mini FTool", self)
        self.ftool.triggered.connect(self.show_popup)

    def show_popup(self):
        # Create and show the pop-up dialog
        pop_up = PopUpDialog()
        pop_up.exec_()


app = QApplication([])
window = WebBrowser()
window.setWindowTitle('FlyffHarcore')
window.show()
a = overwatch()
if a:
    window.addAction(window.ftool)
app.exec_()

