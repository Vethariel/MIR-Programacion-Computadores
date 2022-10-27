import TablasCSV, Usuario, Cuenta

# funciones de logica

def no_loop_inf(a=[0]):
    a[0]+= 1
    if a[0]==6: a[0] = 1
    return a[0]<5

# funciones de interfaz

def crear_usuario(cuenta, usuarios):
    print("\n*Crear usuario*\n")
    nombres = input("Escriba los nombres: ")
    apellidos = input("Escriba los apellidos: ")
    nickname = input("Escriba el nickname: ")
    fecha_nacimiento = input("Escriba la fecha de nacimiento: ")
    TablasCSV.crear_usuario_nuevo(usuarios,nombres,apellidos,nickname,fecha_nacimiento,cuenta)
    print("\nUsuario creado\n")


def ingreso(usuario, cuentas):
    
    print("\n*Ingresar a su cuenta*\n")
    email = input("Escriba el email: ")
    contra = input("Escriba la contrasena: ")
    ingreso = usuario.check_ingreso(cuentas, email, contra)

    while not ingreso:
        
        print("ADV: Email o contrasena incorrecta")
        nueva_cuenta = input("Desea crear una cuenta? ").lower()
        
        if nueva_cuenta == "si":
            crear_cuenta(usuario, cuentas)
            
        print("\n*Ingresar a su cuenta*\n")
        email = input("Escriba el email: ")
        contra = input("Escriba la contrasena: ")
            
        ingreso = usuario.check_ingreso(cuentas, email, contra)

    print(f"\nSatisfactoriamente logeado\n")

    return ingreso

def crear_cuenta(usuario, cuentas):

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

#programa principal
def main():

    print("Bienvenido a MIR")
    
    
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
                logged = ingreso(usuario, cuentas)
                if not check_usuario(cuenta, usuarios):
                    crear_usuario(cuenta, usuarios)
                comandos = interfaz2
            if comando == "ncuenta":
                crear_cuenta(usuario, cuentas)
        
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