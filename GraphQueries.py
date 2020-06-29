# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\graphs-queries.ui'
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

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

sys.argv.append("--disable-web-security")
path = QtCore.QDir.current().filePath('./plotly-latest.min.js')
local = QtCore.QUrl.fromLocalFile(path).toString()


class GraphQueries(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(899, 686)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.btnAll = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btnAll.sizePolicy().hasHeightForWidth())
        self.btnAll.setSizePolicy(sizePolicy)
        self.btnAll.setObjectName("btnAll")
        self.gridLayout.addWidget(self.btnAll, 2, 4, 1, 1)
        self.btnBooks = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btnBooks.sizePolicy().hasHeightForWidth())
        self.btnBooks.setSizePolicy(sizePolicy)
        self.btnBooks.setObjectName("btnBooks")
        self.gridLayout.addWidget(self.btnBooks, 2, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 2, 1, 1, 1)
        self.btnProcesses = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btnProcesses.sizePolicy().hasHeightForWidth())
        self.btnProcesses.setSizePolicy(sizePolicy)
        self.btnProcesses.setObjectName("btnProcesses")
        self.gridLayout.addWidget(self.btnProcesses, 2, 2, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 3, 1, 1)
        self.btnExpand = QtWidgets.QPushButton(self.centralwidget)
        self.btnExpand.setObjectName("btnExpand")
        self.gridLayout.addWidget(self.btnExpand, 6, 0, 1, 1)
        self.btnContract = QtWidgets.QPushButton(self.centralwidget)
        self.btnContract.setObjectName("btnContract")
        self.gridLayout.addWidget(self.btnContract, 6, 2, 1, 1)
        self.view = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        # self.view.setUrl(QtCore.QUrl("about:blank"))
        self.view.setObjectName("view")
        self.gridLayout.addWidget(self.view, 4, 0, 2, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 899, 26))
        self.menubar.setObjectName("menubar")
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
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

        self.btnBooks.clicked.connect(self.setByBooks)
        self.btnProcesses.clicked.connect(self.setByProcesses)
        self.btnAll.clicked.connect(self.setByAll)
        self.btnExpand.setEnabled(False)
        self.btnContract.setEnabled(False)
        self.btnExpand.clicked.connect(self.showExpand)
        self.btnContract.clicked.connect(self.showContract)
        self.startLog()
        self.connectToDb()
        self.show()
        self.graphType = None
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.MainWindow = MainWindow

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Consultas"))
        self.btnAll.setText(_translate("MainWindow", "Todos"))
        self.btnBooks.setText(_translate("MainWindow", "Libros"))
        self.btnProcesses.setText(_translate("MainWindow", "Procesos"))
        self.btnExpand.setText(_translate("MainWindow", "Expandir"))
        self.btnContract.setText(_translate("MainWindow", "Contraer"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionInicio.setText(_translate("MainWindow", "Inicio"))
        self.actionConsulta.setText(_translate("MainWindow", "Gráficas"))
        self.actionBusqueda.setText(_translate("MainWindow", "Búsqueda"))
        self.actionDatoRegulado.setText(
            _translate("MainWindow", "DatoRegulado"))
        self.actionDashboard.setText(_translate("MainWindow", "Dashboard"))

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

    def setByBooks(self):
        self.logger.info("By BOOKS")
        self.btnExpand.setEnabled(False)
        self.btnContract.setEnabled(False)
        data = self.exec(r"{CALL qryResumenUsoGranDatoLibros()}")
        if (len(data) > 0):
            x = self.getColumn(data, 0)
            columns = ("C360", "CU", "DIGIT", "MOCPr", "MtBiom")
            for i in range(len(columns)):
                column = columns[i]
                if (i == 0):
                    fig = go.Figure(
                        go.Bar(x=x, y=self.getColumn(data, i + 2), name=column))
                else:
                    fig.add_trace(
                        go.Bar(x=x, y=self.getColumn(data, i + 2), name=column))
            fig.update_layout(barmode='stack', xaxis={
                              'categoryorder': 'category ascending'})
            self.show(fig, "Vista por libros")

    def setByProcesses(self):
        self.logger.info("By Process")
        self.btnExpand.setEnabled(True)
        self.btnContract.setEnabled(True)
        self.dataChildren = self.exec(
            r"select GranDato, ListaDato, count(*) from MasterLibros group by GranDato, ListaDato;")
        self.dataParents = self.exec(
            r"select GranDato, count(*) from MasterLibros group by GranDato;")
        total = self.exec(r"select count(*) from MasterLibros")
        self.total = total[0][0]
        self.title = "Vista por procesos"
        self.showContract()

    def setByAll(self):
        self.logger.info("By All")
        self.btnExpand.setEnabled(True)
        self.btnContract.setEnabled(True)
        self.dataChildren = self.exec(r"""
                SELECT x.GranDato, x.Libro_Proceso, COUNT(*) 
                FROM qryUnionLibrosyProcesosMaster as x 
                GROUP BY GranDato, Libro_Proceso;
            """)
        self.dataParents = self.exec(
            r"SELECT x.GranDato, COUNT(*) FROM qryUnionLibrosyProcesosMaster as x GROUP BY GranDato;")
        total = self.exec(
            r"SELECT COUNT(*) FROM qryUnionLibrosyProcesosMaster;")
        self.total = total[0][0]
        self.title = "Vista por libros y procesos"
        self.showContract()

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
        self.view.setHtml(raw_html)
        self.view.show()

    def showExpand(self):
        labels = [str(self.total)]
        parents = [""]
        values = [self.total]
        for parent in self.dataParents:
            labels.append(parent[0])
            parents.append(str(self.total))
            values.append(parent[1])
        for child in self.dataChildren:
            totalParent = values[labels.index(child[0])]
            labels.append("{0}\n{1:.2f} %".format(
                child[1], child[2] / totalParent * 100))
            parents.append(child[0])
            values.append(child[2])
        fig = go.Figure(go.Sunburst(
            labels=labels,
            parents=parents,
            values=values,
            branchvalues="total",
        ))
        self.show(fig, self.title)

    def showContract(self):
        labels = [str(self.total)]
        parents = [""]
        values = [self.total]
        for parent in self.dataParents:
            labels.append(parent[0])
            parents.append(str(self.total))
            values.append(parent[1])
        fig = go.Figure(go.Sunburst(
            labels=labels,
            parents=parents,
            values=values,
            branchvalues="total",
        ))
        self.show(fig, self.title)

    def setOptionsMenu(self, toMenu, toRegulatedData, toGraph, toSearchByWord, toDashboard):
        self.toMenu = toMenu
        self.toRegulatedData = toRegulatedData
        self.toGraph = toGraph
        self.toSearchByWord = toSearchByWord
        self.toDashboard = toDashboard


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GraphQueries()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
