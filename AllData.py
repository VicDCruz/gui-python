# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\AllData.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pyodbc
import logging

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

atributes = {
    'LibroProceso': None,
    'NombreProcesoLibro': None,
    'ClasificaciondeGranDato': None,
    'GranDato': None,
    'ListaTotal': None,
    'Uso': None,
    'DoctoFront': None,
    'NombreDatoenDocumento': None
}


class AllData(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.btnClean = QtWidgets.QPushButton(self.centralwidget)
        self.btnClean.setObjectName("btnClean")
        self.gridLayout.addWidget(self.btnClean, 9, 0, 1, 1)

        self.ddlValuesListaTotal = QtWidgets.QComboBox(self.centralwidget)
        self.ddlValuesListaTotal.setObjectName("ddlValuesListaTotal")
        self.gridLayout.addWidget(self.ddlValuesListaTotal, 0, 1, 1, 1)
        self.txtUse = QtWidgets.QTableWidget(self.centralwidget)
        self.txtUse.setObjectName("txtUse")
        self.txtUse.setColumnCount(0)
        self.txtUse.setRowCount(0)
        self.gridLayout.addWidget(self.txtUse, 8, 0, 1, 2)
        self.ddlValuesGranDato = QtWidgets.QComboBox(self.centralwidget)
        self.ddlValuesGranDato.setObjectName("ddlValuesGranDato")
        self.gridLayout.addWidget(self.ddlValuesGranDato, 1, 1, 1, 1)
        self.ddlValuesClasificaciondeGranDato = QtWidgets.QComboBox(
            self.centralwidget)
        self.ddlValuesClasificaciondeGranDato.setObjectName(
            "ddlValuesClasificaciondeGranDato")
        self.gridLayout.addWidget(
            self.ddlValuesClasificaciondeGranDato, 2, 1, 1, 1)
        self.ddlValuesNombreProcesoLibro = QtWidgets.QComboBox(
            self.centralwidget)
        self.ddlValuesNombreProcesoLibro.setObjectName(
            "ddlValuesNombreProcesoLibro")
        self.gridLayout.addWidget(self.ddlValuesNombreProcesoLibro, 3, 1, 1, 1)
        self.ddlValuesLibroProceso = QtWidgets.QComboBox(self.centralwidget)
        self.ddlValuesLibroProceso.setObjectName("ddlValuesLibroProceso")
        self.gridLayout.addWidget(self.ddlValuesLibroProceso, 4, 1, 1, 1)
        self.ddlValuesUso = QtWidgets.QComboBox(self.centralwidget)
        self.ddlValuesUso.setObjectName("ddlValuesUso")
        self.gridLayout.addWidget(self.ddlValuesUso, 5, 1, 1, 1)
        self.ddlValuesDoctoFront = QtWidgets.QComboBox(self.centralwidget)
        self.ddlValuesDoctoFront.setObjectName("ddlValuesDoctoFront")
        self.gridLayout.addWidget(self.ddlValuesDoctoFront, 6, 1, 1, 1)
        self.ddlValuesNombreDatoenDocumento = QtWidgets.QComboBox(
            self.centralwidget)
        self.ddlValuesNombreDatoenDocumento.setObjectName(
            "ddlValuesNombreDatoenDocumento")
        self.gridLayout.addWidget(
            self.ddlValuesNombreDatoenDocumento, 7, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 100, 26))
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
        self.actionDataInventary = QtWidgets.QAction(MainWindow)
        self.actionDataInventary.setObjectName("actionDataInventary")
        self.actionDataInventary.triggered.connect(self.toDataInventary)

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

        self.enableUse = True
        self.lastChange = None
        self.connectToDb()
        self.populateAll()
        self.getUse()
        self.btnClean.clicked.connect(self.cleanAtributes)
        self.ddlValuesLibroProceso.currentTextChanged.connect(
            self.populateTabsLibroProceso)
        self.ddlValuesNombreProcesoLibro.currentTextChanged.connect(
            self.populateTabsNombreProcesoLibro)
        self.ddlValuesClasificaciondeGranDato.currentTextChanged.connect(
            self.populateTabsClasificaciondeGranDato)
        self.ddlValuesGranDato.currentTextChanged.connect(
            self.populateTabsGranDato)
        self.ddlValuesListaTotal.currentTextChanged.connect(
            self.populateTabsListaTotal)
        self.ddlValuesUso.currentTextChanged.connect(self.populateTabsUso)
        self.ddlValuesDoctoFront.currentTextChanged.connect(
            self.populateTabsDoctoFront)
        self.ddlValuesNombreDatoenDocumento.currentTextChanged.connect(
            self.populateTabsNombreDatoenDocumento)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Linaje"))
        MainWindow.setWindowIcon(QtGui.QIcon('favicon.ico'))

        self.btnClean.setText(_translate(
            "MainWindow", "Limpiar búsqueda"))

        self.label_5.setText(_translate("MainWindow", "Libro Proceso"))
        self.label_6.setText(_translate("MainWindow", "Uso"))
        self.label_7.setText(_translate("MainWindow", "Documento o Aplicativo"))
        self.label_8.setText(_translate(
            "MainWindow", "Nombre Dato en Documento"))
        self.label_2.setText(_translate("MainWindow", "Gran Dato"))
        self.label_3.setText(_translate(
            "MainWindow", "Clasificación de gran dato"))
        self.label_4.setText(_translate("MainWindow", "Nombre Proceso libro"))
        self.label.setText(_translate("MainWindow", "Lista total"))
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

    def connectToDb(self):
        accessDriver = r'Microsoft Access Driver (*.mdb, *.accdb)'
        filepath = r'./AnaliticaData.accdb'
        self.conn = pyodbc.connect(driver=accessDriver,
                                   dbq=filepath, autocommit=True)

    def exec(self, query, values=None):
        cursor = self.conn.cursor()
        if (values is not None):
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        output = cursor.fetchall()
        cursor.close()
        return output

    def getColumn(self, data, column):
        output = []
        for element in data:
            output.append(element[column])
        return output

    def populateDdl(self, atribute):
        wheres = self.getWheres()
        addAND = ''
        if wheres != '':
            addAND = 'AND'
        query = r"select distinct {0} from SuperConsultaUsos where {0} <> '' {1} {2}".format(
            atribute, addAND, wheres)
        data = self.getColumn(self.exec(query), 0)
        data.insert(0, 'Selecciona un dato')
        return data

    def populateAll(self):
        if self.lastChange != 'LibroProceso' and atributes['LibroProceso'] is None:
            self.ddlValuesLibroProceso.clear()
            self.ddlValuesLibroProceso.addItems(
                self.populateDdl('LibroProceso'))
        if self.lastChange != 'NombreProcesoLibro' and atributes['NombreProcesoLibro'] is None:
            self.ddlValuesNombreProcesoLibro.clear()
            self.ddlValuesNombreProcesoLibro.addItems(
                self.populateDdl('NombreProcesoLibro'))
        if self.lastChange != 'ClasificaciondeGranDato' and atributes['ClasificaciondeGranDato'] is None:
            self.ddlValuesClasificaciondeGranDato.clear()
            self.ddlValuesClasificaciondeGranDato.addItems(
                self.populateDdl('ClasificaciondeGranDato'))
        if self.lastChange != 'GranDato' and atributes['GranDato'] is None:
            self.ddlValuesGranDato.clear()
            self.ddlValuesGranDato.addItems(self.populateDdl('GranDato'))
        if self.lastChange != 'ListaTotal' and atributes['ListaTotal'] is None:
            self.ddlValuesListaTotal.clear()
            self.ddlValuesListaTotal.addItems(self.populateDdl('ListaTotal'))
        if self.lastChange != 'Uso' and atributes['Uso'] is None:
            self.ddlValuesUso.clear()
            self.ddlValuesUso.addItems(self.populateDdl('Uso'))
        if self.lastChange != 'DoctoFront' and atributes['DoctoFront'] is None:
            self.ddlValuesDoctoFront.clear()
            self.ddlValuesDoctoFront.addItems(self.populateDdl('DoctoFront'))
        if self.lastChange != 'NombreDatoenDocumento' and atributes['NombreDatoenDocumento'] is None:
            self.ddlValuesNombreDatoenDocumento.clear()
            self.ddlValuesNombreDatoenDocumento.addItems(
                self.populateDdl('NombreDatoenDocumento'))

    def cleanAtributes(self):
        for key in atributes:
            atributes[key] = None
        self.enableUse = False
        self.txtUse.setRowCount(0)
        self.lastChange = None
        self.populateAll()
        for key in atributes:
            atributes[key] = None
        self.lastChange = None
        self.enableUse = True
        self.getUse()

    def populateTabs(self):
        if self.enableUse:
            self.populateAll()
            self.getUse()

    def populateTabsLibroProceso(self):
        atributes['LibroProceso'] = self.ddlValuesLibroProceso.currentText()
        self.lastChange = 'LibroProceso'
        self.populateTabs()

    def populateTabsNombreProcesoLibro(self):
        atributes['NombreProcesoLibro'] = self.ddlValuesNombreProcesoLibro.currentText()
        self.lastChange = 'NombreProcesoLibro'
        self.populateTabs()

    def populateTabsClasificaciondeGranDato(self):
        atributes['ClasificaciondeGranDato'] = self.ddlValuesClasificaciondeGranDato.currentText()
        self.lastChange = 'ClasificaciondeGranDato'
        self.populateTabs()

    def populateTabsGranDato(self):
        atributes['GranDato'] = self.ddlValuesGranDato.currentText()
        self.lastChange = 'GranDato'
        self.populateTabs()

    def populateTabsListaTotal(self):
        atributes['ListaTotal'] = self.ddlValuesListaTotal.currentText()
        self.lastChange = 'ListaTotal'
        self.populateTabs()

    def populateTabsUso(self):
        atributes['Uso'] = self.ddlValuesUso.currentText()
        self.lastChange = 'Uso'
        self.populateTabs()

    def populateTabsDoctoFront(self):
        atributes['DoctoFront'] = self.ddlValuesDoctoFront.currentText()
        self.lastChange = 'DoctoFront'
        self.populateTabs()

    def populateTabsNombreDatoenDocumento(self):
        atributes['NombreDatoenDocumento'] = self.ddlValuesNombreDatoenDocumento.currentText()
        self.lastChange = 'NombreDatoenDocumento'
        self.populateTabs()

    def getWheres(self):
        output = ''
        for key in atributes:
            element = atributes[key]
            if element != 'Selecciona un dato' and element is not None and element != '':
                output += key + '=' + "'" + element + "' AND "
        return output[:-5]

    def getUse(self):
        headers = ('Libro de Procesos', 'Nombre del proceos en libro', 'Clasificación del gran dato', 'Gran dato',
                   'Lista total', 'Uso', 'Documento o Aplicativo', 'Nombre del dato en Documento')
        wheres = self.getWheres()
        addWhere = "WHERE"
        if (wheres == ''):
            addWhere = ''
        data = self.exec(r"""
            select LibroProceso, NombreProcesoLibro, ClasificaciondeGranDato,
                GranDato, ListaTotal, Uso, DoctoFront, NombreDatoenDocumento
            from SuperConsultaUsos
            {1} {0}
        """.format(self.getWheres(), addWhere))
        self.txtUse.setRowCount(len(data))
        self.txtUse.setColumnCount(len(headers))
        self.txtUse.setHorizontalHeaderLabels(headers)
        for i in range(len(headers)):
            for j in range(len(data)):
                self.txtUse.setItem(
                    j, i, QtWidgets.QTableWidgetItem(data[j][i]))

    def summary(self, headers, row):
        output = ""
        width = len(headers)
        for x in range(width):
            output += "<b>{0}:</b> {1}<br/>".format(headers[x], row[x])
        return output

    def setOptionsMenu(self, toMenu, toRegulatedData, toGraph, toSearchByWord,
                       toDashboard, toAllData, toResidenceBigData,
                       toProcessesBigData, toResidenceAndProcessesBigData,
                       toDataInventary):
        self.toMenu = toMenu
        self.toRegulatedData = toRegulatedData
        self.toGraph = toGraph
        self.toSearchByWord = toSearchByWord
        self.toDashboard = toDashboard
        self.toAllData = toAllData
        self.toResidenceBigData = toResidenceBigData
        self.toProcessesBigData = toProcessesBigData
        self.toResidenceAndProcessesBigData = toResidenceAndProcessesBigData
        self.toDataInventary = toDataInventary


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = AllData()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
