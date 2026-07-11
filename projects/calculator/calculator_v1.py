
num1=float(input("enter first number: "));
num2=float(input("enter second number: "));
operator=input("Enter operator(+,-,*,/,//) :");
if operator=="+":
    print ("the answer is"+ str (num1+num2));
elif operator=="-":
    print("the answer is"+ str(num1-num2));
elif operator=="*":
    print("E she jawab "+( str(num1*num2)));
elif operator=="/":
    print("the answer is"+ str(num1/num2));
elif operator=="//":
    print("the answer is"+ str(num1//num2));
else:
    print("Invalid operator");
