n = int(input())

for i in range(1,n+1):
    a, b = map(int,input().split())
    print("Case #"+str(i)+":",(a+b))
    # 초기 : print("Case #"+str(i)+":"+(a+b))
    # str과 숫자를 섞어 쓸때는 , 사용 / str끼리 쓸때는 +