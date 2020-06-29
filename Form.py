# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Form.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pyodbc
import logging

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"


class Form(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(829, 686)
        font = QtGui.QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 9, 1, 1, 2)
        self.btnSearch = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btnSearch.sizePolicy().hasHeightForWidth())
        self.btnSearch.setSizePolicy(sizePolicy)
        self.btnSearch.setObjectName("btnSearch")
        self.btnSearch.clicked.connect(self.search)
        self.gridLayout.addWidget(self.btnSearch, 3, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setTitle("")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.radioProcess = QtWidgets.QRadioButton(self.groupBox)
        self.radioProcess.setGeometry(QtCore.QRect(100, 0, 171, 20))
        self.radioProcess.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.radioProcess.setChecked(True)
        self.radioProcess.setObjectName("radioProcess")
        self.radioProcess.clicked.connect(self.setByProcess)
        self.radioName = QtWidgets.QRadioButton(self.groupBox)
        self.radioName.setGeometry(QtCore.QRect(290, 0, 211, 20))
        self.radioName.setObjectName("radioName")
        self.radioName.clicked.connect(self.setByName)
        self.radioDataType = QtWidgets.QRadioButton(self.groupBox)
        self.radioDataType.setGeometry(QtCore.QRect(510, 0, 181, 20))
        self.radioDataType.setObjectName("radioDataType")
        self.radioDataType.clicked.connect(self.setByDataType)
        self.gridLayout.addWidget(self.groupBox, 2, 1, 1, 3)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setOverwriteMode(False)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 4, 1, 4, 2)
        self.btnNext = QtWidgets.QPushButton(self.centralwidget)
        self.btnNext.setObjectName("btnNext")
        self.btnNext.clicked.connect(self.setNext)
        self.gridLayout.addWidget(self.btnNext, 5, 3, 1, 1)
        self.btnBack = QtWidgets.QPushButton(self.centralwidget)
        self.btnBack.setObjectName("btnBack")
        self.btnBack.clicked.connect(self.setBack)
        self.gridLayout.addWidget(self.btnBack, 4, 3, 1, 1)
        self.txtWord = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.txtWord.sizePolicy().hasHeightForWidth())
        self.txtWord.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.txtWord.setFont(font)
        self.txtWord.setObjectName("txtWord")
        self.gridLayout.addWidget(self.txtWord, 3, 1, 1, 2)
        self.btnPolicy = QtWidgets.QPushButton(self.centralwidget)
        self.btnPolicy.setEnabled(False)
        self.btnPolicy.setObjectName("btnPolicy")
        self.gridLayout.addWidget(self.btnPolicy, 6, 3, 1, 1)
        self.lblPagination = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lblPagination.sizePolicy().hasHeightForWidth())
        self.lblPagination.setSizePolicy(sizePolicy)
        self.lblPagination.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPagination.setObjectName("lblPagination")
        self.gridLayout.addWidget(self.lblPagination, 8, 1, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 899, 26))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionInicio = QtWidgets.QAction(MainWindow)
        self.actionInicio.setObjectName("actionInicio")
        if (self.toMenu is not None):
            self.actionInicio.triggered.connect(self.toMenu)
        self.actionConsulta = QtWidgets.QAction(MainWindow)
        self.actionConsulta.setObjectName("actionConsulta")
        if (self.toGraph is not None):
            self.actionConsulta.triggered.connect(self.toGraph)
        self.actionBusqueda = QtWidgets.QAction(MainWindow)
        self.actionBusqueda.setObjectName("actionBusqueda")
        if (self.toSearchByWord is not None):
            self.actionBusqueda.triggered.connect(self.toSearchByWord)
        self.actionDatoRegulado = QtWidgets.QAction(MainWindow)
        self.actionDatoRegulado.setObjectName("actionDatoRegulado")
        if (self.toRegulatedData is not None):
            self.actionDatoRegulado.triggered.connect(self.toRegulatedData)
        self.actionDashboard = QtWidgets.QAction(MainWindow)
        self.actionDashboard.setObjectName("actionDashboard")
        if (self.toDashboard is not None):
            self.actionDashboard.triggered.connect(self.toDashboard)
        self.menuMenu.addAction(self.actionInicio)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionConsulta)
        self.menuMenu.addAction(self.actionBusqueda)
        self.menuMenu.addAction(self.actionDatoRegulado)
        self.menuMenu.addAction(self.actionDashboard)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.MainWindow = MainWindow
        self.startLog()
        self.connectToDb()
        self.setByProcess()
        self.index = 1
        self.limitPagination = 1
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Resultados"))
        self.btnSearch.setText(_translate("MainWindow", "Buscar"))
        self.label.setText(_translate("MainWindow", "Dato"))
        self.radioProcess.setText(_translate("MainWindow", "Uso por Proceso"))
        self.radioName.setText(_translate("MainWindow", "Nombre Dato"))
        self.radioDataType.setText(_translate("MainWindow", "Tipo de dato"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Sin resultados</span></p></body></html>"))
        self.btnNext.setText(_translate("MainWindow", "Siguiente"))
        self.btnBack.setText(_translate("MainWindow", "Anterior"))
        self.btnPolicy.setText(_translate("MainWindow", "Ver política"))
        self.lblPagination.setText(_translate("MainWindow", "de"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionInicio.setText(_translate("MainWindow", "Inicio"))
        self.actionConsulta.setText(_translate("MainWindow", "Gráficas"))
        self.actionBusqueda.setText(_translate("MainWindow", "Búsqueda"))
        self.actionDatoRegulado.setText(
            _translate("MainWindow", "DatoRegulado"))
        self.actionDashboard.setText(_translate("MainWindow", "Dashboard"))

    def setOptionsMenu(self, toMenu, toRegulatedData, toGraph, toSearchByWord, toDashboard):
        self.toMenu = toMenu
        self.toRegulatedData = toRegulatedData
        self.toGraph = toGraph
        self.toSearchByWord = toSearchByWord
        self.toDashboard = toDashboard

    def setByProcess(self):
        query = r"{CALL qryConsultaporTextoListaDatoUsoProceso(?)}"
        headers = ('Clave Proceso', 'Lista Total', 'INAI Gran Dato',
                   'Guia BAUM', 'Tipo de uso', 'Documento',
                   'Tipo de dato', 'Agrupación a Tipo de dato INAI con casu', 'Nivel INAI')
        self.setEnvironment(query, headers)

    def setByName(self):
        query = r"{CALL qryConsultaporTextoenNombreDato(?)}"
        headers = ('Libro', 'Nombre del dato', 'Lista dato',
                   'Gran dato', 'Descripción del dato', 'Tipo de dato',
                   'CDE', 'Dato obligatorio', 'Clasificación',
                   'Fuente de referencia', 'Validaciones', 'Impacto regulatorio',
                   'Impacto sistemas', 'Impacto Negocio', 'Regulación',
                   'Reporte asociado', 'Clasificación')
        self.setEnvironment(query, headers)

    def setByDataType(self):
        query = r"{CALL qryConsultaporTextoenTipodeDato(?)}"
        headers = ('Nombre del dato', 'Libro', 'IdDato',
                   'Fuente de referencia', 'Tipo de dato')
        self.setEnvironment(query, headers)

    def setBack(self):
        if (self.index > 1):
            self.index -= 1
            self.populateTable()

    def setNext(self):
        if (self.index < self.limitPagination):
            self.index += 1
            self.populateTable()

    def setEnvironment(self, query, headers):
        self.query = query
        self.headers = headers

    def connectToDb(self):
        self.logger.info("Connection to DB")
        accessDriver = r'Microsoft Access Driver (*.mdb, *.accdb)'
        filepath = r'./AnaliticaData.accdb'
        self.conn = pyodbc.connect(driver=accessDriver,
                                   dbq=filepath, autocommit=True)
        # cursor = conn.cursor()
        # cursor.execute('select IdDato from UsoLibros')
        # for row in cursor.fetchall():
        #     self.comboBox.addItem(row[0])

    def exec(self, query, values=None):
        self.logger.info("Execute query")
        self.logger.debug("QUERY: {0}".format(query))
        cursor = self.conn.cursor()
        if (values is not None):
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        output = cursor.fetchall()
        cursor.close()
        self.logger.debug("LENGTHDATA: {0}".format(len(output)))
        return output

    def search(self):
        word = self.txtWord.text()
        self.logger.debug("Word: " + word)
        if (word is not None and word != ''):
            self.data = self.exec(self.query, word)
            if (len(self.data) > 0):
                self.index = 1
                self.limitPagination = len(self.data)
                self.populateTable()
        else:
            self.logger.info("Empty word")

    def populateTable(self):
        self.textEdit.setHtml(self.summary(self.data[self.index - 1]))
        self.lblPagination.setText("{0} de {1}".format(
            self.index, self.limitPagination))

    def summary(self, row):
        output = ""
        width = len(self.headers)
        for x in range(width):
            output += "<b>{0}:</b> {1}<br/>".format(self.headers[x], row[x])
        return output

    def startLog(self):
        logging.basicConfig(filename='Lumberjack.log',
                            level=logging.DEBUG, format=LOG_FORMAT)
        self.logger = logging.getLogger()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
