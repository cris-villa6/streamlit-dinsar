Aplicación Web DInSAR para Monitoreo de Desplazamientos del Terreno
📋 Descripción del Proyecto
Esta aplicación web interactiva está diseñada para el análisis y seguimiento de desplazamientos del terreno en Ciudad Victoria, Loja, Ecuador, utilizando datos recolectados mediante la técnica DInSAR (Interferometría Diferencial con Radar de Apertura Sintética).
La aplicación permite identificar, visualizar y analizar movimientos del suelo a través del tiempo, proporcionando una herramienta esencial para la gestión de riesgos naturales como subsidencias, deslizamientos y deformaciones superficiales.
🎯 Objetivos
Objetivo General
Desarrollar una aplicación que facilite el estudio, visualización e interpretación de cambios del terreno en Ciudad Victoria, procesando datos DInSAR para detectar áreas de riesgo y apoyar la toma de decisiones en la gestión territorial.
Objetivos Específicos

Implementar herramientas de análisis de patrones de desplazamiento temporal
Crear una interfaz intuitiva para visualizar y gestionar datos de deformación del suelo
Facilitar la comparación de datos históricos y actuales para la toma de decisiones

🛠️ Tecnologías Utilizadas
Librerías Principales

Streamlit - Desarrollo de la interfaz web interactiva
Pandas - Manipulación y análisis de datos
Matplotlib - Generación de gráficos estáticos
Plotly - Creación de gráficos interactivos y dinámicos

Lenguaje de Programación

Python 3.x

📁 Estructura del Proyecto
streamlit-dinsar/
├── app.py                  # Aplicación principal de Streamlit
├── utils.py               # Funciones auxiliares para análisis y visualización
├── requirements.txt       # Dependencias del proyecto
├── data/                  # Directorio de datos CSV
│   ├── Corrida_1.csv
│   ├── Corrida_2.csv
│   └── Corrida_3.csv
└── README.md
🔧 Instalación y Configuración
Requisitos Previos

Python 3.7 o superior
pip (gestor de paquetes de Python)

Pasos de Instalación

Clonar el repositorio
bashgit clone https://github.com/DevX-SAS/streamlit-dinsar.git
cd streamlit-dinsar

Instalar dependencias
bashpip install -r requirements.txt

Ejecutar la aplicación
bashstreamlit run app.py

Acceder a la aplicación
La aplicación se abrirá automáticamente en tu navegador web, generalmente en http://localhost:8501

📊 Funcionalidades
Análisis de Datos

Carga de datos: Selección de archivos CSV con datos DInSAR
Estadísticas descriptivas: Cálculo de media, desviación estándar, máximo, mínimo, mediana y percentil 95
Visualización temporal: Gráficos de desplazamiento en el tiempo

Herramientas de Visualización

Gráficos estáticos: Visualización con Matplotlib
Gráficos interactivos: Exploración visual con Plotly
Análisis multicolumna: Comparación de múltiples estaciones de monitoreo

Interfaz de Usuario

Sidebar interactiva: Selección de archivos y parámetros
Visualización de datos originales: Opción para mostrar dataset completo
Análisis por columna: Selección individual de estaciones de monitoreo

📈 Interpretación de Resultados
Estabilidad del Terreno
La aplicación permite evaluar la estabilidad del terreno mediante:

Tendencias temporales: Identificación de movimientos progresivos
Variabilidad estadística: Análisis de desviaciones y oscilaciones
Valores críticos: Detección de desplazamientos significativos

Indicadores de Riesgo

Tendencia ascendente: Posible deformación plástica del terreno
Valores negativos: Zonas con deslizamientos activos
Alta variabilidad: Terrenos frágiles susceptibles a lluvias intensas

🌍 Contexto Geológico
Área de Estudio
Ciudad Victoria, Loja, Ecuador - Zona caracterizada por:

Precipitaciones significativas que provocan deslizamientos
Suelos susceptibles a saturación durante temporadas invernales
Reducción de esfuerzos efectivos en taludes durante lluvias intensas

Técnica DInSAR
La interferometría radar de satélite (InSAR) constituye una técnica remota empleada para determinar la magnitud de los desplazamientos de la superficie del terreno, permite la medición precisa de la topografía de la superficie, la deformación del suelo y el hundimiento, con una precisión centimétrica.
👥 Equipo de Desarrollo
Universidad Técnica Particular de Loja
Facultad de Ingenierías y Arquitectura
Carrera de Geología
Integrantes

Jheison Jhoel González
Cristopher Villavicencio
Yanela Valladarez

Docente

Ing. Santiago Quiñonez Cuenca

🔮 Mejoras Futuras
La aplicación actual puede expandirse con:

Actualización automática de datos: Integración con fuentes de datos en tiempo real
Análisis predictivo: Implementación de modelos de machine learning
Sistema de alertas: Notificaciones automáticas para desplazamientos críticos
Integración de múltiples fuentes: Incorporación de datos meteorológicos y geológicos
Análisis espacial avanzado: Mapas interactivos con georeferenciación

📚 Referencias

Estudio de los deslizamientos en la ciudad de Loja-Ecuador. ResearchGate. Enlace

📄 Licencia
Este proyecto fue desarrollado como parte de un proyecto integrador académico en la Universidad Técnica Particular de Loja (Abril - Agosto 2025).
🤝 Contribuciones
Las contribuciones son bienvenidas. Por favor:

Fork el proyecto
Crea una rama para tu característica (git checkout -b feature/AmazingFeature)
Commit tus cambios (git commit -m 'Add some AmazingFeature')
Push a la rama (git push origin feature/AmazingFeature)
Abre un Pull Request
