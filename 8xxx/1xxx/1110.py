num = int(input())

i = 0
num_ = num

while True:
    
    i+=1
    
    A = num//10
    B = num%10
    C = (A+B)%10
    num = B*10 + C

    if num_==num:
        break

print(i)