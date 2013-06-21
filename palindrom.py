n=int(raw_input())
mas=[]
i=0
check=0
while(n>9):
    s=n%10
    n=n/10
    mas.insert(i,s)
    i+=1
mas.insert(i,n%10)
mUrt=len(mas)
for x in range(0,mUrt/2):
    if mas[x]!=mas[mUrt-1-x]:
        print "NO"
        check=0
        break
    else:
        check=1 
if check==1:
    print "YES"
