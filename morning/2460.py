people = 0
num = 0

for i in range(10):
    D, U = map(int,input().split())
    people = people + U - D
    
    if people > num :
        num = people
print(num)