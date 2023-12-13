
import time
import sys
import mysql.connector
import re   
configuracion={
    'user':'root',
    'password':'12345',
    'host':'localhost',
    'raise_on_warnings':True,
}








def crear_base_datos(nombre_base):
    print("CREANDO BASE")
    try:
        conectar=mysql.connector.connect(**configuracion)
        cursor=conectar.cursor()
        cursor.execute(f"CREATE DATABASE {nombre_base};")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error {err}")
def crear_tablas_base(nombre_base_tablas,tablas_script):
    print("CREANDO TABLAS")
    try:
        conexion=mysql.connector.connect(**configuracion)
        cursor=conexion.cursor()
        cursor.execute(f"USE {nombre_base_tablas};")
        cursor.execute(tablas_script)
        #cursor.execute("CREATE TABLE marca(id int,descripcion char(10));")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error {err}")

def insertar_data_tablas(nombre_base_datos_llenar,script_llenado_data):
    print("LLENANDO DATOS")
    try:
        conexion_tabla=mysql.connector.connect(**configuracion)
        cursor=conexion_tabla.cursor()
        cursor.execute(f"USE {nombre_base_datos_llenar};")
        cursor.execute(script_llenado_data)
        conexion_tabla.commit()
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error {err}")

def acceso_mysql_workbench():
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
        crear_base_datos(nombre)
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
            datita=''.join(data)
            
            #cursor=connection.cursor()
            linea_create=[linea.strip() for linea in data if not linea.startswith('INSERT')]
            data_create=''.join(linea_create)
            linea_insert=[linea.strip() for linea in data if linea.startswith('INSERT')]
            data_insert=''.join(linea_insert).replace(")I",");I")
            data_insert.replace(")I",");I")
            #print("LINEAS DE CREATE --->",linea_create)
            #print("LINEAS CREATE MOD--->",data_create)
            
        #cursor.execute(f"CREATE DATABASE {nombre};")
            #cursor.execute(f"USE {nombre};")
            #cursor.execute("SELECT CURRENT_DATE()")
            #print(data_insert)
            #cursor.execute(data_create)
            #cursor.execute(data_insert)
            #connection.commit()
            #print("\n")
            ##linea_insert=[linea.strip() for linea in data if linea.startswith('INSERT')]
            ##data_insert=''.join(linea_insert).replace(")I",");I")
            ##data_insert.replace(")I",");I")
            #patron_insert = re.compile(r'INSERT\s+[^;]+;')
            #coincidencias=patron_insert.findall(data_insert)
            #for sentencia in coincidencias:
            #    print("ES: ",sentencia)
                #connection_i=mysql.connector.connect(**configuracion)
                #cursor_insert=connection_i.cursor()
                #cursor_insert.execute(f'USE {nombre};')
            #    cursor.execute(f"USE {nombre};")
            #    cursor.execute(sentencia)
            ##cursor.execute(f"USE {nombre};")
            ##cursor.execute(data)
            ##connection.commit()
            ##filas_insertadas=cursor.rowcount
            ##print("filas registradas -->",filas_insertadas)
        crear_tablas_base(nombre,data_create)
        insertar_data_tablas(nombre)
    except:
        print(f"Error")
   