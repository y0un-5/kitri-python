# 파일명 :  s0127_birth2.py

"""
birthday(ssn)   -> 년월일 출력
gender(ssn) -> 남/여 출력
"""
"""
class SSN:
   def __init__(self,ssn):
      if not isinstance(ssn,str):
         raise ValueError
      elif len(ssn) != 14:
         raise ValueError
      #elif not ssn[0:6].isdigit() or ssn[6] != '-' or not ssn[7:14].isdigit():
      elif not (ssn[0:6].isdigit()
          and ssn[6] == '-'
           and ssn[7:14].isdigit()):
         raise ValueError
      self.ssn = ssn


def birthday(self):

    uid = int(self.ssn[7])
    c18xx, c19xx, c20xx = (9, 0), (1, 2, 5, 6), (3, 4, 7, 8)

    if uid in c19xx:
        c = 1900
    if uid in c20xx:
        c = 2000
    if uid in c18xx:
        c = 1800

    year = c + int(self.ssn[0:2])
    month = int(self.ssn[2:4])
    day = int(self.ssn[4:6])
    return (year, month, day)

    #print(f"생년월일: {year}년{month}월 {day}일")

def age(self):

    uid = int(self.ssn[7])
    c18xx, c19xx, c20xx = (9, 0), (1, 2, 5, 6), (3, 4, 7, 8)

    if uid in c19xx:
        c = 1900
    if uid in c20xx:
        c = 2000
    if uid in c18xx:
        c = 1800

    year = c + int(self.ssn[0:2])
    month = int(self.ssn[2:4])
    day = int(self.ssn[4:6])
    
    today = int(datetime.date.today().strftime("%Y%m%d"))
    birth = year * 10000 + month * 100 + day
    age = (today - int(birth)) // 10000
    
    return age

def gender(self):

    uid = int(self.ssn[7])
    male, female = (1, 3, 5, 7, 9), (2, 4, 6, 8)
    
    if uid in male :
        gender = "남자"
    elif uid in female :
        gender = "여자"

    return gender


"""
## 주민등록번호 : 800512-1133555
##for s in data1:
##    if s not in ['0', '1', '2', '3', '4', ... '9']
##        result = False
##
## 위 내용은 아래 함수와 같다.
##
## data1.isdigit()

## 데 이 터 형 : 문자형(str)
## type(ssn1) == type('')
## isinstance(ssn1, str)

## 길      이 : 14자리 
## len(ssn1) != 14

## 위 조건이 만족되지 않으면 입력받지 않도록 설정 
"""


ssn  = input('주민등록번호 : ')
a = SSN(ssn)

print(f"생년월일 : {a.birthday()}")
print(f"만나이: {a.age()}")
print(f"성별: {a.gender()}")
"""

# 파일명: module1.py



def udir(object):
   attrs = []
   for attr in dir(object):
      if attr[0] != '_':
         attrs.append(attr)
   return attrs

class FourCal:
   def __init__(self, first, second):
      self.first = first
      self.second = second
   def setdata(self, first, second):
      self.first = first
      self.second = second
   def add(self):
      result = self.first + self.second
      return result
   def sub(self):
      result = self.first - self.second
      return result
   def mul(self):
      result = self.first * self.second
      return result
   def div(self):
      result = self.first / self.second
      return result

class MoreFourCal(FourCal):
   def pow(self):
      result = self.first ** self.second # **는 제곱
      return result

class SafeFourCal(FourCal):
   def div(self):
      if self.second == 0:
         result = 0
      else:
         result = self.first / self.second
      return result
      
# 파일명: s0125_birthday.py

"""
   if not isinstance(ssn, str):         # 34~40까지는 무결성 검사. 주민등록번호 입력받을 때,정확히 입력받도록
      return None
   elif len(ssn) != 14:
      return None
   elif not(ssn[0:6].isdigit() 
       and ssn[6] == '-' 
       and ssn[7:14].isdigit()):    # not 바로 뒤의 ()안에 있으면 줄 바꿔도 상관x
#   elif not ssn[0:6].isdigit() or ssn[6] != '-' or not ssn[7:14].isdigit():  전부 True and True and True 해도됨. 다 똑같은 논리(회로)
      return None
"""

class SSN:
   def __init__(self, ssn):
      if not isinstance(ssn, str):
         raise ValueError
      elif len(ssn) != 14:
         raise ValueError
      elif not(ssn[0:6].isdigit()
          and ssn[6] == '-' 
          and ssn[7:14].isdigit()):
         raise ValueError
      self.ssn = ssn
      
   def birthday(self):
      import datetime
      uid = int(self.ssn[7])
      Cen21, Cen20, Cen19 = (3,4,7,8), (1,2,5,6), (9,0)
      male, female = (1,3,5,7,9), (2,4,6,8,0)
      if uid in Cen20:         # 1900년대
         century = 1900
      elif uid in Cen21:         # 2000년대
         century = 2000
      elif uid in Cen19:         # 1800년대
         century = 1800
      year = century + int(self.ssn[0:2])
      month = int(self.ssn[2:4])
      day = int(self.ssn[4:6])   
      return datetime.date(year,month,day)

   def age(self):
      import datetime   
      today = int(datetime.date.today().strftime("%Y%m%d"))
      birthday = int(self.birthday().strftime("%Y%m%d"))
      age = (today - birthday) // 10000
      return age
      
   def gender(self):
      uid = int(self.ssn[7])
      male = (1, 3, 5, 7, 9)
      if uid in male:
         return 'M'
      else:
         return 'F'

if __name__ == "__main__":
   ssn = input("주민등록번호: ")
   a = SSN(ssn)
   print(f"생년월일: {a.birthday()}")
   print(f"만 나이: {a.age()}")
   print(f"성   별: {a.gender()}")