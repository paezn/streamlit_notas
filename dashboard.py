import pandas as pd
import plotly.express as px
import streamlit as st
import warnings

warnings.filterwarnings('ignore')

st.header(':blue[Colegio San José de Guanentá]:school:')
st.code("Especialidad en Sistemas", language="python")
st.title(':green[Dashboard Academy]')


# creación de dataframes vacios
df_notas_media = pd.DataFrame()
df_notas_basica = pd.DataFrame()

####################################
## Creacion sidebar y filtros
####################################

# Crear sidebar y poner imagen
st.sidebar.image('escudoGuanenta.png')

# Agregar título a sidebar
st.sidebar.title('Filtros')

# lista niveles
niveles = ['Todos','Básica', 'Media']
niveles = st.sidebar.selectbox('Nivel', niveles)

# lista jornadas
jornadas = ['Mañana' , 'Tarde']
#jornadas = sorted(list(df_notas_basica['jornada'].unique()))
jornadas = st.sidebar.multiselect('Jornada', jornadas)

# lista grados
grados = ['6','7','8','9','10','11']
grados = st.sidebar.multiselect('Grado', grados)

# lista grupos
#grupos1 = sorted(list(df_notas_basica['grupo'].unique()))
#grupos2 = sorted(list(df_notas_media['grupo'].unique()))
#grupos = grupos1 + grupos2
#grupos = st.sidebar.multiselect('Grupo', grupos)

# lista asignaturas
#asignaturas = ['Biología','Sociales', 'Cátedra Paz', 'Artística', 'Etica', 'Religión','Educación Física', 'Castellano', 'Inglés', 'Matemáticas', 'Geometría','Estadística', 'Tecnología', 'Informática', 'Dibujo Técnico', 'Filosofía','Física', 'Química','Ciencias Políticas']
#asignaturas = sorted(asignaturas)
#asignaturas = st.sidebar.multiselect('Asignaturas', asignaturas)

## aplicacion de filtros de la sidebar

# Nivel - Al seleccionar el nivel se crean los dataframes respectivos
if niveles == 'Todos':
    # crear dataframe con notas de nivel basica, alojados en github
    df_notas_basica = pd.read_csv('https://raw.githubusercontent.com/paezn/streamlit_notas/main/notas_periodo_II_basica_secundaria.csv')
    
    # crear dataframe con notas de nivel media, alojados en github
    #df_notas_media = pd.read_csv('https://raw.githubusercontent.com/paezn/streamlit_notas/main/notas_periodo_II_media_tecnica.csv')

    # crear dataframe con notas de nivel media, guardados localmente en esta carpeta
    df_notas_media = pd.read_csv('notas_periodo_II_media_tecnica.csv')
    df_notas_media = df_notas_media.astype({'grupo':'str'})

    # limpieza de los dataframes
    #df_notas_basica = df_notas_basica.astype({'codigo':'str'})
    #df_notas_basica.set_index('codigo', inplace=True)

    #df_notas_media = df_notas_media.astype({'codigo':'str'})
    #df_notas_media.set_index('codigo', inplace=True)

elif niveles == 'Básica':
    # crear dataframe con notas de nivel basica, alojados en github
    #df_notas_basica = pd.read_csv('https://raw.githubusercontent.com/paezn/streamlit_notas/main/notas_periodo_II_basica_secundaria.csv')
    # limpieza de los dataframes
   # df_notas_basica = df_notas_basica.astype({'codigo':'str'})
    #df_notas_basica.set_index('codigo', inplace=True)
    pass
else:
    # crear dataframe con notas de nivel media, alojados en github
    #df_notas_media = pd.read_csv('https://raw.githubusercontent.com/paezn/streamlit_notas/main/notas_periodo_II_media_tecnica.csv')
    # limpieza de los dataframes
    #df_notas_media = df_notas_media.astype({'codigo':'str'})
    #df_notas_media.set_index('codigo', inplace=True)
    pass


# Jornada
if jornadas:
    df_notas_basica = df_notas_basica[df_notas_basica['jornada'].isin(jornadas)]
    df_notas_media = df_notas_media[df_notas_media['jornada'].isin(jornadas)]

# Grado
if grados:
    grupos_basica = sorted(list(df_notas_basica['grupo'].unique()))
    lista_grupos_basica = []
    for i in grupos_basica:
        if (i.split('-')[0] in grados):
            lista_grupos_basica.append(i)
    df_notas_basica = df_notas_basica[df_notas_basica['grupo'].isin(lista_grupos_basica)]
    #st.dataframe(df_notas_basica)

    grupos_media = sorted(list(df_notas_media['grupo'].unique()))
    lista_grupos_media = []
    for i in grupos_media:
        if (i.split('-')[0] in grados):
            lista_grupos_media.append(i)
    df_notas_media = df_notas_media[df_notas_media['grupo'].isin(lista_grupos_media)]
    
    #df_notas_media['grupo'] = df_notas_media['grupo'].astype(str)
    #st.dataframe(df_notas_media)


##################################
## Pestañas visualización gráficas
##################################

tab1, tab2, tab3 = st.tabs(['Asignaturas', 'Estudiantes', 'Grupos'])

