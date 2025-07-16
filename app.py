import streamlit as st
import pandas as pd
from utils import cargar_datos, calcular_estadisticas, graficar_matplotlib, graficar_plotly, graficar_todas_columnas

# Título principal
st.title("Análisis de desplazamientos en Ciudad Victoria | Loja ")

# Sidebar para seleccionar archivo
st.sidebar.header("Datos")
archivo = st.sidebar.selectbox(
    "Selecciona los datos a analizar",
    ("Corrida_1.csv", "Corrida_2.csv", "Corrida_3.csv")
)

ruta_archivo = f"data/{archivo}"

# Cargar datos
df = cargar_datos(ruta_archivo)
st.success(f"Archivo '{archivo}' cargado correctamente ✅") # Mensaje de confirmación 
