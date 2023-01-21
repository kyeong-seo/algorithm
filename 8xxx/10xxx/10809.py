s = list(input())
a = list('abcdefghijklmnopqrstuvwxyz')
l = []
for i in a:
    if i in s:
      l.append(s.index(i))
    else:
        l.append(-1)
print(*l)