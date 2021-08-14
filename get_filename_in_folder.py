import os


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
path = "/videos"
path_name = ROOT_DIR+path

# for file_name in os.listdir(path_name):
#     print("filename:",file_name +"  path:",path_name)

list_name_myfolder = []
for file_name in os.listdir(path_name):


    print(list_name_myfolder)