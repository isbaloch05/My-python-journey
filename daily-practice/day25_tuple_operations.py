tpl=(1,2,3,4,5,6,7,8,9);
print(tpl)
print(type(tpl));
print("for opration on tuple first u need to change it into list".upper());
chng=list(tpl);
print(chng)
print(type(chng));
chng.append(10);
print(chng)
print("lets change it back to tuple")
tpl=tuple(chng);
print(tpl)
print(type(tpl));
s=tpl.index();
print(s)
