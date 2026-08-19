print("Topic_decoraters_used to modify a function ")
def deco(fx):
    def dfx():
     print("lets modify it")
     fx()
     print("modified")
    return dfx
# @deco#the first method(syntax ) to use/call decoraters by @ statement
def hi():#the function to be modified
    print("Hey! how r u.")
deco(hi)()#the second way to use decoreters
print("now functions with arguments are decorated somehow differently".title())
def fun_arg(fx):
   def cfx(*args,**kwargs):
      print("the arguments(x,y)")
      result=fx(*args,**kwargs)
      print("gave them as u can see the result")
      return result
   return cfx
@fun_arg
def arthimatic_operation(x,y):
   print(x+y)
   print( x*y)
arthimatic_operation(34,67)
print("thanks")