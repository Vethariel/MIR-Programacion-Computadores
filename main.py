import TablasCSV, Usuario, Cuenta, Consola

def main():

    print("Bienvenido a MIR")
    
    # Pre init
    
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

    interfaz1 = {"login":"Ingresar a su cuenta", "ncuenta":"Crear una nueva cuenta", 
                 "exit":"Salir"}
    interfaz2 = {"spatron":"Seguir un patrones", "apatron":"Agregar patron nuevo", 
                  "gcuenta":"Gestionar cuenta","signout":"Cerrar sesion", "exit":"Salir"}
    interfaz3 = {"mcuenta":"Modificar cuenta","minfo":"Modificar informacion",
                 "delcuenta":"Eliminar cuenta",
                 "back":"Volver al menu principal"}
    interfaces = (interfaz1,interfaz2,interfaz3)
    interfaz_actual = 0
    comandos = interfaces[interfaz_actual]
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
                logged = Consola.ingreso(usuario, cuentas)
                if not usuario.check_info(usuarios):
                    Consola.crear_info_usuario(usuario, usuarios)
                interfaz_actual = 1
                comandos = interfaces[interfaz_actual]
            if comando == "ncuenta":
                Consola.crear_cuenta(usuario, cuentas)
        
        if logged:
            if comando == "gcuenta":
                comandos = Consola.mostrar_info_usuario(usuario)
                interfaz_actual = 2
                comandos = interfaces[interfaz_actual]
            if comando == "mcuenta":
                Consola.modificar_cuenta_usuario(usuario,cuentas)
            if comando == "minfo":
                Consola.modificar_cuenta_usuario(usuario,usuarios)
            if comando == "delcuenta":
                cuenta_eliminada = Consola.eliminar_cuenta_usuario(usuario,cuentas,usuarios)
                if cuenta_eliminada:
                    comando = "signout"
            if comando == "back":
                interfaz_actual-=1
                comandos = interfaces[interfaz_actual]
            
            if comando == "signout":
                usuario.vaciar_usuario()
                logged = False
                interfaz_actual = 1
                comandos = interfaces[interfaz_actual]
            if comando == "spatron":
                #seguir_patron()
                pass
            if comando == "apatron":
                #agregar_patron()
                pass
            #if comando
        
            
main()