class GrandParent:
    def __init__(self,grand_father,grand_mother):
        self.grand_father = grand_father
        self.grand_mother = grand_mother
    def show(self):
        print(f"{self.grand_father} and {self.grand_mother} are father and mother ,along with grand parents ")
class Child(GrandParent):
    def __init__(self,grand_father,grand_mother,father,mother):
        super().__init__(grand_father,grand_mother)
        self.father = father
        self.mother = mother
    def info(self):
        print(f"we are {self.father} and {self.mother} , {self.grand_father} and {self.grand_mother} are our parents")
class GrandChild(GrandParent):
    def __init__(self,grand_father,grand_mother,child1,child2):
        super().__init__(grand_father,grand_mother)
        self.child1 = child1
        self.child2 = child2
    def details(self):
        print(f"{self.grand_father} and {self.grand_mother} are grand parents of {self.child1} and {self.child2}")
g=GrandParent("juma","BB")
g.show()
a=Child("juma","BB","sadiq","BB")
a.info()
b=GrandChild("juma","BB","ismail","salman")
b.details()
