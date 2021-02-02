# 파일명: s0202_2.py

print("프로그램을 시작합니다.")

try:
    a = [1, 2]
    print(a[3])
    4 / 0
except IndexError as message:
    print("인덱싱 할 수 없습니다.")
    print(f"에러 메세지: {message}")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except:
    print("예상 외의 에러")
print("프로그램 종료")