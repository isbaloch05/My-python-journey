class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    #Alternatie constructers
    @classmethod
    def fromstr(cls,string):
        return cls(string.split(",")[0],int(string.split(",")[1]))
p=person("ismail",18)
print(p.name)
print(p.age)
string="saddam,45"
p2=person.fromstr(string)
print(p2.name)
print(p2.age)

class dog:
    def __init__(self,race,age):
        self.race=race
        self.age=age
    @classmethod
    def str_type(cls,string):
        return cls(string.split("-")[0],int(string.split("-")[1]))
d1=dog("GS",45)
print(d1.race)
print(d1.age)
string="BD-34"
d2=dog.str_type(string)
print(d2.race)
print(d2.age)

class Resident:
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city
    @classmethod
    def from_str(cls,string):
        name,age,city=string.split(",")
        return cls(name,int(age),city)
string="ismail,18,panjgoor"
C=Resident.from_str(string)
print(C.name)
print(C.age)
print(C.city)