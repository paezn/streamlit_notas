import pandas as pd
import plotly.express as px
import streamlit as st
import warnings
import math

warnings.filterwarnings('ignore')

st.header('Colegio San José de Guanentá:school:')
st.code("Especialidad en Sistemas", language="python")
st.title(":green[Dashboard Academy]")


# crear dataframe con notas de nivel basica, alojados en github
df_notas_basica = pd.read_csv('https://raw.githubusercontent.com/paezn/streamlit_notas/main/notas_periodo_II_basica_secundaria.csv')

# crear dataframe con notas de nivel media, alojados en github
df_notas_media = pd.read_csv('https://raw.githubusercontent.com/paezn/streamlit_notas/main/notas_periodo_II_media_tecnica.csv')

# limpieza dataframes
df_notas_basica = df_notas_basica.drop(columns=['periodo'])
df_notas_basica = df_notas_basica.astype({'codigo':'str'})
df_notas_basica.set_index('codigo', inplace=True)
df_notas_basica = df_notas_basica.sort_values('grupo',ascending=True)

df_notas_media = df_notas_media.drop(columns=['periodo'])
df_notas_media = df_notas_media.astype({'codigo':'str'})
df_notas_media.set_index('codigo', inplace=True)

# Crear sidebar y poner imagen
st.sidebar.image('escudoGuanenta.png')

# mostrar dataframes
st.header(':blue[Notas Periodo II 2024 - Básica Secundaria]')

## Metricas basica

col1, col2, col3 = st.columns(3)

with col1:
    # Numero de estudiantes total
    st.metric(':red[Número estudiantes]', df_notas_basica.shape[0])
    # Número estudiantes jornada mañana
    st.metric(':red[Número estudiantes J. Mañana]', df_notas_basica[df_notas_basica['jornada'] == 'Mañana'].shape[0])
    # Número estudiantes jornada mañana
    st.metric(':red[Número estudiantes J. Tarde]', df_notas_basica[df_notas_basica['jornada'] == 'Tarde'].shape[0])
with col2:
    # promedio general basica
    st.metric(':orange[Promedio general]',math.trunc(df_notas_basica['promedio'].mean()),delta_color="normal")
    # promedio general basica j. mañana
    st.metric(':orange[Promedio general J. Mañana]',math.trunc(df_notas_basica[df_notas_basica['jornada'] == 'Mañana']['promedio'].mean()),delta_color="normal")
    # promedio general basica j. tarde
    st.metric(':orange[Promedio general J. Tarde]',math.trunc(df_notas_basica[df_notas_basica['jornada'] == 'Tarde']['promedio'].mean()),delta_color="normal")

with col3:
    # promedio general basica
    st.metric(':violet[Desviación estándar]',math.trunc(df_notas_basica['promedio'].std()),delta_color="normal")
    # Desviacion estandar j. mañana
    st.metric(':violet[Desviación estándar J. Mañana]',math.trunc(df_notas_basica[df_notas_basica['jornada'] == 'Mañana']['promedio'].std()),delta_color="inverse")
    # Desviación estándar j. tarde
    st.metric(':violet[Desviación estándar J. Tarde]',math.trunc(df_notas_basica[df_notas_basica['jornada'] == 'Tarde']['promedio'].std()),delta_color="normal")

st.dataframe(df_notas_basica)


st.header(':blue[Notas Periodo II 2024 - Media Técnica]')

# Metricas media

col1, col2, col3 = st.columns(3)

with col1:
    # Numero de estudiantes
    st.metric('Número estudiantes', df_notas_media.shape[0])
    # Número estudiantes jornada mañana
    st.metric('Número estudiantes J. Mañana', df_notas_media[df_notas_media['jornada'] == 'Mañana'].shape[0])
    # Número estudiantes jornada mañana
    st.metric('Número estudiantes J. Tarde', df_notas_media[df_notas_media['jornada'] == 'Tarde'].shape[0])

with col2:
    # promedio general basica
    st.metric('Promedio general',math.trunc(df_notas_media['promedio'].mean()),delta_color="normal")
    # promedio general basica j. mañana
    st.metric('Promedio general J. Mañana',math.trunc(df_notas_media[df_notas_media['jornada'] == 'Mañana']['promedio'].mean()),delta_color="normal")
    # promedio general basica j. tarde
    st.metric('Promedio general J. Tarde',math.trunc(df_notas_media[df_notas_media['jornada'] == 'Tarde']['promedio'].mean()),delta_color="normal")

with col3:
    # promedio general basica
    st.metric('Desviación estándar',math.trunc(df_notas_media['promedio'].std()),delta_color="normal")
    # Desviacion estandar j. mañana
    st.metric('Desviación estándar J. Mañana',math.trunc(df_notas_media[df_notas_media['jornada'] == 'Mañana']['promedio'].std()),delta_color="inverse")
    # Desviación estándar j. tarde
    st.metric('Desviación estándar J. Tarde',math.trunc(df_notas_media[df_notas_media['jornada'] == 'Tarde']['promedio'].std()),delta_color="normal")

st.dataframe(df_notas_media)







