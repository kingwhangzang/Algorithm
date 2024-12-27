N, M = map(int,input().split())

min = 0
max = 0

for i in range(1, N+1):
    if N%i == 0:
        if M%i == 0:
            min = i
max = min*(N/min)*(M/min)
print(min, int(max))