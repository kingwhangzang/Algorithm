N, K =map(int,input().split())

num = list(map(int,input().split()))

value = sum(num[:K])
max_value = value

for i in range(K, N):
    value += num[i]
    value -= num[i-K]
    
    if value > max_value:
        max_value = value
print(max_value)