print("hello world")
print("myName is p")
# 주석입니다

#data type :
#list tuple dictionary string (python은 array 없다.)

#LIST
a=[10,20,30,40,50]                  
print("a[0]=",a[0]," , a[1]=",a[1])   #a[0]= 10 , a[1]= 20
print("a[0]=",a[-1],"a[1]=",a[-2])    #뒤에서부터

b=[10,20,'hello',[True,3.24]]      #True 첫글자 반드시 대문자
print(b[3][0])                     #True
print(b[-1][-2])                   #True

c=[]
c.append(100),c.append(200),c.append(300),c.append([1,2]) 
print(c)

a=[10,20,30,40,50]
print(a[0:2])         #[10,20] #슬라이스 : 앞수부터 뒷수-1까지 나타냄. 뒤에 숫자가 앞수보다 커야함 . 
print(a[1:2])         #[20]
print(a[1:])          #[20,30,40,50] : [1]부터 다
print(a[:3])          #[10,20,30]
print(a[:-2])         #[10,20,30]
print(a[:])           #[10,20,30,40,50]
print(a[:-1])         # #[10,20,30,40]

#TUPLE 튜플 : 
# list와 유사. 상수처럼 변경이 불가. ()에 선언한다.
a=(10,20,30,40,50)
#a[0]=4                #TypeError: 'tuple' object does not support item assignment 변경이 불가

#DICTIONARY 딕셔너리
#KEY VALUE 값으로 데이터가 쌍으로 존재
score={"kim":90,"lee":29,"park":99}
print(score['kim'])   #90
print(score)          #{"kim":90,"lee":29,"park":99}
#print(score.kim)     #AttributeError: 'dict' object has no attribute 'kim'  안됨
print(score.keys())   #dict_keys(['kim', 'lee', 'park'])
print(score.values()) #dict_values([90, 29, 99])
print(score.items())  #dict_items([('kim', 90), ('lee', 29), ('park', 99)])
#값 변경
score["kim"]=44
print(score['kim'])   #44

#string 
a='a24,sa'            #문자열을 list처리 한다.
print(a[1])           #2 라는 문자열을 리턴
print(a[3])           #,
a=a+',hello'
print(a)              #a24,sa,hello
b=a.split(',')        #특정 구분자(,) 로 구분함.
print(b)              #['a24', 'sa', 'hello']



#FUNCTION 종류

a=[10,20,30,40,50]
b=(10,20,30,40,50)
c={"kim":90,"lee":29,"park":99}
d="hello world"
e=[[100,200],[300,400],[500,600]]


#type : 데이터타입을 알려줌
print(type(a))  #<class 'list'>
print(type(b))  #<class 'tuple'>
print(type(c))  #<class 'dict'>
print(type(d))  #<class 'str'>
print(type(e))  #<class 'list'>

#length :데이터 길이 알려줌
print(len(a),len(b),len(c),len(d),len(e))       #5 5 3 11 3

#list : list형으로 바꿔줌
a="hello"
print(list(a))                    #['h', 'e', 'l', 'l', 'o']
print(a[0])                       #h

#str :str로 바꿔줌
print(str(3.14))                #3.14
print(str('3.14'))              #3.14
print(str('3.14')+ ' 3.14')     #3.14 3.14
print(str([1,2,3]))             #[1, 2, 3] 

#int :정수로 바꿔줌
print(int(3.14))                #3
print(int('3'))                 #3

#float: 실수로 바꿔줌
print(float('3.14'))            #3.14
print(float(3))                 #3.0

