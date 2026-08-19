class Father:
    def __init__(self,father_name):
        self.father_name=father_name
    def show(self):
        print(f"the father is {self.father_name}")
class Mother:
    def __init__(self,mother_name):
        self.mother_name=mother_name
    def details(self):
        print(f"the mother is {self.mother_name}")
class Son(Father,Mother):
    def __init__(self,identity,father_name,mother_name):
        Father.__init__(self,father_name)
        Mother.__init__(self,mother_name)
        self.identity=identity
    def check(self):
        print(f"he is the {self.identity} of {self.father_name} and {self.mother_name}.")
c=Son("son","ryaz","mahrang")
c.check()
c.show()
c.details()

#Another practice
class Employee:
    def __init__(self,name,id_num):
        self.name = name
        self.id_num = id_num
    def detail(self):
        print(f"Employee id:{self.id_num} is {self.name}")
class Programmer:
    def __init__(self,job_title):
        self.job_title = job_title
    def info(self):
        print(f"He is an {self.job_title}")
class EmployeeProgrammer(Employee,Programmer):
    def __init__(self,name,id_num,job_title,salary):
        Employee.__init__(self,name,id_num)
        Programmer.__init__(self,job_title)
        self.salary=salary
    def show(self):
        print(f"Mr.{self.name} , employee id: {self.id_num} gets salary {self.salary}$ as a {self.job_title}")
a = EmployeeProgrammer("Ismail Sadiq",2913,"AI Engineer",9999999)
a.show()
a.detail()
a.info()
print(EmployeeProgrammer.mro())#for checking the order of methods