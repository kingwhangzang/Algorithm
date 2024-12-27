T = int(input())
for _ in range(T):
    cloth = {}
    N = int(input())
    for i in range(N):
        name, type = input().split()
        if type in cloth:
            cloth[type].append(name)
        else:
            cloth[type]=[name]
    
    cnt = 1
    for x in cloth:
        cnt *= (len(cloth[x])+1)
    print(cnt-1)