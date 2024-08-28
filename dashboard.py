import pandas as pd
import plotly.express as px
import streamlit as st
import warnings

warnings.filterwarnings('ignore')

st.header(':blue[Colegio San José de Guanentá]')
st.code("Especialidad en Sistemas", language="python")
st.title('Dashboard Academy :school:')


# crear dataframe con notas de nivel basica, alojados en github
df_notas_basica = pd.read_csv('https://raw.githubusercontent.com/paezn/streamlit_notas/main/notas_periodo_II_basica_secundaria.csv')

# crear dataframe con notas de nivel media, alojados en github
df_notas_media = pd.read_csv('https://raw.githubusercontent.com/paezn/streamlit_notas/main/notas_periodo_II_media_tecnica.csv')

# limpieza de los dataframes
df_notas_basica = df_notas_basica.astype({'codigo':'str'})
st.write(df_notas_basica.dtypes)

# Crear sidebar y poner imagen
st.sidebar.image('escudoGuanenta.png',)

# Agregar título a sidebar
st.sidebar.title('Filtros')

# lista niveles
niveles = ['Básica', 'Media']
niveles = st.sidebar.multiselect('Nivel', niveles)

# lista jornadas
jornadas = sorted(list(df_notas_basica['jornada'].unique()))
jornadas = st.sidebar.multiselect('Jornada', jornadas)

# lista grados
grados = ['6','7','8','9','10','11']
grados = st.sidebar.multiselect('Grado', grados)

# lista grupos
grupos1 = sorted(list(df_notas_basica['grupo'].unique()))
grupos2 = sorted(list(df_notas_media['grupo'].unique()))
grupos = grupos1 + grupos2
grupos = st.sidebar.multiselect('Grupo', grupos)

# lista asignaturas
asignaturas_basica = list(df_notas_basica.columns.values)
asignaturas = st.sidebar.multiselect('Asignaturas', asignaturas_basica)


