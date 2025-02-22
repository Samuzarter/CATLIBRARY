#CatLibrary
import os
import requests
import json
from decouple import config


def cats():
    """
    Esta funcion retorna un diccionario con el ID y TAGS de los primeros 10 gatos de la API CATAAS
    """
    #Se realiza el request a la Api por medio de una variable de entorno que contiene la URL, concatenado con el direccionamiento
    data = requests.get(config('URL_API')+"/cats")

    #Se verifica el código de estado de la solcitud
    if data.status_code == 200:
        data = data.json()
        cats = {}
        #Se itera la respuesta para obtener solo lo que se quiere en este caso el ID y TAGS
        for e in data:
            cats[e['id']] = e['tags']
        # Por medio de la libreria JSON se convierte el diccionario cats en un JSON para retornarlo
        data = json.dumps(cats)
        return data
    else:
        return f"Hubo un error en el proceso :c, Status Code: {data.status_code}"
            
    
def cats_count():
    """
    Retorna la cantidad de gatos que hay en la API CATAAS
    """
    # Se realiza el request a la Api por medio de una variable de entorno que contiene la URL, concatenado con el direccionamiento
    data = requests.get(config('URL_API')+"/count")
    #Se verifica el código de estado de la solcitud
    if data.status_code == 200:
        data = data.json()
        #Se retorna en este caso el valor de gatos que se encuentra en la API CATAAS
        return(data['count'])
    else:
        return f"Hubo un error en el proceso :c, Status Code: {data.status_code}"
    


def cat_say(txt: str):
    """
    Esta funcion retorna la imagen de un gato aletaoria, con el texto que sea ingresado

    Parámetros

    txt (string): La frase que se quiere poner en la imagen

    Retorna:
    Un aviso en donde se le especifcia la ruta donde se guardo la imagen en su dispositivo.
    """
    #Se realiza el request a la Api por medio de una variable de entorno que contiene la URL, concatenado con el direccionamiento
    data = requests.get(config('URL_CAT')+f"/says/{txt}?")
    #Se verifica el código de estado de la solcitud
    if data.status_code == 200:
        imagen = data.content
        #Se crea un path en donde por medio de la libreria OS se busca la carpeta Downloads para guardar la imagen
        path = obtener_ruta_carpeta()
        
        with open(os.path.join(path,'Imagen.jpg'),'wb') as f:
            f.write(imagen)
        return(f"Imagen guardada en {path} con el nombre de imagen.jpg")


def obtener_ruta_carpeta():
    """
    Esta funcion retorna un path de la carpeta descargas
    """
    # Se tiene una lista con las posibles rutas de descarga 
    rutas = [os.path.join(os.path.expanduser('~'),'Downloads'),os.path.join(os.path.expanduser('~'),'Descargas')]
    # Se itera para encontrar la acorde con el idioma del dispositivo
    for ruta in rutas:
        #En caso de que se encuentre una de estas se retornará
        if os.path.exists(ruta):
            return ruta
    # En caso de no encontrarla se retorma la dirección home del computado
    return os.path.expanduser('~')
