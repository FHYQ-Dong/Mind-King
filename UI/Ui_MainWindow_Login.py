# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Program\Python\Mind-King\UI\MainWindow_Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_Login(object):
    def setupUi(self, MainWindow_Login):
        MainWindow_Login.setObjectName("MainWindow_Login")
        MainWindow_Login.resize(1197, 863)
        MainWindow_Login.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow_Login)
        self.centralwidget.setObjectName("centralwidget")
        self.MainWindow_Login_Frame_Left = QtWidgets.QFrame(self.centralwidget)
        self.MainWindow_Login_Frame_Left.setGeometry(QtCore.QRect(130, 130, 411, 621))
        self.MainWindow_Login_Frame_Left.setStyleSheet("#MainWindow_Login_Frame_Left {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(27, 109, 255, 255), stop:1 rgba(255, 46, 84, 255));\n"
"    border-radius:20px;\n"
"}")
        self.MainWindow_Login_Frame_Left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainWindow_Login_Frame_Left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainWindow_Login_Frame_Left.setObjectName("MainWindow_Login_Frame_Left")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.MainWindow_Login_Frame_Left)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.MainWindow_Login_Frame_Left)
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_Minimize = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_Minimize.setGeometry(QtCore.QRect(30, 0, 20, 20))
        self.pushButton_Minimize.setStyleSheet("background-color: rgb(0, 0, 255);\n"
"border-radius:10px;")
        self.pushButton_Minimize.setText("")
        self.pushButton_Minimize.setFlat(False)
        self.pushButton_Minimize.setObjectName("pushButton_Minimize")
        self.pushButton_Quit = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_Quit.setGeometry(QtCore.QRect(0, 0, 20, 20))
        self.pushButton_Quit.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border-radius:10px;")
        self.pushButton_Quit.setText("")
        self.pushButton_Quit.setAutoDefault(False)
        self.pushButton_Quit.setDefault(False)
        self.pushButton_Quit.setFlat(False)
        self.pushButton_Quit.setObjectName("pushButton_Quit")
        self.verticalLayout.addWidget(self.frame_2)
        self.label = QtWidgets.QLabel(self.MainWindow_Login_Frame_Left)
        self.label.setStyleSheet("image: url(:/img/resource/icon.png)")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.frame_3 = QtWidgets.QFrame(self.MainWindow_Login_Frame_Left)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout.addWidget(self.frame_3)
        self.MainWindow_Login_Frame_Right = QtWidgets.QFrame(self.centralwidget)
        self.MainWindow_Login_Frame_Right.setGeometry(QtCore.QRect(540, 160, 461, 561))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainWindow_Login_Frame_Right.sizePolicy().hasHeightForWidth())
        self.MainWindow_Login_Frame_Right.setSizePolicy(sizePolicy)
        self.MainWindow_Login_Frame_Right.setMinimumSize(QtCore.QSize(211, 285))
        self.MainWindow_Login_Frame_Right.setStyleSheet("#MainWindow_Login_Frame_Right{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-top-right-radius:20px;\n"
"    border-bottom-right-radius:20px;\n"
"}")
        self.MainWindow_Login_Frame_Right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainWindow_Login_Frame_Right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainWindow_Login_Frame_Right.setObjectName("MainWindow_Login_Frame_Right")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.MainWindow_Login_Frame_Right)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.MainWindow_Login_Frame_Right)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QtCore.QSize(461, 561))
        self.stackedWidget.setStyleSheet("#stackedWidget{    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-top-right-radius:20px;\n"
"    border-bottom-right-radius:20px;\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.Page_Server = QtWidgets.QWidget()
        self.Page_Server.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.Page_Server.setObjectName("Page_Server")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Page_Server)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.Page_Server)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("QLineEdit{\n"
"    border: none;\n"
"    border-bottom: 1px solid black\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_4.addWidget(self.frame_5)
        self.lineEdit_Server_URL = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineEdit_Server_URL.sizePolicy().hasHeightForWidth())
        self.lineEdit_Server_URL.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.lineEdit_Server_URL.setFont(font)
        self.lineEdit_Server_URL.setObjectName("lineEdit_Server_URL")
        self.verticalLayout_4.addWidget(self.lineEdit_Server_URL)
        self.frame_7 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_4.addWidget(self.frame_7)
        self.lineEdit_Server_Port = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineEdit_Server_Port.sizePolicy().hasHeightForWidth())
        self.lineEdit_Server_Port.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.lineEdit_Server_Port.setFont(font)
        self.lineEdit_Server_Port.setObjectName("lineEdit_Server_Port")
        self.verticalLayout_4.addWidget(self.lineEdit_Server_Port)
        self.verticalLayout_3.addWidget(self.frame)
        self.frame_4 = QtWidgets.QFrame(self.Page_Server)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout.setContentsMargins(11, 0, 11, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_Server_Status = QtWidgets.QLabel(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Server_Status.sizePolicy().hasHeightForWidth())
        self.label_Server_Status.setSizePolicy(sizePolicy)
        self.label_Server_Status.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_Server_Status.setText("")
        self.label_Server_Status.setObjectName("label_Server_Status")
        self.horizontalLayout.addWidget(self.label_Server_Status)
        self.pushButton_Server_Sure = QtWidgets.QPushButton(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Server_Sure.sizePolicy().hasHeightForWidth())
        self.pushButton_Server_Sure.setSizePolicy(sizePolicy)
        self.pushButton_Server_Sure.setStyleSheet("image: url(:/img/resource/next.png);")
        self.pushButton_Server_Sure.setText("")
        self.pushButton_Server_Sure.setFlat(True)
        self.pushButton_Server_Sure.setObjectName("pushButton_Server_Sure")
        self.horizontalLayout.addWidget(self.pushButton_Server_Sure)
        self.verticalLayout_5.addWidget(self.frame_6)
        self.frame_9 = QtWidgets.QFrame(self.frame_4)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_5.addWidget(self.frame_9)
        self.frame_8 = QtWidgets.QFrame(self.frame_4)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_5.addWidget(self.frame_8)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.stackedWidget.addWidget(self.Page_Server)
        self.Page_Login = QtWidgets.QWidget()
        self.Page_Login.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.Page_Login.setObjectName("Page_Login")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.Page_Login)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_10 = QtWidgets.QFrame(self.Page_Login)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_15 = QtWidgets.QFrame(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_9.addWidget(self.frame_15)
        self.label_Login_Status = QtWidgets.QLabel(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_Login_Status.sizePolicy().hasHeightForWidth())
        self.label_Login_Status.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.label_Login_Status.setFont(font)
        self.label_Login_Status.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_Login_Status.setText("")
        self.label_Login_Status.setObjectName("label_Login_Status")
        self.verticalLayout_9.addWidget(self.label_Login_Status)
        self.verticalLayout_6.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.Page_Login)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setStyleSheet("QLineEdit{\n"
"    border: none;\n"
"    border-bottom: 1px solid black\n"
"}\n"
"")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.lineEdit_Login_Username = QtWidgets.QLineEdit(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.lineEdit_Login_Username.sizePolicy().hasHeightForWidth())
        self.lineEdit_Login_Username.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.lineEdit_Login_Username.setFont(font)
        self.lineEdit_Login_Username.setObjectName("lineEdit_Login_Username")
        self.verticalLayout_7.addWidget(self.lineEdit_Login_Username)
        self.frame_13 = QtWidgets.QFrame(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_7.addWidget(self.frame_13)
        self.lineEdit_Login_Password = QtWidgets.QLineEdit(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.lineEdit_Login_Password.sizePolicy().hasHeightForWidth())
        self.lineEdit_Login_Password.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.lineEdit_Login_Password.setFont(font)
        self.lineEdit_Login_Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_Login_Password.setObjectName("lineEdit_Login_Password")
        self.verticalLayout_7.addWidget(self.lineEdit_Login_Password)
        self.frame_14 = QtWidgets.QFrame(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_2.setContentsMargins(0, 11, 0, 11)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_Login_Back = QtWidgets.QPushButton(self.frame_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Login_Back.sizePolicy().hasHeightForWidth())
        self.pushButton_Login_Back.setSizePolicy(sizePolicy)
        self.pushButton_Login_Back.setStyleSheet("image: url(:/img/resource/previous.png);")
        self.pushButton_Login_Back.setText("")
        self.pushButton_Login_Back.setFlat(True)
        self.pushButton_Login_Back.setObjectName("pushButton_Login_Back")
        self.horizontalLayout_2.addWidget(self.pushButton_Login_Back)
        self.pushButton_Login_Register = QtWidgets.QPushButton(self.frame_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Login_Register.sizePolicy().hasHeightForWidth())
        self.pushButton_Login_Register.setSizePolicy(sizePolicy)
        self.pushButton_Login_Register.setStyleSheet("image: url(:/img/resource/register.png);")
        self.pushButton_Login_Register.setText("")
        self.pushButton_Login_Register.setFlat(True)
        self.pushButton_Login_Register.setObjectName("pushButton_Login_Register")
        self.horizontalLayout_2.addWidget(self.pushButton_Login_Register)
        self.pushButton_Login_Sure = QtWidgets.QPushButton(self.frame_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Login_Sure.sizePolicy().hasHeightForWidth())
        self.pushButton_Login_Sure.setSizePolicy(sizePolicy)
        self.pushButton_Login_Sure.setStyleSheet("image: url(:/img/resource/login.png);")
        self.pushButton_Login_Sure.setText("")
        self.pushButton_Login_Sure.setFlat(True)
        self.pushButton_Login_Sure.setObjectName("pushButton_Login_Sure")
        self.horizontalLayout_2.addWidget(self.pushButton_Login_Sure)
        self.verticalLayout_7.addWidget(self.frame_14)
        self.verticalLayout_6.addWidget(self.frame_11)
        self.frame_12 = QtWidgets.QFrame(self.Page_Login)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_6.addWidget(self.frame_12)
        self.stackedWidget.addWidget(self.Page_Login)
        self.Page_Register = QtWidgets.QWidget()
        self.Page_Register.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.Page_Register.setObjectName("Page_Register")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.Page_Register)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_16 = QtWidgets.QFrame(self.Page_Register)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_12.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_21 = QtWidgets.QFrame(self.frame_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy)
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.verticalLayout_12.addWidget(self.frame_21)
        self.label_Register_Status = QtWidgets.QLabel(self.frame_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_Register_Status.sizePolicy().hasHeightForWidth())
        self.label_Register_Status.setSizePolicy(sizePolicy)
        self.label_Register_Status.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_Register_Status.setText("")
        self.label_Register_Status.setObjectName("label_Register_Status")
        self.verticalLayout_12.addWidget(self.label_Register_Status)
        self.verticalLayout_10.addWidget(self.frame_16)
        self.frame_17 = QtWidgets.QFrame(self.Page_Register)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy)
        self.frame_17.setStyleSheet("QLineEdit{\n"
"    border: none;\n"
"    border-bottom: 1px solid black\n"
"}")
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_17)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.lineEdit_Register_Username = QtWidgets.QLineEdit(self.frame_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.lineEdit_Register_Username.sizePolicy().hasHeightForWidth())
        self.lineEdit_Register_Username.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.lineEdit_Register_Username.setFont(font)
        self.lineEdit_Register_Username.setEchoMode(QtWidgets.QLineEdit.NoEcho)
        self.lineEdit_Register_Username.setObjectName("lineEdit_Register_Username")
        self.verticalLayout_11.addWidget(self.lineEdit_Register_Username)
        self.frame_19 = QtWidgets.QFrame(self.frame_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.verticalLayout_11.addWidget(self.frame_19)
        self.lineEdit_Register_Password_1 = QtWidgets.QLineEdit(self.frame_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.lineEdit_Register_Password_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_Register_Password_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.lineEdit_Register_Password_1.setFont(font)
        self.lineEdit_Register_Password_1.setEchoMode(QtWidgets.QLineEdit.NoEcho)
        self.lineEdit_Register_Password_1.setObjectName("lineEdit_Register_Password_1")
        self.verticalLayout_11.addWidget(self.lineEdit_Register_Password_1)
        self.frame_20 = QtWidgets.QFrame(self.frame_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy)
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.verticalLayout_11.addWidget(self.frame_20)
        self.lineEdit_Register_Password_2 = QtWidgets.QLineEdit(self.frame_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.lineEdit_Register_Password_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_Register_Password_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.lineEdit_Register_Password_2.setFont(font)
        self.lineEdit_Register_Password_2.setEchoMode(QtWidgets.QLineEdit.NoEcho)
        self.lineEdit_Register_Password_2.setObjectName("lineEdit_Register_Password_2")
        self.verticalLayout_11.addWidget(self.lineEdit_Register_Password_2)
        self.verticalLayout_10.addWidget(self.frame_17)
        self.frame_18 = QtWidgets.QFrame(self.Page_Register)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_18)
        self.verticalLayout_13.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_22 = QtWidgets.QFrame(self.frame_18)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy)
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_22)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_Register_Back = QtWidgets.QPushButton(self.frame_22)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Register_Back.sizePolicy().hasHeightForWidth())
        self.pushButton_Register_Back.setSizePolicy(sizePolicy)
        self.pushButton_Register_Back.setStyleSheet("image: url(:/img/resource/previous.png);")
        self.pushButton_Register_Back.setText("")
        self.pushButton_Register_Back.setFlat(True)
        self.pushButton_Register_Back.setObjectName("pushButton_Register_Back")
        self.horizontalLayout_3.addWidget(self.pushButton_Register_Back)
        self.pushButton_Register_Sure = QtWidgets.QPushButton(self.frame_22)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Register_Sure.sizePolicy().hasHeightForWidth())
        self.pushButton_Register_Sure.setSizePolicy(sizePolicy)
        self.pushButton_Register_Sure.setStyleSheet("image: url(:/img/resource/login.png);")
        self.pushButton_Register_Sure.setText("")
        self.pushButton_Register_Sure.setFlat(True)
        self.pushButton_Register_Sure.setObjectName("pushButton_Register_Sure")
        self.horizontalLayout_3.addWidget(self.pushButton_Register_Sure)
        self.verticalLayout_13.addWidget(self.frame_22)
        self.frame_23 = QtWidgets.QFrame(self.frame_18)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy)
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.verticalLayout_13.addWidget(self.frame_23)
        self.verticalLayout_10.addWidget(self.frame_18)
        self.stackedWidget.addWidget(self.Page_Register)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.MainWindow_Login_Frame_Right.raise_()
        self.MainWindow_Login_Frame_Left.raise_()
        MainWindow_Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_Login)
        self.stackedWidget.setCurrentIndex(2)
        self.pushButton_Quit.clicked.connect(MainWindow_Login.close) # type: ignore
        self.pushButton_Minimize.clicked.connect(MainWindow_Login.showMinimized) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow_Login)

    def retranslateUi(self, MainWindow_Login):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_Login.setWindowTitle(_translate("MainWindow_Login", "MainWindow"))
        self.label.setText(_translate("MainWindow_Login", "<html><head/><body><p><br/></p></body></html>"))
        self.lineEdit_Server_URL.setPlaceholderText(_translate("MainWindow_Login", "服务器："))
        self.lineEdit_Server_Port.setPlaceholderText(_translate("MainWindow_Login", "端口:6677"))
        self.lineEdit_Login_Username.setPlaceholderText(_translate("MainWindow_Login", "用户名:"))
        self.lineEdit_Login_Password.setPlaceholderText(_translate("MainWindow_Login", "密码:"))
        self.lineEdit_Register_Username.setPlaceholderText(_translate("MainWindow_Login", "用户名:"))
        self.lineEdit_Register_Password_1.setPlaceholderText(_translate("MainWindow_Login", "密码:"))
        self.lineEdit_Register_Password_2.setPlaceholderText(_translate("MainWindow_Login", "重复密码:"))
import resource.img_rc
