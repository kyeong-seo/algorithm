hour, minute = map(int,input().split())
oven_time = int(input())

minute += oven_time

if minute>=60:
    hour_ = minute//60
    hour+=hour_
    minute-=(60*hour_)
    
if hour > 23:
    hour-=24
    print('{} {}'.format(hour,minute))
else:
    print('{} {}'.format(hour,minute))