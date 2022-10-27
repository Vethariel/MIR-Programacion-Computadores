import Cuenta

class Usuario(Cuenta.Cuenta):
    
    def __init__(self) -> None:
        
        self.nombres = ""
        self.apellidos = ""
        self.nickname = ""
        self.fecha_de_nacimiento = ""
    
    
    def check_info(self, usuarios):
        
        datos_usuario = usuarios.check_dato({"accountID":self.accountID})
        
        if datos_usuario:
            
            info_usuario = usuarios.get_registro("accountID",self.accountID)
            self.nombres = info_usuario["nombres"]
            self.apellidos = info_usuario["apellidos"]
            self.nickname = info_usuario["nickname"]
            self.fecha_de_nacimiento = info_usuario["fecha_nacimiento"]
        
        return datos_usuario
            
    
    def crear_info(self, usuarios, nombres,apellidos,nickname,fecha_nacimiento):
        
        usuarios.crear_registro_nuevo(nombres,apellidos,nickname,fecha_nacimiento,self.accountID)
        self.nombres = nombres
        self.apellidos = apellidos
        self.nickname = nickname
        self.fecha_de_nacimiento = fecha_nacimiento