# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\RegulatedData.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pyodbc
import logging

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"


class RegulatedData(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.ddlValues = QtWidgets.QComboBox(self.centralwidget)
        self.ddlValues.setObjectName("ddlValues")
        self.horizontalLayout.addWidget(self.ddlValues)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabInformation = QtWidgets.QWidget()
        self.tabInformation.setObjectName("tabInformation")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tabInformation)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.txtInformation = QtWidgets.QTextEdit(self.tabInformation)
        self.txtInformation.setObjectName("txtInformation")
        self.horizontalLayout_2.addWidget(self.txtInformation)
        self.tabWidget.addTab(self.tabInformation, "")
        self.tabUse = QtWidgets.QWidget()
        self.tabUse.setObjectName("tabUse")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabUse)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.txtUse = QtWidgets.QTableWidget(self.tabUse)
        self.txtUse.setObjectName("txtUse")
        self.txtUse.setColumnCount(0)
        self.txtUse.setRowCount(0)
        self.verticalLayout_2.addWidget(self.txtUse)
        self.tabWidget.addTab(self.tabUse, "")
        self.verticalLayout.addWidget(self.tabWidget)
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

        self.connectToDb()
        self.populateDropDown()
        self.ddlValues.currentTextChanged.connect(self.populateTabs)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Datos regulados"))
        MainWindow.setWindowIcon(QtGui.QIcon('favicon.ico'))
        self.label.setText(_translate("MainWindow", "Valor"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tabInformation), _translate("MainWindow", "Información"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tabUse), _translate("MainWindow", "Uso"))
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

    def populateDropDown(self):
        query = r"select ListaTotal from RegulacionDato"
        data = self.getColumn(self.exec(query), 0)
        data.insert(0, 'Selecciona un dato')
        self.ddlValues.addItems(data)

    def populateTabs(self):
        if ('Selecciona' not in self.ddlValues.currentText()):
            self.getInformation()
            self.getUse()

    def getInformation(self):
        headers = ('Regla de presentación RENAPO', 'Regla de longitud RENAPO', 'Fuente de regulación',
                   'Columna de regulación', 'Objetivo regulatorio PLD',
                   'Regla de distribución para uso de la autoridad PLD',
                   'Regla de presentación de reporte regulatorio PLD',
                   'Tipo de dato PLD', 'Longitud del dato PLD', 'Dato obligatorio',
                   'Regla de captura del dato',
                   'Regla de emisión envio y caracteres del archivo',
                   'Reglas de la nomenclatura de nombre del archivo PLD',
                   'Regla presentación de catálogo de sucursales',
                   'Regla para sujeto obligado PLD',
                   'Incluirlo en reporte relevante PLD',
                   'Incluirlo en reporte inusual PLD',
                   'Incluirlo en reporte relevante PLD',
                   'ID grupo INAI', 'Tipo de dato INAI', 'Descripción del nivel INAI',
                   'Fundamento regulatorio INAI', 'Tratamiento regulatorio INAI',
                   'Derecho regulatorio de las personas INAI',
                   'Sanciones regulatorias INAI', 'Características regulatorias del dato INAI',
                   'Validación regulatoria INAI', 'Dato ley instituciones financieras LIC',
                   'Regla de dato LIC', 'Regla operativa LIC', 'Regla de identificación LIC',
                   'Regla de expediente LIC', 'Regla de resguardo documento digital LIC',
                   'Regla de secreto bancario LIC', 'Reglas de contratación LIC',
                   'Regla de uso de firma electrónica avanzada LIC',
                   'Regla para extranjeros LIC', 'Regla de validación CURP LIC',
                   'Regla de validación canal digital')
        data = self.exec(r"""
            select RegladePresentacionRENAPO, RegladeLongitudRenapo, FuenteRegulatoriaPLD, ColumnaRegulacionLayoutPLD,
            ObjetivoRegulatorioPLD, RegladeDistribucionParaUsodelaAutoridadPLD, RegladePresentaciondeReporteRegulatirioPLD,
            TipodeDatoPLD, LongituddelDatoPLD, DatoObligatorio, RegladeCapturadelDato, RegladeEmisionEnvioycaracteresdelArchivo,
            ReglasdelaNomenclaturadeNombredelArchivoPLD, REGLADEPRESENTACIONDECATALOGODESUCURSALES, REGLAPARASUJETOOBLIGADOPLD,
            INCLUIRLOENREPORTERELEVANTEPLD, INCLUIRLOENREPORTEINUSUALPLD, INCLUIRLOENREPORTEPREOCUPANTEPLD, IDGRUPOINAI,
            TIPODEDATOINAI, DESCRIPCIONDENIVELINAI, FUNDAMIENTOREGULATORIOINAI, TRATAMIENTOREGULATORIOINAI, DERECHOREGULATORIODELASPERSONASINAI,
            SANCIONESREGULATORIASINAI, CARACTERISTICASREGULATORIASDELDATOINAI, VALIDACIONREGULATORIAINAI, DATOLEYINSTITUCIONESFINANCIERAS_LIC,
            REGLADEDATOLIC, REGLAOPERATIVALIC, REGLADEIDENTIFICACIONLIC, REGLADEEXPEDIENTELIC, REGLADERESGUARDODOCUMENTODIGITALLIC,
            REGLADESECRETOBANCARIOLIC, REGLASDECONTRATACIONLIC, REGLADEUSODEFIRMAELECTRONICAAVANZADALIC, REGLAPARAEXTRANJEROSLIC,
            REGLADEVALIDACIONCURPLIC, REGLADEVALIDACIONCANALDIGITAL
            from RegulacionDato
            where ListaTotal = '{0}'
        """.format(self.ddlValues.currentText()))
        self.txtInformation.setHtml(self.summary(headers, data[0]))

    def getUse(self):
        headers = ('Nombre del proceos en libro', 'Clasificación del gran dato', 'Gran dato',
                   'Lista total', 'Uso', 'DoctoFront')
        data = self.exec(r"""
            select super.NombreProcesoLibro, super.ClasificaciondeGranDato,
                super.GranDato, super.ListaTotal, super.Uso, super.DoctoFront
            from SuperConsultaUsos as super
            where ListaTotal = '{0}'
        """.format(self.ddlValues.currentText()))
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
    ui = RegulatedData()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
