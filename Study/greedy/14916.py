N = int(input())
count = 0

while N > 0:
    if N % 5 == 0:
        count += N // 5
        N = 0
        break
    N -= 2
    count += 1

if N < 0:
    print(-1)
else :
    print(count)