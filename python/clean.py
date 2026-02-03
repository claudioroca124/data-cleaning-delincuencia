# Importamos las librerias que vamos a utilizar
import pandas as pd

# Cargamos el dataset en un dataframe
delincuencia_data = pd.read_csv("data/delitos_2024.csv")

# Damos un primer vistazo a los datos
print(delincuencia_data.head(10))

# Vemos la información del DataFrame
print(delincuencia_data.info())

# Hacemos un chequeo del año para estar seguros de que todos los datos correspondan a 2024 y podamos eliminar la columna con seguridad
print(delincuencia_data['anio'].unique())

# Hacemos una versión sólo con las columnas que nos interesan.
# eliminando las inecesarias
delincuencia_data_clean = delincuencia_data.drop(columns=[
    'id-mapa',
    'anio',
    'subtipo',
    'comuna',
    'latitud',
    'longitud',
    'cantidad'
])

# Comprobamos que todo haya salido bien
print(delincuencia_data_clean.info())


# Observamos los valores de las columnas tipo y barrio para buscar inconsistencias
print(delincuencia_data_clean['mes'].unique())
print(delincuencia_data_clean['tipo'].unique())
print(delincuencia_data_clean['barrio'].unique())

# Vemos la cantidad de datos nulos en cada columna
for columna in delincuencia_data_clean.columns:
    print(f'La cantidad de datos nulos en la columna {columna} es {delincuencia_data_clean[columna].isnull().sum()}')

# Cambiamos los datos nulos por 'n/d' (no disponible) y chequeamos la informacion
delincuencia_data_clean.fillna({
    'franja': 'n/d',
    'barrio': 'n/d'
}, inplace=True)

print(f"La cantidad de nulos en la columna 'franja' es de {delincuencia_data_clean['franja'].isna().sum()}\n" \
    f"La cantidad de nulos en la columna 'barrio' es de {delincuencia_data_clean['barrio'].isna().sum()}")

# Guardamos los datos limpios
delincuencia_data_clean.to_csv("data/delincuencia_clean.csv")

