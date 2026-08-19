import os
folder_path="C:/Users/Acer/Desktop/testfile"
counter={}
os.listdir(folder_path)
for files_name in os.listdir(folder_path):
    files_name,  extension=os.path.splitext(files_name)
 
new_name="1.png"
old_path="C:/Users/Acer/Desktop/testfile"
new_path="C:/Users/Acer/Desktop/testfile"
os.rename("C:/Users/Acer/Desktop/testfile/files_name","C:/Users/Acer/Desktop/testfiles/new_name")
