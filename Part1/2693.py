T = int(input())
num = []

for i in range(T):
    num = list(map(int,input().split()))
    num.sort()
    print(num[-3])