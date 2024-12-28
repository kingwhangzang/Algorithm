N = int(input())

for i in range(N):
    a, b = map(int,input().split())
    
    # 최대공약수수
    num1 = 0
    for i in range(1, min(a,b)+1):
        if a % i ==0 and b % i==0:
            num1 = i
    # 최소공배수
    num2 = (a*b)//num1
    print(num2)