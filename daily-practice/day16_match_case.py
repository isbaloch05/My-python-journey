x =  int(input("enter ur no::"))
match x:
    case 0:
        print ("x is zero")
    case 1:
        print("x is 1")
    case 3:
        print("x is 3")
    case _ if x!= 70:
        print (x,"is not equal to 70");
    case _ if x>60:
        print(x,"is grater than 60");
