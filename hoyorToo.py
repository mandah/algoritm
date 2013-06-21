n=raw_input()
mas=[]
mas=n.split()
if mas[0]<mas[1]:
    mas[0]=mas[1]
elif mas[0]>mas[1]:
    mas[1]=mas[0]
elif mas[0]==mas[1]:
    mas[1]=0
    mas[0]=0
print mas[0], mas[1]
