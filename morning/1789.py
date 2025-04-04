S = int(input())
sum = 0
i = 0

while True:
    i += 1
    sum = sum + i
    if sum > S:
        print(i-1)
        break
        