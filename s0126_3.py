# 파일명 : s0126_3.py

a = int(input("1번부터 몇 까지 더할까요? "))

sum = 0

for x in range(1, a+1):
       sum = sum + x

print(f"합계는 {sum}입니다.")
