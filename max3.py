n=raw_input()
mas=[]
mas=n.split()
x,y,z=float(mas[0]),float(mas[1]),float(mas[2])
a=x+y+z
b=x*y*z
if a>b:
    print a
else:
    print b
