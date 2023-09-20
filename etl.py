import pandas as pd

<<<<<<< HEAD
# ETL: Extract, Transform, Load

# Ruta al archivo CSV de origen
archivo_origen = "g3etl/data.csv"
=======

# ETL: Extract, Transform, Load

# Ruta al archivo CSV de origen
archivo_origen = "g3etl\data.csv"
>>>>>>> Daniela_Florez

# Leer los datos desde el archivo CSV y especificar que la primera fila es el encabezado
datos = pd.read_csv(archivo_origen, delimiter=';', header=0)

# Verificar los primeros registros
print(datos.head())
print(datos.columns)
# Agregar una nueva columna 'suma' que contenga la suma de dos columnas existentes
# Asumiendo que las columnas se llaman 'columna1' y 'columna2' en tu archivo CSV
datos['suma'] = datos['columna1'] + datos['columna2']
<<<<<<< HEAD
=======
datos['resta'] = datos['columna1'] - datos['columna2']
datos['multiplicación'] = datos['columna1'] * datos['columna2']
datos['Par_Impar'] = ['Par' if resultado % 2 == 0 else 'Impar' for resultado in datos['multiplicación']]
>>>>>>> Daniela_Florez

# Verificar los cambios
print(datos.head())

# Ruta al archivo CSV de destino
archivo_destino = "datos_transformados.csv"

# Guardar los datos transformados en un nuevo archivo CSV
datos.to_csv(archivo_destino, index=False)

# Verificar que se haya guardado correctamente
print(f"Los datos transformados se han guardado en {archivo_destino}")

<<<<<<< HEAD
datos['resta'] = datos['columna1'] - datos['columna2']
datos['multiplicacion'] = datos['columna1'] * datos['columna2']
datos['division'] = datos['columna1'] / datos['columna2']

print(datos.head())
archivo_destino = "datos_transformados.csv"

datos['Paridad']=['0' if resultado % 2==0 else '1' for resultado in datos['multiplicacion']]
print(datos.head())
archivo_destino = "datos_transformados.csv"
datos.to_csv(archivo_destino, index=False)
    


    
=======

>>>>>>> Daniela_Florez
