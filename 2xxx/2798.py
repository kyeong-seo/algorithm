import random

n, b = map(int, input().split())
l = list(map(int, input().split()))
    
s = b
for i in range(len(l)):
    for j in range(len(l)):
        for k in range(len(l)):
            if l[i] != l[j] and l[i] != l[k] and l[j] != l[k]:    
                m_ = l[i]+l[j]+l[k]
                
                if m_ <= b:
                    s_ = b-m_
                    if s_ < s:
                        s = s_
                        m = m_

print(m)