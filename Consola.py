import Cuenta

def crear_info_usuario(usuario, usuarios):
    
    print("\n*Crear usuario*\n")
    
    nombres = input("Escriba los nombres: ")
    apellidos = input("Escriba los apellidos: ")
    nickname = input("Escriba el nickname: ")
    fecha_nacimiento = input("Escriba la fecha de nacimiento: ")
    
    usuario.crear_info(usuarios,nombres,apellidos,nickname,fecha_nacimiento)
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