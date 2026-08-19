class Book:
    """a simple book with name and author"""#this will also be shown in help 
    def __init__(self,name,author):
        self.name=name
        self.author=author
    
b=Book("rich dad poor dad","robert tikysio")
print(dir(b))           #it tells us all the methods and attributes in the class 
print(b.__dict__)       #it shows the object instances in dictionary representation 
print(help(b))          #shows the documentation help of an object 