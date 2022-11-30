import sys
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QDialog, QApplication
from PyQt6.uic import loadUi
from PyQt6.QtCore import QDate
import Modules.TablasCSV as TablasCSV, Modules.Usuario as Usuario, Modules.Cuenta as Cuenta
import ctypes

class Bienvenida_UI(QDialog):
    def __init__(self):
        super(Bienvenida_UI,self).__init__()
        loadUi("UI files/bienvenida.ui",self)
        self.boton_ingresar.clicked.connect(self.ir_ingresar)
        self.boton_crear_cuenta.clicked.connect(self.ir_crear_cuenta)
    
    def ir_ingresar(self):
        ingreso = Ingreso_UI()
        widget.addWidget(ingreso)
        widget.removeWidget(widget.currentWidget())
    
    def ir_crear_cuenta(self):
        crear_cuenta = Crear_Cuenta_UI()
        widget.addWidget(crear_cuenta)
        widget.removeWidget(widget.currentWidget())

class Ingreso_UI(QDialog):
    def __init__(self):
        super(Ingreso_UI,self).__init__()
        loadUi("UI files/iniciarSesion.ui",self)
        self.boton_ingreso.clicked.connect(self.ingreso)
        self.contra_in.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.boton_crear_cuenta.clicked.connect(self.ir_crear_cuenta)
        self.boton_regreso.clicked.connect(self.ir_bienvenida)

    def ingreso(self):
        email = self.email_in.text()
        contra = self.contra_in.text()
        adv = ""
        if len(email)==0 or len(contra)==0:
            adv = "Debe llenar todos los campos"
        elif Cuenta.check_email_valido(email):
            adv = "El email no es valido"
        elif not usuario.check_ingreso(cuentas, email, contra):
            adv = "Email o contrasena incorrecta"
        else:
            if not usuario.check_info(usuarios):
                crear_datos = Crear_Datos_UI()
                widget.addWidget(crear_datos)
                widget.removeWidget(widget.currentWidget())
            else:
                menu_principal = Menu_Principal_UI()
                widget.addWidget(menu_principal)
                widget.removeWidget(widget.currentWidget())
            print("Ingreso")
        try:
            self.adv_ingreso.setText(adv)
        except:
            print("Ya eliminado")
    
    def ir_crear_cuenta(self):
        crear_cuenta = Crear_Cuenta_UI()
        widget.addWidget(crear_cuenta)
        widget.removeWidget(widget.currentWidget())
    
    def ir_bienvenida(self):
        bienvenida = Bienvenida_UI()
        widget.addWidget(bienvenida)
        widget.removeWidget(widget.currentWidget())
        
class Crear_Cuenta_UI(QDialog):
    def __init__(self):
        super(Crear_Cuenta_UI,self).__init__()
        loadUi("UI files/crearCuenta.ui",self)
        self.boton_nueva_cuenta.clicked.connect(self.crear_cuenta)
        self.contra_in.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.conf_contra_in.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.boton_regreso.clicked.connect(self.ir_bienvenida)
    
    def crear_cuenta(self):
        email = self.email_in.text()
        contra = self.contra_in.text()
        conf_contra = self.conf_contra_in.text()
        adv = ""
        if len(email)==0 or len(contra)==0 or len(conf_contra)==0:
            adv = "Debe llenar todos los campos"
        elif Cuenta.check_email_valido(email):
            adv = "El email no es valido"
        elif Cuenta.check_email_existe(cuentas, email):
            adv = "El email ya esta registrado"
        elif Cuenta.check_contra_valida(contra):
            adv = "La contraseña no es valida"
        elif contra != conf_contra:
            adv = "Las contraseñas no coinciden"
        else:
            Cuenta.crear_cuenta_nueva(cuentas, email, contra)
            print("Crear cuenta")
            ingreso = Ingreso_UI()
            widget.addWidget(ingreso)
            widget.removeWidget(widget.currentWidget())
        
        try:
            self.adv_ingreso.setText(adv)
        except:
            print("Ya eliminado")
    
    def ir_bienvenida(self):
        bienvenida = Bienvenida_UI()
        widget.addWidget(bienvenida)
        widget.removeWidget(widget.currentWidget())

