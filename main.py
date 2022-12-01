import sys
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QDialog, QApplication
from PyQt6.uic import loadUi
from PyQt6.QtCore import QDate
import Modules.TablasCSV as TablasCSV, Modules.Usuario as Usuario, Modules.Cuenta as Cuenta
import Modules.Patron as Patron
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
        self.boton_agregar_patron.clicked.connect(self.ir_nuevo_patron)
        self.i = 0
        if len(patrones) == 0:
            self.patron_label.setText("Aun no tienes patrones")
        else:
            self.patron = patrones[0]
            self.patron_label.setText(self.patron.titulo)
            self.boton_anterior.clicked.connect(self.anterior_patron)
            self.boton_siguiente.clicked.connect(self.siguiente_patron)
            self.boton_ver.clicked.connect(self.ir_gestionar_patron)
        
    
    def cerrar_sesion(self):
        usuario.vaciar_usuario()
        bienvenida = Bienvenida_UI()
        widget.addWidget(bienvenida)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def ir_cuenta(self):
        gestionar_cuenta = Gestionar_Cuenta_UI()
        widget.addWidget(gestionar_cuenta)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def ir_nuevo_patron(self):
        nuevo_patron = Nuevo_Patron_UI()
        widget.addWidget(nuevo_patron)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def ir_gestionar_patron(self):
        gestionar_patron = Gestionar_Patron_UI(self.patron)
        widget.addWidget(gestionar_patron)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def anterior_patron(self):
        self.i -= 1
        if self.i == -1:
            self.i = len(patrones)-1
        self.patron = patrones[self.i]
        self.patron_label.setText(self.patron.titulo)
    
    def siguiente_patron(self):
        self.i += 1
        if self.i == len(patrones):
            self.i = 0
        self.patron = patrones[self.i]
        self.patron_label.setText(self.patron.titulo)

class Editar_Patron_UI(QDialog):
    def __init__(self,patron):
        super(Editar_Patron_UI,self).__init__()
        loadUi("UI files/editarPatron.ui",self)
        self.patron = patron
        self.boton_cerrar_sesion.clicked.connect(self.cerrar_sesion)
        self.boton_cuenta.clicked.connect(self.ir_cuenta)
        self.boton_regreso.clicked.connect(self.ir_gestionar_patron)
        self.titulo_in.setText(self.patron.titulo)
        self.categorias_in.setPlainText("\n".join(self.patron.categorias))
        self.materiales_in.setPlainText("\n".join(self.patron.materiales))
        self.abreviaturas_in.setPlainText("\n".join(self.patron.abreviaturas))
        self.pasos_in.setPlainText("\n".join(self.patron.pasos))
        self.boton_guardar_patron.clicked.connect(self.guardar_patron)
        self.boton_eliminar_patron.clicked.connect(self.ir_eliminar_patron)
    
    def cerrar_sesion(self):
        usuario.vaciar_usuario()
        bienvenida = Bienvenida_UI()
        widget.addWidget(bienvenida)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def ir_cuenta(self):
        gestionar_cuenta = Gestionar_Cuenta_UI()
        widget.addWidget(gestionar_cuenta)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def ir_gestionar_patron(self):
        gestionar_patron = Gestionar_Patron_UI(self.patron)
        widget.addWidget(gestionar_patron)
        widget.removeWidget(widget.currentWidget())
        
    def guardar_patron(self):
        titulo = self.titulo_in.text()
        categorias_s = self.categorias_in.toPlainText()
        materiales_s = self.materiales_in.toPlainText()
        abreviaturas_s = self.abreviaturas_in.toPlainText()
        pasos_s = self.pasos_in.toPlainText()
        
        categorias = categorias_s.splitlines()
        materiales = materiales_s.splitlines()
        abreviaturas = abreviaturas_s.splitlines()
        pasos = pasos_s.splitlines()
        
        self.patron.editar_patron(titulo,categorias,materiales,abreviaturas,pasos,patrones)
        
        gestionar_patron = Gestionar_Patron_UI(self.patron)
        widget.addWidget(gestionar_patron)
        widget.removeWidget(widget.currentWidget())
    
    def ir_eliminar_patron(self):
        eliminar_patron = Eliminar_Patron_UI(self.patron)
        widget.addWidget(eliminar_patron)
        widget.removeWidget(widget.currentWidget())

