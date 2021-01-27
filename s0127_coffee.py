# 파일명: s0127_coffee.py

# 커피자판기는 잔량이 남은 동안 동작
# 판매하고 잔량이 0이되면,
# 판매를 종료한다.

coffee = 10

while True:
    money = int(input("돈을 넣어주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee -= 1
    elif money > 300:
        print(f"커피를 드립니다. {money-300}원을 거슬러드립니다.")
        coffee -= 1
    else:
        print(f"{300-money}원이 모자랍니다.")

    if coffee == 0:
        print("커피가 모두 판매되었습니다.")
        break
