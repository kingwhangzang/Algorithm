N, K = map(int,input().split())
arr = []
for i in range(1,N+1):
    if N%i == 0:
        arr.append(i)

if len(arr) < K : # len(arr)이 0인거만 생각함..
    print(0)
else:
    print(arr[K-1])