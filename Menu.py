# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Menu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pyodbc
import logging

from Form import Form
from GraphQueries import GraphQueries

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"


class Menu(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btnGraphs = QtWidgets.QPushButton(self.centralwidget)
        self.btnGraphs.setObjectName("btnGraphs")
        self.gridLayout.addWidget(self.btnGraphs, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.btnSearchByWord = QtWidgets.QPushButton(self.centralwidget)
        self.btnSearchByWord.setObjectName("btnSearchByWord")
        self.gridLayout.addWidget(self.btnSearchByWord, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.btnGraphs.clicked.connect(self.toGraph)
        self.btnSearchByWord.clicked.connect(self.toSearchByWord)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.MainWindow = MainWindow

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnGraphs.setText(_translate("MainWindow", "Gráficas"))
        self.pushButton_3.setText(_translate("MainWindow", "Otro"))
        self.btnSearchByWord.setText(_translate(
            "MainWindow", "Búsqueda por palabra"))

    def toSearchByWord(self):
        self.ui = Form()
        self.MainWindow.move(600, 100)
        self.ui.setupUi(self.MainWindow)

    def toGraph(self):
        self.ui = GraphQueries()
        self.MainWindow.move(600, 100)
        self.ui.setupUi(self.MainWindow)

    def startLog(self):
        logging.basicConfig(filename='Lumberjack.log',
                            level=logging.DEBUG, format=LOG_FORMAT)
        self.logger = logging.getLogger()


# if __name__ == "__main__":
    # import sys
    # app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Menu()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())
