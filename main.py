import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

# Data frame
datos = pd.read_csv('https://datos.gob.cl/uploads/recursos/RecaudacionPagoDerechosInscripcion_2011-2012.csv', sep=';')
datos.columns = ['Año', 'Mes', 'Recaudacion']
datos['Fecha'] = pd.to_datetime(datos['Año'].astype(str) + datos['Mes'].astype(str), format='%Y%m')

# Graficas de analisis
plt.figure(figsize=(10,20))
plt.plot(datos['Fecha'], datos['Recaudacion'], marker='o', linestyle='-', color='g')
plt.xlabel('Año y mes')
plt.ylabel('Recaudacion')
plt.title('tiempo')
plt.show()

# Pagina 
st.title("Gráfico de Recaudación por Mes y Año")
st.dataframe(datos)
st.pyplot(plt)
