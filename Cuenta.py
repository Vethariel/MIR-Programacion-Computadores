import hashlib
import re
import string
import uuid

from TablasCSV import TablasCSV

class Cuenta():
    """Crear un objeto cuenta
    """    
    def __init__(self) -> None:
        
        self.email = ""
        self.contra = ""
        self.accountID = ""
        
    
    def check_ingreso(self, cuentas:TablasCSV, email:str, contra:str)->bool:
        """Verifica que la cuenta existe en el archivo csv.
        Si lo esta, asigna los datos a este objeto
        """        
        contra_hash = codificar_contra(contra)
        cuenta_valida = cuentas.check_dato({"email":email,"contra":contra_hash})
        
        if cuenta_valida:
            
            cuenta = cuentas.get_registro("email",email)
            self.email = cuenta["email"]
            self.contra = cuenta["contra"]
            self.accountID = cuenta["accountID"]
        
        return cuenta_valida
    
    
    def eliminar_cuenta(self, cuentas:TablasCSV):
        """Elimina la cuenta del registro en el csv y vacia este objeto
        """        
        
        cuentas.eliminar_registro({"accountID":self.accountID})
        self.email = ""
        self.contra = ""
        self.accountID = ""
    
    def editar_cuenta(self, cuentas:TablasCSV, email:str, contra:str):
        """Modifica el valor del registro en el archivo csv de cuentas 
        y actualiza los valores de este objeto
        """        
        self.email = email
        
        cod_contra = codificar_contra(contra)
        self.contra = cod_contra
            
        cuentas.editar_registro(("accountID",self.accountID),{"email":email,"contra":cod_contra})
    
# Misc 

def crear_cuenta_nueva(cuentas:TablasCSV, email:str, contra:str):
    """Asigna un nuevo registro en el archivo csv de cuentas
    """    
    
    contra_hash = codificar_contra(contra)
    uid = uuid.uuid1()
    cuentas.crear_registro_nuevo(email,contra_hash,uid)
        
        
def codificar_contra(contra:str)->str:
    """Codifica la contrasenna en hexadecimal
    """    
    
    auth = contra.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    
    return auth_hash


def check_email_valido(email:str)->bool:
    """Verifica si el correo cumple con el formato estandar
    """    
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email_valido = re.match(pat,email)

    return not email_valido


def check_email_existe(cuentas:TablasCSV, email:str)->bool:
    """Verifica si el email existe en el archivo csv de cuentas
    """    
    cuenta_existe = cuentas.check_dato({"email":email})
    
    return cuenta_existe


def check_contra_valida(contra:str)->bool:
    """Verifica si la contraseña cumple con los requerimientos - 
    minimo 8 caracteres, una mayuscula, una minuscula, un numero y 
    un simbolo
    """    
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