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
        self.actionSalir.triggered.connect(exit)

    def calcular(self):
        texto1=float(self.num1.text())
        texto2=float(self.num2.text())
        
        if self.sumar.isChecked()==True:
            self.resultado.setText(str(texto1+texto2))
        elif self.restar.isChecked()==True:
            self.resultado.setText(str(texto1-texto2))
        elif self.multiplicar.isChecked()==True:
            self.resultado.setText(str(texto1*texto2))
        else: 
            self.resultado.setText(str(texto1/texto2))
    
def main():
    app= PyQT.QApplication([])
    window= Principal()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()