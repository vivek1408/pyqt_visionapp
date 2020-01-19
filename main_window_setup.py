# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'trial2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import image_viewer
import cv2
import show_video
import show_crop

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        self.p1 = 0
        self.p2 = 0
        self.p3 = 0
        self.p4 = 0
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 1000)
        MainWindow.setWindowOpacity(10.0)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 860, 161, 51))
        self.pushButton.setObjectName("pushButton")
        self.ImageViewer = image_viewer.ImageViewer(self.centralwidget)
        self.ImageViewer.setEnabled(True)
        self.ImageViewer.setGeometry(QtCore.QRect(0, 0, 1000, 800))
        self.ImageViewer.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.ImageViewer.setAutoFillBackground(True)
        self.ImageViewer.setObjectName("ImageViewer")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 860, 151, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.crop_viewer = image_viewer.ImageViewer(self.centralwidget)
        self.crop_viewer.setGeometry(QtCore.QRect(1030, 60, 351, 341))
        self.crop_viewer.setAutoFillBackground(True)
        self.crop_viewer.setObjectName("cropViewer")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1110, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(390, 800, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(True)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1400, 26))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menuhelp = QtWidgets.QMenu(self.menubar)
        self.menuhelp.setObjectName("menuhelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionquit = QtWidgets.QAction(MainWindow)
        self.actionquit.setObjectName("actionquit")
        self.actionopen_top_lvl = QtWidgets.QAction(MainWindow)
        self.actionopen_top_lvl.setObjectName("actionopen_top_lvl")
        self.actionshortcuts = QtWidgets.QAction(MainWindow)
        self.actionshortcuts.setObjectName("actionshortcuts")
        self.actionabout = QtWidgets.QAction(MainWindow)
        self.actionabout.setObjectName("actionabout")
        self.menufile.addAction(self.actionquit)
        self.menufile.addAction(self.actionopen_top_lvl)
        self.menuhelp.addAction(self.actionshortcuts)
        self.menuhelp.addAction(self.actionabout)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.obj = image_viewer.ImageViewer.obj

        self.thread = QtCore.QThread()
        self.thread.start()
        self.vid = show_video.ShowVideo()
        self.vid.moveToThread(self.thread)

        #SLOTS
        self.vid.VideoSignal.connect(self.ImageViewer.setImage)

        self.obj.click_signal.connect(self.vid.cropstart)
        self.pushButton.clicked.connect(self.vid.startVideo)
        #self.pushButton_2.clicked.connect(lambda: self.vid.cropstart(100, 100, 400, 400))
        self.obj.click_signal.connect(self.cropstart)




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Processing for Inspection"))
        self.pushButton.setText(_translate("MainWindow", "Show Vid"))
        self.pushButton_2.setText(_translate("MainWindow", "Save Image"))
        self.label.setText(_translate("MainWindow", "CROPPED IMAGE"))
        self.label_2.setText(_translate("MainWindow", "LIVE FEED FROM CAMERA"))
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.menuhelp.setTitle(_translate("MainWindow", "help"))
        self.actionquit.setText(_translate("MainWindow", "quit"))
        self.actionopen_top_lvl.setText(_translate("MainWindow", "open top lvl"))
        self.actionshortcuts.setText(_translate("MainWindow", "shortcuts"))
        self.actionabout.setText(_translate("MainWindow", "about"))


    def cropstart(self, p1, p2, p3, p4):

        self.thread2 = QtCore.QThread()
        self.thread2.start()
        self.crop = show_crop.ShowVideo(p1, p2, p3, p4)
        self.crop.moveToThread(self.thread2)
        self.crop.CropSignal.connect(self.crop_viewer.setImage)


