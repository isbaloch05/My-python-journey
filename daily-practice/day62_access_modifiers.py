print("access modifiers".upper())
defination=("types:\n" "1.public access modifiers\n" "2.privte access modifiers\n" "3.protected access modifiers")
print(defination)

print("Public Access Modifiers")
class sports_gala:
    def __init__(self,name,kit_no,sport):#everything was defined in class 
        self.name=name
        self.kit_no=kit_no
        self.sport=sport
    def check(self):
        print(f"Student {self.name} with id {self.kit_no} plays {self.sport}")
details=sports_gala("ismail",2913,"football")
details.check() 
class public:
    pass#nothing is defined in it but as u can see but still outside of class i accessed it
a=public()
a.name="ismail"#from here and
print(a.name)                 #here
        
print("Private Access Modifiers")
syntax=("_classname__attribute name")
print(syntax)
class info:
    def __init__(self):
        # self.name="ismail sadiq"#not private yet to make it private we use __
        self.__name="ismail sadiq"#private and can't be called without the __
nm=info()
# print(nm.name)#not accessible
print(nm._info__name)#accesible 

print("protected access modifiers".upper())
class child:
    def __init__(self):
        self._name="droshum"#_name  indicate pretected
    def _protectedFunc(self):#protected method
        print("droshumbaloch")
    
     
obj=child()
print(obj._name)
obj._protectedFunc()
# ---- ACCESS MODIFIERS IN PYTHON ----
# Python has no real access modifiers (unlike Java/C++) - just naming conventions:
#
# PUBLIC     -> self.name        : accessible from anywhere, no restriction
# PROTECTED  -> self._name       : convention only, "please don't touch outside class", not enforced
# PRIVATE    -> self.__name      : name-mangled to self._ClassName__name
#                                   -> nm.__name fails (AttributeError)
#                                   -> nm._ClassName__name still works (not truly private)
#                                   -> proper way to access = use a public method (getter)
#
# Point of private/protected = force access through class methods (encapsulation),
# not to make data 100% unreachable.         