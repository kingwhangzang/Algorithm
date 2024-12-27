A, B = input().split()

A = int(A)
B = int(B)

print(A+B)
print(A-B)
print(A*B)
print(int(A/B))
# A/B가 나누어 떨어지지 않는경우, float로 반환 
# > int형으로 변경해줘야 함
print(A%B)