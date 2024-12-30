N, M = map(int,input().split())

Nlist = list(map(int,input().split()))
Mlist = list(map(int,input().split()))

arr = Nlist+Mlist
arr.sort()

print(*arr)
