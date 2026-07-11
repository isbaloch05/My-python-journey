set={"tang","dilband","jagar","tabahag","dilband"};
print (set);
for item in set:
    print(item);
print("As u can see it did not printed the dilband two times bcz it is a set and it does does not maintain order".upper());
print("SETS METHODS".center(50))
print(".union()".center(50).upper());
set1={1,4,8,3,5};
set2={8,9,6,5,3};
print(set1.union(set2))
set1.update(set2)
print(set1)

print("intersection".upper())
print(set1.intersection(set2));

print("symmetric_difference".upper())
print(set1.symmetric_difference(set2));

print("isdisjoint".upper())
print(set1.isdisjoint(set2))

print("issuperset".upper())
print(set1.issuperset(set2))

print("issubset".upper())
print(set1.issubset(set2))

print("add".upper())
print(set1.add(10));

print("remove".upper())
print(set1.remove(8))


print("discard".upper())
print(set1.discard(8))


print("pop".upper())
print(set1.pop())


print("delete(del)".upper())
# del set1