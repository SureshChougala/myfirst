import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication,QFileDialog

class open_file():
    def openfile(self):
        file_name=QFileDialog.getOpenFileName(self, "Open file", "D:")
        self.filename.setText(file_name[0])
        file_name.show()
open_file()
app=QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
widget.show()
sys.exit(app.exec_())