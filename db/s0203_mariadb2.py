# 파일명 : s0203_mariadb2.py

# shopping_db의 purchase table 을 참조하여
# 1월 ~ 6월까지의 월별 총 매출액을 구하여 출력하기

import pymysql

def yearly(rows):
    sales = {}
    for year in range(2017, 2021):
        for month in range(1, 13):
            sales[year] = {}

def monthly(rows):
    sales = {}
    for month in range(1,7):
        sales[month] = 0
        
    for row in rows:
        month, price = row[2].month, row[4]
        sales[month] += price
    
    for month, total_amt in sales.items():
        print(f"{month}월의 총 매출: {total_amt}")

def product(rows):
    sql = "SELECT DISTINCT product FROM purchase"
    count = cursor.execute(sql)
    products = cursor.fetchall()
    
    psales = {}
    
    for product in products:
        psales[product[0]] = {'count':0, 'sum':0}
    
    for row in rows:
        product, price = row[3], row[4]
        psales[product]['count'] +=1
        psales[product]['sum'] += price
    
    for product, count_sum in psales.items():
        count = count_sum['count']
        tot_amt = count_sum['sum']
        print(f"{product} 판매 횟수 : {count}, 누적 금액 : {tot_amt:,}")

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
 
sql = "select * from purchase"
count = cursor.execute(sql)
rows = cursor.fetchall()
monthly(rows)
product(rows)