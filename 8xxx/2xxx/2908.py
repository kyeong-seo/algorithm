s,d = input().split()

s_ = (list(s))
s_.reverse()
s_=int(''.join(s_))
d_ = (list(d))
d_.reverse()
d_=int(''.join(d_))
if s_ > d_:
    print(s_)
else:
    print(d_)
