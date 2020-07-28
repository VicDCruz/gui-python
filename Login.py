# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Menu import Menu
import pyodbc
import logging

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"


class Login(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(413, 418)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFormAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(-1, -1, -1, 0)
        self.formLayout.setVerticalSpacing(7)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.txtUser = QtWidgets.QLineEdit(self.centralwidget)
        self.txtUser.setObjectName("txtUser")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.txtUser)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.txtPwd = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPwd.setObjectName("lineEdit")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.txtPwd)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.checkCredentials)
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        self.lblIncorrect = QtWidgets.QLabel(self.centralwidget)
        self.lblIncorrect.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.lblIncorrect.setFont(font)
        self.lblIncorrect.setObjectName("lblIncorrect")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.lblIncorrect)
        self.verticalLayout.addLayout(self.formLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 413, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.startLog()
        self.retranslateUi(MainWindow)
        MainWindow.setWindowIcon(QtGui.QIcon('favicon.ico'))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.MainWindow = MainWindow


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Iniciar sesión"))
        MainWindow.setWindowIcon(QtGui.QIcon('favicon.ico'))
        self.label.setText(_translate("MainWindow", "Usuario"))
        self.label_2.setText(_translate("MainWindow", "Contraseña"))
        self.pushButton.setText(_translate("MainWindow", "Ingresar"))

    def changeToLogin(self):
        self.ui = Menu()
        self.MainWindow.move(600, 100)
        self.logger.info("Successful login")
        self.ui.setupUi(self.MainWindow)

    def checkCredentials(self):
        if (self.txtUser.text() == 'admin' and self.txtPwd.text() == 'admin'):
            self.lblIncorrect.setText('Correcto')
            self.changeToLogin()
        else:
            self.lblIncorrect.setText('Datos incorrectos')

    def startLog(self):
        logging.basicConfig(filename='Lumberjack.log',
                            level=logging.DEBUG, format=LOG_FORMAT)
        self.logger = logging.getLogger()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Login()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
