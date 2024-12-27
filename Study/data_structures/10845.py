import sys
N = int(input())
que = []

for i in range(N):
    command = sys.stdin.readline().split()
    
    if command[0] == 'push':
        que.append(command[1])
    elif command[0] == 'pop':
        if len(que) == 0:
            print(-1)
        else:
            print(que.pop(0))
            # pop은 그 값을 출력하고 삭제
            # pop(0)은 인덱스 값 위치에 있는 값을 출력하고 삭제
    elif command[0] == 'size':
        print(len(que))
        
    elif command[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)            
    elif command[0] == 'front':
        if len(que) == 0 :
            print(-1)
        else:
            print(que[0])
    elif command[0] == 'back':
        if len(que) == 0 :
            print(-1)
        else:
            print(que[-1])