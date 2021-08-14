import os
import list

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


path_delete = ROOT_DIR+"/videos"

def delete():
    print(list.delete_file_array)
    for file_de in list.delete_file_array:
        os.remove(path_delete+'\\'+file_de)
        print("Delete file :"+file_de+":Success")
