import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st 

# Codigo de Zamora (hace falta el grafico)
url = 'https://datos.gob.cl/dataset/63e116db-0db9-4dc3-b1f4-e5cc51f7cff6/resource/9078be17-bb39-414d-bc56-0f8c0e994ce9/download/precio_consumidor_2021.zip'  

st.set_page_config(
        page_title="Analisis de datos", page_icon=":chart_with_upwards_trend:")

with st.sidebar:
        st.header("Bases de datos")
        delimiter = st.text_input("Delimitador", value=",")

st.title(f"Vista de datos")
st.markdown("## Data frame")
database = pd.read_csv(url, delimiter=delimiter)
st.write(database.iloc[1:11])


# Codigo de Simon

# Leer el archivo CSV usando la coma como separador
datos = pd.read_csv('https://datos.gob.cl/dataset/da14f0de-e6b0-4ee4-8ae2-8c05782dd20b/resource/59fdc96c-62e9-48fe-ae10-1e9eeded81d8/download/ejecucion-presupuestaria_nivel-nacional_a-septiembre-2024.csv', delimiter=';')

# Elimina los valores nulos
datos.dropna(inplace=True)

# Imprimir el DataFrame
print(datos)

# Convertir las columnas a valores numéricos
datos['Ejecución de Septiembre'] = pd.to_numeric(datos['Ejecución de Septiembre'], errors='coerce')
datos['Ejecución a Septiembre'] = pd.to_numeric(datos['Ejecución a Septiembre'], errors='coerce')

# Eliminar filas con valores NaN
datos.dropna(subset=['Ejecución de Septiembre', 'Ejecución a Septiembre'], inplace=True)

# Crear el gráfico de barras
fig, ax = plt.subplots()

# Definir el ancho de las barras
bar_width = 0.35

# Definir las posiciones de las barras
index = np.arange(len(datos))

# Crear las barras
bar1 = ax.bar(index, datos['Ejecución de Septiembre'], bar_width, label='Ejecución de Septiembre')
bar2 = ax.bar(index + bar_width, datos['Ejecución a Septiembre'], bar_width, label='Ejecución a Septiembre')

# Añadir etiquetas y título
ax.set_xlabel('Índice')
ax.set_ylabel('Valores')
ax.set_title('Ejecución de Septiembre vs Ejecución a Septiembre')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(index)
ax.legend()

# Streamlit

st.title("Ejecucion presupuestaria nivel nacional a _SEPTIEMBRE_")
col1, col2 = st.columns([2, 3])

with col1:
    st.write('Tabla de datos')
    st.dataframe(datos, width=1000, height=400)

with col2:
    st.write('Graficos')
    st.pyplot(fig)
