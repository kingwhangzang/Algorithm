N, C = map(int,input().split())

num = list(map(int,input().split()))
dic = {}

# 숫자 : [등장빈도][입력빈도]
# [숫자][] : 입력빈도

for i in len(num):
    if num[i] in dic:
        dic[i][1] += 1