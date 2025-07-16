import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def cargar_datos(ruta):
    
    #Carga archivo CSV y devuelve un DataFrame.
    return pd.read_csv(ruta)

def calcular_estadisticas(df, columna):
    
    # Calcula estadísticas básicas para una columna numérica.
    return {
        'media': df[columna].mean(),
        'desviacion_std': df[columna].std(),
        'maximo': df[columna].max(),
        'minimo': df[columna].min(),
        'mediana': df[columna].median(),
        'percentil_95': df[columna].quantile(0.95)
    }

def graficar_matplotlib(df, columna):
    
    #Devuelve figura Matplotlib del desplazamiento en el tiempo.
    fig, ax = plt.subplots()
    ax.plot(df.index, df[columna], marker='o', linestyle='-')
    ax.set_xlabel("Índice")
    ax.set_ylabel(columna)
    ax.set_title(f"Desplazamiento en el tiempo: {columna}")
    ax.grid(True)
    return fig

def graficar_plotly(df, columna):
    
    # Devuelve gráfico interactivo Plotly.
    fig = px.line(df, y=columna, title=f"Desplazamiento interactivo: {columna}")
    return fig


def graficar_todas_columnas(df, columnas):
    
    # Devuelve figura Plotly con todas las columnas numéricas graficadas en la misma figura.
    fig = px.line(df, y=columnas, title="Todas las columnas numéricas")
    return fig