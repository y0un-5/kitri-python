# 파일명 : s0201_1.py
#
# 명령 프롬프트를 사용하여 매개변수 주기
# import sys 사용


import csv
import sys

def average(scores):
    sum = 0
    for score in scores:
        sum += int(score)
    avg = sum / len(scores)
    return avg

filenames = sys.argv[1:]
# 파일명이 포함된 0번 인덱스 확인 안함
# 파일명 입력

for filename in filenames:
    
    file = open(filename, "r")
    #파일 불러오기
    rows = csv.reader(file)
    #불러온 파일 내용을 rows 변수에 저장
    print(f"\n 파일명: {filename}")

    for row in rows:
        name, scores = row[0], row[1:]
        avg = average(scores)
        print(row + [avg])
