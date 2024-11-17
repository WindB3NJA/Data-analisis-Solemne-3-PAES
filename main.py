import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st 


# Leer el archivo CSV usando la coma como separador
datos = pd.read_csv('https://datos.gob.cl/dataset/da14f0de-e6b0-4ee4-8ae2-8c05782dd20b/resource/59fdc96c-62e9-48fe-ae10-1e9eeded81d8/download/ejecucion-presupuestaria_nivel-nacional_a-septiembre-2024.csv', delimiter=';')

# Elimina los valores nulos
datos.dropna(inplace=True)


# Convertir las columnas a valores numéricos
datos['Ejecución de Septiembre'] = pd.to_numeric(datos['Ejecución de Septiembre'], errors='coerce')
datos['Ejecución a Septiembre'] = pd.to_numeric(datos['Ejecución a Septiembre'], errors='coerce')

# Eliminar filas con valores NaN
datos.dropna(subset=['Ejecución de Septiembre', 'Ejecución a Septiembre'], inplace=True)


# Grafico 1: Bar Chart

# Crear el gráfico de barras
fig, ax = plt.subplots(figsize=(10, 6))

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




# Grafico 2: Line Chart

# Limitar los datos a un índice máximo de 14 para el gráfico
x = datos['Ejecución de Septiembre']
y = datos['Ejecución a Septiembre']

# plot
fig2, ax2 = plt.subplots(figsize=(10, 6))

ax2.plot(range(len(x)), x, label='Ejecución de Septiembre')
ax2.plot(range(len(y)), y, label='Ejecución a Septiembre')

ax2.set_xlabel('Índice')
ax2.set_ylabel('Valores')
ax2.set_title('Ejecución de Septiembre vs Ejecución a Septiembre')
ax2.legend()



# Streamlit

st.title("Ejecución presupuestaria nivel nacional a _SEPTIEMBRE_")


st.subheader('Tabla de datos')
st.dataframe(datos, width=1000, height=400)

st.subheader('Graficos')

option = st.selectbox(
    "Cual grafico estas interesado en ver?",
    ("Grafico de barras", "Grafico de lineas"),
)


if option == "Grafico de barras":
    st.pyplot(fig)
else:
    st.pyplot(fig2)

st.write("Seleccionaste:", option)


