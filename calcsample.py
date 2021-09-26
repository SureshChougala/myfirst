# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calcsample.ui'
#
# Created by: PyQt UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 720)
        MainWindow.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.first_num = QtWidgets.QLineEdit(self.centralwidget)
        self.first_num.setEnabled(True)
        self.first_num.setGeometry(QtCore.QRect(180, 90, 200, 31))
        self.first_num.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                     "font: 10pt \"Arial\";\n"
                                     "")
        self.first_num.setText("")
        self.first_num.setObjectName("first_num")
        self.second_num = QtWidgets.QLineEdit(self.centralwidget)
        self.second_num.setGeometry(QtCore.QRect(180, 170, 200, 31))
        self.second_num.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "font: 10pt \"Arial\";\n"
                                      "")
        self.second_num.setText("")
        self.second_num.setObjectName("second_num")
        self.calcLB = QtWidgets.QLabel(self.centralwidget)
        self.calcLB.setGeometry(QtCore.QRect(90, 10, 220, 41))
        self.calcLB.setStyleSheet("color:rgb(255, 255, 0);\n"
                                  "text-decoration: underline;\n"
                                  "font: 75 20pt \"Arial\";\n"
                                  "text-decoration: underline;")
        self.calcLB.setObjectName("calcLB")
        self.addBN = QtWidgets.QPushButton(self.centralwidget)
        self.addBN.setGeometry(QtCore.QRect(50, 260, 95, 30))
        self.addBN.setStyleSheet("background-color: rgb(85, 255, 255);\n"
                                 "font: 8pt \"Arial\";\n"
                                 "color:rgb(0, 0, 0);")
        self.addBN.setObjectName("addBN")
        self.subBN = QtWidgets.QPushButton(self.centralwidget)
        self.subBN.setGeometry(QtCore.QRect(240, 260, 95, 30))
        self.subBN.setStyleSheet("background-color: rgb(85, 255, 255);\n"
                                 "font: 8pt \"Arial\";\n"
                                 "color:rgb(0, 0, 0);")
        self.subBN.setObjectName("subBN")
        self.mulBN = QtWidgets.QPushButton(self.centralwidget)
        self.mulBN.setGeometry(QtCore.QRect(50, 350, 95, 30))
        self.mulBN.setStyleSheet("background-color: rgb(85, 255, 255);\n"
                                 "font: 8pt \"Arial\";\n"
                                 "color:rgb(0, 0, 0);")
        self.mulBN.setObjectName("mulBN")
        self.divBN = QtWidgets.QPushButton(self.centralwidget)
        self.divBN.setGeometry(QtCore.QRect(240, 350, 95, 30))
        self.divBN.setStyleSheet("background-color: rgb(85, 255, 255);\n"
                                 "font: 8pt \"Arial\";\n"
                                 "color:rgb(0, 0, 0);")
        self.divBN.setObjectName("divBN")
        self.resultLB = QtWidgets.QLabel(self.centralwidget)
        self.resultLB.setGeometry(QtCore.QRect(135, 400, 111, 31))
        self.resultLB.setStyleSheet("color:rgb(0, 0, 0);\n"
                                    "font: 75 italic 16pt \"Arial\";\n"
                                    "text-decoration: underline;")
        self.resultLB.setObjectName("resultLB")
        self.firstinLB = QtWidgets.QLabel(self.centralwidget)
        self.firstinLB.setGeometry(QtCore.QRect(40, 90, 121, 30))
        self.firstinLB.setStyleSheet("font: 75 10pt \"Arial\";")
        self.firstinLB.setObjectName("firstinLB")
        self.secondinLB = QtWidgets.QLabel(self.centralwidget)
        self.secondinLB.setGeometry(QtCore.QRect(40, 170, 121, 30))
        self.secondinLB.setStyleSheet("font: 75 10pt \"Arial\";")
        self.secondinLB.setObjectName("secondinLB")

        
        self.outputLB = QtWidgets.QLabel(self.centralwidget)
        self.outputLB.setEnabled(True)
        self.outputLB.setGeometry(QtCore.QRect(90, 460, 220, 40))
        self.outputLB.setToolTip("")
        self.outputLB.setStatusTip("")
        self.outputLB.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "font: 16pt \"Arial\";")
        self.outputLB.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.outputLB.setLineWidth(12)
        self.outputLB.setObjectName("outputLB")
        self.second_num.raise_()
        self.first_num.raise_()
        self.calcLB.raise_()
        self.addBN.raise_()
        self.subBN.raise_()
        self.mulBN.raise_()
        self.divBN.raise_()
        self.resultLB.raise_()
        self.firstinLB.raise_()
        self.secondinLB.raise_()
        self.outputLB.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.addBN.clicked.connect(self.addfuc)
        self.subBN.clicked.connect(self.subfuc)
        self.mulBN.clicked.connect(self.mulfuc)
        self.divBN.clicked.connect(self.divfuc)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def addfuc(self):
        num1 = self.first_num.text()
        num2 = self.second_num.text()
        result = str(int(num1) + int(num2))
        self.outputLB.setText(result)

    def subfuc(self):
        num1 = self.first_num.text()
        num2 = self.second_num.text()
        result = str(int(num1) - int(num2))
        self.outputLB.setText(result)

    def mulfuc(self):
        num1 = self.first_num.text()
        num2 = self.second_num.text()
        result = str(int(num1) * int(num2))
        self.outputLB.setText(result)

    def divfuc(self):
        num1 = self.first_num.text()
        num2 = self.second_num.text()
        result = str(int(num1) / int(num2))
        self.outputLB.setText(result)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.calcLB.setText(_translate("MainWindow", "CALCULATOR"))
        self.addBN.setText(_translate("MainWindow", "ADD"))
        self.subBN.setText(_translate("MainWindow", "SUB"))
        self.mulBN.setText(_translate("MainWindow", "MUL"))
        self.divBN.setText(_translate("MainWindow", "DIV"))
        self.resultLB.setText(_translate("MainWindow", "RESULT"))
        self.firstinLB.setText(_translate("MainWindow", "First number"))
        self.secondinLB.setText(_translate("MainWindow", "Second number"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())