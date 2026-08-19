print("OOPs programming");
print("Class and object");
print("class- the design or blueprint, object-the execution of the desigh and blue print");
class student:#student is the class wit student name
    name="ismail sadiq"
    grade=11
    college="FG college"
    def detail(self):
        print(f"{self.name} is a student  in {self.grade} class reading in {self.college}.")

a=student();# a is acting as object
b=student();# b is acting as object
b.name="Anes ur rehman"
print(a.name, a.grade)
print(b.name, b.grade)
a.detail()
b.detail()
# import os #to make the next day file
# open("constructors_day_58.py","x").close()