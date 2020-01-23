from PyQt5 import QtCore, QtGui, QtWidgets
import cv2

class ShowVideo(QtCore.QObject):
    # initiating the built in camera
    camera_port = 0
    camera = cv2.VideoCapture(camera_port)
    VideoSignal = QtCore.pyqtSignal(QtGui.QImage)
    imagemat = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        super(ShowVideo, self).__init__(parent)

    @QtCore.pyqtSlot()
    def startVideo(self):
        run_video = True
        while run_video:
            ret, image = self.camera.read()

            color_swapped_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            height, width, _ = color_swapped_image.shape

            qt_image = QtGui.QImage(color_swapped_image.data,
                                    width,
                                    height,
                                    color_swapped_image.strides[0],
                                    QtGui.QImage.Format_RGB888)

            pixmap = QtGui.QPixmap(qt_image)
            qt_image = pixmap.scaled(1000, 800, QtCore.Qt.KeepAspectRatio)
            qt_image = QtGui.QImage(qt_image)

            self.VideoSignal.emit(qt_image)
            self.imagemat.emit(image)
    # def cropstart(self, p1, p2, p3, p4):
    #     self.cropflag = True
    #     self.p1 = p1
    #     self.p2 = p2
    #     self.p3 = p3
    #     self.p4 = p4
    #     print("points", p1, p2, p3, p4)