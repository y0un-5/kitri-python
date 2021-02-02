# 파일명 : s0202_last.py
# 에러처리



import csv

def average(scores):
    sum = 0
    for score in scores:
        sum += int(score)
    avg = sum / len(scores)
    return avg


for i in range(1,5):
    try:
        filename = f"class_{i}.csv"
        file = open(filename, "r")
    except FileNotFoundError as message:
        print(f"없는 파일 입니다.\n{message}")
    except:
        print("예상외의 에러입니다.")
    else:
        rows = csv.reader(file)
        for row in rows:
            name, scores = row[0], row[1:]
            avg = average(scores)
            print(row + [avg])
        file.close()
    print()