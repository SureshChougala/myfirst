# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'heading_3.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from pathlib import Path
from os import path
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QPushButton, QTableWidgetItem
import xml.etree.ElementTree as et
import itertools as it
import xml.dom.minidom as minidom

physical=700
functional=900
currentTime=QtCore.QTime.currentTime()
time=currentTime.toString()
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1011, 608)
        MainWindow.setStyleSheet("background-color: rgb(175, 175, 175);")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 131, 291))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.protocolLB = QtWidgets.QLabel(self.frame)
        self.protocolLB.setGeometry(QtCore.QRect(4, 10, 111, 31))
        self.protocolLB.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.protocolLB.setObjectName("protocolLB")
        self.connectBN = QtWidgets.QPushButton(self.frame)
        self.connectBN.setGeometry(QtCore.QRect(10, 250, 100, 28))
        self.connectBN.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.connectBN.setObjectName("connectBN")
        self.protocolBX = QtWidgets.QComboBox(self.frame)
        self.protocolBX.setGeometry(QtCore.QRect(10, 50, 101, 22))
        self.protocolBX.setObjectName("protocolBX")
        self.protocolBX.addItem("")
        self.protocolBX.addItem("")
        self.protocolBX.addItem("")
        self.phy_funBX = QtWidgets.QComboBox(self.frame)
        self.phy_funBX.setGeometry(QtCore.QRect(10, 90, 101, 31))
        self.phy_funBX.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.phy_funBX.setObjectName("phy_funBX")
        self.phy_funBX.addItem("")
        self.phy_funBX.addItem("")
        self.phy_funBX.addItem("")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(130, 0, 881, 301))
        self.frame_2.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        self.frame_7.setGeometry(QtCore.QRect(10, 220, 351, 80))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.hometab = QtWidgets.QTabWidget(self.frame_2)
        self.hometab.setGeometry(QtCore.QRect(0, 0, 871, 291))
        self.hometab.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.hometab.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.hometab.setObjectName("hometab")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.data_tree = QtWidgets.QTreeWidget(self.tab)
        self.data_tree.setGeometry(QtCore.QRect(0, 10, 260, 210))
        self.data_tree.setObjectName("data_tree")
        self.data_tree.headerItem().setText(0, "1")
        self.browseBN = QtWidgets.QPushButton(self.tab)
        self.browseBN.setGeometry(QtCore.QRect(0, 10, 260, 30))
        self.browseBN.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.browseBN.setObjectName("browseBN")
        self.outWD = QtWidgets.QLineEdit(self.tab)
        self.outWD.setGeometry(QtCore.QRect(0, 230, 170, 25))
        self.outWD.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.outWD.setObjectName("outWD")
        self.tarnsmitBN = QtWidgets.QPushButton(self.tab)
        self.tarnsmitBN.setGeometry(QtCore.QRect(180, 230, 85, 25))
        self.tarnsmitBN.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.tarnsmitBN.setObjectName("tarnsmitBN")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(280, 20, 251, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.hometab.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.hometab.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.hometab.addTab(self.tab_3, "")
        self.data_table = QtWidgets.QTableWidget(self.centralwidget)
        self.data_table.setGeometry(QtCore.QRect(10, 300, 521, 181))
        self.data_table.setSizeIncrement(QtCore.QSize(0, 0))
        self.data_table.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.data_table.setLineWidth(10)
        self.data_table.setMidLineWidth(0)
        self.data_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.data_table.setObjectName("data_table")
        self.data_table.setColumnCount(4)
        self.data_table.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(3, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1011, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuSettings_2 = QtWidgets.QMenu(self.menuTools)
        self.menuSettings_2.setObjectName("menuSettings_2")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setIconSize(QtCore.QSize(30, 30))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionnew = QtWidgets.QAction(MainWindow)
        self.actionnew.setObjectName("actionnew")
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionclose = QtWidgets.QAction(MainWindow)
        self.actionclose.setObjectName("actionclose")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionPaste_2 = QtWidgets.QAction(MainWindow)
        self.actionPaste_2.setObjectName("actionPaste_2")
        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionImpot = QtWidgets.QAction(MainWindow)
        self.actionImpot.setObjectName("actionImpot")
        self.actionRecent_Files = QtWidgets.QAction(MainWindow)
        self.actionRecent_Files.setObjectName("actionRecent_Files")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionDisplay_Settings = QtWidgets.QAction(MainWindow)
        self.actionDisplay_Settings.setObjectName("actionDisplay_Settings")
        self.actionFont_Settings = QtWidgets.QAction(MainWindow)
        self.actionFont_Settings.setObjectName("actionFont_Settings")
        self.actionWindow_Setting = QtWidgets.QAction(MainWindow)
        self.actionWindow_Setting.setObjectName("actionWindow_Setting")
        self.actionNew_Window = QtWidgets.QAction(MainWindow)
        self.actionNew_Window.setObjectName("actionNew_Window")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit_2 = QtWidgets.QAction(MainWindow)
        self.actionExit_2.setObjectName("actionExit_2")
        self.actionSave_2 = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("PySide_icons/icons8-save-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_2.setIcon(icon)
        self.actionSave_2.setObjectName("actionSave_2")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("PySide_icons/icons8-copy-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon1)
        self.actionCopy.setObjectName("actionCopy")
        self.actionNew = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("PySide_icons/icons8-new-file-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon2)
        self.actionNew.setObjectName("actionNew")
        self.actionCopy_2 = QtWidgets.QAction(MainWindow)
        self.actionCopy_2.setObjectName("actionCopy_2")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("PySide_icons/icons8-opened-folder-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon3)
        self.actionOpen.setObjectName("actionOpen")
        self.actionImport = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("PySide_icons/icons8-import-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionImport.setIcon(icon4)
        self.actionImport.setObjectName("actionImport")
        self.actionExport_2 = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("PySide_icons/icons8-export-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExport_2.setIcon(icon5)
        self.actionExport_2.setObjectName("actionExport_2")
        self.actionSave_3 = QtWidgets.QAction(MainWindow)
        self.actionSave_3.setIcon(icon)
        self.actionSave_3.setObjectName("actionSave_3")
        self.actionCopy_3 = QtWidgets.QAction(MainWindow)
        self.actionCopy_3.setIcon(icon1)
        self.actionCopy_3.setObjectName("actionCopy_3")
        self.actionDelete_2 = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("PySide_icons/icons8-delete-file-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete_2.setIcon(icon6)
        self.actionDelete_2.setObjectName("actionDelete_2")
        self.actionCut_2 = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("PySide_icons/icons8-cut-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut_2.setIcon(icon7)
        self.actionCut_2.setObjectName("actionCut_2")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("PySide_icons/icons8-settings-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon8)
        self.actionSettings.setObjectName("actionSettings")
        self.actionDisplay_Settings_2 = QtWidgets.QAction(MainWindow)
        self.actionDisplay_Settings_2.setObjectName("actionDisplay_Settings_2")
        self.actionFont_Settings_2 = QtWidgets.QAction(MainWindow)
        self.actionFont_Settings_2.setObjectName("actionFont_Settings_2")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionExport_2)
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionRecent_Files)
        self.menuFile.addAction(self.actionSave_3)
        self.menuFile.addAction(self.actionExit_2)
        self.menuEdit.addAction(self.actionCut_2)
        self.menuEdit.addAction(self.actionPaste_2)
        self.menuEdit.addAction(self.actionDelete_2)
        self.menuEdit.addAction(self.actionCopy_3)
        self.menuSettings_2.addAction(self.actionDisplay_Settings_2)
        self.menuSettings_2.addAction(self.actionFont_Settings_2)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.menuSettings_2.menuAction())
        self.menuHelp.addAction(self.actionDocumentation)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionSave_2)
        self.toolBar.addAction(self.actionCopy)
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionImport)
        self.toolBar.addAction(self.actionExport_2)
        self.toolBar.addAction(self.actionDelete_2)
        self.toolBar.addAction(self.actionCut_2)
        self.toolBar.addAction(self.actionSettings)

        self.retranslateUi(MainWindow)
        self.hometab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
        self.connectBN.clicked.connect(self.select)
        self.browseBN.clicked.connect(self.browse)
        self.lineEdit.textChanged[str].connect(self.convert_to_xml)
        self.data_tree.itemDoubleClicked.connect(self.tree_content)
        

    def tree_content(self):
        self.outWD.clear()
        x=self.data_tree.currentItem()
        self.outWD.setText(str(x.text(0)))

    #Function for browsing the files.........
    def browse(self,filename):
        filename = QFileDialog.getOpenFileName(None, "Open File"," ", "Text Files (*.txt*)")
        print(filename[0])
        self.lineEdit.setText(filename[0])

    #Function for converting text file to xml file.......
    def convert_to_xml(self,filename):
        root_name=Path(filename)
        root = et.Element(root_name.name)
        with open(filename) as f:
            lines = f.read().splitlines()
        celldata = et.SubElement(root, 'FileData')
        for line in it.groupby(lines):
            line=line[0]
            if not line:
                celldata = et.SubElement(root, 'FileData')
            else:
                tag = line.split(":")
                el=et.SubElement(celldata,tag[0].replace(" ",""))
                tag=' '.join(tag[1:]).strip()
                if 'File Name' in line:
                    tag = line.split("\\")[-1].strip()
                elif 'File Size' in line:
                    splist =  filter(None,line.split(" "))
                    tag = splist[splist.index('Low:')+1]
                    #splist[splist.index('High:')+1]
                el.text = tag
        formatedXML = minidom.parseString(et.tostring(root)).toprettyxml(indent=" ",encoding='utf-8').strip()
        with open("test_ambi.xml","wb") as f:
            f.write(formatedXML)
        self.data_tree.show()

        #Reading the file...........
        f=open("test_ambi.xml","r").read()
        self.printtree(f)
        
    def printtree(self,s):
        tree=et.fromstring(s)
        self.data_tree.setColumnCount(1)
        a=QtWidgets.QTreeWidgetItem([tree.tag])
        self.data_tree.addTopLevelItem(a)
        def displaytree(a,s):
            for child in s:
                branch=QtWidgets.QTreeWidgetItem([child.tag])
                a.addChild(branch)
                displaytree(branch,child)
            if s.text is not None:
                content=s.text
                a.addChild(QtWidgets.QTreeWidgetItem([content]))
        displaytree(a,tree)
        

    def select(self):
        choice=self.phy_funBX.currentText()
        if choice=="Physical":
            self.data_table.setItem(0,1,QtWidgets.QTableWidgetItem(str(physical)))
            self.data_table.setItem(0,0,QtWidgets.QTableWidgetItem(str(time)))
            self.data_table.setItem(0,2,QTableWidgetItem(str(self.outWD.text())))
            self.data_table.setItem(0,2,QtWidgets.QTableWidgetItem("    RX"))
            id=format(700, "b")
            slid=format(8, "b")
            #self.data_table.setItem(0,1,QtWidgets.QTableWidgetItem("    "+ str(700)))
            self.data_table.setItem(0,3,QtWidgets.QTableWidgetItem(str(id)+"  "+str(slid)))
        elif choice=="Functional":
            self.data_table.setItem(0,1,QtWidgets.QTableWidgetItem(str(physical)))
            self.data_table.setItem(0,0,QtWidgets.QTableWidgetItem(str(time)))
            self.data_table.setItem(0,2,QTableWidgetItem(str(self.outWD.text())))
            self.data_table.setItem(0,2,QtWidgets.QTableWidgetItem("    TX"))
            id=format(900, "b")
            slid=format(8, "b")
            self.data_table.setItem(0,3,QtWidgets.QTableWidgetItem(str(id)+"  "+str(slid)))
        
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ATSSL"))
        self.protocolLB.setText(_translate("MainWindow", "Select Protocol"))
        self.connectBN.setText(_translate("MainWindow", "Connect"))
        self.protocolBX.setItemText(0, _translate("MainWindow", "Blutooth"))
        self.protocolBX.setItemText(1, _translate("MainWindow", "WiFi"))
        self.protocolBX.setItemText(2, _translate("MainWindow", "USB"))
        self.phy_funBX.setItemText(0, _translate("MainWindow", "-Select-"))
        self.phy_funBX.setItemText(1, _translate("MainWindow", "Physical"))
        self.phy_funBX.setItemText(2, _translate("MainWindow", "Functional"))
        self.browseBN.setText(_translate("MainWindow", "Browse"))
        self.tarnsmitBN.setText(_translate("MainWindow", "Transmit"))
        self.hometab.setTabText(self.hometab.indexOf(self.tab), _translate("MainWindow", "Dignostic Service"))
        self.hometab.setTabText(self.hometab.indexOf(self.tab_2), _translate("MainWindow", "Flash Programming"))
        self.hometab.setTabText(self.hometab.indexOf(self.tab_3), _translate("MainWindow", "Self Test DIDs"))
        item = self.data_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.data_table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.data_table.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.data_table.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.data_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Time"))
        item = self.data_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "CAN ID"))
        item = self.data_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "TX/RX"))
        item = self.data_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Response"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuSettings_2.setTitle(_translate("MainWindow", "Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionnew.setText(_translate("MainWindow", "New Window"))
        self.actionnew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionopen.setText(_translate("MainWindow", "Open"))
        self.actionopen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionclose.setText(_translate("MainWindow", "Close"))
        self.actionclose.setShortcut(_translate("MainWindow", "Ctrl+F4"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionPaste_2.setText(_translate("MainWindow", "Paste"))
        self.actionPaste_2.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionImpot.setText(_translate("MainWindow", "Import"))
        self.actionRecent_Files.setText(_translate("MainWindow", "Recent Files"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionDelete.setShortcut(_translate("MainWindow", "Ctrl+Shift+D"))
        self.actionDisplay_Settings.setText(_translate("MainWindow", "Display Settings"))
        self.actionFont_Settings.setText(_translate("MainWindow", "Font Settings"))
        self.actionWindow_Setting.setText(_translate("MainWindow", "Window Setting"))
        self.actionNew_Window.setText(_translate("MainWindow", "New Window"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit_2.setText(_translate("MainWindow", "Exit"))
        self.actionSave_2.setText(_translate("MainWindow", "Save"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionCopy_2.setText(_translate("MainWindow", "Copy"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
        self.actionExport_2.setText(_translate("MainWindow", "Export"))
        self.actionSave_3.setText(_translate("MainWindow", "Save"))
        self.actionSave_3.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionCopy_3.setText(_translate("MainWindow", "Copy"))
        self.actionCopy_3.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionDelete_2.setText(_translate("MainWindow", "Delete"))
        self.actionDelete_2.setShortcut(_translate("MainWindow", "Ctrl+Shift+D"))
        self.actionCut_2.setText(_translate("MainWindow", "Cut"))
        self.actionCut_2.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionDisplay_Settings_2.setText(_translate("MainWindow", "Display Settings"))
        self.actionFont_Settings_2.setText(_translate("MainWindow", "Font Settings"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
