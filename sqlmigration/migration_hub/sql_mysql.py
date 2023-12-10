def migration_convertion(archivo_origen):
    try:
       archivo_txt=archivo_origen.replace('.sql','.txt')
       
       with open(archivo_origen,'r')as origen:
           contenido_sql=origen.read()

       with open(archivo_txt,'w')as destino_origen:
           destino_origen.write(contenido_sql)

       with open(archivo_txt,'r')as archivo_txt_lectura:
           contenido_txt=archivo_txt_lectura.read()
           print(contenido_txt) 
    except:
        print("Error de lectura de archivo")
    