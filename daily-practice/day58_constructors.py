class teacher:
    def __init__(self,nm,sl):
        # print("hey i am a teacher")
        self.name=nm
        self.salary=sl
    def detail(self):
        print(f"i am {self.name} my salary is {self.salary}")    
a=teacher("nabil","5 lacs")
b=teacher("salim ","3.5 lacs")
# v=teacher() # the arguments sl and nm are missing 
# nm="nabil"
# sl="5 lacs"
a.detail()
b.detail()