with tab1:
    # graficas asignaturas
    col1, col2 = st.columns(2)

    with col1:
        # Top 5 asignaturas con mas alto promedio nivel media
        df_asignaturas = df_notas_media[df_notas_media.columns[7:]]
        lista_asignaturas = list(df_notas_media.columns[7:])
        df_promedio_asignaturas = df_asignaturas[lista_asignaturas].mean()
        df_promedio_asignaturas = pd.DataFrame(df_promedio_asignaturas)
        df_promedio_asignaturas.reset_index(inplace=True)
        df_promedio_asignaturas.columns = ['asignatura', 'promedio']
        df_promedio_asignaturas = df_promedio_asignaturas.sort_values('promedio', ascending=False)
        df_promedio_asignaturas['promedio'] = df_promedio_asignaturas['promedio'].astype(int)
        #grafica barras
        fig_top_asig_media_promedio = px.bar(df_promedio_asignaturas.head(), x='asignatura', y = 'promedio', text_auto=True, title='Top  asignaturas mejor promedio nivel media')
        st.plotly_chart(fig_top_asig_media_promedio, use_container_width = True)

        # Top 5 asignaturas con mas alto promedio nivel media
        df_promedio_asignaturas = df_promedio_asignaturas.sort_values('promedio', ascending=True)
        df_promedio_asignaturas['promedio'] = df_promedio_asignaturas['promedio'].astype(int)
        #grafica barras
        fig_top_asig_media_promedio = px.bar(df_promedio_asignaturas.head(), x='asignatura', y = 'promedio', text_auto=True, title='Top  asignaturas peor promedio nivel media')
        st.plotly_chart(fig_top_asig_media_promedio, use_container_width = True)
        

    with col2:
         # Top 5 asignaturas con mas alto promedio nivel basica
        df_asignaturas = df_notas_basica[df_notas_basica.columns[6:26]]
        lista_asignaturas = list(df_notas_basica.columns[7:])
        df_promedio_asignaturas = df_asignaturas[lista_asignaturas].mean()
        df_promedio_asignaturas = pd.DataFrame(df_promedio_asignaturas)
        df_promedio_asignaturas.reset_index(inplace=True)
        df_promedio_asignaturas.columns = ['asignatura', 'promedio']
        df_promedio_asignaturas = df_promedio_asignaturas.sort_values('promedio', ascending=False)
        df_promedio_asignaturas['promedio'] = df_promedio_asignaturas['promedio'].astype(int)
        #grafica barras
        fig_top_asig_basica_promedio = px.bar(df_promedio_asignaturas.head(), x='asignatura', y = 'promedio', text_auto=True, title='Top  asignaturas mejor promedio nivel basica')
        st.plotly_chart(fig_top_asig_basica_promedio, use_container_width = True)

        # Top 5 asignaturas con mas alto promedio nivel media
        df_promedio_asignaturas = df_promedio_asignaturas.sort_values('promedio', ascending=True)
        df_promedio_asignaturas['promedio'] = df_promedio_asignaturas['promedio'].astype(int)
        #grafica barras
        fig_top_asig_basica_promedio = px.bar(df_promedio_asignaturas.head(), x='asignatura', y = 'promedio', text_auto=True, title='Top  asignaturas peor promedio nivel basica')
        st.plotly_chart(fig_top_asig_basica_promedio, use_container_width = True)

with tab2:
    # graficas estudiantes
    col1, col2 = st.columns(2)

    with col1:
        # Top 5 estudiantes con mas alto promedio
        pass
    with col2:
        # Top 5 estudiantes con mas materias reprobadas
        pass

with tab3:
    # graficas grupos
    col1, col2 = st.columns(2)

    with col1:
        # Top 5 grupos con mas alto promedio nivel básica
        top_grupos_basica_promedio = df_notas_basica.groupby('grupo')[['promedio']].mean().sort_values('promedio', ascending=False)
        top_grupos_basica_promedio.reset_index(inplace=True)
        fig_top_grupos_basica_promedio = px.bar(top_grupos_basica_promedio.head(), x='grupo', y = 'promedio', text_auto=True, title='Top  grupos mejor promedio nivel basica')
        st.plotly_chart(fig_top_grupos_basica_promedio, use_container_width = True)
        st.dataframe(top_grupos_basica_promedio)
        st.write(top_grupos_basica_promedio.dtypes)

    with col2:
        # Top 5 grupos con mas alto promedio nivel media
        top_grupos_media_promedio = df_notas_media.groupby('grupo')[['promedio']].mean().sort_values('promedio', ascending=False)
        top_grupos_media_promedio.reset_index(inplace=True)
        top_grupos_media_promedio['grupo'] = top_grupos_media_promedio['grupo'].astype(str)
        fig_top_grupos_media_promedio = px.bar(top_grupos_media_promedio.head(), x='grupo', y = 'promedio', text_auto=True, title='Top  grupos mejor promedio nivel media')
        st.plotly_chart(fig_top_grupos_media_promedio, use_container_width = True)
        st.dataframe(top_grupos_media_promedio)
        st.write(top_grupos_media_promedio.dtypes)
        
        # Top 5 grupos con mas mortalidad
        pass
