#Addition and equal  operator overloading
class Vector:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def __str__(self):
        return f"{self.a}i + {self.b}w +  {self.c}z"
    def __add__(self,other):
        return  Vector(  self.a+other.a, self.b + other.b , self.c + other.c)
    def __eq__(self,other):
        return (self.b==other.b)  #it gives true and false according to the repective value of b as the b value of x and y are equal so it give true 

x=Vector(2,4,6)
print(x)
y=Vector(3,4,9)
print(y)
print(x+y)  #it add them according to the operator overloading
print(x==y)

#Another practice 
class  Book:
    def __init__(self,title,num_pages,author):
        self.title = title
        self.num_pages = num_pages
        self.author = author
    def __str__(self):
        return f"The book '{self.title}' with {self.num_pages} pages is written by {self.author}"
    def __sub__(self,other):
        return (self.num_pages - other.num_pages)
    def __lt__(self,other):
        return (self.num_pages < other.num_pages)
    def __len__(self):
        return (self.num_pages )
        # for i in range(1,self.num_pages+1):
        #     print(i)
        # return (i)
            
a=Book("Atomic Habits",178,"James Clear")    
print(a)
b=Book("The Alchemist",250,"Paulo Cohelo")
print(b)
# print(a - b) #-72
print(f"Difference: {a - b} pages")
print(b - a) #+72 #the both are compared according to the num_pages only as it is the condition 
print(a < b)  #the both are compared according to the num_pages only as it is the condition 
print(a > b)  #not defined but python itself reflect it and checks it
print(len(a))