import sys
input = sys.stdin.readline

N = int(input())
numlist = list(map(int,input().split()))
    
for i in range(1,min(numlist)+1):
    cnt = 0
    for num in numlist:
        if num % i == 0:
            cnt += 1
        else:
            break
    if cnt == len(numlist):
        print(i)
        

n = int(input())
li = sorted(list(map(int,input().split())))

if n == 2:
    for i in range(1,li[0]+1):
        if li[0]%i == 0 and li[1]&i == 0:
            print(i)
else:
    for i in range(1,li[0]+1):
        if li[0]%i == 0 and li[1]&i == 0 and li[2]%i==0:
            print(i)