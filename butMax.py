n=int(raw_input())
i=raw_input()
mas=[]
mas=i.split()
maximum=0
for x in range(0,n):
    if maximum<float(mas[x]):
        maximum=float(mas[x])
print round(maximum,1)
