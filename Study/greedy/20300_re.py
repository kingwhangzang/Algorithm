N = int(input())
c = list(map(int,input().split()))
c.sort()
m = 0
b = []

if len(c)%2 == 1:
    m = c.pop(-1)

for i in range(len(c)//2):
    k = c[i] + c[-i-1]
    b.append(k)
    
b.append(m)
print(max(b))