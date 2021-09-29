# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menubar.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1065, 862)
        MainWindow.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(170, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.vline1 = QtWidgets.QFrame(self.centralwidget)
        self.vline1.setGeometry(QtCore.QRect(200, 0, 20, 585))
        self.vline1.setCursor(QtGui.QCursor(QtCore.Qt.SplitHCursor))
        self.vline1.setMouseTracking(True)
        self.vline1.setStyleSheet("")
        self.vline1.setLineWidth(4)
        self.vline1.setFrameShape(QtWidgets.QFrame.VLine)
        self.vline1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vline1.setObjectName("vline1")
        self.hline1 = QtWidgets.QFrame(self.centralwidget)
        self.hline1.setGeometry(QtCore.QRect(0, 570, 1080, 20))
        self.hline1.setCursor(QtGui.QCursor(QtCore.Qt.SplitVCursor))
        self.hline1.setMouseTracking(False)
        self.hline1.setLineWidth(4)
        self.hline1.setFrameShape(QtWidgets.QFrame.HLine)
        self.hline1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hline1.setObjectName("hline1")
        self.big_window_frame = QtWidgets.QFrame(self.centralwidget)
        self.big_window_frame.setGeometry(QtCore.QRect(210, 0, 851, 575))
        self.big_window_frame.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 170, 255);")
        self.big_window_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.big_window_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.big_window_frame.setObjectName("big_window_frame")
        self.left_window_fame = QtWidgets.QFrame(self.centralwidget)
        self.left_window_fame.setGeometry(QtCore.QRect(0, 0, 205, 575))
        self.left_window_fame.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.left_window_fame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_window_fame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_window_fame.setObjectName("left_window_fame")
        self.bottom_window_frame = QtWidgets.QFrame(self.centralwidget)
        self.bottom_window_frame.setGeometry(QtCore.QRect(0, 580, 1060, 211))
        self.bottom_window_frame.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.bottom_window_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottom_window_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom_window_frame.setObjectName("bottom_window_frame")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1065, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuTheme = QtWidgets.QMenu(self.menuView)
        self.menuTheme.setObjectName("menuTheme")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.newLB = QtWidgets.QAction(MainWindow)
        self.newLB.setEnabled(True)
        font = QtGui.QFont()
        self.newLB.setFont(font)
        self.newLB.setObjectName("newLB")
        self.openLB = QtWidgets.QAction(MainWindow)
        self.openLB.setObjectName("openLB")
        self.saveLB = QtWidgets.QAction(MainWindow)
        self.saveLB.setObjectName("saveLB")
        self.save_asLB = QtWidgets.QAction(MainWindow)
        self.save_asLB.setObjectName("save_asLB")
        self.copyLB = QtWidgets.QAction(MainWindow)
        self.copyLB.setObjectName("copyLB")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.darkLB = QtWidgets.QAction(MainWindow)
        self.darkLB.setCheckable(True)
        self.darkLB.setObjectName("darkLB")
        self.lightLb = QtWidgets.QAction(MainWindow)
        self.lightLb.setCheckable(True)
        self.lightLb.setObjectName("lightLb")
        self.defaultLB = QtWidgets.QAction(MainWindow)
        self.defaultLB.setCheckable(True)
        self.defaultLB.setObjectName("defaultLB")
        self.tool1LB = QtWidgets.QAction(MainWindow)
        self.tool1LB.setObjectName("tool1LB")
        self.tool2LB = QtWidgets.QAction(MainWindow)
        self.tool2LB.setObjectName("tool2LB")
        self.tool3LB = QtWidgets.QAction(MainWindow)
        self.tool3LB.setObjectName("tool3LB")
        self.actionNew_window = QtWidgets.QAction(MainWindow)
        self.actionNew_window.setObjectName("actionNew_window")
        self.menuFile.addAction(self.newLB)
        self.menuFile.addAction(self.openLB)
        self.menuFile.addAction(self.saveLB)
        self.menuFile.addAction(self.save_asLB)
        self.menuFile.addAction(self.actionNew_window)
        self.menuEdit.addAction(self.copyLB)
        self.menuEdit.addAction(self.actionPaste)
        self.menuTheme.addAction(self.darkLB)
        self.menuTheme.addAction(self.lightLb)
        self.menuTheme.addAction(self.defaultLB)
        self.menuView.addAction(self.menuTheme.menuAction())
        self.menuTools.addAction(self.tool1LB)
        self.menuTools.addAction(self.tool2LB)
        self.menuTools.addAction(self.tool3LB)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Demowindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuTheme.setTitle(_translate("MainWindow", "Theme"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.newLB.setText(_translate("MainWindow", "New"))
        self.newLB.setToolTip(_translate("MainWindow", "New"))
        self.newLB.setWhatsThis(_translate("MainWindow", "Cteart a file"))
        self.newLB.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.openLB.setText(_translate("MainWindow", "Open"))
        self.openLB.setWhatsThis(_translate("MainWindow", "Open a file"))
        self.openLB.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.saveLB.setText(_translate("MainWindow", "Save"))
        self.saveLB.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.save_asLB.setText(_translate("MainWindow", "Save as"))
        self.save_asLB.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.copyLB.setText(_translate("MainWindow", "Copy"))
        self.copyLB.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.darkLB.setText(_translate("MainWindow", "Dark"))
        self.lightLb.setText(_translate("MainWindow", "Light"))
        self.defaultLB.setText(_translate("MainWindow", "Default"))
        self.tool1LB.setText(_translate("MainWindow", "tool1LB"))
        self.tool2LB.setText(_translate("MainWindow", "Tool 2"))
        self.tool3LB.setText(_translate("MainWindow", "Tool 3"))
        self.actionNew_window.setText(_translate("MainWindow", "New window"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())