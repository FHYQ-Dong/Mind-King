import sys
from PyQt5 import QtCore
from UI.Ui_MainWindow_Login import *
import network.hash, network.http_request
from PyQt5.QtWidgets import QApplication, QMainWindow
import requests

class LoginWindow(QMainWindow):
    def __init__(self):

        self.server = ('',0)
        self.secret = {
            'Username': '',
            'Password': '',
            'Salt': '',
            'HashedPwd': '',
            'Target': ''
        }

        super().__init__()
        self.Ui = Ui_MainWindow_Login()
        self.Ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Ui.stackedWidget.setCurrentIndex(0)

        self.setPageServerLogic()
        self.setPageLoginLogic()
        self.setPageRegisterLogic()

        self.show()
    
    # Server Page
    def setPageServerLogic(self):
        self.Ui.pushButton_Server_Sure.clicked.connect(self.pushButton_Server_Sure_func)

    def pushButton_Server_Sure_func(self):
        if self.Ui.lineEdit_Server_URL.text() == '' or self.Ui.lineEdit_Server_Port.text() == '':
            self.Ui.label_Server_Status.setText('输入不能为空！')
            return
        else:
            self.server = (self.Ui.lineEdit_Server_URL.text(), int(self.Ui.lineEdit_Server_Port.text()))
            self.Ui.label_Server_Status.setText('连接中...')
            self.Thread_Conn = Thread_Conn(self)
            self.Thread_Conn.res.connect(lambda x:
                (self.Ui.stackedWidget.setCurrentIndex(x), 
                 self.Ui.label_Login_Status.setText(''))
            )
            self.Thread_Conn.start()

    # Login Page
    def setPageLoginLogic(self):
        self.Ui.pushButton_Login_Back.clicked.connect(
            lambda: (
            self.Ui.stackedWidget.setCurrentIndex(0), 
            self.Ui.label_Server_Status.setText(''))
        )
        self.Ui.pushButton_Login_Register.clicked.connect(
            lambda: (
            self.Ui.stackedWidget.setCurrentIndex(3),
            self.Ui.label_Register_Status.setText(''))
        )
        self.Ui.pushButton_Login_Sure.clicked.connect(self.pushButton_Login_Sure_func)
            
    def pushButton_Login_Sure_func(self):
        if self.Ui.lineEdit_Login_Username.text() == '' or self.Ui.lineEdit_Login_Password.text() == '':
            self.Ui.label_Login_Status.setText('输入不能为空！')
            return
        self.secret['Username'] = self.Ui.lineEdit_Login_Username.text()
        self.secret['Password'] = self.Ui.lineEdit_Login_Password.text()


    # Register Page
    def setPageRegisterLogic(self):
        self.Ui.pushButton_Register_Back.clicked.connect(
            lambda: (
            self.Ui.stackedWidget.setCurrentIndex(1), 
            self.Ui.label_Login_Status.setText(''))
        )
        self.Ui.pushButton_Register_Sure.clicked.connect(self.pushButton_Register_Sure_func)

    def pushButton_Register_Sure_func(self):
        pass


class Thread_Conn(QtCore.QThread):
    res = QtCore.pyqtSignal(int)

    def __init__(self, parent:LoginWindow) -> None:
        super().__init__(parent=parent)
        self.server = self.parent().server

    def run(self):
        try:
            res = network.http_request.conn(self.server)
            if res:
                self.res.emit(1)
            else:
                self.parent().Ui.label_Server_Status.setText('连接失败！')
                self.res.emit(0)
        except:
            self.parent().Ui.label_Server_Status.setText('连接失败！')
            self.res.emit(0)
        return

class Thread_Login(QtCore.QThread):
    res = QtCore.pyqtSignal(str)

    def __init__(self, parent:LoginWindow) -> None:
        super().__init__(parent=parent)
        self.server = self.parent().server
        self.username = self.parent().secret['Username']
        self.password = self.parent().secret['Password']

    def run(self):
        try:
            resp:requests.Response = network.http_request.login(self.parent().server, self.username, self.password)
            if resp.status_code == 200 and resp.text == 'Success':
                self.res.emit('Success')
            elif resp.status_code == 403:
                if resp.raise_for_status
        except:
            self.res.emit('Exception')
        return
            


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    sys.exit(app.exec_())