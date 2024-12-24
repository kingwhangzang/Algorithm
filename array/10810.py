N, M = map(int,input().split())
box = [0]*(n)

for i in range(M) :
    i,j,k = map(int,input().split())
    for z in range(i,j+1):
        box[z] = k
for i in range(1, N+1):
    print(box[i], end = '')