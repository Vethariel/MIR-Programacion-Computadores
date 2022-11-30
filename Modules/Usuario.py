import Modules.Cuenta as Cuenta
from Modules.TablasCSV import TablasCSV

class Usuario(Cuenta.Cuenta):
    """Crea un objeto usuario y hereda de la clase Cuenta
    """    
    def __init__(self) -> None:
        
        self.nombres = ""
        self.apellidos = ""
        self.nickname = ""
        self.fecha_de_nacimiento = ""
    
    
    def check_info(self, usuarios:TablasCSV)->bool:
        """Verifica que el usuario este registrado en el archivo csv de usuarios.
        Si lo esta, asigna los datos a este objeto
        """        
        datos_usuario = usuarios.check_dato({"accountID":self.accountID})
        
        if datos_usuario:
            
            info_usuario = usuarios.get_registro("accountID",self.accountID)
            self.nombres = info_usuario["nombres"]
            self.apellidos = info_usuario["apellidos"]
            self.nickname = info_usuario["nickname"]
            self.fecha_de_nacimiento = info_usuario["fecha_nacimiento"]
        
        return datos_usuario
            
    
    def crear_info(self, usuarios:TablasCSV, nombres:str,
                   apellidos:str,nickname:str,fecha_nacimiento:str):
        """Agrega un nuevo registro en el archivo csv de usuarios
        y asigna los datos a este objeto
        """        
        
        usuarios.crear_registro_nuevo(nombres,apellidos,nickname,fecha_nacimiento,self.accountID)
        self.nombres = nombres
        self.apellidos = apellidos
        self.nickname = nickname
        self.fecha_de_nacimiento = fecha_nacimiento
    
    def eliminar_usuario(self,usuarios:TablasCSV):
        """Elimina al usuario del registro del archivo csv de usuarios
        """        
        
        usuarios.eliminar_registro({"accountID":self.accountID})
        self.nombres = ""
        self.apellidos = ""
        self.nickname = ""
        self.fecha_de_nacimiento = ""
    
    def vaciar_usuario(self):
        """Desocupa este objeto para ser usado en otras instancias
        """        
        
        self.email = ""
        self.contra = ""
        self.accountID = ""
        self.nombres = ""
        self.apellidos = ""
        self.nickname = ""
        self.fecha_de_nacimiento = ""
    
    def editar_usuario(self, usuarios:TablasCSV, nombres:str,apellidos:str,nickname:str,fecha_nacimiento:str):
        
        self.nombres = nombres
        self.apellidos = apellidos
        self.nickname = nickname
        self.fecha_de_nacimiento = fecha_nacimiento
        
        datos = {"nombres":nombres,"apellidos":apellidos,"nickname":nickname,"fecha_nacimiento":fecha_nacimiento}
            
        usuarios.editar_registro(("accountID",self.accountID),datos)