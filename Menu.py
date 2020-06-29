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
from RegulatedData import RegulatedData
from Dashboard import Dashboard

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
        self.btnSearchByWord = QtWidgets.QPushButton(self.centralwidget)
        self.btnSearchByWord.setObjectName("btnSearchByWord")
        self.gridLayout.addWidget(self.btnSearchByWord, 1, 0, 1, 1)
        self.btnRegulatedData = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegulatedData.setObjectName("btnRegulatedData")
        self.gridLayout.addWidget(self.btnRegulatedData, 2, 0, 1, 1)
        self.btnDashboard = QtWidgets.QPushButton(self.centralwidget)
        self.btnDashboard.setObjectName("btnDashboard")
        self.gridLayout.addWidget(self.btnDashboard, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.actionInicio = QtWidgets.QAction(MainWindow)
        self.actionInicio.setObjectName("actionInicio")
        self.actionInicio.triggered.connect(self.toMenu)
        self.actionConsulta = QtWidgets.QAction(MainWindow)
        self.actionConsulta.setObjectName("actionConsulta")
        self.actionConsulta.triggered.connect(self.toGraph)
        self.actionBusqueda = QtWidgets.QAction(MainWindow)
        self.actionBusqueda.setObjectName("actionBusqueda")
        self.actionBusqueda.triggered.connect(self.toSearchByWord)
        self.actionDatoRegulado = QtWidgets.QAction(MainWindow)
        self.actionDatoRegulado.setObjectName("actionDatoRegulado")
        self.actionDatoRegulado.triggered.connect(self.toRegulatedData)
        self.actionDashboard = QtWidgets.QAction(MainWindow)
        self.actionDashboard.setObjectName("actionDashboard")
        self.actionDashboard.triggered.connect(self.toDashboard)
        self.menuMenu.addAction(self.actionInicio)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionConsulta)
        self.menuMenu.addAction(self.actionBusqueda)
        self.menuMenu.addAction(self.actionDatoRegulado)
        self.menuMenu.addAction(self.actionDashboard)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.btnGraphs.clicked.connect(self.toGraph)
        self.btnSearchByWord.clicked.connect(self.toSearchByWord)
        self.btnRegulatedData.clicked.connect(self.toRegulatedData)
        self.btnDashboard.clicked.connect(self.toDashboard)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.MainWindow = MainWindow

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnGraphs.setText(_translate("MainWindow", "Gráficas"))
        self.btnRegulatedData.setText(
            _translate("MainWindow", "Dato regulado"))
        self.btnSearchByWord.setText(_translate(
            "MainWindow", "Búsqueda por palabra"))
        self.btnDashboard.setText(_translate("MainWindow", "Dashboard"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionInicio.setText(_translate("MainWindow", "Inicio"))
        self.actionConsulta.setText(_translate("MainWindow", "Gráficas"))
        self.actionBusqueda.setText(_translate("MainWindow", "Búsqueda"))
        self.actionDatoRegulado.setText(_translate("MainWindow", "Dato Regulado"))
        self.actionDashboard.setText(_translate("MainWindow", "Dashboard"))

    def toSearchByWord(self):
        self.ui = Form()
        self.ui.setOptionsMenu(
            self.toMenu, self.toRegulatedData, self.toGraph, self.toSearchByWord)
        self.MainWindow.move(600, 100)
        self.ui.setupUi(self.MainWindow)

    def toGraph(self):
        self.ui = GraphQueries()
        self.ui.setOptionsMenu(
            self.toMenu, self.toRegulatedData, self.toGraph, self.toSearchByWord)
        self.MainWindow.move(600, 100)
        self.ui.setupUi(self.MainWindow)

    def toRegulatedData(self):
        self.ui = RegulatedData()
        self.ui.setOptionsMenu(
            self.toMenu, self.toRegulatedData, self.toGraph, self.toSearchByWord)
        self.MainWindow.move(600, 100)
        self.ui.setupUi(self.MainWindow)

    def toMenu(self):
        self.ui = self
        self.MainWindow.move(600, 100)
        self.ui.setupUi(self.MainWindow)

    def toDashboard(self):
        self.ui = Dashboard()
        self.MainWindow.move(600, 100)
        self.ui.setupUi(self.MainWindow)

    def startLog(self):
        logging.basicConfig(filename='Lumberjack.log',
                            level=logging.DEBUG, format=LOG_FORMAT)
        self.logger = logging.getLogger()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Menu()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
