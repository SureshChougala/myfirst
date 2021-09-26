from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog,QLineEdit,QFileDialog
import datetime

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1128, 752)
        MainWindow.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 0, 1121, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(226, 234, 255);")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 50, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(200, 167, 148);")
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(40, 90, 71, 21))
        self.comboBox.setStyleSheet("border-color: rgb(170, 0, 127);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(0, 460, 1121, 31))
        self.lineEdit_3.setStyleSheet("background-color: rgb(116, 200, 169);")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.diagnostic = QtWidgets.QPushButton(self.centralwidget)
        self.diagnostic.setGeometry(QtCore.QRect(280, 30, 121, 28))
        self.diagnostic.setObjectName("diagnostic")
        self.flash = QtWidgets.QPushButton(self.centralwidget)
        self.flash.setGeometry(QtCore.QRect(430, 30, 161, 28))
        self.flash.setObjectName("flash")
        self.did = QtWidgets.QPushButton(self.centralwidget)
        self.did.setGeometry(QtCore.QRect(620, 30, 93, 28))
        self.did.setObjectName("did")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(540, 490, 20, 241))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 30, 171, 401))
        self.frame.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(30, 310, 93, 28))
        self.pushButton.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.pushButton.setObjectName("pushButton")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(170, 26, 951, 411))
        self.scrollArea.setStyleSheet("background-color: rgb(255, 174, 193);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 949, 409))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.datak = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.datak.setGeometry(QtCore.QRect(10, 370, 161, 21))
        self.datak.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.datak.setText("")
        self.datak.setObjectName("datak")
        self.transmit = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.transmit.setGeometry(QtCore.QRect(190, 370, 81, 21))
        self.transmit.setStyleSheet("background-color: rgb(255, 170, 255);\n"
"border-color: rgb(0, 0, 127);")
        self.transmit.setObjectName("transmit")
        self.browse = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.browse.setGeometry(QtCore.QRect(200, 60, 61, 21))
        self.browse.setObjectName("browse")
        self.datafile = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.datafile.setGeometry(QtCore.QRect(10, 60, 181, 21))
        self.datafile.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.datafile.setObjectName("datafile")
        self.treeWidget = QtWidgets.QTreeWidget(self.scrollAreaWidgetContents)
        self.treeWidget.setGeometry(QtCore.QRect(20, 100, 331, 241))
        self.treeWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 430, 1121, 31))
        self.lineEdit_2.setStyleSheet("background-color: rgb(165, 200, 125);")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.stime = QtWidgets.QLineEdit(self.centralwidget)
        self.stime.setGeometry(QtCore.QRect(10, 550, 121, 22))
        self.stime.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stime.setObjectName("stime")
        self.canid = QtWidgets.QLineEdit(self.centralwidget)
        self.canid.setGeometry(QtCore.QRect(170, 550, 141, 22))
        self.canid.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.canid.setObjectName("canid")
        self.st = QtWidgets.QLabel(self.centralwidget)
        self.st.setGeometry(QtCore.QRect(30, 510, 81, 21))
        self.st.setStyleSheet("background-color: rgb(170, 170, 0);")
        self.st.setObjectName("st")
        self.can = QtWidgets.QLabel(self.centralwidget)
        self.can.setGeometry(QtCore.QRect(220, 510, 51, 21))
        self.can.setStyleSheet("background-color: rgb(170, 170, 0);\n"
"border-color: rgb(0, 0, 127);")
        self.can.setObjectName("can")
        self.scrollArea.raise_()
        self.frame.raise_()
        self.lineEdit.raise_()
        self.label.raise_()
        self.comboBox.raise_()
        self.lineEdit_3.raise_()
        self.diagnostic.raise_()
        self.flash.raise_()
        self.did.raise_()
        self.line_2.raise_()
        self.lineEdit_2.raise_()
        self.stime.raise_()
        self.canid.raise_()
        self.st.raise_()
        self.can.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1128, 26))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menuNew = QtWidgets.QMenu(self.menufile)
        self.menuNew.setObjectName("menuNew")
        self.menuOpen = QtWidgets.QMenu(self.menufile)
        self.menuOpen.setObjectName("menuOpen")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuTOOLS = QtWidgets.QMenu(self.menubar)
        self.menuTOOLS.setObjectName("menuTOOLS")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionPrint = QtWidgets.QAction(MainWindow)
        self.actionPrint.setObjectName("actionPrint")
        self.actionCUT = QtWidgets.QAction(MainWindow)
        self.actionCUT.setObjectName("actionCUT")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionug = QtWidgets.QAction(MainWindow)
        self.actionug.setObjectName("actionug")
        self.actionDesign_tools = QtWidgets.QAction(MainWindow)
        self.actionDesign_tools.setObjectName("actionDesign_tools")
        self.actionEditing_Tool = QtWidgets.QAction(MainWindow)
        self.actionEditing_Tool.setObjectName("actionEditing_Tool")
        self.actionsn = QtWidgets.QAction(MainWindow)
        self.actionsn.setObjectName("actionsn")
        self.actionBlank = QtWidgets.QAction(MainWindow)
        self.actionBlank.setObjectName("actionBlank")
        self.actionRuled = QtWidgets.QAction(MainWindow)
        self.actionRuled.setObjectName("actionRuled")
        self.actionA4 = QtWidgets.QAction(MainWindow)
        self.actionA4.setObjectName("actionA4")
        self.actionUi = QtWidgets.QAction(MainWindow)
        self.actionUi.setObjectName("actionUi")
        self.menuNew.addAction(self.actionBlank)
        self.menuNew.addAction(self.actionRuled)
        self.menuNew.addAction(self.actionA4)
        self.menuOpen.addAction(self.actionUi)
        self.menufile.addAction(self.menuNew.menuAction())
        self.menufile.addAction(self.menuOpen.menuAction())
        self.menufile.addAction(self.actionSave)
        self.menufile.addAction(self.actionSave_As)
        self.menufile.addAction(self.actionPrint)
        self.menuEdit.addAction(self.actionCUT)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuTOOLS.addAction(self.actionDesign_tools)
        self.menuTOOLS.addSeparator()
        self.menuTOOLS.addSeparator()
        self.menuTOOLS.addAction(self.actionEditing_Tool)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuTOOLS.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        
        self.datafile.close()
        self.browse.close()
        self.treeWidget.close()
        self.datak.close()
        self.transmit.close()

        self.diagnostic.clicked.connect(self.vip)
        self.browse.clicked.connect(self.vpi)
        self.treeWidget.itemDoubleClicked.connect(self.select_data)
        self.transmit.clicked.connect(self.tm)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def vip(self):
        self.browse.show()
        self.datafile.show()
    def vpi(self):
        filename=QFileDialog.getOpenFileName()
        nfile=filename[0].split("/")
        self.datafile.setText("UDS CAN "+"("+nfile[-1]+")")
      
        self.treeWidget.show()
        file=open(filename[0],"r")
        i=0
        for word in file.readlines():
        
            data=word.strip().split(",")
            data_len=len(data)
            for j in range(data_len):
                if j==0:
                    self.treeWidget.topLevelItem(i).setText(0,data[j])
                else:
                    self.treeWidget.topLevelItem(i).child(j-1).setText(0,data[j])
            i=i+1
        
    def select_data(self):

        self.datak.show()
        self.transmit.show()
        content=self.treeWidget.currentItem()
        self.datak.setText(content.text(0))
    def tm(self):
        sys_time=datetime.datetime.now()
        self.stime.setText(str(sys_time.strftime("%H:%M")))
        self.canid.setText("0X700")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setText(_translate("MainWindow", "Shortcut"))
        self.label.setText(_translate("MainWindow", "Select Protocol"))
        self.comboBox.setItemText(0, _translate("MainWindow", "USB"))
        self.comboBox.setItemText(1, _translate("MainWindow", "WiFi"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Bluetooth"))
        self.lineEdit_3.setText(_translate("MainWindow", "Rx Frame"))
        self.diagnostic.setText(_translate("MainWindow", "Diagnostic Services"))
        self.flash.setText(_translate("MainWindow", "Flash programming"))
        self.did.setText(_translate("MainWindow", "Self test DIDs"))
        self.pushButton.setText(_translate("MainWindow", "Connect Button"))
        self.transmit.setText(_translate("MainWindow", "Transmit"))
        self.browse.setText(_translate("MainWindow", "Browse"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "1"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "h1"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "i11"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "i12"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "h2"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "i21"))
        self.treeWidget.topLevelItem(1).child(1).setText(0, _translate("MainWindow", "i22"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow", "h3"))
        self.treeWidget.topLevelItem(2).child(0).setText(0, _translate("MainWindow", "i31"))
        self.treeWidget.topLevelItem(2).child(1).setText(0, _translate("MainWindow", "i32"))
        self.treeWidget.topLevelItem(3).setText(0, _translate("MainWindow", "h4"))
        self.treeWidget.topLevelItem(3).child(0).setText(0, _translate("MainWindow", "i41"))
        self.treeWidget.topLevelItem(3).child(1).setText(0, _translate("MainWindow", "i42"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.lineEdit_2.setText(_translate("MainWindow", "Tx Frame"))
        self.st.setText(_translate("MainWindow", "System Time"))
        self.can.setText(_translate("MainWindow", "Can ID"))
        self.menufile.setTitle(_translate("MainWindow", "File"))
        self.menuNew.setTitle(_translate("MainWindow", "New"))
        self.menuOpen.setTitle(_translate("MainWindow", "Open"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuTOOLS.setTitle(_translate("MainWindow", "Tools"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionPrint.setText(_translate("MainWindow", "Print"))
        self.actionPrint.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionCUT.setText(_translate("MainWindow", "Cut"))
        self.actionCUT.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Y"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionug.setText(_translate("MainWindow", "ug"))
        self.actionDesign_tools.setText(_translate("MainWindow", "Design tools"))
        self.actionEditing_Tool.setText(_translate("MainWindow", "Editing Tool"))
        self.actionsn.setText(_translate("MainWindow", "sn"))
        self.actionBlank.setText(_translate("MainWindow", "Blank"))
        self.actionRuled.setText(_translate("MainWindow", "Ruled"))
        self.actionA4.setText(_translate("MainWindow", "A4"))
        self.actionUi.setText(_translate("MainWindow", "Ui"))



import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())