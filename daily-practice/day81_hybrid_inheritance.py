class Person:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"I am {self.name}")
class Profession(Person):
    def __init__(self,name,job):
        super().__init__(name)
        self.job=job
    def details(self):
        print(f"I am {self.name} and I am a {self.job}")
class Sport:
    def __init__(self,sport):
        self.sport=sport
    def info(self):
        print(f"I like {self.sport}")
class Profile(Profession,Sport):
    def __init__(self,name,job,sport,graduation,):
        Profession.__init__(self,name,job)
        Sport.__init__(self,sport)
        self.graduation = graduation

    def describe(self):
        print(f"MY name is {self.name}, i am a {self.job} , i play {self.sport} and i am a graduate in {self.graduation} ")


a=Person("Ismail sadiq")
a.show()
b=Profession("Zaid Baloch","Student")
b.details()
c=Sport("football")
c.info()
d=Profile("saddam","nurse","cricket","nursing")
d.describe()
d.show()
d.details()
d.info()