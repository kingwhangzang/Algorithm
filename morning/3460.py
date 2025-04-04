T = int(input())

for _ in range(T):
    n = bin(int(input()))[2:] # 앞에 0b가 붙기 때문에

    n_reverse=n[::-1]

    for i in range(len(n)):
        if n_reverse[i] == '1' :
            print(i)

