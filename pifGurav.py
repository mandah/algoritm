n=int(raw_input())
a=b=c=1
for a in range(1,n):
    if a*a+b*b==c*c:
        print a,b,c
    for b in range(1,n):
        if a*a+b*b==c*c:
            print a,b,c
        for c in range(1,n):
            if a*a+b*b==c*c:
                print a,b,c