class Eliminar_Patron_UI(QDialog):
    def __init__(self,patron):
        super(Eliminar_Patron_UI,self).__init__()
        loadUi("UI files/eliminarPatron.ui",self)
        self.patron = patron
        self.boton_eliminar.clicked.connect(self.eliminar_patron)
        self.boton_cancelar.clicked.connect(self.ir_editar_patron)
    
    def ir_editar_patron(self):
        editar_patron = Editar_Patron_UI(self.patron)
        widget.addWidget(editar_patron)
        widget.removeWidget(widget.currentWidget())
    
    def eliminar_patron(self):
        self.patron.eliminar_patron(patrones)
        del(self.patron)
        menu_principal = Menu_Principal_UI()
        widget.addWidget(menu_principal)
        widget.removeWidget(widget.currentWidget())
        

class Gestionar_Patron_UI(QDialog):
    def __init__(self,patron):
        super(Gestionar_Patron_UI,self).__init__()
        loadUi("UI files/gestionarPatron.ui",self)
        self.patron = patron
        self.boton_cerrar_sesion.clicked.connect(self.cerrar_sesion)
        self.boton_cuenta.clicked.connect(self.ir_cuenta)
        self.boton_regreso.clicked.connect(self.ir_menu_principal)
        self.titulo_label.setText(self.patron.titulo)
        self.categorias_label.setText("\n".join(self.patron.categorias))
        self.materiales_label.setText("\n".join(self.patron.materiales))
        self.abreviaturas_label.setText("\n".join(self.patron.abreviaturas))
        self.pasos_label.setText("\n".join(self.patron.pasos))
        self.boton_editar_patron.clicked.connect(self.ir_editar_patron)
    
    def cerrar_sesion(self):
        usuario.vaciar_usuario()
        bienvenida = Bienvenida_UI()
        widget.addWidget(bienvenida)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def ir_cuenta(self):
        gestionar_cuenta = Gestionar_Cuenta_UI()
        widget.addWidget(gestionar_cuenta)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def ir_menu_principal(self):
        menu_principal = Menu_Principal_UI()
        widget.addWidget(menu_principal)
        widget.removeWidget(widget.currentWidget())
    
    def ir_editar_patron(self):
        editar_patron = Editar_Patron_UI(self.patron)
        widget.addWidget(editar_patron)
        widget.removeWidget(widget.currentWidget())
    
class Nuevo_Patron_UI(QDialog):
    def __init__(self):
        super(Nuevo_Patron_UI,self).__init__()
        loadUi("UI files/nuevoPatron.ui",self)
        self.boton_cerrar_sesion.clicked.connect(self.cerrar_sesion)
        self.boton_cuenta.clicked.connect(self.ir_cuenta)
        self.boton_nuevo_patron.clicked.connect(self.guardar_patron)
        self.boton_regreso.clicked.connect(self.ir_menu_principal)
    
    def cerrar_sesion(self):
        usuario.vaciar_usuario()
        bienvenida = Bienvenida_UI()
        widget.addWidget(bienvenida)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def ir_cuenta(self):
        gestionar_cuenta = Gestionar_Cuenta_UI()
        widget.addWidget(gestionar_cuenta)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def ir_menu_principal(self):
        menu_principal = Menu_Principal_UI()
        widget.addWidget(menu_principal)
        widget.removeWidget(widget.currentWidget())
    
    def guardar_patron(self):
        titulo = self.titulo_in.text()
        categorias_s = self.categorias_in.toPlainText()
        materiales_s = self.materiales_in.toPlainText()
        abreviaturas_s = self.abreviaturas_in.toPlainText()
        pasos_s = self.pasos_in.toPlainText()
        
        categorias = categorias_s.splitlines()
        materiales = materiales_s.splitlines()
        abreviaturas = abreviaturas_s.splitlines()
        pasos = pasos_s.splitlines()
        
        patron1 = Patron.Patron()
        patron1.escribir_patron(titulo,categorias,materiales,abreviaturas,pasos,patrones)
        
        menu_principal = Menu_Principal_UI()
        widget.addWidget(menu_principal)
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
    patrones = Patron.leer_patron()

    app = QApplication(sys.argv)
    bienvenida = Bienvenida_UI()
    widget = QtWidgets.QStackedWidget()
    widget.setWindowTitle("MIR")
    widget.setWindowIcon(QtGui.QIcon('Icons/logo.png'))
    widget.addWidget(bienvenida)
    widget.setFixedWidth(750)
    widget.setFixedHeight(550)
    widget.show()
    try:
        sys.exit(app.exec())
    except:
        print("Exiting")