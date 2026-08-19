import argparse
if __name__ == "__main__":  
    parser = argparse.ArgumentParser()
    parser.add_argument("number_one",help="the first number")
    parser.add_argument("operation",help="add, sub", choices= ["add","sub"])
    parser.add_argument("number_two",help="the second number")


    args = parser.parse_args()

    print(args.number_one)
    print(args.number_two)
    print(args.operation)
    n1= int(args.number_one)
    n2= int(args.number_two)
    result = None
    if args.operation == "add":
        result  = n1 + n2
    elif args.operation == "sub":
        result  = n1 - n2
    print(result)

    

