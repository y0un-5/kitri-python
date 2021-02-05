# 파일명 : lotto.py

import random
import time


lottos = []
mylottos = []
for m in range(0, 6):
    a = input("lotto : ")
    mylottos.append(a)
print(mylottos)

    
    
"""   
for i in range(0, 6):
    num = random.randint(1, 45)
    if i > 0:
        while num in lottos:
            num = random.randint(1, 45)
    lottos.append(str(num))
    print(lottos[i])
    time.sleep(1)
count = 0

lottos.sort()

print(f"당첨 Lotto: {lottos}")
"""