A = []

n = -1
R = 0
C = 0

for row in range(9):
    A.append(list(map(int,input().split())))

for row in range(9):
    for col in range(9):
        if A[row][col] >= n:
            n = A[row][col]
            R = row+1 # +1 꼭 해주기
            C = col+1

print(n)
print(R, C)