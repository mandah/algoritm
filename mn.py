n=int(raw_input())
c=1
a=n
while(n>9):
    n=n/10
    c=c*10
b=a%10
a=a/10
a=a*10+n
a=a%c
b=b*c
a=a+b
print a
