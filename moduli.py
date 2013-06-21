import math
n=raw_input()
mas=[]
mas=n.split()
a,b=float(mas[0]),float(mas[1])
x=(a+b)/2
y=math.sqrt(math.fabs(a)*math.fabs(b))
print float(x)
print int(y) 
