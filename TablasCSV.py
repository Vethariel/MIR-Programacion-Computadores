import csv

class TablasCSV():
    def __init__(self, nombre_csv, fieldnames) -> None:
        
        self.nombre_csv = nombre_csv  
        self.fieldnames = fieldnames   
    
    # Inicializar tabla
    def crear_csv_si_no_existe(self):

        try:
            with open(self.nombre_csv, "x") as tabla_csv:
                writer = csv.DictWriter(tabla_csv, fieldnames=self.fieldnames)
                writer.writeheader()

        except FileExistsError:
            pass        
    
    # Validacion de datos
    def check_dato(self, *args, **kwargs):
        
        dato_existe = False

        with open(self.nombre_csv, mode='r') as tabla_csv:
            csv_reader = csv.DictReader(tabla_csv)

            for row in csv_reader:
                for key, value in kwargs.items():
                    if row[key] == value:
                        dato_existe = True
                    else:
                        dato_existe = False

        return dato_existe
    
    # Obtencion de datos
    def get_registro(self, key, value):
        
        registro = {}
        
        with open(self.nombre_csv, mode='r') as tabla_csv:
            csv_reader = csv.DictReader(tabla_csv)

            for row in csv_reader:
                if row[key] == value:
                    registro = row

        return registro

    # Crear nuevas entradas
    def crear_registro_nuevo(self,*args):
        
        registro = {}
        
        for n in range(len(self.fieldnames)):
            registro[self.fieldnames[n]] = args[n]

        with open(self.nombre_csv, mode='a') as tabla_csv:
            writer = csv.DictWriter(tabla_csv, fieldnames=self.fieldnames)
            writer.writerow(registro)