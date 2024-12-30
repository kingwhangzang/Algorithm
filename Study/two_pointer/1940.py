# 시간 초과..
# N = int(input())
# M = int(input())

# num = list(map(int,input().split()))
# cnt = 0

# for i in range(N-1):
#     for j in range(i+1,N):
#         result = num[i] + num[i]
#         if result != M:
#             continue
#         cnt += 1
# print(cnt)

N = int(input())
M = int(input())

num = list(map(int,input().split()))
num.sort()

left, right = 0, len(num)-1
cnt = 0

while left < right:
    result = num[left]+num[right]
    if result > M:
        right -= 1
    elif result < M:
        left += 1
    else:
        cnt += 1
        left += 1
        right -= 1
print(cnt)