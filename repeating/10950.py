n = int(input())
for _ in range(n): # 변수 설정이 필요없다면, _ 사용하기
    a,b = map(int,input().split())
    print(a+b)