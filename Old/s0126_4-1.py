# 파일명: s0126_4-1.py

students = [['홍길동', 81, 93, 80, 88],
            ['황진이', 79, 80, 68, 72],
            ['멍멍이', 58, 42, 50, 63],
            ['야옹이', 91, 87, 90, 95]]

for student in students:
    sum = 0
    for i in range(1, len(student)):
        sum += student[i]
    avg = sum / len(student)
    print(f"{student[0]}의 평균 점수: {avg:.2f}")
