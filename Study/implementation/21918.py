N, M = map(int, input().split())
s = list(map(int, input().split()))

for i in range(M):
    a, b, c = map(int, input().split())
    if a == 1:
        s[b - 1] = c  
    elif a == 2:
        for j in range(b - 1, c):  # 인덱스가 b-1
            if s[j] == 0:
                s[j] = 1  
            elif s[j] == 1:
                s[j] = 0 
    elif a == 3:
        for j in range(b - 1, c):
            s[j] = 0  
    elif a == 4:
        for j in range(b - 1, c):
            s[j] = 1 
for i in range(len(s)):
    print(s[i], end=' ')
