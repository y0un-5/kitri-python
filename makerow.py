# makerow.py

import csv

def file2list(file):
        lines = file.readlines()
        rows = []
        for line in lines:
            row = line.rstrip().split(",")
            rows.append(row)
        return rows

"""
file = open("students.csv", "r")
rows1 = file2list(file)
print(rows1)
"""

def average(scores):
    sum = 0
    for score in scores:
        sum += int(score)
    avg = sum / len(scores)
    return avg

file = open("students.csv", "r")
rows2 = csv.reader(file)
rows = list(rows2)

for c in ['A', 'B']:
    total_sum = 0
    total_count = 0

    for row in rows:
        uid, name, clas = row[0:3]
        scores = row[3:]
        avg = average(scores)

        if clas == c:
            total_sum += avg
            total_count += 1
    total_avg = total_sum / total_count
    print(f"{c}반 평균 : {total_avg:.1f}")

"""
total_clas = {'A':{'sum':0, 'count':0},
              'B':{'sum':0, 'count':0}}

for row in rows2:
    uid, name, clas = row[0:3]
    scores = row[3:]
    avg = average(scores)
    total_class[clas]['sum'] += avg
    total_class[clas]['sum'] += 1

for clas in total_class.keys():
        avg = total_class['sum'] / total_class[clas]['count']
        print(f"{clas}의 평균 : {avg:.1f}")
"""
