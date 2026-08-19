#level one the first class
class Vehicle:
    def __init__(self,brand):
        self.brand =brand
    def car(self):
        print(f"this a {self.brand}.")
#level two the first class(Vehicle) is inherited by second class(BMW)
class BMW(Vehicle):
    def __init__(self,brand,model):
      super().__init__(brand)
      self.model = model
    def details(self):
        print(f"the car is {self.brand},{self.model}")
#level three the third class(CarType) is inherits the second class (BMW) which has also inherited the first class (Vehicle) showing three level
class CarType(BMW):
    def __init__(self,brand,model,type):
        super().__init__(brand,model)
        self.type=type
    def show(self):
        print(f"He drives a {self.type} {self.brand},{self.model}")
a = BMW("bmw",2024)
a.car()
a.details()
b=CarType("Ferrari",1995,"Manual")
b.show()