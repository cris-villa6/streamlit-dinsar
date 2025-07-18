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
st.success(f"Archivo '{archivo}' cargado correctamente ✅")

# Mostrar DataFrame
if st.checkbox("Mostrar data"):
    st.dataframe(df)

# Seleccionar columna numérica
columnas_numericas = df.select_dtypes(include='number').columns.tolist()

if columnas_numericas:
    columna = st.selectbox("Columna de analisis", columnas_numericas)

    # Calcular estadísticas
    st.subheader("📊 Estadísticas básicas")
    stats = calcular_estadisticas(df, columna)
    st.write(stats)

    # Graficar con Matplotlib
    st.subheader("📈 Gráfico estatico")
    fig_mat = graficar_matplotlib(df, columna)
    st.pyplot(fig_mat)

    # Graficar interactivo con Plotly
    st.subheader("⚡ Gráfico interactivo")
    fig_plotly = graficar_plotly(df, columna)
    st.plotly_chart(fig_plotly)


      # Nueva opción: graficar todas las columnas
    if st.checkbox("Mostrar gráfico con todas las columnas numéricas"):
        st.subheader("🌐 Todas las columnas numéricas juntas")
        fig_all = graficar_todas_columnas(df, columnas_numericas)
        st.plotly_chart(fig_all)

else:
    st.warning("⚠️ No se encontraron columnas numéricas en este archivo.")

st.sidebar.info("Universidad Técnica Particular de Loja - Geología")
