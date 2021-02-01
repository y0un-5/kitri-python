# 파일명 :  s0127_birth2.py

"""
birthday(ssn)   -> 년월일 출력
gender(ssn) -> 남/여 출력
"""

def birthday(ssn):
    if not isinstance(ssn, str):
        return None
    elif len(ssn) != 14:
        return None
    elif not (ssn[0:6].isdigit() and ssn[6] == '-' and ssn[7:14].isdigit()):
        return None
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
    return (year, month, day)

    #print(f"생년월일: {year}년{month}월 {day}일")


"""
## 주민등록번호 : 800512-1133555
##for s in data1:
##    if s not in ['0', '1', '2', '3', '4', ... '9']
##        result = False
##
## 위 내용은 아래 함수와 같다.
##
## data1.isdigit()

## 데 이 터 형 : 문자형(str)
## type(ssn1) == type('')
## isinstance(ssn1, str)

## 길      이 : 14자리 
## len(ssn1) != 14

## 위 조건이 만족되지 않으면 입력받지 않도록 설정 
"""

"""
def gender(ssn):
    
    uid = int(ssn[7])
    male, female = (1, 3, 5, 7, 9), (2, 4, 6, 8)
    
    if uid in male :
        gender = "남자"
    elif uid in female :
        gender = "여자"

    print(f"성별: {gender}")
"""


ssn  = input('주민등록번호 : ')
print(birthday(ssn))
#gender(ssn)
#파일 자체 출력시