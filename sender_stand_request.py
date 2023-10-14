import configuration #se improta el archivo  configuration
import requests #se importa la librería para ser las pruebas
import data #se importa el archivo data

def post_new_user ():# Función que genera crea un usuario
    #se realiza la petición enviando la  url de la api y el end point, que se encuentarn en archivo configuration.py
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=data.user_body,#se envia el los datos del json del archivo data.py
                         headers=data.headers)#se envía los encabezados  del archivo data.py
    response.json()['authToken']#Del resultado d la ejecución, extraemos del json, el token

def get_new_user_token():#definiendo el método
    token = post_new_user() #Almacenamos en la variable token, el resultado de la petición
    data.headers["Authorization"] = f'Bearer {token}';#Actualizamos el elemento "Authorization"+  del diccionario  header,
    # se agrega el token extraido del json de la respuesta de la generacion de usuario

def post_new_client_kit(NameKit):#función que recibe como parametro el nombre del Kit.
    get_new_user_token() #llama el metodo para asignar el token
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,#Se asigna  la ruta de la api + el end point
                             json=NameKit,#se envia el nombre del kid
                             headers=data.headers #Se envia  el header, incluyendo el token
                            );





