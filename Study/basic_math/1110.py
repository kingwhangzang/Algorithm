N = int(input())
num = N
cnt = 0

while True:
    a = num // 10 # 십의 자리
    b = num % 10 # 일의 자리
    c = (a+b)%10 # 새로운 숫자의 일의자리
    num = (b*10)+c
    
    cnt += 1
    if (num == N):
        break
print(cnt)