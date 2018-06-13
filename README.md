# Python Script to upload files to Google Drive

## Installation

- Windows/Python3.5:

To get credentials and activate Drive API, follow steps detailed in: https://developers.google.com/drive/api/v3/quickstart/python?authuser=3

Once your "client_secret_XXXXXXXXXXX.json" file is downloaded, rename it to "client_secret.json" and save it in project root folder.

Save your images in "Pictures" folder and change FILES variable accordingly:

'''
FILES = (
    ('Pictures/foto1.jpg', 'image/jpeg'),
    ('Pictures/foto2.jpg', 'image/jpeg'),
)
'''

Don't forget to change mimetype depending on your file type.

Install needed libraries:

Open a console and install modules using pip.

1) Google-API-Python-Client Library:

pip install --upgrade google-api-python-client

2) OAuth Library:

pip install --upgrade oauth2client

Finally, you can test your file using:

python img_uploader.py

First time you do it, your browser will open to approve permissions. It is only first time.