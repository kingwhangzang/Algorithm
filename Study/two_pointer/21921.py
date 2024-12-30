N, X = map(int,input().split())
num = list(map(int,input().split()))

left, right = 0, len(num)-1

if max(num)==0: # 최대 방문자가 0인 경우
    print("SAD")
else:
    value = sum(num[:X]) # 0번부터 X번까지의 합
    max_value = value
    max_cnt = 1
    
    for i in range(X,N):
        value += num[i]
        value -= num[i-X]
        
        if value > max_value:
            max_value = value
            max_cnt = 1
        elif value == max_value:
            max_cnt += 1
    print(max_value)
    print(max_cnt)