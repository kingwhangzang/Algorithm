M = int(input())
N = int(input())

sosu = []

for i in range(M, N+1):
    count = 0
    if i > 1:
        for j in range(2, i): # 여기 범위 조심하기.. 자꾸 i가 아니라 M을 써..
            if i % j == 0:
                count += 1
                break
        if count == 0:
            sosu.append(i)

if len(sosu) > 0:
    print(sum(sosu))
    print(min(sosu))
else:
    print(-1)