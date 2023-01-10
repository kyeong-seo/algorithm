r = int(input())
for i in range(r):
    n_s = (input().split())
    n = int(n_s[0])
    s = list(n_s[1])
    l=''
    for j in range(len(s)):
        l+=(s[j]*n)
    print(l)
            