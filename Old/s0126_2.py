# 파일명: s0126_2.py

marks = [90, 25, 67, 45, 80]

for n in [0, 1, 2, 3, 4]:
    count = n + 1
    if marks[0] >= 60:
        print(f"{count}번 학생, 합격입니다.")
    else:
        print(f"{count}번 학생, 불합격입니다.")

#for mark in marks:
#    count = count + 1
#    if mark >= 60:
#        print(f"{count}번 학생, 합격입니다.")
#    else:
#        print(f"{count}번 학생, 불합격입니다.")
