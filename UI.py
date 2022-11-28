import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication
from PyQt6.uic import loadUi
import Cuenta
from TablasCSV import TablasCSV
from Usuario import Usuario

class Ingreso_UI(QDialog):
    def __init__(self):
        super(Ingreso_UI,self).__init__()
        loadUi("iniciarSesion.ui",self)
        self.boton_ingreso.clicked.connect(self.ingreso)
        self.contra_in.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.boton_crear_cuenta.clicked.connect(self.ir_crear_cuenta)
    
    def ingreso(self):
        email = self.email_in.text()
        contra = self.contra_in.text()
        print("Ingreso")
    
    def ir_crear_cuenta(self):
        crear_cuenta = Crear_Cuenta_UI()
        widget.addWidget(crear_cuenta)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Crear_Cuenta_UI(QDialog):
    def __init__(self):
        super(Crear_Cuenta_UI,self).__init__()
        loadUi("crearCuenta.ui",self)
        self.boton_nueva_cuenta.clicked.connect(self.crear_cuenta)
        self.contra_in.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.conf_contra_in.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
    
    def crear_cuenta(self):
        email = self.email_in.text()
        if self.contra_in.text() == self.conf_contra_in.text():
            contra = self.contra_in.text()
            print("Crear cuenta")
            ingreso = Ingreso_UI()
            widget.addWidget(ingreso)
            widget.setCurrentIndex(widget.currentIndex()+1)

app = QApplication(sys.argv)
mainwindow = Ingreso_UI()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(480)
widget.setFixedHeight(620)
widget.show()
app.exec()