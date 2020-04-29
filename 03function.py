#def : definition 의준말로 함수 선언하는 키워드.
def sum(x,y):
    s=x+y
    return s

result=sum(10,20)
print(result)              #30

def multiFunc(x):
    return x+1,x+2,x+3      #리턴 여러개 받기 가능(자바는 불가)

x1,x2,x3=multiFunc(1)
print(x1,x2,x3)            #2,3,4

#LAMBDA 람다식 (함수를 간단하게 만들어주는 익명함수)
f=lambda x:x+100
for i in range(3):
    print(f(i))  #100,101,102

def print_hello():
    print('hello')
def test_lambda(s,t):
    print(s,t)

fx=lambda x,y:test_lambda(x,y)
fy=lambda x,y:print_hello()
fx(500,100)  #500 100
fy(300,600)  #hello

