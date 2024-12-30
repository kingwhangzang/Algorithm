N, K = map(int,input().split())

c = []
for i in range(N):
    c.append(int(input()))
c.sort(reverse=True)

count = 0

for i in c:
    if K == 0:
        break
    count += K//i
    K %= i

print(count)