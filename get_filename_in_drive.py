from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os



gauth = GoogleAuth()
# Try to load saved client credentials
gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
    # Authenticate if they're not there
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()
# Save the current credentials to a file
gauth.SaveCredentialsFile("mycreds.txt")

drive = GoogleDrive(gauth)


folder = "Peafowl"  
folder_id = "" 


#list id file from google drive folder_name : Peafowl
file_folder = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for folder in file_folder:
    # print('title: %s, id: %s' % (folder['title'], folder['id']))
    if folder['title'] == "Peafowl" :
        folder_id = folder['id']
    

list_name_mydrive = []
list_file = drive.ListFile({'q': "'"+folder_id+"' in parents and trashed=false"}).GetList()
for file in list_file:
    #print('title: %s, id: %s' % (file['title'], file['id']))
    list_name_mydrive.__iadd__([file['title']])
print(list_name_mydrive)