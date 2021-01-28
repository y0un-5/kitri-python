# 파일명 : s0128_password3.py 


def bad_passwd(password):
    
        
    p1 = int(password[0])
    p2 = int(password[1])
    p3 = int(password[2])
    p4 = int(password[3])
    
    increment = p1 + 1 == p2 and p2 + 1 == p3 and p3 + 1 == p4
    decrement = p1 - 1 == p2 and p2 - 1 == p3 and p3 - 1 == p4
    duplicate = p1 in (p2, p3, p4) or p2 in (p3, p4) or p3 == p4
    
    bad_passwd = increment or decrement or duplicate

    return bad_passwd

a = 1

while a:

    password = input("사용할 암호 : ")
    
    a = bad_passwd(password)
   
    if a:
        print("사용못함")

print("사용 가능 종료")
