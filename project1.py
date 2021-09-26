from PyQt5.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem, QWidget, QInputDialog,QLineEdit,QFileDialog,QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
import xml.etree.ElementTree as xml

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1230, 847)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.vline = QtWidgets.QFrame(self.centralwidget)
        self.vline.setGeometry(QtCore.QRect(232, 0, 31, 541))
        self.vline.setFrameShape(QtWidgets.QFrame.VLine)
        self.vline.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vline.setObjectName("vline")
        self.stabs = QtWidgets.QTabWidget(self.centralwidget)
        self.stabs.setGeometry(QtCore.QRect(260, 10, 961, 531))
        self.stabs.setObjectName("stabs")
        self.diago = QtWidgets.QWidget()
        self.diago.setObjectName("diago")
        self.dia_tree = QtWidgets.QTreeWidget(self.diago)
        self.dia_tree.setGeometry(QtCore.QRect(0, 10, 301, 341))
        self.dia_tree.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.dia_tree.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.dia_tree.setObjectName("dia_tree")
        self.lineEdit = QtWidgets.QLineEdit(self.diago)
        self.lineEdit.setGeometry(QtCore.QRect(0, 380, 251, 41))
        self.lineEdit.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.diago)
        self.pushButton.setGeometry(QtCore.QRect(260, 380, 120, 40))
        self.pushButton.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")

        self.pushButton1 = QtWidgets.QPushButton(self.diago)
        self.pushButton1.setGeometry(QtCore.QRect(0, 10, 280, 30))
        self.pushButton1.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.pushButton1.setObjectName("pushButton1")

        self.stabs.addTab(self.diago, "")
        self.flash = QtWidgets.QWidget()
        self.flash.setObjectName("flash")
        self.stabs.addTab(self.flash, "")
        self.self_dids = QtWidgets.QWidget()
        self.self_dids.setObjectName("self_dids")
        self.stabs.addTab(self.self_dids, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1230, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.dia_tree.close()
        self.lineEdit.close()
        self.pushButton.close()
        #self.stabs.setCurrentIndex(1)
        self.pushButton1.clicked.connect(self.change_tab)
        self.dia_tree.itemDoubleClicked.connect(self.select_data)
        self.pushButton.clicked.connect(self.show_msg)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def show_msg(self):
        msg=QMessageBox()
        msg.setWindowTitle("Status")
        msg.setText("Yor data key is transmited      ")
        msg.setIcon(QMessageBox.Information)
        x=msg.exec_()

    def change_tab(self):
        tab=self.stabs.currentIndex()
        if tab==0:
            filename=QFileDialog.getOpenFileName(None,"Open file"," ", "Text files(*.txt*)")
            nfile=filename[0].split("/")
            self.dia_tree.clear()
            self.pushButton1.setText("UDS CAN "+"("+nfile[-1]+")")
            self.fill_data(filename[0])

    def fill_data(self,path):
        self.dia_tree.show()
        file=open(path, "r")
        nfile=file.readlines()
        root=xml.Element("ATSSL")
        for word in nfile:
            data=word.strip().split(",")
            print(data)
            d1=xml.Element(str(data[0]))
            root.append(d1)
            data.remove(data[0])
            i=0
            for cont in data:
                i=i+1
                if i%2!=0:
                    d2=xml.SubElement(d1,str(cont))
            
                else:
                    d2.text=str(cont)

        tree=xml.ElementTree(root)
        dataf="data_xml.xml"
        tree.write(dataf)
        self.choose_xml(dataf)

    def choose_xml(self, dataf):
        mytree=xml.parse(dataf)
        myroot=mytree.getroot()
        i=0
        for dt in myroot:
            a=QTreeWidgetItem([dt.tag])
            self.dia_tree.addTopLevelItem(a)
            for dt1 in myroot[i]:
                br=QTreeWidgetItem([dt1.tag])
                a.addChild(br)
                cr=QTreeWidgetItem([dt1.text])
                br.addChild(cr)
            i=i+1

    def select_data(self):
        content=self.dia_tree.currentItem()
        cnt=content.text(0)
        cnt1=cnt[1:-1]
        cnt2=len(cnt1.split(" "))
        self.lineEdit.setText("0" + str(cnt2) + " " + cnt1)
        self.lineEdit.show()
        self.pushButton.show()
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HomeWindow"))
        __sortingEnabled = self.dia_tree.isSortingEnabled()
        self.dia_tree.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("MainWindow", "Transmit"))
        self.pushButton1.setText(_translate("MainWindow", "Browse file"))
        self.stabs.setTabText(self.stabs.indexOf(self.diago), _translate("MainWindow", "Diagnostic Services"))
        self.stabs.setTabText(self.stabs.indexOf(self.flash), _translate("MainWindow", "Flash Programming"))
        self.stabs.setTabText(self.stabs.indexOf(self.self_dids), _translate("MainWindow", "Self test DIDs"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
print("hello world")