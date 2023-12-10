import os
from archivos_sql import * 
import migration_hub.sql_mysql as func_translation
def accederDocumento():
    try:
        extension='.sql'
        ruta='sqlmigration/archivos_sql/'
        ruta_completa=os.path.join(ruta,'.')
        archivos = [archivo for archivo in os.listdir(ruta_completa) if archivo.endswith(extension)]
        lista_archivos_sql=[]
        for indice,archivo in enumerate(archivos):
            print(indice,archivo)
            lista_archivos_sql.append(archivo)
        while True:
            archivo_a_trasladar=input("Elige un archivo a migrar: \n")
            try:
                indice_archivo=int(archivo_a_trasladar)
                if 0<= indice_archivo< len(lista_archivos_sql):
                    archivo_seleccionado=archivos[indice_archivo]
                    func_translation.migration_convertion(archivo_seleccionado)
                    break
                else:
                    print("Indice de Archivo No Encontrado")

            except:
                print("¡No existe el archivo!")
                           
    except:
        print("No es un comando valido")
