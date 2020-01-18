from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
import main_app_window

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = main_app_window.Ui_MainWindow()
    mainWindow = QtWidgets.QMainWindow()
    window.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())