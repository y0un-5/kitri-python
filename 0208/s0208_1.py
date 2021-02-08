# 파일명 : s0208_1.py
# members.txt 내부의 내용 중 주민등록번호(rrn)을 찾아
# 뒷자리를 * 로 치환한다.


file = open("members.txt", "r")
read = file.read()
print(read)
print("-" * 20)

rows = read.split("\n")
for row in rows:
# 행 단위 반복
    datas = row.split()
    for data in datas:
    # 열 단위 반복
        if (len(data) == 14 
            and data[0:6].isdigit() 
            and data[6] == '-' 
            and data[7:14].isdigit()):
            print(data[0:7] + "*******", end=" ")
        else:
           print(data, end = " ")
    print(end = "\n")