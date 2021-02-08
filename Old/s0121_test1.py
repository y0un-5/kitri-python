# 파일명 : s0121_test1.py

pocket = input("소지물품: ").split()
if "현금" in pocket:
    money = int(input("소지현금: "))
card = input("카드 소지 [y/n]:").lower() in ['yes', 'no']


if money >= 3000 :
    print("택시타")
elif card :
    print("택시타")
else :
    print("걸어가")
