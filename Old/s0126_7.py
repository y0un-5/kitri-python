# 파일명 : s0126_7.py

prompt = """
1. Add
2. Del
3. List
4. Quit
Enter Number: """

choice = int(input(prompt))

while choice != 4:
    print("작업이 잘 수행 되었습니다.")
    choice = int(input(prompt))
print("작업을 종료합니다.")
