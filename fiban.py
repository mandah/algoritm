n=int(raw_input())
a=0
b=1
mas=[]
for x in range(0,n,2):
    b=b+a
    a=a+b
    mas.insert(x,b)
    mas.insert(x+1,a)
print 0
for x in range(0,n):
    print mas[x]
