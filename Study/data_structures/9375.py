T = int(input())

for i in range(T):
    cloth = {}
    N = int(input())
    for _ in range(N):
        name, type = input().split()
        if type in cloth:
            cloth[type].append(name)
        else:
            cloth[type] = [name]

    cnt = 1

    # 조합식 세우기
    for x in cloth:
        cnt *= (len(cloth[x]) + 1)
    print(cnt-1)