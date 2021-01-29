# 파일명 : s0129_1.py

import csv


def file2list(file):
    lines = file.readlines()
    rows = []
    for line in lines:
        row = line.rstrip().split(",")
        rows.append(row)
    return rows

def average(scores):
    sum = 0
    for score in scores:
        sum += int(score)
    avg = sum / len(scores)
    return avg
"""
file = open("class_1.csv", "r")
rows2 = csv.reader(file)
rows = list(rows2)

total_class = {'유재석':{'sum':0, 'count':0},
               '박명수':{'sum':0, 'count':0}}

for row in rows:
    
    name = row[0]
    scores = row[1:]
    avg = average(scores)
    total_class[name]['sum'] += avg
    total_class[name]['sum'] += 1

    for name in total_class.keys():
        avg = total_class['sum'] / total_class[name]['count']
    print(f"{name}의 평균 : {avg:.1f}")
"""
for n in range(1,4):
        
    print(f"---------{n}----------")

    file = open(f"class_{n}.csv", "r")
    rows = csv.reader(file)

    sum, cnt, max = 0, 0, 0

    for row in rows:
        name, scores = row[0], row[1:]
        avg = average(scores)
        print(f"{name}의 평균: {avg:.1f}")
        sum += avg
        cnt += 1
        if max < avg:
            max = avg

    class_avg = sum / cnt
    
    print(f"{n}반 평균 : {class_avg:.2f}")
    print(f"{n}반 최고 득점 : {max}")
