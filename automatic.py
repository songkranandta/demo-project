from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os





ROOT_DIR = os.path.dirname(os.path.abspath(__file__))



class GoogleDriveUpload:



    def __init__(self,path) :
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
        
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


        path_delete = ROOT_DIR+"/videos"


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
        #print(list_name_mydrive)
        

        
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        path = "/videos"
        path_name = ROOT_DIR+path

        # for file_name in os.listdir(path_name):
        #     print("filename:",file_name +"  path:",path_name)


        list_name_myfolder = []
        for file_name in os.listdir(path_name):
            list_name_myfolder.__iadd__([file_name])

        #print(list_name_myfolder)


#upload file ที่ชื่อไม่ซ้ำรหว่างใน my floder กับ my Drive
        list_upload = []
        list_upload = (str(list_name_myfolder) != str(list_name_mydrive))

        def filter_file(file_folder):
            file_cloud = list_name_mydrive

            if( file_folder in file_cloud):
                return False
            else:
                return True
        
        # import record
        fill_file_upload = filter(filter_file,list_name_myfolder) 
        upload_file_array = []
        
        # name_v2 = time_stamp_static+sec
        # sec = 10
        # time_stamp_static = name_v2

        f = open("recording_video.txt", "r")


        name_v2 = f.read()
        print(name_v2)
        for file_name_upload in fill_file_upload:
            if file_name_upload != name_v2:
                upload_file_array.__iadd__([file_name_upload])
        # print("Unique file name")
        #print(upload_file_array)
        print("Doing!!!"+name_v2)

        list_delete = []
        list_delete = (str(list_name_mydrive) != str(list_name_myfolder))

        def filter_file(file_cloud):
            file_folder = list_name_myfolder
            if( file_cloud in file_folder):
                return True
            else:
                return False

        fill_file_delete = filter(filter_file,list_name_mydrive) 
        delete_file_array = []

        for file_name_delete in fill_file_delete:
            delete_file_array.__iadd__([file_name_delete])
        #print("Duplicate file name")
        #print(delete_file_array)


        def delete():
            print(delete_file_array)
            for file_de in delete_file_array:
                if file_de != name_v2:
                    os.remove(path_delete+'\\'+file_de)
                    print("Delete file :"+file_de+":Success")

        


        path_name = ROOT_DIR+path
        for file_up in upload_file_array:
            f = drive.CreateFile({
                'title': file_up,
                "parents": [{'id':'1lohHkgXjFL-z8qXWOunyACgZbeL8-C1n'}],
                
                })
            f.SetContentFile(os.path.join(path_name, file_up))
            f.Upload()
            print("Upload : "+os.path.join(path_name,file_up)+" done!!")
            print(file_up)
            print("#####################################################################")
            f = None
        delete()   

