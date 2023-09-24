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
st.title('Proyecto1')
col1, col2 = st.columns([1,1.5])

####
# Variables #
col1.subheader('Variables')
#genrerations
cantGeneraciones = col1.number_input('la cantidad de generaciones',value=cantGeneraciones)
#poblation
tamPoblacion = col1.number_input('el tamaño de la población',value=tamPoblacion)

####
# Image Uploader #
def uploader_callback(): 
    print('Uploaded file')

imgObjetivo = col1.file_uploader("cargar la imagen", 
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

####
# Boton iniciar #
def button_callback():
    print('iniciar')
    st.session_state.disabled = True

btnIniciar = col1.button('Iniciar', 
                         on_click=button_callback)

####
# Reproduccion de Imagenes #
col2.subheader('Reproduccion')
loc_imgGenActual = col2.empty()

if imgGenActual == None :
    imgGenActual = imgInicial
loc_imgGenActual.image(imgGenActual)

####
#Grafico de fitness
col1.subheader('Grafico')

#mostrar el grafico
loc_plot = col1.empty()

###########
## Funcs ##

#para cambiar la imagen en reproduccion
def camImgReprod(nuevaImagen):
    imgGenActual = nuevaImagen;

