N = int(input())
color = input()

cnt = 0
temp = [color[0]]
cddict = {'B':0, 'R':0}
precolor = ''

for c in color:
    if c != precolor:
        cddict[c] += 1
    precolor = c

if cddict['B']>cddict['R']:
    count = cddict['R']+ 1
else:
    cddict['B']+1
print(count)