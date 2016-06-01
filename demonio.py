#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twython import Twython
from random import randint

# Claves de la aplicacion Twitter

app_key = ''
app_secret = ''
oauth_token = ''
oauth_token_secret = ''
twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)

def leertxtenlista():

    # Bucle infinito
    mensaje = ""

    # Abrimos el archivo
    archi = open('twit', 'r')
    lineas = archi.readlines()

    # Elegir un twit aleatorio
    t = randint(0, len(lineas) - 1)
    mensaje = lineas[t]
    # Agrega el Tweet
    twitter.update_status(status=mensaje)
    archi.close()


def imagen_lista():

    #Variable donde se almacena la imagen
    imagen = ""

    #Elegimos un valor aleatorio entre el numero de archivos
    i = randint(1, 30)

    #Creamos la ruta del archivo aleatorio
    imagen = 'imagenes/' + str(i) + '.png'

    #Abrimos el archivo de tipo imagen con la opción open y lo almacenamos en la variable photo
    photo = open(imagen, 'rb')

    #Cargamos en twitter la imagen mediante la opción twitter.upload_media(media=photo)
    response = twitter.upload_media(media=photo)

    #Enviamos el twit
    twitter.update_status(status='Texto del twit ', media_ids=[response['media_id']])

# leertxtenlista()
imagen_lista()
