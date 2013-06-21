n=raw_input()
mas=[]
mas=n.split()
x,y,z= float(mas[0]),float(mas[1]),float(mas[2]) 
if x<y:
    if y<z:
         print z
    else:
         print y
elif y<x:
    if x<z:
         print z
    else:
         print x
else:
    print z
