#파일명 : s0121_test3.py
import datetime


c_year = datetime.date.today().year
c_month = datetime.date.today().month
c_day = datetime.date.today().day


birth = input("생일을 입력 :")


b_year = int(birth[0:4])
b_month = int(birth[4:6])
b_day = int(birth[6:8])


if b_month < c_month:
    age = c_year - b_year
elif b_month == c_month:
    if b_day <= c_day:
        age = c_year - b_year
    elif b_day > c_day:
        age = c_year - b_year -1
elif b_month > c_month:
    age = c_year - b_year -1

print(f"만 나이는 {age}세 입니다.")

#print(c_year, c_month, c_day)
#print(b_year, b_month, b_day)
