x=56 #global variable
def local__variable():
    y=78; #local variable
    print(f" the local variable is  {y}");
local__variable();
print(f"the global variable is {x}")
j=58
print(j)
def takeglabalvariable():
      global j
      print(j)
      k=56
      print(k)
takeglabalvariable();
