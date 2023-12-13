import time
import sys
import os_acceso.acceder_archivos as access
import migration_hub.acceso_base_datos as acceso_bd
print("===================")
print("BIENVENIDO")
for _ in range(35):
    sys.stdout.write("#")
    sys.stdout.flush()
    time.sleep(0.1)
print("\n")
print("SQL MIGRATION HUB IS READY!!!\n")
for _ in range(35):
    sys.stdout.write("#")
    sys.stdout.flush()
    time.sleep(0.1)
print("\n")
ruta_origen=input("Acceder a ruta de archivo origen a migrar: \n")
access.accederDocumento()
acceso_bd.acceso_mysql_workbench()
#acceso_bd.crear_base_datos()
#acceso_bd.crear_tablas_base()
#acceso_bd.insertar_data_tablas()
#acceso_bd.crear_db()
