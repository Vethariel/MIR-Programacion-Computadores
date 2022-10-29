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
    
    
    def check_dato(self, dict:dict):
        """Revisa si un registro existe de acuerdo a un dato o una serie de datos 

        Args:
            dict (dict): Datos a verificar 

        Returns:
            bool: Valor si encuentra o no el registro
        """        
        
        dato_existe = False

        with open(self.nombre_csv, mode='r') as tabla_csv:
            csv_reader = csv.DictReader(tabla_csv)

            for row in csv_reader:
                for key, value in dict.items():
                    if row[key] == value:
                        dato_existe = True
                    else:
                        dato_existe = False
                if dato_existe == True:
                    break

        return dato_existe
    
    
    def get_registro(self, key:str, value:str):
        """Devuelve el valor del registro segun un identificador

        Args:
            key (string): Nombre del campo del identificador
            value (string): Valor del identificador

        Returns:
            diccionario: Registro indicado del csv
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
        
        Args:
            *args: Recibe una cantidad variable de datos que va en orden 
            de acuerdo a los fieldnames
        """        
        
        registro = {}
        
        for n in range(len(self.fieldnames)):
            registro[self.fieldnames[n]] = args[n]

        with open(self.nombre_csv, mode='a') as tabla_csv:
            writer = csv.DictWriter(tabla_csv, fieldnames=self.fieldnames)
            writer.writerow(registro)
    

    def eliminar_registro(self,dict:dict):
        """Elimina un registro del archivo csv por medio de reescritura

        Args:
            dict (diccionario): Recibe la clave y el valor que se excluira.
            Recibe multiples datos.
        """        
        
        temp_csv = []
        
        with open(self.nombre_csv, mode='r') as tabla_csv:
            csv_reader = csv.DictReader(tabla_csv)
            for row in csv_reader:
                for key, value in dict.items():
                    if row[key] != value:
                        temp_csv.append(row)
        
        with open(self.nombre_csv, "w") as tabla_csv:
                writer = csv.DictWriter(tabla_csv, fieldnames=self.fieldnames)
                writer.writeheader()
                writer.writerows(temp_csv)