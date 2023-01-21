N, X = map(int,input().split())

list_ = list(map(int,input().split()))

print(*[a for a in list_ if a<X])