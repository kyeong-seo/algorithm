A, B, C = map(int,input().split())

if A==B and B==C:
    money = A*1000 + 10000
elif A==B and A!=C:
    money = A*100 + 1000
elif B==C and A!=C:
    money = B*100 + 1000
elif A==C and A!=B:
    money = A*100 + 1000
else:
    money = (max(A,B,C))*100
print(money)    
