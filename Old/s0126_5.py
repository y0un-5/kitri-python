# 파일명 : s0126_5.py

a = 2
b = 1

for a in range(2,10):
    print(f"-------{a}단-----------")
    for b in range(1,10):
        print(f"{a} * {b} = {a * b}")
    print("--------절취선-----------")
    print("\n")
