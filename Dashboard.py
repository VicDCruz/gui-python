# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWebEngineWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
import pyodbc
import logging
import plotly
import plotly.graph_objs as go
import sys

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
sys.argv.append("--disable-web-security")
path = QtCore.QDir.current().filePath('./plotly-latest.min.js')
local = QtCore.QUrl.fromLocalFile(path).toString()


class Dashboard(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(841, 840)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 100))
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
        self.ddlNameProcessBook = QtWidgets.QComboBox(self.centralwidget)
        self.ddlNameProcessBook.setObjectName("ddlNameProcessBook")
        self.gridLayout.addWidget(self.ddlNameProcessBook, 0, 1, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 350))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(
            QtCore.QRect(0, -657, 796, 1005))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.tableTotalCount = QtWidgets.QTableWidget(
            self.scrollAreaWidgetContents)
        self.tableTotalCount.setMinimumSize(QtCore.QSize(0, 300))
        self.tableTotalCount.setObjectName("tableTotalCount")
        self.tableTotalCount.setColumnCount(0)
        self.tableTotalCount.setRowCount(0)
        self.verticalLayout.addWidget(self.tableTotalCount)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.tableBigData = QtWidgets.QTableWidget(
            self.scrollAreaWidgetContents)
        self.tableBigData.setMinimumSize(QtCore.QSize(0, 300))
        self.tableBigData.setObjectName("tableBigData")
        self.tableBigData.setColumnCount(0)
        self.tableBigData.setRowCount(0)
        self.verticalLayout.addWidget(self.tableBigData)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.tableFullTotalCount = QtWidgets.QTableWidget(
            self.scrollAreaWidgetContents)
        self.tableFullTotalCount.setMinimumSize(QtCore.QSize(0, 300))
        self.tableFullTotalCount.setObjectName("tableFullTotalCount")
        self.tableFullTotalCount.setColumnCount(0)
        self.tableFullTotalCount.setRowCount(0)
        self.verticalLayout.addWidget(self.tableFullTotalCount)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 2)
        self.graph = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.graph.setUrl(QtCore.QUrl("about:blank"))
        self.graph.setObjectName("graph")
        self.gridLayout.addWidget(self.graph, 2, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 841, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.startLog()
        self.connectToDb()
        self.populateDropDown()
        self.ddlNameProcessBook.currentTextChanged.connect(
            self.populateDashboard)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Nombre de ProcesoLibro"))
        self.label_2.setText(_translate("MainWindow", "Cuenta total"))
        self.label_3.setText(_translate("MainWindow", "Gran dato"))
        self.label_4.setText(_translate("MainWindow", "Cuenta total desglosada"))

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

    def populateDropDown(self):
        query = r"select distinct NombreProcesoLibro from SuperConsultaUsos"
        data = self.getColumn(self.exec(query), 0)
        data.insert(0, 'Selecciona un dato')
        self.ddlNameProcessBook.addItems(data)

    def populateTable(self, table, headers, data):
        table.setRowCount(len(data))
        table.setColumnCount(len(headers))
        table.setHorizontalHeaderLabels(headers)
        for i in range(len(data)):
            for j in range(len(headers)):
                table.setItem(
                    i, j, QtWidgets.QTableWidgetItem(str(data[i][j])))

    def populateDashboard(self):
        if (self.ddlNameProcessBook.currentText() != "Selecciona un dato"):
            headerTotalCount = self.getColumn(self.exec(r"""select distinct DoctoFront
                from SuperConsultaUsos
                where NombreProcesoLibro = '{0}'
                order by DoctoFront""".format(self.ddlNameProcessBook.currentText())), 0)
            dataTotalCount = self.exec(r"""
                select ClasificaciondeGranDato, DoctoFront, count(*) 
                from SuperConsultaUsos 
                where NombreProcesoLibro = '{0}' 
                group by ClasificaciondeGranDato, DoctoFront
                order by ClasificaciondeGranDato;
            """.format(self.ddlNameProcessBook.currentText()))
            transformedData = self.transform(dataTotalCount, headerTotalCount)
            headerTotalCount.insert(0, "Clasificación de Gran Dato")
            headerTotalCount.append("Total general")
            if (headerTotalCount[1] is None):
                headerTotalCount[1] = '(En blanco)'
            self.populateTable(self.tableTotalCount,
                               headerTotalCount, transformedData)

            headerBigData = ('Gran dato', 'Cuenta total')
            dataBigData = self.exec(r"""
                select GranDato, count(*)
                from SuperConsultaUsos
                where NombreProcesoLibro = '{0}'
                group by GranDato
            """.format(self.ddlNameProcessBook.currentText()))
            self.populateTable(self.tableBigData, headerBigData, dataBigData)

            headerFullTotal = ['Destino', 'Origen', 'Residencia']
            dataFullTotal = self.exec(r"""
                SELECT ListaTotal, Uso, count(*)
                from SuperConsultaUsos
                where NombreProcesoLibro = 'Libro 360' AND 
                (Uso = 'Destino' OR Uso = 'Origen' OR Uso = 'Residencia')
                group by ListaTotal, Uso;
            """)
            transformedData = self.transform(dataFullTotal, headerFullTotal)
            headerFullTotal.insert(1, 'Dato')
            headerFullTotal.append('Total general')
            self.populateTable(self.tableFullTotalCount,
                               headerFullTotal, transformedData)

            self.displayPie()

    def transform(self, data, headers):
        output = []
        actualName = ""
        d = {}
        total = 0
        tmp = []
        for element in data:
            if (actualName != element[0]):
                if (actualName != ""):
                    tmp = [actualName]
                for header in headers:
                    if (actualName != ""):
                        tmp.append(d[header])
                    d[header] = 0
                if (actualName != ""):
                    tmp.append(total)
                    output.append(tmp)
                actualName = element[0]
                total = 0
            if (actualName == element[0]):
                d[element[1]] = element[2]
                total += d[element[1]]
        if (len(tmp) > 0):
            tmp = [actualName]
            for header in headers:
                tmp.append(d[header])
            tmp.append(total)
            output.append(tmp)
        return output

    def displayPie(self):
        data = self.exec(r"""
            select ClasificaciondeGranDato, count(*)
            from SuperConsultaUsos 
            where NombreProcesoLibro = '{0}'
            group by ClasificaciondeGranDato;
        """.format(self.ddlNameProcessBook.currentText()))
        fig = go.Figure(go.Pie(
            labels=self.getColumn(data, 0),
            values=self.getColumn(data, 1),
        ))
        self.show(fig, "Súper consulta")

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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Dashboard()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
