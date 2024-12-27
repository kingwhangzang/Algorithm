n, m = map(int, input().split())

arr1 = set()
arr2 = set()
for i in range(n):
    arr1.add(input())
for i in range(m):
    arr2.add(input())

answer = list(set(arr1)&set(arr2)) # &는 중복값 의미
answer.sort()
print(len(answer))
for i in answer:
    print(i)
    
