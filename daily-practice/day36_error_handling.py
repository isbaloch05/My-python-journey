
# try:
#    a=int(input("enter ur num :"))
#    print("ur num is ",a)
# except:
#    print("Data type error");


b=input("Enter ur num:")
print(f"the multiplication table of {b} is:")
try:
   for i in range(1,11):
       print(f"{int(b)} X {i}={int(b)*i}")
except ValueError:
    print("input error")   
