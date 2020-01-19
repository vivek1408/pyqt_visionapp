import cv2
import numpy as np
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class customObject(QObject):
    click_signal = QtCore.pyqtSignal(int, int, int, int)
    def __init__(self, parent=None):
        super(customObject, self).__init__(parent)

class ImageViewer(QtWidgets.QWidget):
    obj = customObject()
    count = 0
    tri_coords_X = np.array([0, 0, 0])
    tri_coords_Y = np.array([0, 0, 0])
    p2 = QtCore.QPoint()
    p1 = QtCore.QPoint()
    def __init__(self, parent=None):
        super(ImageViewer, self).__init__(parent)
        self.image = QtGui.QImage()
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
        # if not(all(x == 0 for x in self.tri_coords_X) & all(y ==0 for y in self.tri_coords_Y)):
        #     for i in range(self.count):
        #         painter.drawPoint(self.tri_coords_X[i], self.tri_coords_Y[i])
        #     if self.count == 3:
        #         pen.setStyle(Qt.DotLine)
        #         painter.setPen(pen)
        #         painter.drawLine(self.tri_coords_X[0], self.tri_coords_Y[0], self.tri_coords_X[1], self.tri_coords_Y[1])
        #         painter.drawLine(self.tri_coords_X[0], self.tri_coords_Y[0], self.tri_coords_X[2], self.tri_coords_Y[2])
        #         painter.drawLine(self.tri_coords_X[1], self.tri_coords_Y[1], self.tri_coords_X[2], self.tri_coords_Y[2])
        #
        # #self.image = QtGui.QImage()

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

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = event.pos()
        self.update()
        self.p1 = self.begin
        #     self.mouseclickcoorX = event.pos().x()
        #     self.mouseclickcoorY = event.pos().y()
        #     self.obj.click_signal.emit()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        self.begin = event.pos()
        self.end = event.pos()
        self.p2 = self.end
        self.obj.click_signal.emit(self.p1.x(), self.p1.y(), self.p2.x(), self.p2.y())
        #print(self.p1.x(), self.p1.y(), self.p2.x(), self.p2.y())
        self.update()

    # def click_history(self):
    #     if (self.count < 3):
    #         self.tri_coords_X[self.count] = self.mouseclickcoorX
    #         self.tri_coords_Y[self.count] = self.mouseclickcoorY
    #         print(self.mouseclickcoorX, self.mouseclickcoorY, self.count)
    #         self.count = self.count + 1

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.count = 0
            self.tri_coords_Y.fill(0)
            self.tri_coords_X.fill(0)

