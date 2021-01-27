# 파일명 : s0127_test1.py

prompt = "원하는 코드(a/d/l/q)는? "

code = ""

while code != "q":

    code = input(prompt)
    if code in ["a", "d", "l","q"]:
        print("실행되었습니다.")
    else:
        print("다시 입력하세요.")
        code

print("종료")
