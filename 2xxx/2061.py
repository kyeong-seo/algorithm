k, l = map(int, input().split())
s=0
for i in range(2, l):
    if k % i == 0:
        s = i
        break
    
if s==0:
    print('GOOD')
else:
    print('BAD {}'.format(s))