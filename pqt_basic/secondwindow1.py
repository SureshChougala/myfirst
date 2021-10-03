
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_second_window(object):
    def setupUi(self, second_window):
        second_window.setObjectName("second_window")
        second_window.resize(637, 324)
        second_window.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.centralwidget = QtWidgets.QWidget(second_window)
        self.centralwidget.setObjectName("centralwidget")


        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 80, 421, 61))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n" "font: 16pt \"Arial\";")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText("You opened New Window")

        second_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(second_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 637, 26))
        self.menubar.setObjectName("menubar")
        second_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(second_window)
        self.statusbar.setObjectName("statusbar")
        second_window.setStatusBar(self.statusbar)

        self.retranslateUi(second_window)
        QtCore.QMetaObject.connectSlotsByName(second_window)

    def msg(self, result):
        self.lineEdit.setText("You clicked on " + result)

    def retranslateUi(self, second_window):
        _translate = QtCore.QCoreApplication.translate
        second_window.setWindowTitle(_translate("second_window", "Demowindow2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    second_window = QtWidgets.QMainWindow()
    ui = Ui_second_window()
    ui.setupUi(second_window)
    second_window.show()
    sys.exit(app.exec_())
