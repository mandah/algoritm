n=int(raw_input())
i=raw_input()
mas=[]
count=0
mas=i.split()
for x in range(0,n):
    if int(mas[x])%7==1: 
        count+=1   
    elif int(mas[x])%7==2: 
        count+=1
    elif int(mas[x])%7==5:
        count+=1
print count
