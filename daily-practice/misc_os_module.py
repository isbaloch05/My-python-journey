import os

# if( not os.path.exists("kkkk")):
#     os.mkdir("kkkk")

# for i in range (0,50):
    # os.mkdir(f"kkkk\\class{i+1}")
folder=os.listdir("kkkk");

for list in folder:
    print(list)
    print(os.listdir(f"kkkk\\{folder}"))

# for i in range(0,3366):
    # os.rmdir (f"C:\\Users\\Acer\\Desktop\\os module in python\\practice\\lessson {i+101}");
# for i in range(1,101):
    # os.rmdir(f"practice/lesson {i }")
print(os.getcwd());