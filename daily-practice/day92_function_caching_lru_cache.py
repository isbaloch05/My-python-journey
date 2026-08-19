from functools import lru_cache
import time
@lru_cache(maxsize=128)
def square(n):
    time.sleep(3)
    return n * n


print("First time")
print(square(2))
print(square(3))
print(square(4))
print(square(5))

print("second time")
print(square(2))
print(square(3))
print(square(4))
print(square(5))
