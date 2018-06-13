#!/usr/bin/env python

from __future__ import print_function
import os

from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

SCOPES = 'https://www.googleapis.com/auth/drive'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
DRIVE = discovery.build('drive', 'v3', http=creds.authorize(Http()))

# Aquí definimos los parámetros del archivo a subir, carpeta y enlace. 
# JAVO, deberías linkar con tu script de TD las variables localname, servername y URL_drive.

# Ruta del archivo local
localname = 'Pictures/foto1.jpg'

# Nombre del archivo en el servidor
servername = 'sonarabsolute2018.jpg'

# Tipo del archivo -MIME TYPE-
mimeType = 'image/jpeg'

# Id de la carpeta "Pictures" creada en Google Drive.
folder = ['1MQE1O81aZgC8k2Nxg_i9RSOksJZsQigB']

metadata = {'name': servername, 'mimeType': mimeType, 'parents': folder}

# Subimos el archivo y recibimos la respuesta
res = DRIVE.files().create(body=metadata, media_body=localname, fields='id, webViewLink').execute()

if res:
    print('Subido "%s" con id: %s' % (localname, res['id']))
    URL_drive = res['webViewLink']


# En la variable URL tienes el enlace para verlo
print('URL Link: %s' % URL_drive)


