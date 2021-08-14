import get_filename_in_folder as gf
import get_filename_in_drive as gd

# print(gf.list_name_myfolder)
# print(gd.list_name_mydrive)


#upload file ที่ชื่อไม่ซ้ำรหว่างใน my floder กับ my Drive
list_upload = []
list_upload = (str(gf.list_name_myfolder) != str(gd.list_name_mydrive))

def filter_file(file_folder):
    file_cloud = gd.list_name_mydrive

    if( file_folder in file_cloud):
        return False
    else:
        return True

fill_file_upload = filter(filter_file, gf.list_name_myfolder) 
upload_file_array = []

for file_name_upload in fill_file_upload:
    upload_file_array.__iadd__([file_name_upload])
print("Unique file name")
print(upload_file_array)


#Delete ไฟล์ ที่มีชื่อซ้ำกันระหว่างใน my Drive กับ my folder 

# list_delete = []
# list_delete = (str(gd.list_name_mydrive) != str(gf.list_name_myfolder))

# def filter_file(file_cloud):
#     file_folder = gf.list_name_myfolder
#     if( file_cloud in file_folder):
#         return True
#     else:
#         return False

# fill_file_delete = filter(filter_file, gd.list_name_mydrive) 
# delete_file_array = []

# for file_name_delete in fill_file_delete:
#     delete_file_array.__iadd__([file_name_delete])
# print("Duplicate file name")
# print(delete_file_array)


len_upload_file_array = len(upload_file_array)


