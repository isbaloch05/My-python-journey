a=2;
b=2;
print(a == b);
print(a is b);

#using immutable data type
tuple1=(1,3,4,5,7);
tuple2=(1,3,4,5,7);
print(tuple1==tuple2)
print(tuple1 is tuple2)

#checking on mutable data tyoe
list1=[1,3,4,5,7];
list2=[1,3,4,5,7];
print(list1 == list2)
print(list1 is list2)

# == copares the values
# is only checks the memory location
# import os 
# d=open("oops_day_55.py","x").close()

