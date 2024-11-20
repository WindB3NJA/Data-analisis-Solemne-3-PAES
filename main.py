import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Ruta al archivo XLS
url = "https://datos.gob.cl/dataset/84d6e373-10af-41c9-a4d2-e80db6f94e01/resource/e72a5cc2-d0ec-4d8f-b092-637a513f2c5b/download/aeronaves-inscritas-en-el-r.n.a.-al-31.oct.2024-plataforma-del-gobierno.xlsx"
new_url = "https://datosabiertos.mineduc.cl/wp-content/uploads/2024/05/PAES-2024-Inscritos-Puntajes.rar"
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

# Gráfico de pastel
x = database['TIPO DE AERONAVE'].value_counts()
colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(x)))

# plot
fig, ax = plt.subplots()
ax.pie(x, colors=colors, radius=3, center=(4, 4),
       wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()
