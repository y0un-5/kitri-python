# 파일명 : s0203_mariadb.py

# mariadb 연동 연습
# db 서버 정보
# ip주소 : 192.168.0.155
# port : 3306
# 계정명 : python
# 암호 : --------
# db명 : shopping_db

class pymysqlError(Exception):
    def __str__(self):
        return "오류 1"

class pymysqlError2(Exception):
    def __str__(self):
        return "오류 2"

import pymysql

host = "192.168.0.155"
port = 3306
user = "python"
password = "--------"
db = "shopping_db"

#db 서버와 연결
import pymysql
connect = pymysql.connect(host = host,
                          port = port,
                          user = user,
                          password = password,
                          db = db)
 
 #db 연결 객체 커서 불러오기
cursor = connect.cursor()
 
while True:

    sql = input("MariaDB [shopping_db] > ").strip()

    if sql == '':
        continue
    elif sql.lower() in ('quit', 'exit'):
        break
   
    try:
        count = cursor.execute(sql)
        if count == 0:
            print("조회 결과 없음")
            continue
    except pymysql.err.OperationalError as message:
        print(f"에러 발생 : {message}")
    except pymysql.err.ProgrammingError as message:
        print(f"에러 발생 : 잘못된 SQL문 입니다.\n{message}")
    else:
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    finally:
        print()