import sys
import os
import streamlit as st

# Configurar importaciones desde scripts/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from scripts.load_data import extraer_datos_procesados
from graficos.graficos_emisiones import (
    grafico_emisiones_totales,
    grafico_co2_per_capita,
    grafico_pib_vs_co2
)

# Configuración de la página
st.set_page_config(page_title="Emisiones CO₂", layout="wide", page_icon="🌍")

# Título y descripción
st.title("🌿 Dashboard de Emisiones de CO₂")
st.markdown("Este panel interactivo muestra las emisiones de CO₂ por país a lo largo del tiempo utilizando datos de Our World in Data.")

# Cargar y transformar datos
df = extraer_datos_procesados()

# Sidebar para selección de país
paises = sorted(df["country"].unique())
pais_seleccionado = st.sidebar.selectbox("🌐 Selecciona un país", paises)

# Mostrar métricas ejecutivas
st.markdown("### 🔍 Indicadores clave")
ultimo = df[df["country"] == pais_seleccionado].sort_values("year").iloc[-1]
col1, col2, col3 = st.columns(3)
col1.metric("CO₂ Total", f"{ultimo['co2']:,.2f} Mt")
col2.metric("CO₂ per cápita", f"{ultimo['co2_per_capita']:.2f} t/persona")
col3.metric("PIB", f"${ultimo['gdp']/1e9:.2f} B USD")

# Gráficos
grafico_emisiones_totales(df, pais_seleccionado)
grafico_co2_per_capita(df, pais_seleccionado)
grafico_pib_vs_co2(df, pais_seleccionado)
