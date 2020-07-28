# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ResidenceAndProcessesBigData.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWebEngineWidgets
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import pyodbc
import logging
import plotly
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import numbers

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

sys.argv.append("--disable-web-security")
path = QtCore.QDir.current().filePath('./plotly-latest.min.js')
local = QtCore.QUrl.fromLocalFile(path).toString()

QUERYPROCESSES = r"""
    SELECT CatalogoGranDato.NombreGranDato, CarLibrosyProcesos.NombreProcesoLibro, COUNT(*)
    FROM CatalogoGranDato, MasterProcesos, UsoProcesos, CarLibrosyProcesos
    WHERE CatalogoGranDato.NombreGranDato = '{0}'
        AND MasterProcesos.ClaveGrandato = CatalogoGranDato.ClaveGracDato
        AND MasterProcesos.ClaveDatoProceso = UsoProcesos.ClaveDatoProceso
        AND MasterProcesos.ClaveProceso = CarLibrosyProcesos.ClaveProcesoLibro
    GROUP BY CatalogoGranDato.NombreGranDato, CarLibrosyProcesos.NombreProcesoLibro
"""

QUERYSUBPROCESSES = r"""
    SELECT CarLibrosyProcesos.NombreProcesoLibro,
        UsoProcesos.Documento + '<br>' + CarLibrosyProcesos.NombreProcesoLibro,
        COUNT(*)
    FROM CatalogoGranDato, MasterProcesos, UsoProcesos, CarLibrosyProcesos
    WHERE CatalogoGranDato.NombreGranDato = '{0}'
        AND MasterProcesos.ClaveGrandato = CatalogoGranDato.ClaveGracDato
        AND MasterProcesos.ClaveDatoProceso = UsoProcesos.ClaveDatoProceso
        AND MasterProcesos.ClaveProceso = CarLibrosyProcesos.ClaveProcesoLibro
    GROUP BY CatalogoGranDato.NombreGranDato,  CarLibrosyProcesos.NombreProcesoLibro, UsoProcesos.Documento
"""

QUERYBOOKS = r"""
    SELECT GranDato, CarLibrosyProcesos.NombreProcesoLibro, COUNT(*)
    FROM CarLibrosyProcesos, UsoLibros INNER JOIN MasterLibros
    ON UsoLibros.IdDato = MasterLibros.IdDato
    WHERE UsoLibros.Tipo_Linaje = 'Residencia'
    AND GranDato = '{0}'
    AND UsoLibros.Libro <> 'MOCPr'
    AND UsoLibros.Libro = CarLibrosyProcesos.ClaveProcesoLibro
    GROUP BY GranDato, CarLibrosyProcesos.NombreProcesoLibro;
"""

QUERYTABLES = r"""

    SELECT CarLibrosyProcesos.NombreProcesoLibro, IIF(ISNULL(Tabla), 'Nulo', Tabla) + '<br>' + CarLibrosyProcesos.NombreProcesoLibro, COUNT(*)
    FROM CarLibrosyProcesos, UsoLibros INNER JOIN MasterLibros
    ON UsoLibros.IdDato = MasterLibros.IdDato
    WHERE UsoLibros.Tipo_Linaje = 'Residencia'
    AND GranDato = '{0}'
    AND UsoLibros.Libro <> 'MOCPr'
    AND UsoLibros.Libro = CarLibrosyProcesos.ClaveProcesoLibro
    GROUP BY GranDato, CarLibrosyProcesos.NombreProcesoLibro, Tabla;
"""

