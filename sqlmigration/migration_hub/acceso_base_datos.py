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
        cursor.execute(f"USE {nombre};")
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
        ruta_script_destino='sqlmigration/archivos_sql/destino_migracion.sql'
        with open(ruta_script_destino,'r')as lineas_sintaxis:
            data=lineas_sintaxis.readline()
            cursor.execute(data)
            connection.commit()
        print("Migracion Exitosa !!!! SQL SERVER > MYSQL WORKBENCH")
    except mysql.connector.Error as err:
        print(f"Error {err}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
        
