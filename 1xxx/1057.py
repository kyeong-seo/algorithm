n, l, k = map(int,input().split())

x = max(l,k)
n = min(l,k)
count = 0
while True:
    count+=1
    
    if n%2==1 and (x-n) == 1:
        print(count)
        break
    
    else: 
        if n%2==1:
            n/=2
            n+=0.5
        else:
            n/=2
        if x%2==1:
            x/=2
            x+=0.5
        else:
            x/=2