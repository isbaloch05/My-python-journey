import threading
import time

def fun(seconds):
    time.sleep(seconds)
    print(f"the sleeping time is {seconds} seconds")

# #normal way 
# # a = time.perf_counter()
# # fun(2)
# # fun(3)
# # fun(4)
# # b = time.perf_counter()
# # print(b-a)  #to check how much time it takes in normal way

#threading
t1=threading.Thread(target = fun , args = [2])
t2=threading.Thread(target = fun , args = [3])
t3=threading.Thread(target = fun , args = [5])
e= time.perf_counter()
t1.start()
t2.start()
t3.start()
f= time.perf_counter()
print(f-e)
#wait for execution of one then the other
c = time.perf_counter()
t1.join()
t2.join()
t3.join()
d = time.perf_counter()
print(d-c)  #to check how much time it takes in threading

#concurrent futures
from concurrent.futures import ThreadPoolExecutor
def func(seconds):
    time.sleep(seconds)
    print(f"the sleeping time is {seconds} seconds")
    return seconds

def tpe():  #tpe = "ThreadPoolExecutor" . just for remembering
    with ThreadPoolExecutor() as executor:
        # a = executor.submit(func , 2)
        # b = executor.submit(func , 3)
        # c = executor.submit(func , 1)
        # print(a.result())
        # print(b.result())
        # print(c.result())
 # .map()  alternate of submit()    
       l = [3,4,2,5,1]
       result = executor.map(func, l) 
       for results in result:
           print(results)


tpe()

