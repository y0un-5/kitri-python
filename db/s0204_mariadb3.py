import pymysql
import getpass

host = "192.168.0.155"
port = 3306
user = "python"
password = "--------"
db = "shopping_db"

connect = pymysql.connect(host = host,
                          port = port,
                          user = user,
                          password = password,
                          db = db)

cursor = connect.cursor()

## 날짜 입력받아 정제하기
def refine_date(date):
    date = date.strip()
    if len(date) == 8 and date.isdigit():
        date = int(date)
    else:
        for a in (".", ",", "/", "-"):
            date = date.replace(a, "")
        date = int(date)
    return date

## 날짜 입력값 검사하기
def input_date(point):
    prompt = f"{point}날짜[YYYY-mm-dd]: "
    while True:
        date = input(prompt).strip()
        year = date[0:4].isdigit()
        month = date[5:7].isdigit()
        day = date[8:10].isdigit()
        
        con_date1 = year and month and day
        con_date2 = date[4] == "-" and date[7] == "-"
        con_date3 = len(date) == 10
        
        if con_date1 and con_date2 and con_date3:
            break
    return date


## 로그인
while True:
    userr = input("USER : ")
    #passwd = input("PASSWORD : ")
    passwd = getpass.getpass("PASSWORD : ")
    sql = f'SELECT * FROM customer WHERE id="{userr}" AND password= "{passwd}"'
    count = cursor.execute(sql)
    if count == 1:
        print("로그인에 성공하였습니다.")
        break
    else:
        print("비밀번호가 틀렸습니다.")

## 로그인 후 DB 조회
while True:
    start_date = input("시작 날짜[YYYY-mm-dd] : ")
    start_date = input_date(start_date)
    start_date = refine_date(start_date)
    end_date =  input("종료 날짜[YYYY-mm-dd] : ")
    end_date = input_date(start_date)
    end_date = refine_date(end_date)
    
    sql = f'SELECT * FROM purchase WHERE cust_id="{userr}" AND date >= {start_date} AND date <= {end_date};'
    ## SQL 인젝션 취약점 발생 위치
    count = cursor.execute(sql)
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)
        
    if count > 1:
        break