# 파일명: module_test.py

import module1

a = module1.FourCal(4, 2)
print(f"first = {a.first}")
print(f"second = {a.second}")
print(f"add = {a.add()}")
print(f"sub = {a.sub()}")
print(f"mul = {a.mul()}")
print(f"div = {a.div()}")
print(module1.udir(a))
