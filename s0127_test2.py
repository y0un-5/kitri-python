# 파일명:s0127_test2.py

def say_myself(name, age, man = True):
        print(f"나의 이름은 {name}입니다.")
        print(f"나이는 {age}살 입니다.")
        if man == True:
            print("남자 입니다.")
        else:
            print("여자 입니다.")


def connect_db(host = "127.0.0.1", port = 3306,
                user = "root", password = ""):
    
    cmd = f"mysql -h {host} -P {port} -u {user} -p {password}"
    print(cmd)


connect_db(user = "winadmin", password = "123456")
