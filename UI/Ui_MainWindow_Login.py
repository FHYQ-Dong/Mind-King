# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Program\Python\Mind King\UI\MainWindow_Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_Login(object):
    def setupUi(self, MainWindow_Login):
        MainWindow_Login.setObjectName("MainWindow_Login")
        MainWindow_Login.resize(800, 601)
        self.centralwidget = QtWidgets.QWidget(MainWindow_Login)
        self.centralwidget.setObjectName("centralwidget")
        self.MainWindowFrame = QtWidgets.QFrame(self.centralwidget)
        self.MainWindowFrame.setGeometry(QtCore.QRect(90, 40, 411, 451))
        self.MainWindowFrame.setStyleSheet("#MainWindowFrame {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(27, 109, 255, 255), stop:1 rgba(255, 46, 84, 255));\n"
"    border-radius:20px;\n"
"}")
        self.MainWindowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainWindowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainWindowFrame.setObjectName("MainWindowFrame")
        MainWindow_Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_Login)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_Login)

    def retranslateUi(self, MainWindow_Login):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_Login.setWindowTitle(_translate("MainWindow_Login", "MainWindow"))