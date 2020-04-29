def myName():
    print("hello")
class Person:
    count=0                     #클래스변수(모든 인스턴스변수들이 값을 공유하는 변수)
    def __init__(self,name):    #__init__  :initializing (초기화) 이미 정해져 있는 생성자함수 (자바에서는  클래스이름과  동일해야함)      
        Person.count+=1
        self.name=name      #인스턴스변수 #클래스에선 self 항상 꼭꼭 넣기    #self. : 자바 this.와 같은 개념
        print(self.name+"초기화 함수")

    def work(self,company):
        print(self.name+"회사"+company)

    def sleep(self):
        print(Person.count)        #2
        print(self.name)
        self.__myName()
        myName()                   #외부함수 호출 (self불필요) / 내부(지역변수)는 self 필수
    def __myName(self):            #__def이름(self) : 앞밑줄 두개: PRIVATE함수
        print("hello")
    @classmethod
    def getCount(cls):             #self대신 class의 준말 cls
        return cls.count

obj=Person("park")                 #parkI초기화 함수
obj=Person("parkI") 

obj.work("abc")                    #parki회사abc
obj.sleep()                        #park
print(Person.getCount())           #2
#obj.__myName()                     #PRIVATE함수기에 CLASS 밖에서 선언 불가 


