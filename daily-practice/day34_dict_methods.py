dict={445:67,446:95,447:87};
print(dict);

print("the update method".upper().center(87))
dict.update({448:98});
print(dict);

print("pop method - removes an item ".upper());
dict.pop(446);
print(dict)
 
print("clear".upper())
dict2={45:67,446:95,447:87}
dict2.clear()
print(dict2)

print("popitem()-rmeoves the last key pair vlue".upper())
dict.popitem()
print(dict)

print("del method delete the enitire dictionary".upper())
goat={445:67,446:95,447:87}
del goat
print(goat)