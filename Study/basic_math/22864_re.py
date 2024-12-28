A, B, C, M = map(int,input().split())
Work = 0
T = 0

for i in range(24):
    if T > M:
        print(0)
        # 번아웃 온 경우
    else:
        if T+A <= M: # 일을 한 경우 피로 증가, 일 처리
            T += A
            Work += B
        else:
            if T - C >= 0 :
                T -= C
            else:
                T = 0
print(Work)