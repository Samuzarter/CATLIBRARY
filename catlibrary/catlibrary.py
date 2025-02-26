#CatLibrary
import requests
import json
from decouple import config
from pathlib import Path

path = Path(".")
url_Api = "https://cataas.com/api"
url_Cat = "https://cataas.com/cat"

def cats():
    """
    Esta funcion retorna un diccionario con el ID y TAGS de los primeros 10 gatos de la API CATAAS
    """
    #Se realiza el request a la Api por medio de una variable de entorno que contiene la URL, concatenado con el direccionamiento
    data = requests.get(url_Api+"/cats")

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
    data = requests.get(url_Api+"/count")
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
    data = requests.get(url_Cat+f"/says/{txt}?")
    #Se verifica el código de estado de la solcitud
    if data.status_code == 200:
        imagen = data.content
        #Se crea un path en donde por medio de la libreria OS se busca la carpeta Downloads para guardar la imagen
        imagepath = Verify_Images_Directory() / "Imagen.jpg"
        imagepath.touch()
        imagepath.write_bytes(imagen)
        return(f"Imagen guardada en {imagepath} con el nombre de imagen.jpg")


def Verify_Images_Directory():
    imagesdir = path / "Images"
    if imagesdir.exists():
        return imagesdir
    else:
        imagesdir.mkdir()
        return imagesdir
