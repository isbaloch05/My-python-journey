class library:
    def __init__(self):
        self.books=[]
        self.no_of_books=0
    def add_book(self,book_title):
        self.books.append(book_title)
        self.no_of_books+=1
    def all_books(self):
        for books in self.books:
            print(f"Books Title :{books}")
    def books_quantity(self):
        print(f"Books Quantity: {self.no_of_books}")
        
lib=library()        
lib.add_book("habits")
lib.add_book("python")
lib.add_book("A kit runner")
lib.add_book("Think And Grow Rich ")

print(lib.books)
# print(lib.no_of_books)   
lib.all_books()  
lib.books_quantity()

