N = int(input())
cnt = 0

while N > 0:
    if N % 5 == 0:
        cnt = N // 5
        N = 0
        break
    N -= 2
    cnt += 1
    
if N < 0:
    print(-1)
else:
    print(cnt)
    