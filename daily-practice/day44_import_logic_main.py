print("import".upper())
import math
print(math.sqrt(49))
print(math.pi)

print("as keyword".upper())
import math as m
print(m.sqrt(100));

print("from keyword".upper());
from math import sqrt,pi
print(sqrt(81));

print("* keyword".upper())
print("it imports all the functions from module but it is not recommended")

print("dir keyword".upper());
import math
print(dir(math));
print("dir tells us about all the functions present in the module, and as u can see above it showed functions".title());

import myownmodule as mom
mom.droshum()
# print(dir(mom));



