import hashlib
import re
import string
import uuid

class Cuenta():
    
    def __init__(self) -> None:
        
        self.email = ""
        self.contra = ""
        self.accountID = ""
        
    
    def check_ingreso(self, cuentas, email, contra):
        
        contra_hash = codificar_contra(contra)
        cuenta_valida = cuentas.check_dato({"email":email,"contra":contra_hash})
        
        if cuenta_valida:
            
            cuenta = cuentas.get_registro("email",email)
            self.email = cuenta["email"]
            self.contra = cuenta["contra"]
            self.accountID = cuenta["accountID"]
        
        return cuenta_valida
    
# Misc 

def crear_cuenta_nueva(cuentas, email, contra):
    
    contra_hash = codificar_contra(contra)
    uid = uuid.uuid1()
    cuentas.crear_registro_nuevo(email,contra_hash,uid)
        
        
def codificar_contra(contra):
    
    auth = contra.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    
    return auth_hash


def check_email_valido(email):
    
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email_valido = re.match(pat,email)

    return not email_valido


def check_email_existe(cuentas, email):
    
    cuenta_existe = cuentas.check_dato({"email":email})
    
    return cuenta_existe


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