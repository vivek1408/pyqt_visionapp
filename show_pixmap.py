import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
import custom_label


class Window(QWidget):
    def __init__(self, parent=None):

        QWidget.__init__(self, parent)
        self.setGeometry(490, 200, 950, 620)
        self.setFixedSize(950, 620)
        self.label = custom_label.SquareLabel()

        layout = QGridLayout()
        layout.addWidget(self.label, 0, 0, 1, 3, Qt.AlignCenter)
        self.setLayout(layout)

        self.updateImage()
        self.setWindowTitle(self.tr("Display image"))

    def updateImage(self):
        pixmap = QPixmap('image.JPG')
        pixmap = pixmap.scaledToWidth(950)
        painter = QPainter()
        painter.begin(pixmap)
        painter.end()

        self.label.setPixmap(pixmap)
        self.label.updateGeometry()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
