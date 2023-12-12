import time
import sys
import mysql.connector
configuracion={
    'user':'root',
    'password':'12345',
    'host':'localhost',
    'raise_on_warnings':True,
}
def crear_db():
    for _ in range(15):
        sys.stdout.write("=")
        sys.stdout.flush()
        time.sleep(0.1)
    print("\n")
    print("Accediendo a MYSQL WORKBENCH")
    for _ in range(15):
        sys.stdout.write("=")
        sys.stdout.flush()
        time.sleep(0.1)
    print("\n")
    nombre=input("Ingresa Nombre de Base De Datos Destino A Crear: \n")
    try:
        connection=mysql.connector.connect(**configuracion)
        cursor=connection.cursor()
        cursor.execute(f"CREATE DATABASE {nombre};")
        
        print("Base De Datos Creada Correctamente\n")

        for _ in range(10):
            sys.stdout.write(">")
            sys.stdout.flush()
            time.sleep(0.1)
        print("\n")
        print("Ejecutando Script\n")
        for _ in range(10):
            sys.stdout.write("<")
            sys.stdout.flush()
            time.sleep(0.1)
        print("\n")
        ruta_script_destino='sqlmigration/archivos_sql/destino_migracion.sql'
        with open(ruta_script_destino,'r')as lineas_sintaxis:
            data=lineas_sintaxis.readlines()
            #datita=''.join(data)
            cursor.execute(f"USE {nombre};")
            linea_create=[linea.strip() for linea in data if not linea.startswith('INSERT')]
            data_create=''.join(linea_create)
            #print("LINEAS DE CREATE --->",linea_create)
            #print("LINEAS CREATE MOD--->",data_create)
            cursor.execute(data_create)
            #connection.commit()
            print("\n")
            connection_i=mysql.connector.connect(**configuracion)
            cursor_insert=connection_i.cursor()
            cursor_insert.execute(f'USE {nombre};')
            linea_insert=[linea.strip() for linea in data if linea.startswith('INSERT')]
            data_insert=''.join(linea_insert).replace(")I",");I")
            #data_insert.replace(")I",");I")
            print("\n")
            cursor_insert.execute(data_insert)
            #print("LINEAS INSERT --->",linea_insert)
            print("LINEA INSERT MOD--->",data_insert)
            """connection.commit()
            connection_i.commit()"""
        print("Migracion Exitosa !!!! SQL SERVER > MYSQL WORKBENCH")
        filas_insertadas=cursor_insert.rowcount
        print("FILAS REGISTRADAS: ",filas_insertadas)
    except mysql.connector.Error as err:
        print(f"Error {err}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            connection_i.close()
        
