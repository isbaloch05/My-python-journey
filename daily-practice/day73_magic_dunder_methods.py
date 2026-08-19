class Presentation:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
    def show(self):
        print(f"does {self.name} from {self.grade} grade has a presentation?")
    def __str__(self):
        return f"does {self.name} from {self.grade} grade has a presentation? str"
    def __repr__(self):
        return f"yes {self.name} has one repr"
    def __call__(self,a,b):
        self.a=a
        self.b=b
        return a+b
class School:
    def __init__(self,grade,num_students):
        self.grade=grade
        self.num_students=num_students
    def __eq__(self,other ):
        return      self.num_students==other.num_students    #compare the num_students only whether they are equal or not
    def __lt__(self,other):
        return self.grade < other.grade  and self.num_students<other.num_students
    
p=Presentation("akmal",10)
print(str(p))
print(repr(p))
print(p(2,98))
a=School(12,456)
b=School(3,56)
c=School(3,56)
print(a==b)   #not equal so retuns false
print(c==b)   # equal so retuns true
print(a<b)    #falsa bcz not less than
print(a<c)     #falsa bcz not less than
print(c<a)      #true bcz it is less than
