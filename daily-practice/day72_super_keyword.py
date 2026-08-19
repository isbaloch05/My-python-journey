class father:
    def __init__(self,name ,city):
        self.name=name
        self.city=city
class child(father):
    def __init__(self,name,city,job):
        self.job=job
        super().__init__(name,city)
f=father("azeem","karachi")
print(f.name)
print(f.city)
c=child("\nzaka","quetta","AI engineer")
print(c.name)
print(c.city)
print(c.job)

class Intro:
    def show(self):
        print("hi! i am zaid")
class ChildIntro(Intro):
    def details(self):
        super().show()
        print("hi i am his son")
i=Intro()
i.show()
c=ChildIntro()
c.details()  