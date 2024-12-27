from collections import deque

N = int(input())
que = deque(i for i in range(1,N+1))

while len(que) > 1:
    que.popleft() # 맨 앞에 있는 원소 삭제
    que.rotate(-1) 
    # 원소들을 왼쪽으로 한칸 미뤄 > 맨앞에 있는 것이 제일 뒤로 이동

print(que[0])