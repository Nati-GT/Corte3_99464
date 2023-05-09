import sys
import typing 
import PyQt5.QtWidgets as PyQT
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QWidget 

class Principal(PyQT.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initGui()
    def initGui(self):
        uic.loadUi('PrimeraApp.ui', self)
        self.show()
    
def main():
    app= PyQT.QApplication([])
    window= Principal()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()