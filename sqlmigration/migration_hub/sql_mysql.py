def migration_convertion(archivo):
    try:
        #print("Lectura correcta de archivo")
        with open(archivo, "r") as archivo_origen:
            lineas = archivo_origen.readlines()

        lineas = lineas[12:]

        sql_script = ''.join(lineas)
            
        sql_script=sql_script.replace("AS","BEGIN").replace("as","begin")
        sql_script=sql_script.replace("GO","")
        sql_script=sql_script.replace("[dbo].","").replace("[","").replace("]","")
        sql_script=sql_script.replace("IDENTITY(1,1)","PRIMARY KEY AUTO_INCREMENT")
        sql_script=sql_script.replace("nvarchar","varchar")
        sql_script=sql_script.replace("numeric","").replace("decimal","")
        sql_script=sql_script.replace("WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]", "")    
        sql_script=sql_script.replace("GETDATE()","CURRENT_TIMESTAMP()")


        lineas = sql_script.split('\n')
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
            
            archivo_saliente='sqlmigration/archivos_sql/destino_migracion.sql'
            with open(archivo_saliente, "w") as archivo_saliente:
                archivo_saliente.write(sql_script)
            print("Script transformado")
    except:
        print("Error de lectura de archivo")
    