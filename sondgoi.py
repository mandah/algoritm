x=int(raw_input())
n=raw_input()
mas=[]
mas=n.split()
count=0
for m in range(0,x):
    if int(mas[m])%2!=0:
        count+=1
print count

