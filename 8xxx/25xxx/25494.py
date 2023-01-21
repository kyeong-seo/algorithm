n = int(input())

a = []
b = []
c = [] 
count = []

for p in range(n):
    a,b,c = map(int, input().split())
    count_ = 0
    for i in range(1,a+1):
        for j in range(1,b+1):
            for k in range(1,c+1):
                if i%j == j%k and j%k == k%i and i%j == k%i:
                    count_+= 1
    count.append(count_)

for i in range(len(count)):
    print(count[i])