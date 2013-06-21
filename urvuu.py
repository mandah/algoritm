n=int(raw_input())
a=0
while(n>9):
    a+=n%10
    a=a*10
    n=n/10
n=n%10
a=a+n
print a 
