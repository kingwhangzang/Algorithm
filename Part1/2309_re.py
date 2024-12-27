num = []

for i in range(9):
    a=int(input())
    num.append(a)

num.sort()
sum = sum(num)

for i in range(len(num)):
    for j in range(i+1, len(num)):
        if sum - num[i] - num[j] == 100:
            for k in range(len(num)):
                if k == i or k == j:
                    pass
                else:
                    print(num[k])
            exit()
