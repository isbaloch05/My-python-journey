#function
def boy(a,b):
    logic=(a*b)/(a+b)
    print(logic)


def girl(a,b):
    if (a<b):
        print("first no is greater")
    else:
        print("second no is greater")


a=61
b=56
# gmean1=(a*b)/(a+b)
# print(gmean1)
print("the geometric mean of a and b is:"); 
boy(a,b)
girl(a,b)


c=12
d=19
# gmean2=(c*d)/(c+d)
# print(gmean2)
boy(c,d)
girl(a,b)

e=456575
f=787897
boy(e,f)
girl(e,f)