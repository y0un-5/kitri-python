# 파일명: s0126_4.py

scores1 = [81, 93, 80, 88]
scores2 = [79, 80, 68, 72]
scores3 = [58, 42, 50, 63]
scores4 = [91, 87, 90, 95]

scores = [scores1, scores2, scores3, scores4]


for x in range(0,4):
    sum = 0
    for score in scores[x]:
        sum += score
    avg = sum / len(scores[x])
    print(f"평균 점수: {avg:.2f}")
