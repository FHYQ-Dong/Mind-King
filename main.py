import sys
from PyQt5 import QtCore
from UI.Ui_MainWindow_Login import *
from PyQt5.QtWidgets import QApplication, QMainWindow

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Ui = Ui_MainWindow_Login()
        self.Ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    sys.exit(app.exec_())