import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import custom_label
import numpy as np

class Window(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        #self.setGeometry(490, 200, 1200, 800)
        #self.setFixedSize(1200, 800)
        self.label = custom_label.customLabel()
        custom_label.customLabel.obj.click_signal.connect(self.updateImage)
        layout = QGridLayout()
        layout.addWidget(self.label, 0, 0, 1, 3, Qt.AlignCenter)
        self.setLayout(layout)
        self.pixmap = QPixmap('image.JPG')
        self.pixmap = self.pixmap.scaledToWidth(400)
        self.updateImage()
        #self.setWindowTitle(self.tr("Display image"))
        self.setFocusPolicy(Qt.StrongFocus)
    count = 0
    tri_coords_X = np.array([0,0,0])
    tri_coords_Y = np.array([0,0,0])

    def init_img(self):
        painter = QPainter()
        self.pixmap = QPixmap('image.JPG')
        self.pixmap = self.pixmap.scaledToWidth(400)
        painter.begin(self.pixmap)
        painter.end()
        self.label.setPixmap(self.pixmap)

    def updateImage(self):
        painter = QPainter()
        pen = QPen(Qt.red)
        pen.setWidth(5)
        painter.begin(self.pixmap)
        painter.setPen(pen)
        print("X = ",self.label.mouseclickcoorX, "Y = ", self.label.mouseclickcoorY )
        if(self.label.mouseclickcoorY & self.label.mouseclickcoorX):
            if(self.count<3):
                self.tri_coords_X[self.count] = self.label.mouseclickcoorX
                self.tri_coords_Y[self.count] = self.label.mouseclickcoorY
                self.count = self.count+1
                painter.drawPoint(self.label.mouseclickcoorX, self.label.mouseclickcoorY)
            if self.count == 3:
                pen.setStyle(Qt.DotLine)
                painter.setPen(pen)
                painter.drawLine(self.tri_coords_X[0], self.tri_coords_Y[0], self.tri_coords_X[1], self.tri_coords_Y[1])
                painter.drawLine(self.tri_coords_X[0], self.tri_coords_Y[0], self.tri_coords_X[2], self.tri_coords_Y[2])
                painter.drawLine(self.tri_coords_X[1], self.tri_coords_Y[1], self.tri_coords_X[2], self.tri_coords_Y[2])

        painter.end()

        self.label.setPixmap(self.pixmap)
        self.label.updateGeometry()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.count = 0
            self.tri_coords_Y.fill(0)
            self.tri_coords_X.fill(0)
            self.init_img()


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Window()
#     window.show()
#     sys.exit(app.exec_())
