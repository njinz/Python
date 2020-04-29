#IF문
a=1
if a > 0:
    print("1. a ==",a)
elif a==0:
    print("2. a ==",a)
else:
    print("3 .a ==",a)
    print("if문 끝부분")
    
print("종료")  # 1. a == 1 
               # 종료

a=[10,20,30,40,50]
b=(10,20,30,40,50)
c={"kim":90,"lee":29,"park":99}

#IF IN 
if 45 in a:             #배열에 45있는지 여부
    print('is 45')
else:
    print('is not 45')  #is not 45

if 'kim' in c:
    print('is kim')     #is kim
else:
    print('is not kim')

#반복문 for
for data in range(10):  #data가 0부터 10개 찍기
    print (data)        #0 1 2 3 4 5 6 7 8 9

for data in range(0,10,2): #0부터 10개의 수(0~9)중에 2개씩 증가하는수 
    print(data)         #0,2,4,6,8

for data in a:
    print(data)         #10,20,30,40,50

c={"kim":90,"lee":29,"park":99}

for data in c:
    print(data)         #kim lee park : key값만 찍힘

for data in c:
    print(data," ",c[data])  #kim   90  lee   29  park   99 ?????

    print (c[data])  #99  ???
   

for data,value in c.items():
    print(data,"",value)     #kim   90  lee   29  park   99

a=[x**2 for x in range(5)]  # **: 제곱
print(a)                    #0,1,4,9,16 :0~4까지 제곱한 것들을 배열로 만듦


e=[[100,200],[300,400],[500,600]]

a=[x for x in e]
print(a)                        #e가 찍힘
                             
a=[x[0] for x in e]
print(a)                       #[100,300,500]
                             
a=[x[1] for x in e]
print(a)                       #[200,400,600]

#10이하의 짝수를 list에 넣어 출력해보자.
a=[x for x in range(2,11,2)]
print(a)                       #[2,4,6,8,10]

b=[]
for data in range(11):
    if data %2 ==0:
        b.append(data)         #[0,2,4,6,8,10]
print(b)

#while
a=5
while a>=0 and a<=10:
    print(a)
    a=a+1
print('종료')                 #5,6,7,8,9,10 종료

