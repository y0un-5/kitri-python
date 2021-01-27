# 파일명 :  s0127_birth2.py

"""
birthday(ssn)   -> 년월일 출력
gender(ssn) -> 남/여 출력
"""

def birthday(ssn):

    uid = int(ssn[7])
    c18xx, c19xx, c20xx = (9, 0), (1, 2, 5, 6), (3, 4, 7, 8)

    if uid in c19xx:
        c = 1900
    if uid in c20xx:
        c = 2000
    if uid in c18xx:
        c = 1800

    year = c + int(ssn[0:2])
    month = int(ssn[2:4])
    day = int(ssn[4:6])

    print(f"생년월일: {year}년{month}월 {day}일")

def gender(ssn):
    
    uid = int(ssn[7])
    male, female = (1, 3, 5, 7, 9), (2, 4, 6, 8)
    
    if uid in male :
        gender = "남자"
    elif uid in female :
        gender = "여자"

    print(f"성별: {gender}")


ssn  = input('주민등록번호 : ')

birthday(ssn)
gender(ssn)
