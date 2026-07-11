# power= lambda x:x**2

# print(power(5));
# print("the main use is to use it as a argument of the bigger function".upper());
def sqr(fy,value):
    return  fy(value) - 2

sqrty= lambda y: y**2
print(sqr(sqrty,5))
      