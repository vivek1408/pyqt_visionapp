from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class SquareLabel(QLabel):
    def __init__(self, parent=None):
        super(SquareLabel, self).__init__(parent)
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(223, 230, 248))
        self.setPalette(p)
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        print(event.pos().x(), event.pos().y())

    def mousePressEvent(self, event):
        print(event)
