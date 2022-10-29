import csv

class TablasCSV():
    """Crea un objeto csv
    """    
    def __init__(self, nombre_csv, fieldnames) -> None:
        
        self.nombre_csv = nombre_csv  
        self.fieldnames = fieldnames 
        self.crear_csv_si_no_existe()
    
    
    def crear_csv_si_no_existe(self):
        """Crea un archivo csv si no existe en la ubicacion dada
        """        

        try:
            with open(self.nombre_csv, "x") as tabla_csv:
                writer = csv.DictWriter(tabla_csv, fieldnames=self.fieldnames)
                writer.writeheader()

        except FileExistsError:
            pass        
    
    
    def check_dato(self, data:dict)->bool:
        """Revisa si un registro existe de acuerdo a un dato o una serie de datos 
        """        
        
        dato_existe = False

        with open(self.nombre_csv, mode='r') as tabla_csv:
            csv_reader = csv.DictReader(tabla_csv)

            for row in csv_reader:
                for key, value in data.items():
                    if row[key] == value:
                        dato_existe = True
                    else:
                        dato_existe = False
                if dato_existe == True:
                    break

        return dato_existe
    
    
    def get_registro(self, key:str, value:str)->dict:
        """Devuelve el valor del registro segun un identificador
        """        
        
        registro = {}
        
        with open(self.nombre_csv, mode='r') as tabla_csv:
            csv_reader = csv.DictReader(tabla_csv)

            for row in csv_reader:
                if row[key] == value:
                    registro = row

        return registro


    def crear_registro_nuevo(self,*args:any):
        """Adiciona un nuevo registro al final del csv
        """        
        
        registro = {}
        
        for n in range(len(self.fieldnames)):
            registro[self.fieldnames[n]] = args[n]

        with open(self.nombre_csv, mode='a') as tabla_csv:
            writer = csv.DictWriter(tabla_csv, fieldnames=self.fieldnames)
            writer.writerow(registro)
            
    
    def editar_registro(self,id:tuple,data:dict):
        """Edita un registro del archivo csv por reescritura
        de acuerdo a un identificador y la serie de datos que se desean modificar
        """        
        
        temp_csv = []
        
        with open(self.nombre_csv, mode='r') as tabla_csv:
            csv_reader = csv.DictReader(tabla_csv)
            for row in csv_reader:
                if row[id[0]] == id[1]:
                    for key, value in data.items():
                        row[key] = value
                temp_csv.append(row)
        
        with open(self.nombre_csv, "w") as tabla_csv:
                writer = csv.DictWriter(tabla_csv, fieldnames=self.fieldnames)
                writer.writeheader()
                writer.writerows(temp_csv)
    

    def eliminar_registro(self,data:dict):
        """Elimina un registro del archivo csv por medio de reescritura
        """        
        
        temp_csv = []
        
        with open(self.nombre_csv, mode='r') as tabla_csv:
            csv_reader = csv.DictReader(tabla_csv)
            for row in csv_reader:
                for key, value in data.items():
                    if row[key] != value:
                        temp_csv.append(row)
        
        with open(self.nombre_csv, "w") as tabla_csv:
                writer = csv.DictWriter(tabla_csv, fieldnames=self.fieldnames)
                writer.writeheader()
                writer.writerows(temp_csv)