n = int(input())
f = int(input())

n_ = n%100
n__ = n - n_

for i in range(100):
    c = n__ + i
    
    if c%f==0:
        print('%02d'%i)
        break