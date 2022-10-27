import uuid
import hashlib
import csv

class TablasCSV():
    def __init__(self) -> None:
        
        self.cuentas = "cuentas.csv"
        self.fieldnames_cuentas = ["email", "contra", "accountID"]
        
        self.usuarios = "usuarios.csv"
        self.fieldnames_usuarios = ["nombres", "apellidos", "nickname", "fecha_nacimiento",  "accountID"]
        
        self.patrones = "patrones.csv"
        self.fieldnames_patrones = ["ruta_patron", "nombre_patron",  "accountID", "patronID"]        
        
        self.categorias = "categorias.csv"
        self.fieldnames_cateogrias = ["patronID", "categoria"]
        
    
    # Inicializar tablas
    def crear_csv_si_no_existe(fieldnames, nombre_csv):

        try:
            with open(nombre_csv, "x") as csv:
                writer = csv.DictWriter(csv, fieldnames=fieldnames)
                writer.writeheader()

        except FileExistsError:
            pass

    def cuentas_csv(self):
        
        self.crear_csv_si_no_existe(self.fieldnames_cuentas, self.cuentas)
        return self.cuentas

    def usuarios_csv(self):
        
        self.crear_csv_si_no_existe(self.fieldnames_usuarios, self.usuarios)
        return self.usuarios

    def patrones_csv(self):
        
        self.crear_csv_si_no_existe(self.fieldnames_patrones, self.patrones)
        return self.patrones
    
    # Validacion de datos
    def check_usuario(cuenta, usuarios):
        usuario_existe = False

        with open(usuarios, mode='r') as usuarios:
            csv_reader = csv.DictReader(usuarios)

            for row in csv_reader:
                if row["accountID"] == cuenta:
                    usuario_existe = True

        return usuario_existe
    
    def check_email_existe(cuentas, email):
        existe_email = False

        with open(cuentas, mode='r') as cuentas:
            csv_reader = csv.DictReader(cuentas)
            for row in csv_reader:
                if row["email"]==email:
                    existe_email = True

        return existe_email

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

    # Asignar nuevas entradas
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

    def crear_patron_nuevo(patrones, nombre_patron, categorias, accountID):
        fieldnames = ["ruta_patron", "nombre_patron",  "accountID", "categorias"]
        ruta_patron = "unu"#crear_dir_patron("nombre_patron")
        patron = {fieldnames[0]:ruta_patron, fieldnames[1]:nombre_patron, fieldnames[2]:accountID, fieldnames[3]:categorias}
        with open(patrones, mode='a') as patrones:
            writer = csv.DictWriter(patrones, fieldnames=fieldnames)
            writer.writerow(patron)