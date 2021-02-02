# 파일명 : module1.py

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

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

##클래스 상속
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
##FourCal의 모든 기능 + pow 기능 을 쓸 수 있다.

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            result = 0
        else:
            result = self.first
        return result


def udir(object):

    attrs = []

    for attr in dir(object):
        if attr[0] != "_":
            attrs.append(attr)
    return attrs