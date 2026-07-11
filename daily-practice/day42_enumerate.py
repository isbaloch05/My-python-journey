name=["gk","dk","ab","ak","sk","i.ab"];
index=2
for names in name:
    print(names)
    if index==4:
        print("wow godd name")
    index +=1;


print("now with enumerate function");
for index,names in enumerate(name, start=2):
    print(names)
    if(index==3):
        print("at index directly");
