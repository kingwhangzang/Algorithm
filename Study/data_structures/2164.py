# 시간초과 난 코드... deque를 이용하래!!!!
# N = int(input())
# stack = [i for i in range(1, N + 1)]


# while len(stack)>1:
#         stack = stack[1:]
#         k = stack[0]
#         stack[0] = stack[-1]
#         stack[-1] = k
        
# print(stack[0])

from collections import deque
N = int(input())
que = deque(i for i in range(1,N+1))

while len(que)>1:
    que.popleft()
    que.append(que.popleft())
print(que[0])