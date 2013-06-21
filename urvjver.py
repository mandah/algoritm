m=int(raw_input())
n=raw_input()
mas=[]
b=1
mas=n.split()
for x in range(0,m):
     b=b*float(mas[x])
print round(b,1)
