import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

# Leer el archivo CSV usando el delimitador adecuado
datos = pd.read_csv('/Users/simonaspee/Downloads/PAES-2024-Inscritos-Puntajes/A_INSCRITOS_PUNTAJES_PAES_2024_PUB_MRUN.csv', delimiter=';', nrows=1000) # Cambiar el directorio


# Eliminar los valores nulos
datos.dropna(inplace=True)

# Limitar los datos a 250 filas
datos = datos.head(101)



# Grafico 1: Bar Chart

# Convertir las columnas a valores numéricos
datos['MATE1_REG_ACTUAL'] = pd.to_numeric(datos['MATE1_REG_ACTUAL'], errors='coerce')
datos['CLEC_REG_ACTUAL'] = pd.to_numeric(datos['CLEC_REG_ACTUAL'], errors='coerce')

# Eliminar filas con valores NaN
datos.dropna(subset=['MATE1_REG_ACTUAL', 'CLEC_REG_ACTUAL'], inplace=True)


# Crear el gráfico de barras
fig, ax = plt.subplots(figsize=(10, 6))

# Definir el ancho de las barras
bar_width = 0.35

# Definir las posiciones de las barras
index = np.arange(len(datos))

# Crear las barras
bar1 = ax.bar(index, datos['MATE1_REG_ACTUAL'], bar_width, label='C.Matematica 1')
bar2 = ax.bar(index + bar_width, datos['CLEC_REG_ACTUAL'], bar_width, label='C.Lectora')

# Añadir etiquetas y título
ax.set_xlabel('Índice')
ax.set_ylabel('Valores')
ax.set_title('Competencia Matematica 1 vs Competencia Lectora')
ax.set_xticks(index[::20] + bar_width / 2)
ax.set_xticklabels(index[::20])
ax.legend()





# Grafico 2: Line Chart

# Convertir las columnas a valores numéricos
datos['HCSOC_REG_ACTUAL'] = pd.to_numeric(datos['HCSOC_REG_ACTUAL'], errors='coerce')
datos['CIEN_REG_ACTUAL'] = pd.to_numeric(datos['CIEN_REG_ACTUAL'], errors='coerce')

# Eliminar filas con valores NaN
datos.dropna(subset=['HCSOC_REG_ACTUAL', 'CIEN_REG_ACTUAL'], inplace=True)


# Limitar los datos a un índice máximo de 14 para el gráfico
x = datos['HCSOC_REG_ACTUAL']
y = datos['CIEN_REG_ACTUAL']

# plot
fig2, ax2 = plt.subplots(figsize=(10, 6))

ax2.plot(range(len(x)), x, label='P. Historia y Cs. Sociales')
ax2.plot(range(len(y)), y, label='P. Ciencias')

ax2.set_xlabel('Índice')
ax2.set_ylabel('Valores')
ax2.set_title('Prueba Historia y Cs. Sociales vs Prueba Ciencias')
ax2.legend()



# Grafico 3: Scatter Plot

# Crear el gráfico de dispersión
fig3, ax3 = plt.subplots(figsize=(10, 6))

ax3.scatter(datos['HCSOC_REG_ACTUAL'], datos['CIEN_REG_ACTUAL'], label='Puntajes', alpha=0.5)

# Añadir etiquetas y título
ax3.set_xlabel('P. Historia y Cs. Sociales')
ax3.set_ylabel('P. Ciencias')
ax3.set_title('Relación entre P. Historia y Cs. Sociales y P. Ciencias')
ax3.legend()






# Streamlit

st.title("Puntajes PAES 2024")

st.subheader('Tabla de datos')
st.dataframe(datos.head(10), width=1000, height=400)

st.subheader('Gráficos')

option = st.selectbox(
    "¿Cuál gráfico estás interesado en ver?",
    ("Competencia Matematica 1 vs Competencia Lectora (Gráfico de barras)", "Prueba Historia y Cs. Sociales vs Prueba Ciencias (Gráfico de líneas)", "Relación entre P. Historia y Cs. Sociales y P. Ciencias (Gráfico de dispersión)"),
)

if option == "Competencia Matematica 1 vs Competencia Lectora (Gráfico de barras)":
    st.pyplot(fig)
elif option == "Prueba Historia y Cs. Sociales vs Prueba Ciencias (Gráfico de líneas)":
    st.pyplot(fig2)
elif option == "Relación entre P. Historia y Cs. Sociales y P. Ciencias (Gráfico de dispersión)":
    st.pyplot(fig3)

st.write("Seleccionaste:", option)