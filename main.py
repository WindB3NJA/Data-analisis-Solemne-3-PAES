import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import pathlib

# Obtener el directorio raíz del proyecto
ROOT = pathlib.Path(__file__).resolve().parent
ROOT_DATASET = ROOT / "database"

# Leer el archivo CSV usando el delimitador adecuado
datos = pd.read_csv(ROOT_DATASET / "PuntajesPAES2024-D-250.csv")  # Cambiar el directorio

# Limitar los datos a 100 filas
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

ax3.scatter(datos['PTJE_NEM'], datos['CLEC_MAX'], label='Puntajes', alpha=0.5)

# Añadir etiquetas y título
ax3.set_xlabel('Puntaje NEM')
ax3.set_ylabel('Maximo Puntaje de Competencia Lectora')
ax3.set_title('Relacion entre Punta NEM y Maximo Puntaje de Competencia Lectora')
ax3.legend()

# Grafico 4: Boxplot
categorias = { 'H1': 'Humanista Científico Diurno', 'H2': 'Humanista Científico Nocturno', 'H3': 'Humanista Científico – Validación de estudios', 'H4': 'Humanista Científico – Reconocimiento de estudios', 'T1': 'Técnico Profesional Comercial', 'T2': 'Técnico Profesional Industrial', 'T3': 'Técnico Profesional Servicios y Técnica', 'T4': 'Técnico Profesional Agrícola', 'T5': 'Técnico Profesional Marítima', ' ':'No hay registro' }

# Seleccionar las columnas a usar y eliminar filas con valores NaN
columns_to_use = ['RAMA_EDUCACIONAL', 'PTJE_NEM', 'PTJE_RANKING']
filtered_data = datos[columns_to_use].dropna()

# Crear el gráfico de caja
fig4, ax4 = plt.subplots(figsize=(10, 6))

# Crear el boxplot para comparar puntajes por modalidad educacional
unique_ramas = filtered_data['RAMA_EDUCACIONAL'].unique()
data_to_plot = [filtered_data[filtered_data['RAMA_EDUCACIONAL'] == rama]['PTJE_NEM'] for rama in unique_ramas]

box = ax4.boxplot(data_to_plot, labels=unique_ramas, patch_artist=True)

# Asignar un color único a cada caja
colors = plt.cm.Paired(np.linspace(0, 1, len(unique_ramas)))
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Crear la leyenda
patches = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
legend_labels = [categorias[rama] for rama in unique_ramas]
ax4.legend(patches, legend_labels, title="Modalidad Educacional", bbox_to_anchor=(1.05, 1), loc='upper left')

# Títulos y etiquetas
ax4.set_title("Comparación de Puntaje NEM por Modalidad Educacional", fontsize=16)
ax4.set_xlabel("Modalidad Educacional", fontsize=12)
ax4.set_ylabel("Puntaje NEM", fontsize=12)
ax4.set_xticklabels(ax4.get_xticklabels(), rotation=45, fontsize=10)

# Grafico 5: Torta
ramas_counts = datos['RAMA_EDUCACIONAL'].value_counts()

# Crear el gráfico de torta con un tamaño más grande
fig5, ax5 = plt.subplots(figsize=(12, 8))

# Crear el gráfico de torta sin porcentajes en el gráfico, pero manteniéndolos en la leyenda
ax5.pie(ramas_counts, labels=ramas_counts.index, startangle=90, colors=plt.cm.Paired.colors)

# Añadir la leyenda en la esquina inferior izquierda con los porcentajes
ax5.legend(labels=[f'{categorias.get(rama, rama)}: {ramas_counts[rama]} estudiantes, {100*ramas_counts[rama]/ramas_counts.sum():.1f}%'
                   for rama in ramas_counts.index],
           title="Ramas Educacionales", loc='lower left', fontsize=10, bbox_to_anchor=(0.0, -0.1))

# Título
ax5.set_title('Distribución de Estudiantes por Rama Educacional')

# Grafico 6: Histograma
# Calcular el puntaje promedio (asumiendo que el puntaje promedio se puede calcular como la media de los puntajes NEM y Ranking)
datos['Puntaje_Promedio'] = datos[['PTJE_NEM', 'PTJE_RANKING']].mean(axis=1)

# Filtrar los datos para las columnas necesarias
puntajes = datos[['Puntaje_Promedio', 'PTJE_NEM', 'PTJE_RANKING']].dropna()

# Crear el gráfico de histograma
fig6, ax6 = plt.subplots(figsize=(12, 8))

# Crear los histogramas superpuestos
ax6.hist(puntajes['Puntaje_Promedio'], bins=30, alpha=0.5, label='Puntaje Promedio', color='skyblue', edgecolor='black')
ax6.hist(puntajes['PTJE_NEM'], bins=30, alpha=0.5, label='Puntaje NEM', color='lightgreen', edgecolor='black')
ax6.hist(puntajes['PTJE_RANKING'], bins=30, alpha=0.5, label='Puntaje Ranking', color='salmon', edgecolor='black')

# Añadir etiquetas y título
ax6.set_xlabel('Puntaje Ranking', fontsize=12)
ax6.set_ylabel('Frecuencia', fontsize=12)
ax6.set_title('Distribución de Puntajes Promedio, NEM y Ranking', fontsize=16)

# Añadir la leyenda
ax6.legend()

# Streamlit
st.title("Datos de PAES 2024 de 100 estudiantes")

st.subheader('Tabla de datos')
st.dataframe(datos.head(10), width=1000, height=400)
with st.sidebar:
        st.header("Gráficos")
        option = st.selectbox(
            "¿Cuál gráfico estás interesado en ver?",
            ("Selecciona una opción para visualizar el gráfico", "Competencia Matematica 1 vs Competencia Lectora (Gráfico de barras)", "Prueba Historia y Cs. Sociales vs Prueba Ciencias (Gráfico de líneas)", "Relacion entre Punta NEM y Maximo Puntaje de Competencia Lectora (Gráfico de dispersión)", "Comparación de Puntaje NEM por Modalidad Educacional (Gráfico de Caja)", "Distribución de Estudiantes por Rama Educacional (Gráfico de torta)", "Distribución de Puntajes Promedio, NEM y Ranking (Gráfico de histograma)"),
        )

st.subheader('Gráfico seleccionado')
if option == "Competencia Matematica 1 vs Competencia Lectora (Gráfico de barras)":
    st.pyplot(fig)
elif option == "Prueba Historia y Cs. Sociales vs Prueba Ciencias (Gráfico de líneas)":
    st.pyplot(fig2)
elif option == "Relacion entre Punta NEM y Maximo Puntaje de Competencia Lectora (Gráfico de dispersión)":
    st.pyplot(fig3)
elif option == "Comparación de Puntaje NEM por Modalidad Educacional (Gráfico de Caja)":
    st.pyplot(fig4)
elif option == "Distribución de Estudiantes por Rama Educacional (Gráfico de torta)":
    st.pyplot(fig5)
elif option == "Distribución de Puntajes Promedio, NEM y Ranking (Gráfico de histograma)":
    st.pyplot(fig6)
else:
    st.write("#DondeEstaMiGrafico")

st.write("Seleccionaste:", option)
