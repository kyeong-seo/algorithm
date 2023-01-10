s=(list(input().upper()))
s_=list(set(s))
num = 0
for i in s_:
    num_ = s.count(i)
    if num_>num:
        m = i
        num=num_
    elif num_==num:
        m = '?'
        
print(m)