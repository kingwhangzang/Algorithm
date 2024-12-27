A = []

for _ in range(5):
    a=input()
    A.append(a)

# for i in range(5):
#     for j in range(5):
#         print(A[j][i], end='')
# 가로에 5개가 들어간다는 보장이 없어서 오류가 나

for i in range(15):
    for j in range(5):
        if i < len(A[j]):
            print(A[j][i], end='')