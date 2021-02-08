# s0115_test4.py

name = "홍길동"
age = 23
minute = 1
second = 25
taxrate = 20

print("제이름은 '%s'입니다."%name)
print("제 나이는 %d살 입니다."%age)
print("세율은 %d%%입니다."%taxrate)
print("세율은 {0:.2f}%입니다.".format(taxrate))
print(f"세율은 {taxrate:.2f}%입니다.")
print("제 잠수 시간은 %d' %d\"입니다."%(minute, second))
print("제 잠수 시간은 {}' {}\"입니다.".format(minute, second))
print(f"제 잠수 시간은 {minute}' {second}\"입니다.")
print(f"제 이름은 '{name}'입니다.")
