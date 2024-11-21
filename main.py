import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Ruta al archivo XLS
url = "https://datos.gob.cl/dataset/84d6e373-10af-41c9-a4d2-e80db6f94e01/resource/e72a5cc2-d0ec-4d8f-b092-637a513f2c5b/download/aeronaves-inscritas-en-el-r.n.a.-al-31.oct.2024-plataforma-del-gobierno.xlsx"

# Leer el archivo XLS y convertirlo en un DataFrame, especificando que el encabezado está en la tercera fila
database = pd.read_excel(url, header=2)

# Configuración de la página de Streamlit
st.set_page_config(
    page_title="Analisis de datos", page_icon=":chart_with_upwards_trend:")

# Título y descripción en Streamlit
st.title(f"Vista de datos")
st.markdown("### Datos de AERONAVES INSCRITAS EN EL R.N.A ")
st.write(database)

# Graficar los datos
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(database['TIPO DE AERONAVE'], bins=20, edgecolor='black')
ax.set_xlabel('Tipo de Aeronave')
ax.set_ylabel('Frecuencia')
ax.set_title('Histograma de Tipos de Aeronaves')

st.pyplot(fig)

# Grafico de torta

fig, ax = plt.subplots()
