n=int(raw_input())
a=n/10
b=n%10
x=a*a*a+b*b*b
if n*n==x:
    print 'YES'
else:
    print "NO"
