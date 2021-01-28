# 파일명: s0128_test1.py

scores = []

def input_scores1():

        n = int(input("입력할 과목 수?   "))
        
        scores = []

        for i in range(n):
            scores.append(int(input()))
        
        return scores


def input_scores2():

        scores = []

        while True:
            score = input()
            
            if score == "":
                break
            else:
                scores.append(int(score))
        
        return scores

def average(scores):

        sum = 0
        for score in scores:
            sum += score
        avg = sum / len(scores)
        return avg

def output_result(avg):

        if avg >= 60:
            result = "합격"
        else:
            result = "불합격"

        print(f"평균 점수 : {avg}")
        print(f"결과      : {result}")

scores = input_scores2()
avg = average(scores)
output_result(avg)