class Crear_Datos_UI(QDialog):
    def __init__(self):
        super(Crear_Datos_UI,self).__init__()
        loadUi("UI files/crearDatosUsuario.ui",self)
        self.boton_nuevo_usuario.clicked.connect(self.crear_datos)
        self.boton_regreso.clicked.connect(self.ir_ingreso)
    
    def crear_datos(self):
        nombres = self.nombres_in.text()
        apellidos = self.apellidos_in.text()
        nickname = self.nickname_in.text()
        fecha_nacimiento = self.fecha_nacimiento_in.date().toPyDate().strftime("%m/%d/%Y")
        adv = ""
        if len(nombres)==0 or len(apellidos)==0 or len(nickname)==0:
            adv = "Debe llenar todos los campos"
        else:
            usuario.crear_info(usuarios,nombres,apellidos,nickname,fecha_nacimiento)
            menu_principal = Menu_Principal_UI()
            widget.addWidget(menu_principal)
            widget.removeWidget(widget.currentWidget())
            print("Datos creados")
        try:
            self.adv_ingreso.setText(adv)
        except:
            print("Ya eliminado")
    
    def ir_ingreso(self):
        usuario.vaciar_usuario()
        ingreso = Ingreso_UI()
        widget.addWidget(ingreso)
        widget.removeWidget(widget.currentWidget())

class Menu_Principal_UI(QDialog):
    def __init__(self):
        super(Menu_Principal_UI,self).__init__()
        loadUi("UI files/menuPrincipal.ui",self)
        self.boton_cerrar_sesion.clicked.connect(self.cerrar_sesion)
        self.boton_cuenta.clicked.connect(self.ir_cuenta)
    
    def cerrar_sesion(self):
        usuario.vaciar_usuario()
        bienvenida = Bienvenida_UI()
        widget.addWidget(bienvenida)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def ir_cuenta(self):
        gestionar_cuenta = Gestionar_Cuenta_UI()
        widget.addWidget(gestionar_cuenta)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Gestionar_Cuenta_UI(QDialog):
    def __init__(self):
        super(Gestionar_Cuenta_UI,self).__init__()
        loadUi("UI files/gestionar_cuenta.ui",self)
        self.boton_cerrar_sesion.clicked.connect(self.cerrar_sesion)
        self.boton_regreso.clicked.connect(self.ir_ingreso)
        self.correo_label.setText(usuario.email)
        self.contra_label.setText("••••••••")
        self.nombres_label.setText(usuario.nombres)
        self.apellidos_label.setText(usuario.apellidos)
        self.nickname_label.setText(usuario.nickname)
        self.fecha_nacimiento_label.setText(usuario.fecha_de_nacimiento)
        self.boton_editar_cuenta.clicked.connect(self.ir_editar_cuenta)
        self.boton_editar_datos.clicked.connect(self.ir_editar_datos)
    
    def cerrar_sesion(self):
        usuario.vaciar_usuario()
        bienvenida = Bienvenida_UI()
        widget.addWidget(bienvenida)
        widget.removeWidget(widget.currentWidget())
    
    def ir_ingreso(self):
        menu_principal = Menu_Principal_UI()
        widget.addWidget(menu_principal)
        widget.removeWidget(widget.currentWidget())
    
    def ir_editar_cuenta(self):
        editar_cuenta = Editar_Cuenta_UI()
        widget.addWidget(editar_cuenta)
        widget.removeWidget(widget.currentWidget())
    
    def ir_editar_datos(self):
        editar_datos = Editar_Datos_UI()
        widget.addWidget(editar_datos)
        widget.removeWidget(widget.currentWidget())
            
class Editar_Cuenta_UI(QDialog):
    def __init__(self):
        super(Editar_Cuenta_UI,self).__init__()
        loadUi("UI files/editarCuenta.ui",self)
        self.email_in.setText(usuario.email)
        self.boton_guardar_cuenta.clicked.connect(self.editar_cuenta)
        self.contra_in.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.conf_contra_in.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.boton_regreso.clicked.connect(self.ir_gestionar_cuenta)
        self.boton_eliminar_cuenta.clicked.connect(self.ir_eliminar_cuenta)
    
    def editar_cuenta(self):
        email = self.email_in.text()
        contra = self.contra_in.text()
        conf_contra = self.conf_contra_in.text()
        adv = ""
        if len(email)==0 or len(contra)==0 or len(conf_contra)==0:
            adv = "Debe llenar todos los campos"
        elif Cuenta.check_email_valido(email):
            adv = "El email no es valido"
        elif email!= usuario.email and Cuenta.check_email_existe(cuentas, email):
            adv = "El email ya esta registrado"
        elif Cuenta.check_contra_valida(contra):
            adv = "La contraseña no es valida"
        elif contra != conf_contra:
            adv = "Las contraseñas no coinciden"
        else:
            usuario.editar_cuenta(cuentas,email,contra)
            print("Editar cuenta")
            self.ir_gestionar_cuenta()
        try:
            self.adv_ingreso.setText(adv)
        except:
            print("Ya eliminado")
    
    def ir_gestionar_cuenta(self):
        gestionar_cuenta = Gestionar_Cuenta_UI()
        widget.addWidget(gestionar_cuenta)
        widget.removeWidget(widget.currentWidget())
    
    def ir_eliminar_cuenta(self):
        eliminar_cuenta = Eliminar_Cuenta_UI()
        widget.addWidget(eliminar_cuenta)
        widget.removeWidget(widget.currentWidget())

