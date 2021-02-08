# 파일명 : s0125_password.py 

# 4자리 숫자를 입력받아 사용 가능한 암호인지 검증
# 사용할 수 없는 조건
# 조건 1 : 4가지 숫자가 연달아 증가되는 암호
#           ex) 1234, 5678, 3456
# 조건 2 : 4가지 숫자가 연달아 감소하는 암호
#           ex) 4321, 8765, 6543
# 조건 3 : 1가지 이상 중복되는 숫자가 포함된 암호
#           ex) 0230, 7949

password = input("사용할 암호 : ")

p1 = int(password[0])
p2 = int(password[1])
p3 = int(password[2])
p4 = int(password[3])

increment = p1 + 1 == p2 and p2 + 1 == p3 and p3 + 1 == p4
decrement = p1 - 1 == p2 and p2 - 1 == p3 and p3 - 1 == p4
duplicate = p1 in (p2, p3, p4) or p2 in (p3, p4) or p3 == p4

bad_passwd = increment or decrement or duplicate

if bad_passwd:
    print("사용할 수 없는 암호입니다.")
else:
    print("사용할 수 있는 암호입니다.")
