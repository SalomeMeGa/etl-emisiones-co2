def transformar_datos(df):
    # Eliminar filas con países nulos
    df = df[df['country'].notna()]

    # Filtrar solo columnas relevantes
    columnas_interes = ['country', 'year', 'co2', 'co2_per_capita', 'gdp']
    df_filtrado = df[columnas_interes]

    # Eliminar filas con datos faltantes
    df_filtrado = df_filtrado.dropna()

    # Filtrar años a partir del 2000
    df_filtrado = df_filtrado[df_filtrado['year'] >= 2000]

    return df_filtrado
