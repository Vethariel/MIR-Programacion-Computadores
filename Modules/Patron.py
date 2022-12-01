import pickle

class Patron():
    def __init__(self) -> None:
        self.titulo = ""
        self.categorias = []
        self.materiales = []
        self.abreviaturas = []
        self.pasos = []
    
    def escribir_patron(self,titulo,categorias,materiales,abreviaturas,pasos,patrones):
        self.titulo = titulo
        self.categorias = categorias
        self.materiales = materiales
        self.abreviaturas = abreviaturas
        self.pasos = pasos
        with open(f"Patrones/Patrones.txt","wb") as file:
            patrones.append(self)
            pickle.dump(patrones,file)
    
    def editar_patron(self,titulo,categorias,materiales,abreviaturas,pasos,patrones):
        self.titulo = titulo
        self.categorias = categorias
        self.materiales = materiales
        self.abreviaturas = abreviaturas
        self.pasos = pasos
        with open(f"Patrones/Patrones.txt","wb") as file:
            pickle.dump(patrones,file)
    
    def eliminar_patron(self,patrones):
        patrones.remove(self)
        with open(f"Patrones/Patrones.txt","wb") as file:
            pickle.dump(patrones,file)

def leer_patron():
    try:
        with open(f"Patrones/Patrones.txt","rb") as file:
            patrones = pickle.load(file)
    except:
        patrones = []
    return patrones