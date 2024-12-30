N = int(input())
M = int(input())

num = list(map(int,input().split()))
num.sort()

left, right = 0,len(num)-1
cnt = 0

while left < right:
    sum = num[left]+num[right]
    if sum < M : 
        left += 1
    elif sum > M:
        right -= 1
    else:
        cnt += 1
        left += 1
        right -= 1
print(cnt)