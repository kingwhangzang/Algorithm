total = int(input())
k = int(input())
middle = 0

for i in range(k) :
    a, b = map(int,input().split())
    middle = middle + (a*b)
    
if (total == middle) : 
    print("Yes")
else :
    print("No")
