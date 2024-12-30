N, X = map(int,input().split())
num = list(map(int,input().split()))

if max(num)==0:
    print("SAD")
else:
    value = sum(num[:X])
    max_value = value
    cnt = 1
    
    for i in range(X,N):
        value += num[i]
        value -= num[i-X]
        
        if value > max_value:
            max_value = value
            cnt = 1
        elif value == max_value:
            cnt += 1
    print(max_value)
    print(cnt)