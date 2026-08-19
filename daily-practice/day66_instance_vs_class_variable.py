class Bike:
    bike_brand="honda"                #class variable
    def __init__(self,rider_name,age):
        self.rider_name=rider_name   #instance variable  
        self.age=age                 #instance variable
    def details(self):
        print(f"the biker is {self.rider_name} and his age is {self.age} who rides {self.bike_brand}")
person1=Bike("zaid",23)
person1.bike_brand="unique"       #honda to unique (overwrites the class variable to instance variable does not chnage it)
person1.details()
person2=Bike("saddam",25)
person2.age=16                    #age from 25 to 16
person2.details()
print(Bike.bike_brand)           #class variable