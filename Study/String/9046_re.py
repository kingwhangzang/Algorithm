N = int(input())
for i in range(N):
    sentence = input()
    sentence = sentence.replace(" ","") # 공백 없애기
    max = ''
    max_count=0
    
    for j in range(ord('a'), ord('z')+1): # a~z까지 숫자 세기
        current_count = sentence.count(chr(j))
        if current_count > max_count:
            max = chr(j)
            max_count = current_count
        elif current_count == max_count:
            max = '?'
        else:
            continue

    print(max)  
    