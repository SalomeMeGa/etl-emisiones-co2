import pandas as pd

def cargar_datos():
    ruta = 'data/raw/owid-co2-data.csv'
    df = pd.read_csv(ruta)
    return df

if __name__ == '__main__':
    df = cargar_datos()

    print(df.columns)