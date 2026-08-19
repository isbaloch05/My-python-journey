#single inheritance
class Animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
    def show(self):
        print(f"the {self.name} makes '{self.sound}' sound")
class Cat(Animal):
    def __init__(self,name,sound,specie):
        super().__init__(name,sound)
        self.specie=specie
    def show(self):
        # super().show()
        print(f"{self.name} comes in {self.specie}")
a=Animal("dog","wahoo wahoo wahoo")
a.show()
b=Cat("cat","meow","pet animals")
b.show()