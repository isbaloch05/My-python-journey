#list methods
print("append method".center(60));
list=['Ismail','sadiq'];
print(list)
list.append("Baloch");
print(list);
print("as u can see it added one extra element in the same  list by append ".upper());
print("sort method".upper().center(50));
asc=[29,48,87,8,6,0,34,64,1,94,2,3]
print(asc);
asc.sort();
print(asc);
print("it sorted them in ascending order by sort list method".upper());
asc.sort(reverse=True)
print(asc)
print("now in descending oreder".upper())

print("the reverse list method".title().center(65));
name=["I","s","m","a","i","L"];
print(name);
name.reverse();
print(name);
print("now u can see the name is reversed by reverse list method".title());

print("the index method".center(45).title());
ind=[1,3,6,7,8,4,5,];
print(ind);
# print(len(ind));
print (ind.index(6));
print("as u can see it give the idex of 6 which is 2 in the output".upper());

print("the count method of list".title().center(70));
more=[1,2,3,4,5,5,5,5,7,8,6,6];
print(more);
print(more.count(5));
print(more.count(6));
print("it counted 5 and 6 and told that how many itmes they are there:".upper())

print("the copy method of list".title().center(59));
f=more.copy();
print(f);
print("the entire list was copied by copy() method without writing it again".upper());

print("the insert method, it adds new element".upper().center(89));
g=["i","am"];
print(g);
g.insert(2,"ismail");
print(g);
print("it added my name which was not in the list".upper());

print("the extend method, used to extend the list".title().center(67));
k=[3,5,6,7,8,9];
print(k);
j=(0,10,11,12);
k.extend(j);
print(k);
print("as u can see new extended elements were added".capitalize());


print("not sure whether a list method or not but used for jioning/concinate two lists".center(78).title());
a=[1,2,3,4,5];
print(a);
b=[6,7,8,9];
print(b);
c=a+b;
print(c);
print("it added the two lists".upper());
