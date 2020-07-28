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
from AllData import AllData
from ProcessesBigData import ProcessesBigData
from ResidenceBigData import ResidenceBigData
from ResidenceAndProcessesBigData import ResidenceAndProcessesBigData
from DataInventary import DataInventary

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
        self.gridLayout.addWidget(self.btnGraphs, 1, 0, 1, 1)
        self.btnSearchByWord = QtWidgets.QPushButton(self.centralwidget)
        self.btnSearchByWord.setObjectName("btnSearchByWord")
        self.gridLayout.addWidget(self.btnSearchByWord, 2, 0, 1, 1)
        self.btnRegulatedData = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegulatedData.setObjectName("btnRegulatedData")
        self.gridLayout.addWidget(self.btnRegulatedData, 3, 0, 1, 1)
        self.btnDashboard = QtWidgets.QPushButton(self.centralwidget)
        self.btnDashboard.setObjectName("btnDashboard")
        self.gridLayout.addWidget(self.btnDashboard, 4, 0, 1, 1)
        self.btnAllData = QtWidgets.QPushButton(self.centralwidget)
        self.btnAllData.setObjectName("btnAllData")
        self.gridLayout.addWidget(self.btnAllData, 5, 0, 1, 1)
        self.btnResidenceBigData = QtWidgets.QPushButton(self.centralwidget)
        self.btnResidenceBigData.setObjectName("btnResidenceBigData")
        self.gridLayout.addWidget(self.btnResidenceBigData, 6, 0, 1, 1)
        self.btnProcessesBigData = QtWidgets.QPushButton(self.centralwidget)
        self.btnProcessesBigData.setObjectName("btnProcessesBigData")
        self.gridLayout.addWidget(self.btnProcessesBigData, 7, 0, 1, 1)
        self.btnResidenceAndProcessesBigData = QtWidgets.QPushButton(
            self.centralwidget)
        self.btnResidenceAndProcessesBigData.setObjectName(
            "btnResidenceAndProcessesBigData")
        self.gridLayout.addWidget(
            self.btnResidenceAndProcessesBigData, 8, 0, 1, 1)
        self.btnDataInventary = QtWidgets.QPushButton(self.centralwidget)
        self.btnDataInventary.setObjectName("btnDataInventary")
        self.gridLayout.addWidget(
            self.btnDataInventary, 0, 0, 1, 1)

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
        self.actionDataInventary = QtWidgets.QAction(MainWindow)
        self.actionDataInventary.setObjectName("actionDataInventary")
        self.actionDataInventary.triggered.connect(self.toDataInventary)
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
        self.actionAllData = QtWidgets.QAction(MainWindow)
        self.actionAllData.setObjectName("actionAllData")
        self.actionAllData.triggered.connect(self.toAllData)
        self.actionResidenceBigData = QtWidgets.QAction(MainWindow)
        self.actionResidenceBigData.setObjectName("actionResidenceBigData")
        self.actionResidenceBigData.triggered.connect(self.toResidenceBigData)
        self.actionProcessesBigData = QtWidgets.QAction(MainWindow)
        self.actionProcessesBigData.setObjectName("actionProcessesBigData")
        self.actionProcessesBigData.triggered.connect(self.toProcessesBigData)
        self.actionResidenceAndProcessesBigData = QtWidgets.QAction(MainWindow)
        self.actionResidenceAndProcessesBigData.setObjectName(
            "actionResidenceAndProcessesBigData")
        self.actionResidenceAndProcessesBigData.triggered.connect(
            self.toResidenceAndProcessesBigData)

        self.menuMenu.addAction(self.actionInicio)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionConsulta)
        self.menuMenu.addAction(self.actionBusqueda)
        self.menuMenu.addAction(self.actionDatoRegulado)
        self.menuMenu.addAction(self.actionDashboard)
        self.menuMenu.addAction(self.actionAllData)
        self.menuMenu.addAction(self.actionResidenceBigData)
        self.menuMenu.addAction(self.actionProcessesBigData)
        self.menuMenu.addAction(self.actionResidenceAndProcessesBigData)
        self.menuMenu.addAction(self.actionDataInventary)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.btnGraphs.clicked.connect(self.toGraph)
        self.btnSearchByWord.clicked.connect(self.toSearchByWord)
        self.btnRegulatedData.clicked.connect(self.toRegulatedData)
        self.btnDashboard.clicked.connect(self.toDashboard)
        self.btnAllData.clicked.connect(self.toAllData)
        self.btnResidenceBigData.clicked.connect(self.toResidenceBigData)
        self.btnProcessesBigData.clicked.connect(self.toProcessesBigData)
        self.btnResidenceAndProcessesBigData.clicked.connect(
            self.toResidenceAndProcessesBigData)
        self.btnDataInventary.clicked.connect(self.toDataInventary)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.MainWindow = MainWindow

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Menú de opciones"))
        MainWindow.setWindowIcon(QtGui.QIcon('favicon.ico'))
        self.btnGraphs.setText(_translate("MainWindow", "Gráfica de grandes datos en procesos y libros"))
        self.btnRegulatedData.setText(
            _translate("MainWindow", "Usos por dato regulado"))
        self.btnSearchByWord.setText(_translate(
            "MainWindow", "Búsqueda por palabra"))
        self.btnDashboard.setText(_translate("MainWindow", "Dashboard"))
        self.btnAllData.setText(_translate("MainWindow", "Linaje"))
        self.btnResidenceBigData.setText(_translate(
            "MainWindow", "Residencia por Gran Dato"))
        self.btnProcessesBigData.setText(_translate(
            "MainWindow", "Procesos por Gran dato"))
        self.btnResidenceAndProcessesBigData.setText(_translate(
            "MainWindow", "Residencia y Procesos por Gran Dato"))
        self.btnDataInventary.setText(_translate(
            "MainWindow", "Inventario de datos"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionInicio.setText(_translate("MainWindow", "Inicio"))
        self.actionConsulta.setText(_translate("MainWindow", "Gráfica de grandes datos en procesos y libros"))
        self.actionBusqueda.setText(_translate("MainWindow", "Búsqueda"))
        self.actionDatoRegulado.setText(
            _translate("MainWindow", "Usos por dato regulado"))
        self.actionDashboard.setText(_translate("MainWindow", "Dashboard"))
        self.actionAllData.setText(_translate("MainWindow", "Linaje"))
        self.actionResidenceBigData.setText(
            _translate("MainWindow", "Residencia por Gran Dato"))
        self.actionProcessesBigData.setText(
            _translate("MainWindow", "Procesos por Gran dato"))
        self.actionResidenceAndProcessesBigData.setText(
            _translate("MainWindow", "Residencia y Procesos por Gran Dato"))
        self.actionDataInventary.setText(
            _translate("MainWindow", "Inventario de datos"))

    def toSearchByWord(self):
        self.ui = Form()
        self.ui.setOptionsMenu(
            self.toMenu, self.toRegulatedData, self.toGraph, self.toSearchByWord,
            self.toDashboard, self.toAllData, self.toResidenceBigData,
            self.toProcessesBigData, self.toResidenceAndProcessesBigData, self.toDataInventary)
        self.MainWindow.move(600, 100)
        self.ui.setupUi(self.MainWindow)

    def toGraph(self):
        self.ui = GraphQueries()
        self.ui.setOptionsMenu(
            self.toMenu, self.toRegulatedData, self.toGraph, self.toSearchByWord,
            self.toDashboard, self.toAllData, self.toResidenceBigData,
            self.toProcessesBigData, self.toResidenceAndProcessesBigData, self.toDataInventary)
        self.MainWindow.move(600, 100)
        self.ui.setupUi(self.MainWindow)

    def toRegulatedData(self):
        self.ui = RegulatedData()
        self.ui.setOptionsMenu(
            self.toMenu, self.toRegulatedData, self.toGraph, self.toSearchByWord,
            self.toDashboard, self.toAllData, self.toResidenceBigData,
            self.toProcessesBigData, self.toResidenceAndProcessesBigData, self.toDataInventary)
        self.MainWindow.move(600, 100)
        self.ui.setupUi(self.MainWindow)

    def toMenu(self):
        self.ui = self
        self.MainWindow.move(600, 100)
        self.ui.setupUi(self.MainWindow)

    def toDashboard(self):
        self.ui = Dashboard()
        self.ui.setOptionsMenu(
            self.toMenu, self.toRegulatedData, self.toGraph, self.toSearchByWord,
            self.toDashboard, self.toAllData, self.toResidenceBigData,
            self.toProcessesBigData, self.toResidenceAndProcessesBigData, self.toDataInventary)
        self.MainWindow.move(600, 100)
        self.ui.setupUi(self.MainWindow)

    def toAllData(self):
        self.ui = AllData()
        self.ui.setOptionsMenu(
            self.toMenu, self.toAllData, self.toGraph, self.toSearchByWord,
            self.toDashboard, self.toAllData, self.toResidenceBigData,
            self.toProcessesBigData, self.toResidenceAndProcessesBigData, self.toDataInventary)
        self.MainWindow.move(600, 100)
        self.ui.setupUi(self.MainWindow)

    def toResidenceBigData(self):
        self.ui = ResidenceBigData()
        self.ui.setOptionsMenu(
            self.toMenu, self.toResidenceBigData, self.toGraph, self.toSearchByWord,
            self.toDashboard, self.toAllData, self.toResidenceBigData,
            self.toProcessesBigData, self.toResidenceAndProcessesBigData, self.toDataInventary)
        self.MainWindow.move(600, 100)
        self.ui.setupUi(self.MainWindow)

    def toProcessesBigData(self):
        self.ui = ProcessesBigData()
        self.ui.setOptionsMenu(
            self.toMenu, self.toProcessesBigData, self.toGraph, self.toSearchByWord,
            self.toDashboard, self.toAllData, self.toResidenceBigData,
            self.toProcessesBigData, self.toResidenceAndProcessesBigData, self.toDataInventary)
        self.MainWindow.move(600, 100)
        self.ui.setupUi(self.MainWindow)

    def toResidenceAndProcessesBigData(self):
        self.ui = ResidenceAndProcessesBigData()
        self.ui.setOptionsMenu(
            self.toMenu, self.toProcessesBigData, self.toGraph, self.toSearchByWord,
            self.toDashboard, self.toAllData, self.toResidenceBigData,
            self.toProcessesBigData, self.toResidenceAndProcessesBigData, self.toDataInventary)
        self.MainWindow.move(600, 100)
        self.ui.setupUi(self.MainWindow)

    def toDataInventary(self):
        self.ui = DataInventary()
        self.ui.setOptionsMenu(
            self.toMenu, self.toProcessesBigData, self.toGraph, self.toSearchByWord,
            self.toDashboard, self.toAllData, self.toResidenceBigData,
            self.toProcessesBigData, self.toResidenceAndProcessesBigData, self.toDataInventary)
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
