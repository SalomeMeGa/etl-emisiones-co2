import os
import pandas as pd

def extraer_datos():
    ruta_archivo = os.path.join("data", "raw", "owid-co2-data.csv")

    if not os.path.exists(ruta_archivo):
        raise FileNotFoundError(f"No se encontró el archivo en: {ruta_archivo}")

    df = pd.read_csv(ruta_archivo)
    return df


