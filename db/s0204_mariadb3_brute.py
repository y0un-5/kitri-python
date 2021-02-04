import pymysql

host = "192.168.0.155"
port = 3306
user = "python"
password = "toortoor"
db = "shopping_db"

connect = pymysql.connect(host = host,
                          port = port,
                          user = user,
                          password = password,
                          db = db)

cursor = connect.cursor()
passlist = []

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
    rows = cursor.fetchall()