from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui

class customObject(QObject):
    click_signal = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        super(customObject, self).__init__(parent)


class customLabel(QLabel):
    obj = customObject()
    mouseclickcoorX = 0
    mouseclickcoorY = 0
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(223, 230, 248))
        self.setPalette(p)
        self.setMouseTracking(True)

    def mousePressEvent(self, event):

        self.mouseclickcoorX = event.pos().x()
        self.mouseclickcoorY = event.pos().y()
        print(self.mouseclickcoorX, self.mouseclickcoorY)
        self.obj.click_signal.emit()
