# s0129_class.py

import csv

def average(scores):
    sum = 0
    for score in scores:
        sum += int(score)
    avg = sum / len(scores)
    return avg


def write_csv(filename, rows, columns = []):
    
    wfile = open(filename, "w", newline = "")
    csvfile = csv.writer(wfile)

    if columns:
        csvfile.writerow(columns)
    csvfile.writerows(rows)
    wfile.close()

rows2 = []

for n in range(1, 4):
    rfile = open(f"class_{n}.csv", "r")
    rows = csv.reader(rfile)


    for row in rows:
        name, scores = row[0], row[1:]
        avg = average(scores)
        rows2.append([name]+[n]+scores+[avg])

rfile.close()
columns = ['이름', '반', '국어', '영어', '수학', '과학', '역사', '평균']
write_csv("class_total_avg.csv", rows2, columns)
