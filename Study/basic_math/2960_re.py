N, K = map(int,input().split())
arr = list(range(2,N+1))
tmp = 0

while len(arr)!= 0:
    P = arr[0]
    del_list = []
    
    for i in arr:
        if i % P == 0:
            del_list.append(i)
            tmp += 1
            
        if tmp == K:
            print(i)
            exit()
            
    for i in del_list:
        arr.remove(i)