
class student:
    school="BRCL"      #class variable
    def __init__(self,name):
        self.name=name
    def details(self):
        print(f"his name is {self.name} and he studies in {self.school}")
    @classmethod     #it can be used to change a class variable entirel for all instances
    def change_school(cls,new_school):
        cls.school=new_school
a=student("saddam")
a.details()
b=student("ismail")
b.school="fg college"     #overwrote the class variable into an instance variable
b.details()
print(student.school)
c=student("qamar")       #but it changes the class variable to a new one 
c.change_school("ccp")
c.details()
print(student.school)

