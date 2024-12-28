N = int(input())

# 시간 초과
# if N == 1:
#     print(" ")

# for i in range(2,N+1):
#     if N % i == 0:
#         while  N % i == 0 :
#             print(i)
#             N = N / i
            
i = 2
while N > 1:
    if N % i == 0:
        N = N // i
        print(i)
    else:
        i += 1