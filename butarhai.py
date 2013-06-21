s=int(raw_input())
n=raw_input()
mas=[]
mas=n.split()
for x in range(1,s):
    mas[0]=float(mas[0])+float(mas[x])
print round(mas[0],1)

