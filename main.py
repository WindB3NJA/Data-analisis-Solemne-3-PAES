import streamlit as st
import pandas as pd


url = 'https://datos.gob.cl/dataset/63e116db-0db9-4dc3-b1f4-e5cc51f7cff6/resource/9078be17-bb39-414d-bc56-0f8c0e994ce9/download/precio_consumidor_2021.zip'  

st.set_page_config(
        page_title="Analisis de datos", page_icon=":chart_with_upwards_trend:")

with st.sidebar:
        st.header("Bases de datos")
        delimiter = st.text_input("Delimitador", value=";")

st.title(f"Vista de datos")
st.markdown("## Data frame")
database = pd.read_csv(url, delimiter=delimiter)
st.write(database)
