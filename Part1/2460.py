n = 0
middle = 0

for i in range(10):
    D, U = map(int,input().split())
    n = n + U - D
    if n > middle:
        middle = n
print(middle)