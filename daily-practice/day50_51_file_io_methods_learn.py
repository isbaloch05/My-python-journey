print("saak and tell method")
with (open("methods.txt","r")) as mth:
    mth.seek(6)
    

    # th=mth.read(4)
    print(mth.tell())
# print(th)
    # wr=mth.write("hello isamil!")
# print(wr)
print("trincate method")
with (open("method.txt","w")) as m:
    m.write("baloch panjgoor")
    m.truncate(11)
