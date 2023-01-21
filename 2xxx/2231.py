num = input()

b = num

a = len(str(b))

n = int(num)

mini = max(1,(n-(9*a)))

for i in range(mini, n+1):
    if n == i:
        print(0)
        break
    k=i
    for j in str(i):
        k+=int(j)
    
    if k == n:
        print(i)
        break