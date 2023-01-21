n = int(input())

for i in range(n):
    
    l = list(map(int,input().split()))[1:]
    a = [k for k in l if k>(sum(l)/len(l))]  
    print('{:.3f}%'.format(len(a)/len(l)*100))