# := is used for warlus operator 
# it assigns the valus to variables as part of larger expression 
# it helps readability and makes the code simple and avoid massiveness in code 
#let how

#for example 
# print(para = True) would throw an error — = isn't allowed inside a function call
# := works here because it's an expression, not a statement
#with warlus operator
print(para:=True)  #like this 


# sports=list()
# while  True:
#     output=input("which sport do u watch?")
#     if output == "Quit":
#         break
#     sports.append(output)

sports=list()
while  ( output :=  input( "which sport do u watch???").lower() ) !="quit":
    sports.append(output)


      
