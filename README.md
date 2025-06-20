# 📊 Proyecto ETL - Anàlisis de EMisiones de CO2

## Descripciòn

Este proyecto tiene como objetivo desarrollar un pipeline ETL (Extract, Transform, Load) en Python para analizar los niveles de emisiones de co2 por paìs y sector econòmico.

Trabajaremos con fuentes de datos abiertas, haciendo limpieza, transformacioǹ, visualizaciòn y publicaciòn de los resultados. EL proyecto busca aplicar habilidades practicas de ingenierìa de datos.

## 📚 Tabla de Contenidos

- [🎯 Objetivo](#-objetivo)
- [🧰 Tecnologías Utilizadas](#-tecnologías-utilizadas)
- [📁 Estructura del Proyecto](#-estructura-del-proyecto)
- [⚙️ Instalación y Ejecución](#️-instalación-y-ejecución)
- [🧼 Limpieza y Preparación de Datos](#-limpieza-y-preparación-de-datos)
- [📊 Visualizaciones Incluidas](#-visualizaciones-incluidas)
- [🎛️ Interacción](#️-interacción)
- [🧪 Requisitos del Entorno](#-requisitos-del-entorno)
- [🚀 Futuras Mejoras](#-futuras-mejoras)
- [📌 Consideraciones Finales](#-consideraciones-finales)
- [🧠 Autor(a)](#-autora)

---


## 🎯 Objetivo
- Extraer datos de emisiones desde la fuente "Our Worl in Date".
- Transformar y limpiar los datos para facilitar su anàlisis.
- Cargar y vusualizar la informaciòn procesada en un dashboard interactivo.
- Permitir filtrado y anàlisis comparativo por paìas, año, emisiones per càpita y PIB.
- Publicar el proyecto en GitHub como portafolio profesional


## 🧰Tecnologias

- **Lenguajes**: Python 3.12+
- **Entorno virtual**: emisiones
- **Librerias**:
- Pandas
- Matplotlib / Seaborn
- Jupyter Notebooks (para anaàlisis exploratorio)
- Streamlit (opcional, para dashboards)
- **Visual Studio Code**: Como editor
- **Control de versiones**: Git / GitHub


## 📁Estructura del Proyecto

etl_emisiones_co2/
- data/
raw/ processed/
- notebooks/ 
analisis.ipynb
- scripts/
extract_data.py/transform_data.py/load_data.py
-graficos/
graficos_emisiones.py
- app.py
- main.py
- requirements.txt
- README.md


## ⚙️ Instalación y Ejecución

1. Clona este repositorio:
```bash
git clone https://github.com/usuario/etl_emisiones_co2.git
cd analisis_datos_publicos

```
2. Crea un entorno virtual:
```bash
python -m venv emisiones
source emisiones/bin/activate  
``` 
3. Instala las dependencias
```bash
pip install -r requirements.txt
```
4. Ejecuta el dashboard
```bash
streamlit run app.py
```
---

## 🧼 Limpieza y Preparación de Datos

Los datos originales fueron tratados para:

- Eliminar filas con paìses nulos
- FIltrar solo columnas relevantes
- ELiminar filas con datos faltantes
- Filtrar años a partir del 2000

## 📊 Visualizaciones Incluidas

- Indicadores clave
- Emisiones totales por paìs
- Emisiones por càpita
- Evoluciòn històrica de emisiones
- comparaciòn entre PIB y emisiones

## 🎛️ Interacción

   - Puedes filtrar por el paìs que asi se considere analizar del lado superior izquierdo del Dashboard.
   - Layout optimizado para pantallas grandes (layout="wide").


## 🧪 Requisitos del Entorno

Contenido de requirements.txt

streamlit==1.35.0
pandas
matplotlib
seaborn
....

## 🚀 Futuras Mejoras

- Integraciòn con base de datos PostgreSQL
- Implementaciòn de filtros avanzados
- Comparaciòn entre regiones o continentes
- Exportaciòn de resultados a PDF o Excel
- Despliegue en la nube con Streamlit Cloud o Heroku.


## 📌 Consideraciones Finales

- Fuente: Our World in Data - CO2 and Greenhouse Gas Emissions
- El sistema está preparado para escalar con nuevos conjuntos de datos o filtros más complejos.
- Las gráficas están diseñadas para ser simples, interpretables y efectivas para usuarios no técnicos.


## 🧠 Autor(a)

    Nombre: Alberto Mendoza Garcìa
    Correo: [ing.albertomendozagarcia@gmail.com]
    Última actualización: 20 Junio 2025