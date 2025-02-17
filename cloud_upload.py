from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

def upload_to_drive(filename):
    file = drive.CreateFile({'title': filename})
    file.SetContentFile(filename)
    file.Upload()
    print(f"Uploaded {filename} to Google Drive.")
