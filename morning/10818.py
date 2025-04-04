Num = int(input())
arr = []
arr = list(map(int,input().split()))

# M = -1
# N = 1000001

# for i in range(Num):
#     if arr[i] > M :
#         M = arr[i]
#     if arr[i] < N :
#         N = arr[i]

# print(N, M)

print(min(arr), max(arr))