# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'trial.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import show_pixmap
import show_cv2_video
import cv2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 585)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 350, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(380, 350, 381, 151))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 30, 171, 31))
        self.label.setMouseTracking(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 171, 31))
        self.label_2.setMouseTracking(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 171, 31))
        self.label_3.setMouseTracking(False)
        self.label_3.setObjectName("label_3")
        self.widget = show_pixmap.Window(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.widget.setObjectName("widget")
        self.image_view_widget = show_cv2_video.ImageViewer(self.centralwidget)
        self.image_view_widget.setGeometry(QtCore.QRect(400, 0, 400, 300))
        self.image_view_widget.setObjectName("widget_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 350, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menufile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.thread = QtCore.QThread()
        self.thread.start()
        self.vid = ShowVideo()
        self.vid.moveToThread(self.thread)
        self.vid.VideoSignal.connect(self.image_view_widget.setImage)
        self.pushButton.clicked.connect(self.vid.startVideo)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Show Vid"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.label.setText(_translate("MainWindow", "Text1"))
        self.label_2.setText(_translate("MainWindow", "Text1"))
        self.label_3.setText(_translate("MainWindow", "Text1"))
        self.pushButton_2.setText(_translate("MainWindow", "Save Image"))
        self.menufile.setTitle(_translate("MainWindow", "file"))


class ShowVideo(QtCore.QObject):
        # initiating the built in camera
        camera_port = 0
        camera = cv2.VideoCapture(camera_port)
        VideoSignal = QtCore.pyqtSignal(QtGui.QImage)

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
                qt_image = pixmap.scaled(400, 300, QtCore.Qt.KeepAspectRatio)
                qt_image = QtGui.QImage(qt_image)

                self.VideoSignal.emit(qt_image)

