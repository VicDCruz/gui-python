# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ResidenceBigData.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

# from PyQt5 import QtWebEngineWidgets
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
import pyodbc
import logging
import plotly
import plotly.graph_objs as go
import numbers

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

sys.argv.append("--disable-web-security")
path = QtCore.QDir.current().filePath('./plotly-latest.min.js')
local = QtCore.QUrl.fromLocalFile(path).toString()

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

QUERYDROPDOWN = r"""
    SELECT GranDato
    FROM UsoLibros INNER JOIN MasterLibros
    ON UsoLibros.IdDato = MasterLibros.IdDato
    WHERE UsoLibros.Tipo_Linaje = 'Residencia'
    GROUP BY GranDato;
"""


class ResidenceBigData(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btnExpand = QtWidgets.QPushButton(self.centralwidget)
        self.btnExpand.setMinimumSize(QtCore.QSize(350, 0))
        self.btnExpand.setObjectName("btnExpand")
        self.gridLayout.addWidget(self.btnExpand, 2, 1, 1, 1)
        self.btnContract = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btnContract.sizePolicy().hasHeightForWidth())
        self.btnContract.setSizePolicy(sizePolicy)
        self.btnContract.setObjectName("btnContract")
        self.gridLayout.addWidget(self.btnContract, 2, 2, 1, 1)
        self.graph = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.graph.setUrl(QtCore.QUrl("about:blank"))
        self.graph.setObjectName("graph")
        self.gridLayout.addWidget(self.graph, 1, 0, 1, 3)
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
        self.ddlBigData = QtWidgets.QComboBox(self.centralwidget)
        self.ddlBigData.setObjectName("ddlBigData")
        self.gridLayout.addWidget(self.ddlBigData, 0, 1, 1, 2)
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
        self.btnContract.clicked.connect(self.contract)
        self.btnExpand.clicked.connect(self.expand)
        self.populateDropDown()
        self.ddlBigData.currentTextChanged.connect(
            self.populateDashboard)
        self.show()
        self.retranslateUi(MainWindow)
        self.circle = 0
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Residencia de Gran Dato"))
        MainWindow.setWindowIcon(QtGui.QIcon('favicon.ico'))
        self.btnExpand.setText(_translate("MainWindow", "Expandir"))
        self.btnContract.setText(_translate("MainWindow", "Contraer"))
        self.label.setText(_translate("MainWindow", "Gran Dato"))
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
        self.circle = 0
        self.modifyCircles()

    def modifyCircles(self):
        bigdata = self.ddlBigData.currentText()
        if (bigdata != 'Selecciona un dato'):
            if (self.circle >= 0):
                books = self.exec(QUERYBOOKS.format(bigdata))
                parents = [""] + self.getColumn(books, 0)
                names = [bigdata] + self.getColumn(books, 1)
                counts = self.getColumn(books, 2)
                total = self.getTotal(counts)
                values = [total] + counts
                if (self.circle >= 1):
                    tables = self.exec(QUERYTABLES.format(bigdata))
                    parents = parents + self.getColumn(tables, 0)
                    newValues = self.getColumn(tables, 2)
                    if (self.circle == 1):
                        names = names + \
                            self.getPercentages(self.getColumn(
                                tables, 1), newValues, total)
                    else:
                        names = names + self.getColumn(tables, 1)
                    values = values + newValues
                if (self.circle >= 2):
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

    def expand(self):
        if (self.circle < 2):
            self.circle += 1
            self.modifyCircles()

    def contract(self):
        if (self.circle > 0):
            self.circle -= 1
            self.modifyCircles()

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
    ui = ResidenceBigData()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