QUERYFIELDS = r"""
    SELECT IIF(ISNULL(Tabla), 'Nulo', Tabla) + '<br>' + CarLibrosyProcesos.NombreProcesoLibro,
    IIF(ISNULL(Campo), 'Nulo', Campo) + '<br>'
        + IIF(ISNULL(Tabla), 'Nulo', Tabla) + '<br>'
        + CarLibrosyProcesos.NombreProcesoLibro, COUNT(*)
    FROM CarLibrosyProcesos, UsoLibros INNER JOIN MasterLibros
    ON UsoLibros.IdDato = MasterLibros.IdDato
    WHERE UsoLibros.Tipo_Linaje = 'Residencia'
    AND GranDato = '{0}'
    AND UsoLibros.Libro <> 'MOCPr'
    AND UsoLibros.Libro = CarLibrosyProcesos.ClaveProcesoLibro
    GROUP BY GranDato, CarLibrosyProcesos.NombreProcesoLibro, Tabla, Campo;
"""

# TODO: Union entre Procesos y Libros
QUERYDROPDOWN = r"""
    SELECT DISTINCT CatalogoGranDato.NombreGranDato
    FROM CatalogoGranDato, MasterProcesos, UsoProcesos
    WHERE MasterProcesos.ClaveGrandato = CatalogoGranDato.ClaveGracDato
        AND MasterProcesos.ClaveDatoProceso = UsoProcesos.ClaveDatoProceso
"""


