from __future__ import print_function
import os

from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

import threading
import time
import queue


# Daemon thread in background uploading pictures
def upload_pictures(inQ, outQ):
	while True:
		[localname, servername] = inQ.get()
		SCOPES = 'https://www.googleapis.com/auth/drive'
		store = file.Storage('storage.json')
		creds = store.get()

		if not creds or creds.invalid:
			flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
			creds = tools.run_flow(flow, store)

		DRIVE = discovery.build('drive', 'v3', http=creds.authorize(Http()))

		# Tipo del archivo -MIME TYPE-1
		mimeType = 'image/jpeg'

		# Id de la carpeta "Pictures" creada en Google Drive.
		folder = ['1MQE1O81aZgC8k2Nxg_i9RSOksJZsQigB']

		#for i in range(4):
		# Subimos el archivo y recibimos la respuesta
		metadata = {'name': servername, 'mimeType': 'image/jpeg', 'parents': folder}
		res = DRIVE.files().create(body=metadata, media_body=localname, fields='id, webViewLink, webContentLink').execute()

		if res:
			id_drive = res['id']
			URL_drive = res['webViewLink']
			URL_download = res['webContentLink']
			result = [id_drive, URL_drive, URL_download]
			outQ.put(result)

# Clear "results" table
op('results').clear()

# Initialize queues for communication
myInQ = queue.Queue()
myOutQ = queue.Queue()

me.parent().store('inQ', myInQ)
me.parent().store('outQ', myOutQ)

#use dummy values in the actual toe file storage
me.parent().storeStartupValue('inQ', None)
me.parent().storeStartupValue('outQ', None)


# our input Queue is there output Queue and vice versa
myThread = threading.Thread(target=upload_pictures, args=(myOutQ, myInQ,))

# careful about running this more than once
# it will keep spawning threads
myThread.start()