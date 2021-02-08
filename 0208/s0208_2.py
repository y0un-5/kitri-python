# 파일명 : s0208_2.py
# 1.py와 같은 내용을 출력하도록 정규 표현식으로 작성한다.

import re
# 정규 표현식 모듈

file = open("members.txt", "r")
read = file.read()
print(read)
print("-" * 20)

pattern = re.compile("(\d{6})[-]\d{7}")
# 패턴 지정 = 숫자 6개 - 숫자 7개
print(pattern.sub("\g<1>-*******", read))