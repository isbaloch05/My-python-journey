import multiprocessing
import time

def mp(seconds):
    time.sleep(seconds)
    print(f"the program was halted for {seconds} seconds")


p1= multiprocessing.Process(target = mp , args = ( 3, ))
p2= multiprocessing.Process(target = mp , args = ( 4 , ))
p3= multiprocessing.Process(target = mp , args = ( 5, ))
if __name__ == "__main__":
    a= time.perf_counter()
    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()
    b = time.perf_counter()
    print(b-a)