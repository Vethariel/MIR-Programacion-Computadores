import Cuenta
from TablasCSV import TablasCSV
from Usuario import Usuario

def modificar_cuenta_usuario(usuario:Usuario,cuentas:TablasCSV):
        
    print("\n*Modificar cuenta*\n")

    opciones = {"email":usuario.email,
                "contra":"*******",
                "back":"Volver al menu principal"}
    
    back = False
    while not back:
        print("\nElija el dato a editar:\n")

        for opcion in opciones:
            print(f"{opcion} - {opciones[opcion]}")

        print()
        opcion = input(">>> ").lower()

        while opcion not in opciones:
            print("ADV: Opcion no valida")
            opcion = input(">>> ").lower()
            
        if opcion == "email":
            
            email = input("Escriba el email: ")

            while Cuenta.check_email_valido(email):
                
                print("ADV: El email no es valido")
                email = input("Escriba el email: ")
            
            usuario.editar_cuenta(cuentas,opcion,email)
            opciones[opcion] = usuario.email
            
            print("\Correo cambiado")

        if opcion == "contra":
            
            contra = input("Escriba la contrasena: ")

            while Cuenta.check_contra_valida(contra):
                print("ADV: La contrasena no es valida")
                contra = input("Escriba la contrasena: ")

            confirma_contra = input("Confirme la contrasena: ")

            while contra != confirma_contra:
                
                print("ADV: Las contrasenas no coinciden")
                contra = input("Escriba la contrasena: ")

                while Cuenta.check_contra_valida(contra):
                    print("ADV: La contrasena no es valida")
                    contra = input("Escriba la contrasena: ")

                confirma_contra = input("Confirme la contrasena: ")
            
            usuario.editar_cuenta(cuentas,opcion,contra)
            
            print("\nContrasenna cambiada")
                
        if opcion == "back":
            back = True

def modificar_info_usuario(usuario:Usuario,usuarios:TablasCSV):
        
    print("\n*Modificar usuario*\n")
    
    opciones = {"nombres":usuario.nombres,
                "apellidos":usuario.apellidos,
                "nickname":usuario.nickname,
                "fecha_nacimiento":usuario.fecha_de_nacimiento,
                "back":"Volver al menu principal"}
    
    back = False
    while not back:
        print("\nElija el dato a editar:\n")

        for opcion in opciones:
            print(f"{opcion} - {opciones[opcion]}")

        print()
        opcion = input(">>> ").lower()

        while opcion not in opciones:
            print("ADV: Opcion no valida")
            opcion = input(">>> ").lower()
        
            
        if opcion != "back" and opcion in opciones:
                nuevo_dato = input("Editar "+ opcion +": ")
                usuario.editar_usuario(usuarios,opcion,nuevo_dato)
                
        if opcion == "nombres":
            opciones[opcion] = usuario.nombres
        elif opcion == "apellidos":
            opciones[opcion] = usuario.apellidos
        elif opcion == "nickname":
            opciones[opcion] = usuario.nickname
        elif opcion == "fecha_nacimiento":
            opciones[opcion] = usuario.fecha_de_nacimiento
        
        if opcion == "back":
            back = True
        

def eliminar_cuenta_usuario(usuario:Usuario,cuentas:TablasCSV,usuarios:TablasCSV):
    
    eliminar_cuenta = input("\n¿Esta seguro que desea eliminar la cuenta?\nEsta accion no se puede deshacer\n>>> ").lower()
    cuenta_eliminada = False
    
    if eliminar_cuenta == "si":
        
        usuario.eliminar_usuario(usuarios)
        usuario.eliminar_cuenta(cuentas)
        print("\nCuenta eliminada")
        cuenta_eliminada = True
    
    return cuenta_eliminada
    


def mostrar_info_usuario(usuario:Usuario):
    
    print("\n*Gestionar usuario*\n")
    
    print("Correo:",usuario.email)
    print("Contrasenna:","*******")
    print("Nombres:",usuario.nombres)
    print("Apellidos:",usuario.apellidos)
    print("Apodo:",usuario.nickname)
    print("Fecha de nacimiento:",usuario.fecha_de_nacimiento)
    
    
def crear_info_usuario(usuario:Usuario, usuarios:TablasCSV):
    
    print("\n*Crear usuario*\n")
    
    nombres = input("Escriba los nombres: ")
    apellidos = input("Escriba los apellidos: ")
    nickname = input("Escriba el nickname: ")
    fecha_nacimiento = input("Escriba la fecha de nacimiento: ")
    
    usuario.crear_info(usuarios,nombres,apellidos,nickname,fecha_nacimiento)
    print("\nUsuario creado\n")


def ingreso(usuario:Usuario, cuentas:TablasCSV)->bool:
    
    print("\n*Ingresar a su cuenta*\n")
    email = input("Escriba el email: ")
    contra = input("Escriba la contrasena: ")
    ingreso = usuario.check_ingreso(cuentas, email, contra)

    while not ingreso:
        
        print("ADV: Email o contrasena incorrecta")
        nueva_cuenta = input("Desea crear una cuenta? ").lower()
        
        if nueva_cuenta == "si":
            crear_cuenta(cuentas)
            
        print("\n*Ingresar a su cuenta*\n")
        email = input("Escriba el email: ")
        contra = input("Escriba la contrasena: ")
            
        ingreso = usuario.check_ingreso(cuentas, email, contra)

    print(f"\nSatisfactoriamente logeado\n")

    return ingreso

def crear_cuenta(cuentas:TablasCSV):

    print("\n*Crear una nueva cuenta*\n")
    email = input("Escriba el email: ")

    while Cuenta.check_email_valido(email):
        
        print("ADV: El email no es valido")
        email = input("Escriba el email: ")

    while Cuenta.check_email_existe(cuentas, email):
        
        print("ADV: La cuenta ya existe")
        email = input("Escriba el email: ")
        
        while Cuenta.check_email_valido(email):
            
            print("ADV: El email no es valido")
            email = input("Escriba el email: ")

    contra = input("Escriba la contrasena: ")

    while Cuenta.check_contra_valida(contra):
        print("ADV: La contrasena no es valida")
        contra = input("Escriba la contrasena: ")

    confirma_contra = input("Confirme la contrasena: ")

    while contra != confirma_contra:
        
        print("ADV: Las contrasenas no coinciden")
        contra = input("Escriba la contrasena: ")

        while Cuenta.check_contra_valida(contra):
            print("ADV: La contrasena no es valida")
            contra = input("Escriba la contrasena: ")

        confirma_contra = input("Confirme la contrasena: ")

    # agrega la cuenta creada al archivo de cuentas
    Cuenta.crear_cuenta_nueva(cuentas, email, contra)
    print("\nCuenta creada\n")