n = int(input())

for i in range(n):
    t = 0
    s = 0
    l = list(map(str,input()))
    for j in range(len(l)):
        if l[j]=='O':
            s+=1
            t+=s
        else:
            s=0
    print(t)
    
