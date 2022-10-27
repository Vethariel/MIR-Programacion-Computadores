import Cuenta

class Usuario(Cuenta.Cuenta):
    
    def __init__(self) -> None:
        self.nombres = ""
        self.apellidos = ""
        self.nickname = ""
        self.fecha_de_nacimiento = ""