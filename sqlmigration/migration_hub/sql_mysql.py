def migration_convertion(archivo_origen):
    try:
        ruta_origen_migracion='sqlmigration/archivos_sql/'+archivo_origen
        ruta_origen_migracion_txt='sqlmigration/archivos_txt/origen_migracion.txt'
        ruta_destino_migracion_txt='sqlmigration/archivos_txt/destino_migracion.txt'
        ruta_destino_migracion='sqlmigration/archivos_sql/destino_migracion.sql'
        with open(ruta_origen_migracion,'r')as lectura_origen:
            lineas=lectura_origen.read()
            with open(ruta_origen_migracion_txt,'w')as escritura_origen_txt:
                escritura_origen_txt.write(lineas)
        with open(ruta_origen_migracion_txt,'r')as lectura_origen_txt:
            lineas_txt=lectura_origen_txt.readlines()
        lineas_txt=lineas_txt[12:]
        sql_script=''.join(lineas_txt)
        sql_script=sql_script.replace("AS","BEGIN").replace("as","begin")
        #sql_script=sql_script.replace("GO","")
        sql_script=sql_script.replace("[dbo].","").replace("[","").replace("]","")
        sql_script=sql_script.replace("IDENTITY(1,1)","PRIMARY KEY")
        sql_script=sql_script.replace("nvarchar","varchar")
        sql_script=sql_script.replace("numeric","").replace("decimal","")
        sql_script=sql_script.replace("WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]", "")    
        sql_script=sql_script.replace("GETDATE()","CURRENT_TIMESTAMP()")

        lineas=sql_script.split('\n')
        for i, linea in enumerate(lineas):
            if "CONSTRAINT" in linea:
                lineas[i] = ");"
                for j in range(i+1, min(i + 10, len(lineas))):
                    lineas[j] = ""
        for i, linea in enumerate(lineas):
            if ");" in linea:
                lineas[i-1] = lineas[i-1].replace(",","")

        lineas = [linea for linea in lineas if linea.strip() != ""]            
        sql_script = '\n'.join(lineas)

        sql_script = sql_script.replace("CREATE PROCEDURE", "DELIMITER $$\nCREATE PROCEDURE")
        sql_script = sql_script.replace("CREATE TRIGGER", "DELIMITER $$\nCREATE TRIGGER")
        sql_script = sql_script.replace("CREATE FUNCTION", "DELIMITER $$\nCREATE FUNCTION")
        
        #nuevas_lineas=sql_script[24:]
        with open(ruta_destino_migracion_txt,'w')as escritura_destino_txt:
            data=escritura_destino_txt.write(sql_script)
        with open(ruta_destino_migracion_txt,'r')as lectura_destino_:
            lineas_lect=lectura_destino_.read()
            with open(ruta_destino_migracion,'w')as escritura_destino_sql:
                escritura_destino_sql.write(lineas_lect)
            
        print("SINTAXIS TRANSFORMADA CORRECTAMENTE!!!")        
    except:
        print("Error al leer el archivo")
