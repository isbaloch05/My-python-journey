import os
#x represent the files and folders path
png_files_path="C:/Users/Acer/Desktop/x/x/x"  #the files path to rename 
f=os.listdir(png_files_path)
i=1  #give it a value from here for chnaging 
for files in f:
    print(files)
    if files.endswith(".png"):
        os.rename(f"C:/Users/Acer/Desktop/x/x/x/{files}" , f"C:/Users/Acer/Desktop/x/x/x/{i}.png")
        i=i+1
os.rename("C:/Users/Acer/Desktop/x/x/x/x.png","C:/Users/Acer/Desktopx/x/x.png")
