s=list(input().upper())
l=0
for i in s:
    if i =='A' or i =='B' or i =='C':
        l+=(1+2)
    elif i =='D' or i =='E' or i =='F':
        l+=(1+3)
    elif i =='G' or i =='H' or i =='I':
        l+=(1+4)
    elif i =='J' or i =='K' or i =='L':
        l+=(1+5)
    elif i =='M' or i =='N' or i =='O':
        l+=(1+6)
    elif i =='P' or i =='Q' or i =='R' or i=='S':
        l+=(1+7)
    elif i =='T' or i =='U' or i =='V':
        l+=(1+8)
    elif i =='W' or i =='X' or i =='Y' or i=='Z':
        l+=(1+9)
print(l)