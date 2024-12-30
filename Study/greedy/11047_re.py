N, K = map(int,input().split())
c = []

# 돈 종류 넣기기
for i in range(N):
    c.append(int(input()))
    
c.sort(reverse=True)

count = 0

# 돈 갯수 세기
for i in c:
    if K == 0:
        break

    count += K//i
    K %= i

print(count)