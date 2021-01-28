# 파일명 : s0128_1.py


file = open("새파일.txt", "w")

for i in range(1,10):
    file.write(f"{i}번째 줄입니다. 안녕하세요.\n")
file.close()
