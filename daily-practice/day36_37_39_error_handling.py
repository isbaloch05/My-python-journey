
# try:
#    a=int(input("enter ur num :"))
#    print("ur num is ",a)
# except:
#    print("Data type error");


# b=input("Enter ur num:")
# print(f"the multiplication table of {b} is:")
# try:
#    for i in range(1,11):
#        print(f"{int(b)} X {i}={int(b)*i}")
# except ValueError:
#     print("input error")   

a=int(input("ebter no in between 3 to 9::"));
print(a);
if a<3 or a>9:
   raise ValueError("number is greater than 9 and less than 3")
else:
   print("coditions met")
# if a==str("quit"):
#    print(a)
