N, M = map(int,input().split())

# 최대공약수
num1 = 0
for i in range(1, min(N,M)+1):
    if N % i ==0 and M % i==0:
        num1 = i
print(num1)

# 최소공배수
num2 = num1*(N/num1)*(M/num1)
print(int(num2))