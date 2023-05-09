# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PrimeraApp.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(517, 301)
        MainWindow.setStyleSheet(u"color: rgb(199, 168, 43);\n"
"alternate-background-color: rgb(195, 161, 39);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(50, 300, 251, 171))
        self.widget.setStyleSheet(u"color: rgb(85, 255, 0);")
        self.FONDO = QGraphicsView(self.centralwidget)
        self.FONDO.setObjectName(u"FONDO")
        self.FONDO.setGeometry(QRect(20, 10, 431, 271))
        self.FONDO.setStyleSheet(u"background-color: rgb(209, 183, 88);\n"
"")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setGeometry(QRect(120, 0, 211, 81))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"color: rgb(226, 78, 255);\n"
"font: 48pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.label.setAlignment(Qt.AlignCenter)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(60, 80, 231, 141))
        self.frame.setStyleSheet(u"background-color: rgb(255, 227, 83);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.resultado = QLabel(self.frame)
        self.resultado.setObjectName(u"resultado")
        self.resultado.setEnabled(False)
        self.resultado.setGeometry(QRect(90, 70, 131, 21))
        self.resultado.setStyleSheet(u"background-color: rgb(255, 247, 207);\n"
"")
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 214, 52))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(6, 6, 6);")

        self.horizontalLayout.addWidget(self.label_2)

        self.num1 = QLineEdit(self.layoutWidget)
        self.num1.setObjectName(u"num1")
        self.num1.setStyleSheet(u"background-color: rgb(255, 255, 162);")

        self.horizontalLayout.addWidget(self.num1)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(6, 6, 6);")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.num2 = QLineEdit(self.layoutWidget)
        self.num2.setObjectName(u"num2")
        self.num2.setStyleSheet(u"background-color: rgb(255, 255, 162);")

        self.horizontalLayout_2.addWidget(self.num2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(290, 80, 121, 141))
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 127);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.layoutWidget1 = QWidget(self.frame_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 10, 86, 119))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.sumar = QRadioButton(self.layoutWidget1)
        self.sumar.setObjectName(u"sumar")
        self.sumar.setStyleSheet(u"color: rgb(6, 6, 6);")
        self.sumar.setChecked(True)

        self.verticalLayout_3.addWidget(self.sumar)

        self.restar = QRadioButton(self.layoutWidget1)
        self.restar.setObjectName(u"restar")
        self.restar.setStyleSheet(u"color: rgb(12, 12, 12);")

        self.verticalLayout_3.addWidget(self.restar)

        self.multiplicar = QRadioButton(self.layoutWidget1)
        self.multiplicar.setObjectName(u"multiplicar")
        self.multiplicar.setStyleSheet(u"font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_3.addWidget(self.multiplicar)

        self.dividir = QRadioButton(self.layoutWidget1)
        self.dividir.setObjectName(u"dividir")
        self.dividir.setStyleSheet(u"color: rgb(6, 6, 6);")

        self.verticalLayout_3.addWidget(self.dividir)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.pushButton = QPushButton(self.layoutWidget1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background-color: rgb(247, 155, 50);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"font: 75 9pt \"MS Shell Dlg 2\";\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_4.addWidget(self.pushButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 517, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"PRIMERA APP", None))
        self.resultado.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Numero 1", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Numero 2", None))
        self.sumar.setText(QCoreApplication.translate("MainWindow", u"Suma", None))
        self.restar.setText(QCoreApplication.translate("MainWindow", u"Resta", None))
        self.multiplicar.setText(QCoreApplication.translate("MainWindow", u"Multiplicar", None))
        self.dividir.setText(QCoreApplication.translate("MainWindow", u"Dividir", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
    # retranslateUi

