#f-strring a method of string which replaced the format method some how:
x="i am reding in {} class, in {} college "
# print(x.format("11","fg ")
classnum=input("enter your class:");
college=input("enter your college:");
print(f"i am reding in {classnum} class, in {college} college ");
print(f"i am reding in {{classnum}} class, in {{college}} college ");
price=120.333333333;
print(f"the price of the product is {price:.2f} rupees");
print(f"the price of the product is {price:.3f} rupees");