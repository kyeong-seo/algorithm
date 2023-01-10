i=1
l =[]
while i<10000+1:
    l.append(i+sum(map(int,list(str(i)))))
    if i not in l:
        print(i)
    i+=1