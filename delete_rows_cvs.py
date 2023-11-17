import os
import pandas as pd

carpeta = "your_rout_goes_here"

archivos = os.listdir(carpeta)

for archivo in archivos:
    if archivo.endswith('.csv'):  
        ruta_archivo = os.path.join(carpeta, archivo)

        try:
            # Get the file size to check if it's empty
            file_size = os.path.getsize(ruta_archivo)
            if file_size > 0:
                # Attempt to read the CSV file
                df = pd.read_csv(ruta_archivo, sep=';', skiprows=1)#You need to reset the quantity of rows
                
                # Check if the DataFrame is empty
                if not df.empty:
                    # Perform operations on the DataFrame if needed
                    # For example, you can process or modify the DataFrame here
                    
                    df.to_csv(ruta_archivo, index=False)

                    print(f"Se procesó y modificó {archivo}")
                else:
                    print(f"El archivo {archivo} no tiene datos válidos")
            else:
                print(f"El archivo {archivo} está vacío")
        except pd.errors.EmptyDataError:
            print(f"El archivo {archivo} está vacío o no tiene datos válidos")

print("Proceso completado.")