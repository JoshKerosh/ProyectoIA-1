import streamlit as st
from PIL import Image

import pandas as pd
import numpy as np

#variables
cantGeneraciones = 200
tamPoblacion = 10
imgGenActual = None

#imgenes iniciales
imgPrueba = Image.open('test.jpeg') 
imgInicial = Image.open('black.jpg')

## Body ##
st.title('Proyecto1: Del Píxel al Pincel')
col1, col2 = st.columns([1,1.5])

####
# Variables #
col1.subheader('Variables')
#genrerations
cantGeneraciones = col1.number_input('Cantidad de generaciones',value=cantGeneraciones)
#poblation
tamPoblacion = col1.number_input('Tamaño de la población',value=tamPoblacion)

####
# Image Uploader #
def uploader_callback(): 
    print('Imagen subida')

imgObjetivo = col1.file_uploader("Cargar la imagen", 
                                 type=("png", "jpg","jpeg"),
                                 on_change=uploader_callback,
)

####
# Imagen Objetivo #
col2.subheader('Imagen Objetivo')
loc_imgObjetivo = col2.empty()

if imgObjetivo == None :
    imgObjetivo = imgPrueba
loc_imgObjetivo.image(imgObjetivo)


## abajo


####
# Boton iniciar #
def button_callback():
    print('iniciar')
    st.session_state.disabled = True

btnIniciar = st.button('Iniciar', 
                         on_click=button_callback, 
                         use_container_width=True)

####

pan1, pan2 = st.columns([1,1.5])

# Reproduccion de Imagenes #
pan2.subheader('Reproduccion')
loc_imgGenActual = pan2.empty()

if imgGenActual == None :
    imgGenActual = imgInicial
loc_imgGenActual.image(imgGenActual)

####
#Grafico de fitness
pan1.subheader('Grafico')
loc_plot = pan1.empty()

#el dataframe ....
chart_data = pd.DataFrame(
   {
       "col1": np.random.randn(20),
       "col2": np.random.randn(20),
       "col3": np.random.choice(["A", "B", "C"], 20),
   }
)

#mostrar el grafico
loc_plot.line_chart(chart_data, x="col1", y="col2", color="col3")

###########
## Funcs ##

#para cambiar la imagen en reproduccion
def nuevaImgReprod(nuevaImagen):
    imgGenActual = nuevaImagen;

#para poner el grafico
def nuevoGrafico(tablaDatos):
    loc_plot.line_chart(tablaDatos, x="col1", y="col2", color="col3")

