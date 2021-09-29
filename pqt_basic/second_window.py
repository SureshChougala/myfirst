
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_second_window(object):
    def setupUi(self, second_window):
        second_window.setObjectName("second_window")
        second_window.resize(370, 320)
        second_window.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.centralwidget = QtWidgets.QWidget(second_window)
        self.centralwidget.setObjectName("centralwidget")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(10, 20, 341, 360))
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
        second_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(second_window)
        self.statusbar.setObjectName("statusbar")
        second_window.setStatusBar(self.statusbar)
        

        self.retranslateUi(second_window)
        QtCore.QMetaObject.connectSlotsByName(second_window)

    def retranslateUi(self, second_window):
        _translate = QtCore.QCoreApplication.translate
        second_window.setWindowTitle(_translate("second_window", "Demowindow2"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        #self.treeWidget.topLevelItem(0).setText(0, _translate("second_window", "h1"))
        #self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("second_window", "11"))
        #self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("second_window", "12"))
        #self.treeWidget.topLevelItem(1).setText(0, _translate("second_window", "h2"))
        #self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("second_window", "21"))
        #self.treeWidget.topLevelItem(2).setText(0, _translate("second_window", "h3"))
        #self.treeWidget.topLevelItem(2).child(0).setText(0, _translate("second_window", "31"))
        #self.treeWidget.topLevelItem(2).child(1).setText(0, _translate("second_window", "32"))
        #self.treeWidget.topLevelItem(3).setText(0, _translate("second_window", "h4"))
        #self.treeWidget.topLevelItem(3).child(0).setText(0, _translate("second_window", "41"))
        #self.treeWidget.topLevelItem(3).child(1).setText(0, _translate("second_window", "42"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    second_window = QtWidgets.QMainWindow()
    ui = Ui_second_window()
    ui.setupUi(second_window)
    second_window.show()
    sys.exit(app.exec_())
