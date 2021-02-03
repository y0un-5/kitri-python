# 파일명 : s0203_1.py

# 주민등록번호를 입력받아 생년월일
# 만나이, 성별을 출력하는 프로그램

import module1 as mod

def output_result(obj):
    print("-" * 30)
    print("결    과")
    print("-" * 30)
    print(f"생년월일 : {obj.birthday()}")
    print(f"만 나이 : {obj.age()}")
    print(f"성   별 : {obj.gender()}")

while True:
    ssn = input("주민등록번호 : ")
    try:
        obj = mod.SSN(ssn)
    except mod.SSNValueError as message:
        print(f"에러 발생\n발생 에러: {message}")    
    except mod.SSNLenError as message:
        print(f"에러 발생\n발생 에러: {message}")
    except mod.SSNTypeError as message:
        print(f"에러 발생\n발생 에러: {message}")
    except:
        print("예상 발생으로 프로그램을 종료합니다.")
    else:
        output_result(obj)
        break
    finally:
        print()