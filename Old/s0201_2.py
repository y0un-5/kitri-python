# 파일명 : s0201_2.py

def udir(object):
    
    attrs = []
    
    for attr in dir(object):
        if attr[0] != "_":
            attrs.append(attr)
    return attrs


udir(a)
udir(b)
