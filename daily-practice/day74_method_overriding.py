#firt time practicing
class Geometry:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def rec_area(self):
        return self.x * self.y
g=Geometry(2,5)
print(g.rec_area())
class Circle_area(Geometry):
    def __init__(self,radius):
        super().__init__(radius,radius)
        self.radius=radius
    def circle_area(self):
        return 3.14 * super().rec_area()
circle=Circle_area(9)
print(circle.circle_area())

#second time practicing
class Shape:
    def __init__(self,name):
        self.name=name
    def describe(self):
        print(f"This is a shape of {self.name}")
class Circle(Shape):
    def __init__(self,name,radius):
        super().__init__(name)
        self.radius=radius
        # self.name=name   we are inheriting it from Shape class 
    def describe(self):
        super().describe()
        print(f"this is a {self.name} with {self.radius} radius")   
class Triangle(Shape):
    def __init__(self,name,height,base):
        super().__init__(name)
        self.height=height
        self.base=base
    def describe(self):
        super().describe()
        print(f"the {self.name} has a {self.height}cm height and {self.base}cm base\n Area is {self.area()}cm")
    def area(self):
        return 0.5 * self.height * self.base

s=Shape("Triangle")
s.describe()
c=Circle("circle",34)
c.describe()
t=Triangle("triangle",34,45)
t.describe()

#third time practing
class Vehicle:
    def __init__(self,name,model):
        self.name=name
        self.model=model
    def details(self):
        print(f"he has a {self.name} car,{self.model} model")
class Car(Vehicle):
    def __init__(self,name,model,country):
        super().__init__(name,model)
        self.country=country
    def details(self):
        super().details()
        print(f"he imported the {self.name} from {self.country}.")


v=Vehicle("Honda",2011)
v.details()
c=Car("Toyota",2019,"Japan")
c.details()