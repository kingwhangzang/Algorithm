H, M = input().split()

H = int(H)
M = int(M)

if M < 45 :	# 분단위가 45분보다 작을 때 
    if H == 0 :	# 0 시이면
        H = 23
        M += 60
    else :	# 0시가 아니면 (0시보다 크면)
        H -= 1	
        M += 60
        
print(H, M-45)

# if (M < 45 and H >=1 ):
#     H = H-1
#     M = M+15
# elif (M < 45 and H == 0):
#     H = 23
#     M = M+15
# elif(M >= 45 and H >= 1):
#     H = H-1
#     M = M-45
# elif (M >= 45) :
#     M = M-45

# print(H, M)
