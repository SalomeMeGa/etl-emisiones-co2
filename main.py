import sys
import os

# Agregar carpeta scripts al path para importar los módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "scripts")))

from extract_data import extraer_datos
from transform_data import transformar_datos

# Importamos la función de carga si la creas
from load_data import guardar_datos  # Asegúrate que exista scripts/load_data.py

def main():
    # Extracción
    df_original = extraer_datos()
    print("Datos extraídos")

    # Transformación
    df_transformado = transformar_datos(df_original)
    print("Datos transformados")

    # Carga
    guardar_datos(df_transformado)
    print("Datos guardados")

    # Mostrar datos transformados
    print(df_transformado.head())

if __name__ == "__main__":
    main()
