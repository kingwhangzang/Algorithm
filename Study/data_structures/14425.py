N, M = map(int,input().split())
S = set()

for _ in range(N):
    S.add(input())

# for _ in range(M):
#     a = input()
#     Z.append(a)
# 굳이 Z에 넣을 필요 없어! S에 있는거면 cnt += 1 하면돼돼
cnt = 0

for i in range(M):
    t = input()
    if t in S:
        cnt += 1
print(cnt)