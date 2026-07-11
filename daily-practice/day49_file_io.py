print("read statement".upper())
# g=open("letter.txt","r")
# print(g)
# k=g.read("i am fine")
# print(k)
# g.close()


# print("write statement".title())
# g=open("letter.txt","w")
# print(g)
# k=g.write("i am fine")
# print(k)
# g.close()


# print("append statement".upper())
# f=open("letter.txt","a")
# print(f)
# l=f.write(" what about u")
# print(l)
# f.close()

# print("x-statement to create file if not exists")
# e=open("jug.txt","x")
# print(e);
print("as u can see it created a file by x statement")
with open("jug.txt","w") as t:
    t.write(" using with satement where no need for close statement ")
    print(t);
