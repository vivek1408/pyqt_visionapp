from PyQt5.QtWidgets import *
import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSignal
import show_cv2_video
import show_pixmap

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

    def initUI(self):
        self.window1 = show_pixmap.Window()
        self.vid = show_cv2_video.ShowVideo()
        self.window2 = show_cv2_video.ImageViewer()
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.window1)
        layout.addWidget(self.window2)
        push_button = QtWidgets.QPushButton('Start')
        push_button.clicked.connect(self.vid.startVideo)
        main_window = QtWidgets.QMainWindow()
        main_window.setCentralWidget(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.initUI()
    window.show()
    sys.exit(app.exec_())
