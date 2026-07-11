for i in range(6):
    print(i);
else:
    print("the loop was exacuted completely so else was printed");
for x in range(7):
    print(x)
    if x==5:
        break
else:
    print("loop was not executed completely so else was not printed")    

print("""for x in range(7):
    print(x)
    if x==5:
        break
else:
    print("loop was not executed completely so else was not printed") 
      "here the else wont be printed because of break"   """)

y=0
while y<7:
     print(y)
     y=y+1
else:
    print("in while see the else ")    