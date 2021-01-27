# 파일명: s0127_coffee.py

# 커피자판기는 잔량이 남은 동안 동작
# 판매하고 잔량이 0이되면,
# 판매를 종료한다.

coffee = 5
price = 300


while coffee > 0 :
    
    money = int(input(f"돈을 넣어주세요[잔량:{coffee}]: "))
    
    if money == price:
        print("커피를 줍니다.")
    
    elif money > price:
        print(f"커피를 드립니다. {money-price}원을 거슬러드립니다.")
    
    else:
        print(f"{price-money}원이 모자랍니다.")
        continue
    
    coffee -= 1
    print()

print("커피가 모두 판매되었습니다.")
