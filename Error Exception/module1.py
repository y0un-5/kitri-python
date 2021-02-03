# 파일명 :  module1.py

class SSNValueError(Exception):
    def __str__(self):
        return "데이터형이 올바르지 않습니다."

class SSNLenError(Exception):
    def __str__(self):
        return "데이터형의 길이가 맞지 않습니다."

class SSNTypeError(Exception):
    def __str__(self):
        return "숫자 6자리-숫자 7자리 형태가 아닙니다."

"""
def udir(object):
   attrs = []
   for attr in dir(object):
      if attr[0] != '_':
         attrs.append(attr)
   return attrs
"""

class SSN:
   def __init__(self, ssn):
      if not isinstance(ssn, str):
         raise SSNValueError
      elif len(ssn) != 14:
         raise SSNLenError
      elif not(ssn[0:6].isdigit()
          and ssn[6] == '-' 
          and ssn[7:14].isdigit()):
         raise SSNTypeError
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