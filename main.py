import sys
from PyQt5 import QtCore
from UI.Ui_MainWindow_Login import *
from PyQt5.QtWidgets import QApplication, QMainWindow

class LoginWindow(QMainWindow):
    def __init__(self):

        self.server = ('',0)

        super().__init__()
        self.Ui = Ui_MainWindow_Login()
        self.Ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.setPageServerLogic()

        self.show()

    def setPageServerLogic(self):
        self.Ui.pushButton_Server_Sure.clicked.connect(lambda: self.pushButton_Server_Sure_func())

    def pushButton_Server_Sure_func(self):
        self.server = (self.Ui.lineEdit_Server_URL.text(), int(self.Ui.lineEdit_Server_Port.text()))
        self.Ui.stackedWidget.setCurrentIndex(1)
        print(self.server)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    sys.exit(app.exec_())