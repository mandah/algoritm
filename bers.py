x=raw_input()
mas=[]
mas=x.split()
x=int(mas[0])+int(mas[1])
y=int(mas[2])+int(mas[3])
if ((x%2==0 and y%2==0) or(x%2==1 and y%2==1)):
    print 'YES'
else:
    print 'NO'
