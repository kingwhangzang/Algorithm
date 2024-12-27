while True:
    sen = input()
    if sen == 'end':
        break
    count = 0
    lst = ['a','e','i','o','u']
    accept = ['ee','oo']
    
    # 모음개수
    for i in lst:
        if i in sen:
            count += 1
    # 모음 0개
    if count == 0 :
        print(f'<{sen}> is not acceptable.')
        continue
    
        
                
                