import random
n=randam.randint(1,100)
nombretantative=5
while nombretantative>0:
    nombretantative -=1
var=int(input("entrer un nombre:"))
if var < n:
    print("tres petit!")
elif var>n:
    print("plus brang!")
else:
    print("tu as gagner")
