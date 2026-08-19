class library:
    def __init__(self,name,bookid):
        self._name=name
        self._bookid=bookid
    # def name(self):
        # print(f"student name is:{self._name}")
    # def bookid(self):
        # print(f"the book id is:{self._bookid}")
    @property
    def the_name(self):
        # "the getter was used)
        return f"the student name {self._name}"
    @property
    def the_bookid(self):
        # "the getter was used)
        return f"the bookid is {self._bookid}"
    @the_name.setter
    def the_name(self,new_student):
        # "the setter in here"
        self._name=new_student
    @the_bookid.setter
    def the_bookid(self,new_bookid):
        # "the setter in here"
        self._bookid=new_bookid
lib=library("ismail",3453)
print(lib.the_name)
print(lib.the_bookid)
lib.the_name="zaid"
lib.the_bookid=2913
print(lib.the_name)
print(lib.the_bookid)
# lib.name()
# lib.bookid() they are just for my undrstanding

