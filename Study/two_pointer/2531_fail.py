n, d, k, c = map(int,input().split())

plate = []

for i in range(N):
    a = int(input())
    plate.append(a)

sushi = 0
seq = sushi[:k]

# for i in range(n):
#     if i <= n-k:
#         tmp = set(plate[i:i-k])
#     else:
#         tmp = set
