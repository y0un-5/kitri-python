# 파일명 : mod1.py

def add(a, b):
    return a + b
   
def sub(a, b):
    return a - b
    
"""
파일명: mod1.py
def add(a,b)
def sub(a, b)

1. import mod1
    mod1.add()
    mod1.sub()

2. from 모듈명 import 함수명, 변수명
    from mod1 import add
    add()

    from mod1 import add, sub
    add()
    sub()

3. Alias 별칭
    import 모듈명 as 별칭
    from 모듈명 import 함수 as 별칭1, 변수 as 별칭2
    
    예) import mod1 as m
        m.add()
        m.sub()
        
        from mod1 import add as a, sub as s
        a()
        s()

"""