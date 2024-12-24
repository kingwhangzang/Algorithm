n=[]

for i in range(10):
    s = int(input())
    if s%42 not in n:
        n.append(s%42)

print(len(n))
    