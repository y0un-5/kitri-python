students = [87, 93, 48, 67]

max = students[0]

for x in range(0,4):
    count = x + 1
    if 60 <= students[x]:
        result = "합격"
    else:
        result = "불합격"

    if max < students[x]:
        max = students[x]

    print(f"{count}번 학생, {result}입니다.")
    
print(f"최고점 : {max}")
