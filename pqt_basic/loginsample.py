# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginsample.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(False)
        MainWindow.resize(550, 471)
        MainWindow.setStyleSheet("background-color:rgb(167, 173, 255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.loginLB = QtWidgets.QLabel(self.centralwidget)
        self.loginLB.setGeometry(QtCore.QRect(210, -10, 151, 51))
        self.loginLB.setStyleSheet("color:rgb(227, 2, 104);\n"
                                   "font: 63 22pt \"Yu Gothic UI Semibold\";color:rgb(255, 255, 0);\n"
                                   "text-decoration: underline;\n"
                                   "font: 63 22pt \"Yu Gothic UI Semibold\";")
        self.loginLB.setObjectName("loginLB")
        self.usernameLB = QtWidgets.QLabel(self.centralwidget)
        self.usernameLB.setGeometry(QtCore.QRect(50, 70, 81, 51))
        self.usernameLB.setStyleSheet("color:rgb(85, 0, 127);\n"
                                      "font: 75 10pt \"MS Shell Dlg 2\";")
        self.usernameLB.setObjectName("usernameLB")
        self.passwordLB = QtWidgets.QLabel(self.centralwidget)
        self.passwordLB.setGeometry(QtCore.QRect(50, 140, 91, 51))
        self.passwordLB.setStyleSheet("color:rgb(85, 0, 127);\n"
                                      "font: 75 10pt \"MS Shell Dlg 2\";")
        self.passwordLB.setObjectName("passwordLB")
        self.usernameIN = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameIN.setGeometry(QtCore.QRect(150, 80, 200, 30))
        self.usernameIN.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                      "font: 25 8pt \"Yu Gothic UI Light\";")
        self.usernameIN.setObjectName("usernameIN")
        self.passwordIN = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordIN.setGeometry(QtCore.QRect(150, 150, 200, 30))
        self.passwordIN.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                      "font: 25 8pt \"Yu Gothic UI Light\";")
        self.passwordIN.setObjectName("passwordIN")
        self.orLB = QtWidgets.QLabel(self.centralwidget)
        self.orLB.setGeometry(QtCore.QRect(220, 250, 121, 61))
        self.orLB.setStyleSheet("color:rgb(0, 0, 127);\n"
                                "font: 75 italic 18pt \"Comic Sans MS\";\n"
                                "text-decoration: underline;")
        self.orLB.setObjectName("orLB")
        self.registerBN = QtWidgets.QPushButton(self.centralwidget)
        self.registerBN.setGeometry(QtCore.QRect(170, 330, 180, 50))
        self.registerBN.setMouseTracking(False)
        self.registerBN.setAcceptDrops(False)
        self.registerBN.setAutoFillBackground(False)
        self.registerBN.setStyleSheet("background-color:rgb(85, 170, 0);\n"
                                      "color:rgb(0, 0, 0);\n"
                                      "font: 75 italic 20pt \"Arial\";")
        self.registerBN.setObjectName("registerBN")
        self.forgot_username = QtWidgets.QTextBrowser(self.centralwidget)
        self.forgot_username.setGeometry(QtCore.QRect(380, 80, 130, 31))
        self.forgot_username.setStyleSheet("color:rgb(0, 0, 255);\n"
                                           "text-decoration: underline;")
        self.forgot_username.setObjectName("forgot_username")
        self.forgot_password = QtWidgets.QTextBrowser(self.centralwidget)
        self.forgot_password.setGeometry(QtCore.QRect(380, 150, 130, 31))
        self.forgot_password.setStyleSheet("color:rgb(0, 0, 255);\n"
                                           "text-decoration: underline;")
        self.forgot_password.setObjectName("forgot_password")
        self.loginBN = QtWidgets.QPushButton(self.centralwidget)
        self.loginBN.setGeometry(QtCore.QRect(190, 220, 93, 28))
        self.loginBN.setStyleSheet("color: rgb(85, 0, 127);\n"
                                   "border-color: rgb(0, 0, 0);")
        self.loginBN.setObjectName("loginBN")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loginLB.setText(_translate("MainWindow", "LOGIN"))
        self.usernameLB.setText(_translate("MainWindow", "Username"))
        self.passwordLB.setText(_translate("MainWindow", "Password"))
        self.usernameIN.setText(_translate(
            "MainWindow", "Enter your username here"))
        self.passwordIN.setText(_translate(
            "MainWindow", "Enter your password here"))
        self.orLB.setText(_translate("MainWindow", "OR"))
        self.registerBN.setText(_translate("MainWindow", "REGISTER"))
        self.forgot_username.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Forgot Username?</p></body></html>"))
        self.forgot_password.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Forgot Password?</p></body></html>"))
        self.loginBN.setText(_translate("MainWindow", "LogIn"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
