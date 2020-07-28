# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\DataInventary.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

# from PyQt5 import QtWebEngineWidgets
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
import pyodbc
import logging
import plotly
import plotly.graph_objs as go
import sys

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
sys.argv.append("--disable-web-security")
path = QtCore.QDir.current().filePath('./plotly-latest.min.js')
local = QtCore.QUrl.fromLocalFile(path).toString()


class DataInventary(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
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
        self.gridLayout.addWidget(self.btnClean, 2, 0, 1, 1)

        self.ddlValues = QtWidgets.QComboBox(self.centralwidget)
        self.ddlValues.setObjectName("ddlValues")
        self.gridLayout.addWidget(self.ddlValues, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txtUse = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.txtUse.sizePolicy().hasHeightForWidth())
        self.txtUse.setSizePolicy(sizePolicy)
        self.txtUse.setObjectName("txtUse")
        self.txtUse.setColumnCount(0)
        self.txtUse.setRowCount(0)
        self.horizontalLayout.addWidget(self.txtUse)
        self.graph = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.graph.sizePolicy().hasHeightForWidth())
        self.graph.setSizePolicy(sizePolicy)
        self.graph.setUrl(QtCore.QUrl("about:blank"))
        self.graph.setObjectName("graph")
        self.horizontalLayout.addWidget(self.graph)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 2)
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

        self.startLog()
        self.connectToDb()
        self.populateAll()
        self.btnClean.clicked.connect(self.cleanAtributes)
        self.ddlValues.currentTextChanged.connect(self.getUse)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Inventario de datos"))
        MainWindow.setWindowIcon(QtGui.QIcon('favicon.ico'))

        self.btnClean.setText(_translate(
            "MainWindow", "Limpiar búsqueda"))

        self.label.setText(_translate("MainWindow", "Procesos o Libros"))
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

    def getColumn(self, data, column):
        output = []
        for element in data:
            output.append(element[column])
        return output

    def populateDdl(self, atribute):
        query = r"""
        SELECT DISTINCT SuperConsultaUsos.NombreProcesoLibro
        FROM SuperConsultaUsos
        GROUP BY SuperConsultaUsos.LibroProceso, SuperConsultaUsos.NombreProcesoLibro, SuperConsultaUsos.GranDato;
        """
        data = self.getColumn(self.exec(query), 0)
        data.insert(0, 'Todos')
        data.insert(0, 'Selecciona un dato')
        return data

    def populateAll(self):
        self.ddlValues.clear()
        self.ddlValues.addItems(self.populateDdl('ListaTotal'))

    def cleanAtributes(self):
        self.txtUse.setRowCount(0)
        self.populateAll()

    def getUse(self):
        headers = ('Libro o Procesos', 'Nombre del proceos o libro',
                   'Gran dato', 'Total')
        query = r"""
                SELECT SuperConsultaUsos.LibroProceso, SuperConsultaUsos.NombreProcesoLibro, 
                        SuperConsultaUsos.GranDato, Count(SuperConsultaUsos.ListaTotal)
                FROM SuperConsultaUsos
                where NombreProcesoLibro = '{0}'
                GROUP BY SuperConsultaUsos.LibroProceso, SuperConsultaUsos.NombreProcesoLibro, SuperConsultaUsos.GranDato
            """.format(self.ddlValues.currentText())
        if (self.ddlValues.currentText() == 'Todos'):
            headers = ('Gran dato', 'Total')
            query = r"""
                    SELECT GranDato, Count(ListaTotal)
                    FROM SuperConsultaUsos
                    WHERE GranDato <> ''
                    GROUP BY GranDato
                """.format(self.ddlValues.currentText())
        data = self.exec(query)
        self.txtUse.setRowCount(len(data))
        self.txtUse.setColumnCount(len(headers))
        self.txtUse.setHorizontalHeaderLabels(headers)
        for i in range(len(headers)):
            for j in range(len(data)):
                self.txtUse.setItem(
                    j, i, QtWidgets.QTableWidgetItem(str(data[j][i])))
        self.displayPie()

    def summary(self, headers, row):
        output = ""
        width = len(headers)
        for x in range(width):
            output += "<b>{0}:</b> {1}<br/>".format(headers[x], row[x])
        return output

    def displayPie(self):
        query = r"""
            SELECT SuperConsultaUsos.GranDato, Count(SuperConsultaUsos.ListaTotal)
            FROM SuperConsultaUsos
            where NombreProcesoLibro = '{0}'
            GROUP BY SuperConsultaUsos.LibroProceso, SuperConsultaUsos.NombreProcesoLibro, SuperConsultaUsos.GranDato
        """.format(self.ddlValues.currentText())
        if (self.ddlValues.currentText() == 'Todos'):
            query = r"""
                SELECT SuperConsultaUsos.GranDato, Count(SuperConsultaUsos.ListaTotal)
                FROM SuperConsultaUsos
                WHERE GranDato <> ''
                GROUP BY SuperConsultaUsos.GranDato
            """.format(self.ddlValues.currentText())
        data = self.exec(query)
        fig = go.Figure(go.Pie(
            labels=self.getColumn(data, 0),
            values=self.getColumn(data, 1),
        ))
        self.show(fig, "Consulta en pie")

    def show(self, fig=None, title=""):
        raw_html = '<html><head><meta charset="utf-8" />'
        raw_html += '<script src="{}"></script></head>'.format(local)
        raw_html += '<body>'
        if (fig is not None):
            margin = dict(l=0, r=0, t=25)
            if (title != ""):
                fig.update_layout(margin=margin, title_text=title)
            else:
                fig.update_layout(margin=margin)
            raw_html += plotly.offline.plot(fig,
                                            include_plotlyjs=False, output_type='div')
        raw_html += '</body></html>'
        self.graph.setHtml(raw_html)
        self.graph.show()

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
    ui = DataInventary()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
