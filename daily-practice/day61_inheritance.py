defination={"defination":"inheritance is used to take some details from an exiting class without the neeed to write them again"}
print(defination)
class students_details:
    def __init__(self,name,grade,gender):
        self.name=name
        self.grade=grade
        self.gender=gender
    def check_details(self):
        print(f"student name:{self.name}\nstudent grade:{self.grade} \nstudents gender:{self.gender}")
class trnasfer_student(students_details):
    def added_details(self):
        print("destrict:panjgoor")
fg=students_details("ismail",11,"male")    
fg.check_details()  
inheritance=trnasfer_student("zaid",12,"non_binary")
inheritance.check_details()
inheritance.added_details()
