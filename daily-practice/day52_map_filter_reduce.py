print("MAO Function")
print("the long method without map".upper())
def expo(x):
    # y=3 #local variable
    return x**3
print(expo(4))
k=[2,3,4,5,6,7,8,9]
nl=[]
for ele in k:
    nl.append(expo(ele))
print(nl)

print("the  same thing with map".upper())
jk=list(map(expo,k)) #here the list that they should be in list format
print(jk)
io=(2,3,4,5,6,7,8,9)
hut=str(map(expo,io))#here it is in int format
print(hut);


print("filter".upper())
def low_function(a):
    return a<6;
yu=list(filter(low_function,io))
print(yu)

# hg=lambda h:h>4

ji=list(filter(lambda h:h>4,io))#hg is written directly
print(ji)