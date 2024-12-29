N, K = map(int,input().split())

arr = list(range(2,N+1))
cnt = 0


while len(arr) != 0:
    P = arr[0]
    tmp = []
    
    for i in arr:
        if i % P == 0:
            cnt += 1
            tmp.append(i)
            
        if cnt == K :
            print(i)
            exit()
    for num in tmp:  
        arr.remove(num)
    