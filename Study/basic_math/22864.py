A, B, C, M = map(int,input().split())
# 피로도 : A, 일의 양 : B, 휴식하면 피로회복 C, 피로한계 M
Work = 0
T = 0

for i in range(24):
    if T > M :
        print(0)
    else :
        if T + A <= M:
            T += A
            Work += B
        else:
            if T - C >= 0:
                T -= C
            else:
                T = 0
print(Work)