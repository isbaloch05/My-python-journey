import time as t  #now u will be to write  only t for time module 
#time()
print(t.time())   #floating points time in seconds since 1970


#localtime()
a=t.localtime()
print(a)


#strftime() : shows in string
b=t.strftime("%Y-%m-%d %H:%M:%S",a)
print(b)


#sleep(): halt the current execution for some given second
print("after this print it will halt the execution for 4 seconds")
t.sleep(4)   # holds the execution for 4 seconds
print("after 4 seconds it will run ")




#to check the the  time duration of a function execution in seconds
def forloop():
    for i in range(2000):
        print(i)
d = t.time()
forloop()
print("the time which the function took to complete:",t.time() - d)

