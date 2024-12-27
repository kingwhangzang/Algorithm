sen = input().upper()
words = list(set(sen))

cnt_list=[]
for x in words:
    cnt=sen.count(x)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    max=cnt_list.index(max(cnt_list))
    print(words[max])