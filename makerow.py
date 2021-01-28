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






        
for row in rows2:
    uid = row[0]
    name = row[1]
    clas = row[2]
    if clas == 'A':
        scores = row[3:]
        avg = average(scores)
        print(avg)
    else:
        scores = row[3:]
        bavg = average(scores)
        print(avg)
