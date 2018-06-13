# Python Script to upload files to Google Drive

## Installation

- Windows/Python3.5:

To get credentials and activate Drive API, follow steps detailed in: https://developers.google.com/drive/api/v3/quickstart/python?authuser=3

Once your "client_secret_XXXXXXXXXXX.json" file is downloaded, rename it to "client_secret.json" and save it in project root folder.

Install needed libraries:

Open a console and install modules using pip.

1) Google-API-Python-Client Library:

pip install --upgrade google-api-python-client

2) OAuth Library:

pip install --upgrade oauth2client

Finally, you can test your file using:

python img_uploader.py

First time you do it, your browser will open to approve permissions. It is only first time.

## To upload a file you should change following variables:

### Ruta del archivo local
localname = 'Pictures/foto1.jpg'

### Nombre del archivo en el servidor
servername = 'sonarabsolute2018.jpg'

### MimeType depending on the file format
mimeType = 'image/jpeg'

## File Google Drive URL Link
If the uploading is OK it will be stored in URL_drive variable.