class Editar_Datos_UI(QDialog):
    def __init__(self):
        super(Editar_Datos_UI,self).__init__()
        loadUi("UI files/editarDatosUsuario.ui",self)
        self.nombres_in.setText(usuario.nombres)
        self.apellidos_in.setText(usuario.apellidos)
        self.nickname_in.setText(usuario.nickname)
        self.fecha_nacimiento_in.setDate(QDate.fromString(usuario.fecha_de_nacimiento,"dd/MM/yyyy"))
        self.boton_guardar_usuario.clicked.connect(self.editar_datos)
        self.boton_regreso.clicked.connect(self.ir_gestionar_cuenta)
    
    def editar_datos(self):
        nombres = self.nombres_in.text()
        apellidos = self.apellidos_in.text()
        nickname = self.nickname_in.text()
        fecha_nacimiento = self.fecha_nacimiento_in.date().toPyDate().strftime("%m/%d/%Y")
        adv = ""
        if len(nombres)==0 or len(apellidos)==0 or len(nickname)==0:
            adv = "Debe llenar todos los campos"
        else:
            usuario.editar_usuario(usuarios,nombres,apellidos,nickname,fecha_nacimiento)
            print("Editar usuario")
            self.ir_gestionar_cuenta()
        try:
            self.adv_ingreso.setText(adv)
        except:
            print("Ya eliminado")
    
    def ir_gestionar_cuenta(self):
        gestionar_cuenta = Gestionar_Cuenta_UI()
        widget.addWidget(gestionar_cuenta)
        widget.removeWidget(widget.currentWidget())
    
class Eliminar_Cuenta_UI(QDialog):
    def __init__(self):
        super(Eliminar_Cuenta_UI,self).__init__()
        loadUi("UI files/eliminarCuenta.ui",self)
        self.boton_eliminar.clicked.connect(self.eliminar_cuenta)
        self.boton_cancelar.clicked.connect(self.ir_editar_cuenta)
    
    def ir_editar_cuenta(self):
        editar_cuenta = Editar_Cuenta_UI()
        widget.addWidget(editar_cuenta)
        widget.removeWidget(widget.currentWidget())
    
    def eliminar_cuenta(self):
        usuario.eliminar_usuario(usuarios)
        usuario.eliminar_cuenta(cuentas)
        bienvenida = Bienvenida_UI()
        widget.addWidget(bienvenida)
        widget.removeWidget(widget.currentWidget())

if __name__=="__main__":
    myappid = u'mycompany.myproduct.subproduct.version' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    nombre_csv = "CSV files/cuentas.csv"
    fieldnames = ["email", "contra", "accountID"]
    cuentas = TablasCSV.TablasCSV(nombre_csv, fieldnames)

    nombre_csv = "CSV files/usuarios.csv"
    fieldnames = ["nombres", "apellidos", "nickname", "fecha_nacimiento",  "accountID"]
    usuarios = TablasCSV.TablasCSV(nombre_csv, fieldnames)

    usuario = Usuario.Usuario()

    app = QApplication(sys.argv)
    bienvenida = Bienvenida_UI()
    widget = QtWidgets.QStackedWidget()
    widget.setWindowTitle("MIR")
    widget.setWindowIcon(QtGui.QIcon('logo.png'))
    widget.addWidget(bienvenida)
    widget.setFixedWidth(750)
    widget.setFixedHeight(550)
    widget.show()
    try:
        sys.exit(app.exec())
    except:
        print("Exiting")