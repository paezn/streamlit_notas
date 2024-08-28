import pandas as pd
import plotly.express as px
import streamlit as st
import warnings

warnings.filterwarnings('ignore')

st.header('Colegio San José de Guanentá')
st.code("Especialidad en Sistemas", language="python")
st.title("Dashboard Academy :school:")


# crear dataframe con notas de nivel basica, alojados en github
df_notas_basica = pd.read_csv('https://raw.githubusercontent.com/paezn/streamlit_notas/main/notas_periodo_II_basica_secundaria.csv')

# crear dataframe con notas de nivel media, alojados en github
df_notas_media = pd.read_csv('https://raw.githubusercontent.com/paezn/streamlit_notas/main/notas_periodo_II_media_tecnica.csv')

# mostrar dataframes
st.header('Notas Periodo II 2024 - Básica Secundaria')
df_notas_basica = df_notas_basica.astype({'codigo':'str'})
st.dataframe(df_notas_basica)


st.header('Notas Periodo II 2024 - Media Técnica')
st.dataframe(df_notas_media)







