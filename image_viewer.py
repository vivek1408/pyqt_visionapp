import cv2
import numpy as np
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cv2

class customObject(QObject):
    crop_signal = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        super(customObject, self).__init__(parent)

class ImageViewer(QtWidgets.QWidget):
    obj = customObject()
    p2 = QtCore.QPoint()
    p1 = QtCore.QPoint()
    def __init__(self, parent=None):
        super(ImageViewer, self).__init__(parent)
        self.image = QtGui.QImage()
        self.crop = None
        self.setAttribute(QtCore.Qt.WA_OpaquePaintEvent)
        #self.obj.click_signal.connect(self.click_history)
        self.setFocusPolicy(Qt.StrongFocus)
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawImage(0, 0, self.image)
        pen = QPen(Qt.red)
        pen.setWidth(5)
        painter.setPen(pen)
        painter.drawRect(QtCore.QRect(self.begin, self.end))

    def initUI(self):
        self.setWindowTitle('Test')

    @QtCore.pyqtSlot(QtGui.QImage)
    def setImage(self, image):
        if image.isNull():
            print("viewer dropped frame!")

        self.image = image
        if image.size() != self.size():
            self.setFixedSize(image.size())
        self.update()

    def crop_image(self, image):
        self.crop = image
        if(self.p1 and self.p2):
            self.crop = self.crop[self.p1.X():self.p2.X(), self.p1.Y():self.p2.Y()]
            cv2.imshow("crop image", self.crop)
            cv2.waitKey(10)
    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = event.pos()
        self.update()
        self.p1 = self.begin

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        self.begin = event.pos()
        self.end = event.pos()
        self.p2 = self.end
        self.update()


    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.count = 0
            self.tri_coords_Y.fill(0)
            self.tri_coords_X.fill(0)

