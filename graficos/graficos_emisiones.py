import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def grafico_emisiones_totales(df, pais):
    st.subheader(f"🌍 Emisiones Totales de CO₂ - {pais}")
    df_pais = df[df["country"] == pais]
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=df_pais, x="year", y="co2", ax=ax, color="blue")
    ax.set_ylabel("Millones de toneladas (Mt)")
    ax.set_xlabel("Año")
    ax.set_title(f"Evolución de emisiones de CO₂ en {pais}")
    st.pyplot(fig)

def grafico_co2_per_capita(df, pais):
    st.subheader(f"👤 Emisiones per cápita - {pais}")
    df_pais = df[df["country"] == pais]
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=df_pais, x="year", y="co2_per_capita", ax=ax, color="green")
    ax.set_ylabel("Toneladas por persona")
    ax.set_xlabel("Año")
    ax.set_title(f"Evolución de CO₂ per cápita en {pais}")
    st.pyplot(fig)

def grafico_pib_vs_co2(df, pais):
    st.subheader(f"💰 Relación PIB vs CO₂ - {pais}")
    df_pais = df[df["country"] == pais]
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.scatterplot(data=df_pais, x="gdp", y="co2", ax=ax)
    ax.set_xlabel("PIB (USD)")
    ax.set_ylabel("Emisiones de CO₂ (Mt)")
    ax.set_title(f"PIB vs Emisiones de CO₂ en {pais}")
    st.pyplot(fig)
