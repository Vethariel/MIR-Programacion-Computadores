import TablasCSV
import re
import string

# funciones de logica

def no_loop_inf(a=[0]):
    a[0]+= 1
    if a[0]==6: a[0] = 1
    return a[0]<5

def check_email_valido(email):
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email_valido = re.match(pat,email)

    return not email_valido

def check_contra_valida(contra):
    l, u, c, d = 0, 0, 0, 0
    specialchar="$@_"
    if (len(contra) >= 8):

        for i in contra:
            if (i in string.ascii_lowercase): l+=1           
            if (i in string.ascii_uppercase): u+=1           
            if (i in string.digits): d+=1           
            if (i in specialchar): c+=1     

    contra_valida = (l>=1 and u>=1 and c>=1 and d>=1 and l+c+u+d==len(contra))

    return not contra_valida

# funciones de interfaz

def crear_usuario(cuenta, usuarios):
    print("\n*Crear usuario*\n")
    nombres = input("Escriba los nombres: ")
    apellidos = input("Escriba los apellidos: ")
    nickname = input("Escriba el nickname: ")
    fecha_nacimiento = input("Escriba la fecha de nacimiento: ")
    TablasCSV.crear_usuario_nuevo(usuarios,nombres,apellidos,nickname,fecha_nacimiento,cuenta)
    print("\nUsuario creado\n")

def ingreso(cuentas):
    print("\n*Ingresar a su cuenta*\n")
    email = input("Escriba el email: ")
    contra = input("Escriba la contrasena: ")
    ingreso, cuentaID = TablasCSV.check_ingreso(cuentas, email, contra)

    while not ingreso:
        print("ADV: Email o contrasena incorrecta")
        nueva_cuenta = input("Desea crear una cuenta? ").lower()
        if nueva_cuenta == "si":
            crear_cuenta(cuentas)
            print("\n*Ingresar a su cuenta*\n")
            email = input("Escriba el email: ")
            contra = input("Escriba la contrasena: ")
        ingreso, cuentaID = TablasCSV.check_ingreso(cuentas, email, contra)

    print(f"\nSatisfactoriamente logeado\n")

    return cuentaID

def crear_cuenta(cuentas):

    print("\n*Crear una nueva cuenta*\n")
    email = input("Escriba el email: ")

    while check_email_valido(email):
        print("ADV: El email no es valido")
        email = input("Escriba el email: ")

    while TablasCSV.check_email_existe(cuentas, email):
        print("ADV: La cuenta ya existe")
        email = input("Escriba el email: ")

    contra = input("Escriba la contrasena: ")

    while check_contra_valida(contra):
        print("ADV: La contrasena no es valida")
        contra = input("Escriba la contrasena: ")

    confirma_contra = input("Confirme la contrasena: ")

    while contra != confirma_contra:
        print("ADV: Las contrasenas no coinciden")
        contra = input("Escriba la contrasena: ")

        while check_contra_valida(contra):
            print("ADV: La contrasena no es valida")
            contra = input("Escriba la contrasena: ")

        confirma_contra = input("Confirme la contrasena: ")

    # agrega la cuenta creada al archivo de cuentas
    TablasCSV.crear_cuenta_nueva(cuentas, email, contra)
    print("\nCuenta creada\n")

#programa principal
def main():

    print("Bienvenido a MIR")
    
    tablas_csv = TablasCSV()
    cuentas = tablas_csv.cuentas_csv()
    usuarios = tablas_csv.usuarios_csv()
    patrones_usuario = tablas_csv.patrones_csv()

    cuenta = ""
    logged = False

    interfaz1 = {"login":"Ingresar a su cuenta", "ncuenta":"Crear una nueva cuenta", "exit":"Salir"}
    interfaz2 = {"spatron":"Seguir un patrones", "apatron":"Agregar patron nuevo", "signout":"Cerrar sesion", "exit":"Salir"}
    comandos = interfaz1
    exit = False

    while not exit:
        print("\nElija uno de los siguientes comandos:\n")

        for comando in comandos:
            print(f"{comando} - {comandos[comando]}")

        print()
        comando = input(">>> ").lower()

        while comando not in comandos:
            print("ADV: Comando no valido")
            comando = input(">>> ").lower()
        
        if comando == "exit":
            exit = True
            print("\nHasta la proxima!")

        if not logged:
            if comando == "login":
                cuenta = ingreso(cuentas)
                if not tablas_csv.check_usuario(cuenta, usuarios):
                    crear_usuario(cuenta, usuarios)
                logged = True
                comandos = interfaz2
            if comando == "ncuenta":
                crear_cuenta(cuentas)
        
        if logged:
            if comando == "signout":
                cuenta = ""
                logged = False
                comandos = interfaz1
            if comando == "spatron":
                #seguir_patron()
                pass
            if comando == "apatron":
                #agregar_patron()
                pass
            #if comando
        
            
main()