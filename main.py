import hashlib
import csv
import uuid
import re
import string

# funciones de logica

def no_loop_inf(a=[0]):
    a[0]+= 1
    if a[0]==6: a[0] = 1
    return a[0]<5

#Tablas de datos

def cuentas_csv():
    nombre_csv = 'cuentas.csv'

    try:
        with open(nombre_csv, "x") as cuentas:
            fieldnames = ["email", "contra", "accountID"]
            writer = csv.DictWriter(cuentas, fieldnames=fieldnames)
            writer.writeheader()

    except FileExistsError:
        pass

    return nombre_csv

def usuarios_csv():
    nombre_csv = 'usuarios.csv'

    try:
        with open(nombre_csv, "x") as usuarios:
            fieldnames = ["nombres", "apellidos", "nickname", "fecha_nacimiento",  "accountID"]
            writer = csv.DictWriter(usuarios, fieldnames=fieldnames)
            writer.writeheader()

    except FileExistsError:
        pass

    return nombre_csv

#Generacion

def crear_cuenta_nueva(cuentas, email, contra):
    enc = contra.encode()
    hash1 = hashlib.md5(enc).hexdigest()
    fieldnames = ["email", "contra", "accountID"]
    uid = uuid.uuid1()
    cuenta = {fieldnames[0]:email, fieldnames[1]:hash1, fieldnames[2]:uid}

    with open(cuentas, mode='a') as cuentas:
        writer = csv.DictWriter(cuentas, fieldnames=fieldnames)
        writer.writerow(cuenta)

def crear_usuario_nuevo(usuarios, nombres, apellidos, nickname, fecha_nacimiento, cuenta):
    fieldnames = ["nombres", "apellidos", "nickname", "fecha_nacimiento",  "accountID"]
    usuario = {fieldnames[0]:nombres, fieldnames[1]:apellidos, fieldnames[2]:nickname, fieldnames[3]:fecha_nacimiento, fieldnames[4]:cuenta}

    with open(usuarios, mode='a') as usuarios:
        writer = csv.DictWriter(usuarios, fieldnames=fieldnames)
        writer.writerow(usuario)

#Verificacion

def check_ingreso(cuentas, email, contra):
    auth = contra.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    ingreso = False
    cuentaID = ""

    with open(cuentas, mode='r') as cuentas:
        csv_reader = csv.DictReader(cuentas)

        for row in csv_reader:
            if row["email"] == email and row["contra"] == auth_hash:
                ingreso = True
                cuentaID = row["accountID"]

    return ingreso, cuentaID

def check_email_existe(cuentas, email):
    existe_email = False

    with open(cuentas, mode='r') as cuentas:
        csv_reader = csv.DictReader(cuentas)
        for row in csv_reader:
            if row["email"]==email:
                existe_email = True

    return existe_email


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

def check_usuario(cuenta, usuarios):
    usuario_existe = False

    with open(usuarios, mode='r') as usuarios:
        csv_reader = csv.DictReader(usuarios)

        for row in csv_reader:
            if row["accountID"] == cuenta:
                usuario_existe = True

    return usuario_existe

# funciones de interfaz

def crear_usuario(cuenta, usuarios):
    print("\n*Crear usuario*\n")
    nombres = input("Escriba los nombres: ")
    apellidos = input("Escriba los apellidos: ")
    nickname = input("Escriba el nickname: ")
    fecha_nacimiento = input("Escriba la fecha de nacimiento: ")
    crear_usuario_nuevo(usuarios,nombres,apellidos,nickname,fecha_nacimiento,cuenta)
    print("\nUsuario creado\n")

def ingreso(cuentas):
    print("\n*Ingresar a su cuenta*\n")
    email = input("Escriba el email: ")
    contra = input("Escriba la contrasena: ")
    ingreso, cuentaID = check_ingreso(cuentas, email, contra)

    while not ingreso:
        print("ADV: Email o contrasena incorrecta")
        nueva_cuenta = input("Desea crear una cuenta? ").lower()
        if nueva_cuenta == "si":
            crear_cuenta(cuentas)
            print("\n*Ingresar a su cuenta*\n")
            email = input("Escriba el email: ")
            contra = input("Escriba la contrasena: ")
        ingreso, cuentaID = check_ingreso(cuentas, email, contra)

    print(f"\nSatisfactoriamente logeado\n")

    return cuentaID

def crear_cuenta(cuentas):

    print("\n*Crear una nueva cuenta*\n")
    email = input("Escriba el email: ")

    while check_email_valido(email):
        print("ADV: El email no es valido")
        email = input("Escriba el email: ")

    while check_email_existe(cuentas, email):
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
    crear_cuenta_nueva(cuentas, email, contra)
    print("\nCuenta creada\n")

#programa principal
def main():

    print("Bienvenido a MIR")

    cuentas = cuentas_csv()
    usuarios = usuarios_csv()
    #lista_patrones = {"a":["oso", "conejo"]}

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
                if not check_usuario(cuenta, usuarios):
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