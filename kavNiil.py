n=int(raw_input())
#s=raw_input()
mas=[]
#mas=s.split()
for x in range(0,n):
     s=float(raw_input())
     mas.insert(x,s)
t=0
for i in range(0,n):
    z=float(mas[i])
    t+=z*z
print round(t,1)    
