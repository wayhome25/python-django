def numPY(s):
    s = s.lower()
    p_list = []
    y_list = []
    if 'p' in s or 'y' in s:
        for v in s:
            if v == 'p':
                p_list.append(v)
            elif v == 'y':
                y_list.append(v)
        return len(p_list) == len(y_list)
    else:
        return False


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( numPY("pPoooyY") )
print( numPY("Pyy") )
