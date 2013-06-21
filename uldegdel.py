n=raw_input()
mas=[]
mas=n.split()
u=int(mas[0])%int(mas[1])
if u==int(mas[2]):
    print 'R'
elif u==int(mas[3]):
    print 'S'
else:
    print 'No solution'
