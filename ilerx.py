import math
n=raw_input()
mas=[]
mas=n.split()
a,b=float(mas[0]),float(mas[1])
x=math.fabs(a)-math.fabs(b)
y=1+math.fabs(a*b)
print round(x/y,1)
