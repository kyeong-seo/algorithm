hour, minute = map(int,input().split())

if minute<45:
    minute = minute+60-45
    if hour>0:
        hour-=1
    else:
        hour=23
else:
    minute-=45
    
print('{} {}'.format(hour,minute))
