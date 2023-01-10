n = int(input())
d = 0
for i in range(1,n+1):
    l = list(str(i))
    if i<100:
        d+=1   
    else:
        if (int(l[1])-int(l[0])) == (int(l[2])-int(l[1])):
            d+=1
print(d)