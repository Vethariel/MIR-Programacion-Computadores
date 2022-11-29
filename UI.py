import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QWidget
from PyQt6.uic import loadUi
import TablasCSV, Usuario, Cuenta

class Bienvenida_UI(QDialog):
    def __init__(self):
        super(Bienvenida_UI,self).__init__()
        loadUi("bienvenida.ui",self)
        self.boton_ingresar.clicked.connect(self.ir_ingresar)
        self.boton_crear_cuenta.clicked.connect(self.ir_crear_cuenta)
    
    def ir_ingresar(self):
        ingreso = Ingreso_UI()
        widget.addWidget(ingreso)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def ir_crear_cuenta(self):
        crear_cuenta = Crear_Cuenta_UI()
        widget.addWidget(crear_cuenta)
        widget.setCurrentIndex(widget.currentIndex()+1)

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
        adv = ""
        if usuario.check_ingreso(cuentas, email, contra):
            print("Ingreso")
        else:
            adv = "Email o contrasena incorrecta"
        if Cuenta.check_email_valido(email):
            adv = "El email no es valido"
        if len(email)==0 or len(contra)==0:
            adv = "Debe llenar todos los campos"
        self.adv_ingreso.setText(adv)
    
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


nombre_csv = "cuentas.csv"
fieldnames = ["email", "contra", "accountID"]
cuentas = TablasCSV.TablasCSV(nombre_csv, fieldnames)

nombre_csv = "usuarios.csv"
fieldnames = ["nombres", "apellidos", "nickname", "fecha_nacimiento",  "accountID"]
usuarios = TablasCSV.TablasCSV(nombre_csv, fieldnames)

nombre_csv = "patrones.csv"
fieldnames = ["ruta_patron", "nombre_patron",  "accountID", "patronID"]     
patrones = TablasCSV.TablasCSV(nombre_csv, fieldnames)

nombre_csv = "categorias.csv"
fieldnames = ["patronID", "categoria"]
categorias = TablasCSV.TablasCSV(nombre_csv, fieldnames)

usuario = Usuario.Usuario()
logged = False

app = QApplication(sys.argv)
bienvenida = Bienvenida_UI()
widget = QtWidgets.QStackedWidget()
widget.addWidget(bienvenida)
widget.setFixedWidth(750)
widget.setFixedHeight(550)
widget.show()
try:
    sys.exit(app.exec())
except:
    print("Exiting")