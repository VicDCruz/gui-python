# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ResidenceBigData.ui'
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

QUERYDROPDOWN = r"""
    SELECT DISTINCT CatalogoGranDato.NombreGranDato
    FROM CatalogoGranDato, MasterProcesos, UsoProcesos
    WHERE MasterProcesos.ClaveGrandato = CatalogoGranDato.ClaveGracDato
        AND MasterProcesos.ClaveDatoProceso = UsoProcesos.ClaveDatoProceso
"""


class Ui_MainWindow(object):
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

        self.startLog()
        self.connectToDb()
        self.btnContract.clicked.connect(self.contract)
        self.btnExpand.clicked.connect(self.expand)
        self.populateDropDown()
        self.ddlBigData.currentTextChanged.connect(
            self.populateDashboard)
        self.show()
        self.circle = 0
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnExpand.setText(_translate("MainWindow", "Expandir"))
        self.btnContract.setText(_translate("MainWindow", "Contraer"))
        self.label.setText(_translate("MainWindow", "Gran Dato"))

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
        self.circle = 0
        self.modifyCircles()

    def modifyCircles(self):
        bigdata = self.ddlBigData.currentText()
        if (bigdata != 'Selecciona un dato'):
            if (self.circle >= 0):
                processes = self.exec(QUERYPROCESSES.format(bigdata))
                parents = [""] + self.getColumn(processes, 0)
                names = [bigdata] + self.getColumn(processes, 1)
                counts = self.getColumn(processes, 2)
                total = self.getTotal(counts)
                values = [total] + counts
                title = 'Procesos de {0}'.format(bigdata)
                if (self.circle >= 1):
                    tables = self.exec(QUERYSUBPROCESSES.format(bigdata))
                    parents = parents + self.getColumn(tables, 0)
                    newValues = self.getColumn(tables, 2)
                    if (self.circle == 1):
                        names = names + self.getPercentages(self.getColumn(tables, 1), newValues, total)
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
        if (self.circle < 1):
            self.circle += 1
            self.modifyCircles()

    def contract(self):
        if (self.circle > 0):
            self.circle -= 1
            self.modifyCircles()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