class ResidenceAndProcessesBigData(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btnExpandProcesses = QtWidgets.QPushButton(self.centralwidget)
        self.btnExpandProcesses.setMinimumSize(QtCore.QSize(350, 0))
        self.btnExpandProcesses.setObjectName("btnExpandProcesses")
        self.gridLayout.addWidget(self.btnExpandProcesses, 2, 1, 1, 1)
        self.btnContractProcesses = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btnContractProcesses.sizePolicy().hasHeightForWidth())
        self.btnContractProcesses.setSizePolicy(sizePolicy)
        self.btnContractProcesses.setObjectName("btnContractProcesses")
        self.gridLayout.addWidget(self.btnContractProcesses, 2, 2, 1, 1)
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
        self.graph = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.graph.setUrl(QtCore.QUrl("about:blank"))
        self.graph.setObjectName("graph")
        self.gridLayout.addWidget(self.graph, 1, 0, 1, 3)
        self.ddlBigData = QtWidgets.QComboBox(self.centralwidget)
        self.ddlBigData.setObjectName("ddlBigData")
        self.gridLayout.addWidget(self.ddlBigData, 0, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.btnExpandBooks = QtWidgets.QPushButton(self.centralwidget)
        self.btnExpandBooks.setObjectName("btnExpandBooks")
        self.gridLayout.addWidget(self.btnExpandBooks, 3, 1, 1, 1)
        self.btnContractBooks = QtWidgets.QPushButton(self.centralwidget)
        self.btnContractBooks.setObjectName("btnContractBooks")
        self.gridLayout.addWidget(self.btnContractBooks, 3, 2, 1, 1)
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

        self.startLog()
        self.connectToDb()
        self.btnContractProcesses.clicked.connect(self.contractProcesses)
        self.btnExpandProcesses.clicked.connect(self.expandProcesses)
        self.btnContractBooks.clicked.connect(self.contractBooks)
        self.btnExpandBooks.clicked.connect(self.expandBooks)
        self.populateDropDown()
        self.ddlBigData.currentTextChanged.connect(
            self.populateDashboard)
        self.show()
        self.circleProcesses = 0
        self.circleBooks = 0
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Procesos y residencia de Gran Dato"))
        MainWindow.setWindowIcon(QtGui.QIcon('favicon.ico'))
        self.btnExpandProcesses.setText(_translate("MainWindow", "Expandir"))
        self.btnContractProcesses.setText(_translate("MainWindow", "Contraer"))
        self.label.setText(_translate("MainWindow", "Gran dato"))
        self.label_2.setText(_translate("MainWindow", "Procesos"))
        self.label_3.setText(_translate("MainWindow", "Libros"))
        self.btnExpandBooks.setText(_translate("MainWindow", "Expandir"))
        self.btnContractBooks.setText(_translate("MainWindow", "Contraer"))
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
        self.logger.info("Connection to DB")
        accessDriver = r'Microsoft Access Driver (*.mdb, *.accdb)'
        filepath = r'./AnaliticaData.accdb'
        self.conn = pyodbc.connect(driver=accessDriver,
                                   dbq=filepath, autocommit=True)

    def startLog(self):
        logging.basicConfig(filename='Lumberjack.log',
                            level=logging.DEBUG, format=LOG_FORMAT)
        self.logger = logging.getLogger()

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

    def show(self, fig=None, title=""):
        raw_html = '<html><head><meta charset="utf-8" />'
        raw_html += '<script src="{}"></script></head>'.format(local)
        raw_html += '<body>'
        if (fig is not None):
            margin = dict(t=25, l=0, r=0, b=0)
            if (title != ""):
                fig.update_layout(margin=margin, title_text=title)
            else:
                fig.update_layout(margin=margin)
            raw_html += plotly.offline.plot(fig,
                                            include_plotlyjs=False, output_type='div')
        raw_html += '</body></html>'
        self.graph.setHtml(raw_html)
        self.graph.show()

    def getColumn(self, data, column):
        output = []
        for element in data:
            value = element[column]
            output.append(value)
        return output

    def populateDashboard(self):
        self.circleProcesses = 0
        self.circleBooks = 0
        self.modifyCircles()

    def modifyCircles(self):
        bigdata = self.ddlBigData.currentText()
        if (bigdata != 'Selecciona un dato'):
            fig = make_subplots(rows=1, cols=2, specs=[
                [{'type': 'domain'}, {'type': 'domain'}]])
            title = 'Procesos y libros de {0}'.format(bigdata)
            if (self.circleProcesses >= 0):
                processes = self.exec(QUERYPROCESSES.format(bigdata))
                parents = [""] + self.getColumn(processes, 0)
                names = [bigdata] + self.getColumn(processes, 1)
                counts = self.getColumn(processes, 2)
                total = self.getTotal(counts)
                values = [total] + counts
                if (self.circleProcesses >= 1):
                    tables = self.exec(QUERYSUBPROCESSES.format(bigdata))
                    parents = parents + self.getColumn(tables, 0)
                    newValues = self.getColumn(tables, 2)
                    if (self.circleProcesses == 1):
                        names = names + \
                            self.getPercentages(self.getColumn(
                                tables, 1), newValues, total)
                    else:
                        names = names + self.getColumn(tables, 1)
                    values = values + newValues
                fig.add_trace(go.Sunburst(
                    labels=names,
                    parents=parents,
                    values=values,
                    branchvalues="total",
                ), 1, 1)
            bigdata = self.ddlBigData.currentText()
            if (self.circleBooks >= 0):
                books = self.exec(QUERYBOOKS.format(bigdata))
                parents = [""] + self.getColumn(books, 0)
                names = [bigdata] + self.getColumn(books, 1)
                counts = self.getColumn(books, 2)
                total = self.getTotal(counts)
                values = [total] + counts
                if (self.circleBooks >= 1):
                    tables = self.exec(QUERYTABLES.format(bigdata))
                    parents = parents + self.getColumn(tables, 0)
                    newValues = self.getColumn(tables, 2)
                    if (self.circleBooks == 1):
                        names = names + \
                            self.getPercentages(self.getColumn(
                                tables, 1), newValues, total)
                    else:
                        names = names + self.getColumn(tables, 1)
                    values = values + newValues
                if (self.circleBooks >= 2):
                    fields = self.exec(QUERYFIELDS.format(bigdata))
                    parents = parents + self.getColumn(fields, 0)
                    newValues = self.getColumn(fields, 2)
                    names = names + \
                        self.getPercentages(self.getColumn(
                            fields, 1), newValues, total)
                    values = values + newValues
                fig.add_trace(go.Sunburst(
                    labels=names,
                    parents=parents,
                    values=values,
                    branchvalues="total",
                ), 1, 2)
            self.show(fig, title)

    def modifyCirclesProcesses(self):
        bigdata = self.ddlBigData.currentText()
        if (bigdata != 'Selecciona un dato'):
            if (self.circleProcesses >= 0):
                processes = self.exec(QUERYPROCESSES.format(bigdata))
                parents = [""] + self.getColumn(processes, 0)
                names = [bigdata] + self.getColumn(processes, 1)
                counts = self.getColumn(processes, 2)
                total = self.getTotal(counts)
                values = [total] + counts
                title = 'Procesos de {0}'.format(bigdata)
                if (self.circleProcesses >= 1):
                    tables = self.exec(QUERYSUBPROCESSES.format(bigdata))
                    parents = parents + self.getColumn(tables, 0)
                    newValues = self.getColumn(tables, 2)
                    if (self.circleProcesses == 1):
                        names = names + \
                            self.getPercentages(self.getColumn(
                                tables, 1), newValues, total)
                    else:
                        names = names + self.getColumn(tables, 1)
                    values = values + newValues
                    title = 'Procesos y documentos de {0}'.format(bigdata)
                fig = go.Figure(go.Sunburst(
                    labels=names,
                    parents=parents,
                    values=values,
                    branchvalues="total",
                ))
                self.show(fig, title)

    def modifyCirclesBooks(self):
        bigdata = self.ddlBigData.currentText()
        if (bigdata != 'Selecciona un dato'):
            if (self.circleBooks >= 0):
                books = self.exec(QUERYBOOKS.format(bigdata))
                parents = [""] + self.getColumn(books, 0)
                names = [bigdata] + self.getColumn(books, 1)
                counts = self.getColumn(books, 2)
                total = self.getTotal(counts)
                values = [total] + counts
                if (self.circleBooks >= 1):
                    tables = self.exec(QUERYTABLES.format(bigdata))
                    parents = parents + self.getColumn(tables, 0)
                    newValues = self.getColumn(tables, 2)
                    if (self.circleBooks == 1):
                        names = names + \
                            self.getPercentages(self.getColumn(
                                tables, 1), newValues, total)
                    else:
                        names = names + self.getColumn(tables, 1)
                    values = values + newValues
                if (self.circleBooks >= 2):
                    fields = self.exec(QUERYFIELDS.format(bigdata))
                    parents = parents + self.getColumn(fields, 0)
                    newValues = self.getColumn(fields, 2)
                    names = names + \
                        self.getPercentages(self.getColumn(
                            fields, 1), newValues, total)
                    values = values + newValues
                fig = go.Figure(go.Sunburst(
                    labels=names,
                    parents=parents,
                    values=values,
                    branchvalues="total",
                ))
                self.show(fig, 'Residencia de {0}'.format(bigdata))

    def getTotal(self, a):
        output = 0
        for element in a:
            output += element
        return output

    def getPercentages(self, names, values, total):
        count = 0
        for value in values:
            names[count] += "<br>{:.1f} %".format(value / total * 100)
            count += 1
        return names

    def populateDropDown(self):
        data = self.getColumn(self.exec(QUERYDROPDOWN), 0)
        data.insert(0, 'Selecciona un dato')
        self.ddlBigData.addItems(data)

    def expandProcesses(self):
        if (self.circleProcesses < 1):
            self.circleProcesses += 1
            self.modifyCirclesProcesses()

    def contractProcesses(self):
        if (self.circleProcesses > 0):
            self.circleProcesses -= 1
            self.modifyCirclesProcesses()

    def expandBooks(self):
        if (self.circleBooks < 2):
            self.circleBooks += 1
            self.modifyCirclesBooks()

    def contractBooks(self):
        if (self.circleBooks > 0):
            self.circleBooks -= 1
            self.modifyCirclesBooks()

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
    ui = ResidenceAndProcessesBigData()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
