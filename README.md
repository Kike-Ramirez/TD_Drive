# Python Script to upload files to Google Drive

## Installation Windows/Python3.5:

### Credentials

To get credentials and activate Drive API, follow steps detailed in: https://developers.google.com/drive/api/v3/quickstart/python?authuser=3

Once your "client_secret_XXXXXXXXXXX.json" file is downloaded, rename it to "client_secret.json" and save it in project root folder.

### Install needed modules:

Open a console and install modules using pip.

1. Google-API-Python-Client Library:

pip install --upgrade google-api-python-client

2. OAuth Library:

pip install --upgrade oauth2client

Finally, you can test your file using:

python img_uploader.py

## To upload a file you should change following variables:

### Path for local file to upload
localname = 'Pictures/foto1.jpg'

### Name for file in Drive Server
servername = 'sonarabsolute2018.jpg'

### MimeType depending on the file format
mimeType = 'image/jpeg'

## File Google Drive URL Link
If the uploading is OK it will be stored in URL_drive variable.

## NOTE

First time you run the script, your browser will open to approve permissions. It is only first time.
