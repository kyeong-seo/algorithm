num = int(input())

i=666
k=0
while True:
    a = str(i)
    
    if '666' in a:
        k+=1     
        if k==num:
            break
    
    i+=1
    
print(a)