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

        self.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        texto1=self.num1.text()
        self.resultado.setText(texto1)
    
def main():
    app= PyQT.QApplication([])
    window= Principal()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()