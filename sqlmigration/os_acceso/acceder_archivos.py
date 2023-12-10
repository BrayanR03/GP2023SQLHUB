import os
from archivos_sql import * 

def accederDocumento():
    try:
        extension='.sql'
        ruta='sqlmigration/archivos_sql/'
        ruta_completa=os.path.join(ruta,'.')
        archivos = [archivo for archivo in os.listdir(ruta_completa) if archivo.endswith(extension)]
    
        for indice,archivo in enumerate(archivos):
            print(indice,archivo)
        while True:
            archivo_a_trasladar=input("Elige un archivo a migrar: \n")
            if archivo_a_trasladar==archivo:
                print("Existe")
                break
            else:
                print("¡No existe el archivo!")
                           
    except:
        print("No es un comando valido")
