# Generators are a special type of function that let you create an iterable sequence of values,
# producing one value at a time instead of building the whole sequence in memory upfront.
# This makes them memory-efficient — unlike a list, which stores every value at once,
# a generator only computes and holds the current value, then "pauses" until the next one is requested.
# `yield` is used instead of `return`: it pauses the function and remembers its state,
# so the next call to next() resumes right where it left off.

def generator():
    for i in range(100):
        yield i

gen = generator()
print(next(gen))    # 0
print(next(gen))    # 1
print(next(gen))    # 2
print(next(gen))    # 3
print(next(gen))    # 4
print(next(gen))    # 5
print(next(gen))    # 6
