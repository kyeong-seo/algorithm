
n = int(input())

order = []

for i in range(n):
    kg, cm = map(int, input().split())
    dd = kg,cm
    order.append(dd)

rank = []
for i in range(len(order)):
    kg_, cm_ = order[i]
    c = 1
    for j in range(len(order)):
        kg__, cm__ = order[j]
        
        if kg_ < kg__ and cm_ < cm__:
            c+=1
    rank.append(c)

print(*rank)