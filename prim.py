import math
i=raw_input()
m=[]
m=i.split()
r=float(m[0])
n=float(m[1])
print round(n*math.sqrt(2*r*r-2*r*r*math.cos(2*3.14/n)))

