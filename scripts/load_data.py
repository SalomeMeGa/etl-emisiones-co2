import os
import pandas as pd

def guardar_datos(df, nombre_archivo='data/processed/owid_co2_processed.csv'):
    # Crear carpeta si no existe
    carpeta = os.path.dirname(nombre_archivo)
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    
    # Guardar dataframe en CSV
    df.to_csv(nombre_archivo, index=False)
    print(f"Datos guardados en {nombre_archivo}")



def extraer_datos_procesados():
    ruta_procesada = os.path.join('data','processed', 'owid_co2_processed.csv')

    if not os.path.exists(ruta_procesada):
        raise FileNotFoundError(f"No se encontro el alrchivo procesado en: {ruta_procesada}")
    
    return pd.read_csv(ruta_procesada)
