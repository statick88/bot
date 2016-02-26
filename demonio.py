from twython import Twython
import time
import os

# Claves de la aplicacion Twitter

app_key = ""
app_secret = ""
oauth_token = ""
oauth_token_secret = ""
twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)

def leertxtenlista():
 
 # Bucle infinito
 while True:
  
  mensaje = ""
  
  # Abrimos el archivo
  archi=open('twit','r')
  lineas=archi.readlines()
  
  # Bucle para recorrer todas las entradas
  for li in lineas:
   time.sleep(0.01)
   mensaje = li
   # Agrega el Tweet
   twitter.update_status(status=mensaje)
   # Lapso de tiempo entre Tweets
   time.sleep(600)
   
  archi.close()
  
 

leertxtenlista()
