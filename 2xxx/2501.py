num, count = map(int, input().split())
c = []
for i in range(1,num+1):
    if num%i==0:
        c.append(i)
c.sort()

if len(c) >= count:
    print(c[count-1])    
else:
    print(0)