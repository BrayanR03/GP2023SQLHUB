import time
import sys
import os_acceso.acceder_archivos as access

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
