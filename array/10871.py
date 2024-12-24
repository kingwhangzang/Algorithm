N, X = map(int,input().split())
V = list(map(int,input().split()))

for i in range(N) :
    if (X > V[i]):
        print(V[i])