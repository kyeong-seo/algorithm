total = int(input())
items = int(input())

total_ = 0
for i in range(items):
    price, item = map(int,input().split())
    total_+=(price*item)
    
if total_ == total:
    print('Yes')
else:
    print('No')