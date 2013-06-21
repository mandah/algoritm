n=int(raw_input())
a=n
c=1
while (a>9):
    a=a/10
    c=c*10
b=n%10
n=n/10
n=n*10
n=n+a
n=n%c
n=b*c+n
print n
