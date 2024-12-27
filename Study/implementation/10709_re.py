H, W = map(int,input().split())
arr = []
for _ in range(H):
    arr.append(input())

for a in arr:
    lst = [-1]*W
    for i in range(W):
        if a[i] == 'c':
            lst[i] = 0
    count = 0
    
    for j in range(1, W):
        if lst[j] == 0:
            count = 0
        if lst[j-1] != -1:
            if lst[j] != 0:
                count += 1
                lst[j] = count
    print(*lst)