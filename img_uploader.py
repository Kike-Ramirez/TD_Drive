#!/usr/bin/env python

from __future__ import print_function
import os

from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

import threading
import time
import logging


# Hilo individual que sube cada foto
def upload_pictures():

	SCOPES = 'https://www.googleapis.com/auth/drive'
	store = file.Storage('storage.json')
	creds = store.get()

	if not creds or creds.invalid:
		flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
		creds = tools.run_flow(flow, store)

	DRIVE = discovery.build('drive', 'v3', http=creds.authorize(Http()))

	# Aqui definimos los parametros del archivo a subir, carpeta y enlace. 
	# JAVO, deberias linkar con tu script de TD las variables localname, servername y URL_drive.

	# Ruta del archivo local
	localname = ['pics/p0.jpeg', 'pics/p1.jpeg', 'pics/p2.jpeg', 'pics/p3.jpeg']

	# Nombre del archivo en el servidor
	servername = ['ppsonarabsolute2018_0.jpeg', 'ppsonarabsolute2018_1.jpeg', 'ppsonarabsolute2018_2.jpeg', 'ppsonarabsolute2018_3.jpeg']

	# Tipo del archivo -MIME TYPE-1
	mimeType = 'image/jpeg'

	# Id de la carpeta "Pictures" creada en Google Drive.
	folder = ['1MQE1O81aZgC8k2Nxg_i9RSOksJZsQigB']

	for i in range(4):
		# Subimos el archivo y recibimos la respuesta
		logging.debug('Started uploading: ' + str(i))
		metadata = {'name': servername[i], 'mimeType': 'image/jpeg', 'parents': folder}
		res = DRIVE.files().create(body=metadata, media_body=localname[i], fields='id, webViewLink, webContentLink').execute()

		if res:
			URL_drive = res['webViewLink']
			URL_download = res['webContentLink']
			logging.debug('Finished: ' + str(i) + ' - ' + URL_drive + ' - ' + URL_download)

# Funcion principal que lanza los 4 hilos
if __name__ == '__main__':

	logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-9s) %(message)s',)
	t = threading.Thread(name='upload',target=upload_pictures)
	t.setDaemon(True)
	t.start()
	#time.sleep(10)
