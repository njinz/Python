import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9,10,11,12]).reshape(4,3)
print(a.shape)  #(4,3)
print(a)        #[[1 2 3] [4 5 6 ] [7 8 9] [10 11 12]]
print(a[0][0],a[0,0])   # 1 1
print(a[0][1],a[0,1])   # 2 2

print(a[0:-1,1:2])  # : 의미= 범위에 맞는 수 모두 출력 [[2][5][8]] 
#a:b,c:d = 행a부터 행b이전까지,열c부터 열d이전까지 출력
print(a[:,0])  # [1 4 7 10]
print(a[:,:])  # 행렬 a가 나온다. [[1 2 3] [4 5 6 ] [7 8 9] [10 11 12]]


#a행렬의 값을 순서대로 하나씩 다 뽑아보자
#iterator 생성
it=np.nditer(a,flags=['multi_index'],op_flags=['readwrite'])
while not it.finished: #마지막데이터가 아닌동안 반복
    idx=it.multi_index
    print(idx,a[idx]) 
    it.iternext()  #(0,0)1 (0,1)2 (0,2)3 (1,0)4 (1,1)5 (1,2)6 (2,0)7 (2,1)8 (2,2)9 (3,0)10 (3,1)11 (3,2)12

#concatenate :배열 합치기
a=np.array([[10,20,30],[40,50,60]])
print(a)
b=np.array([70,80,90]).reshape(1,3)
a1=np.concatenate((a,b),axis=0)  #axis(중심선) 축을 0으로 행에 1이면 열에 추가 . 괄호 필수! 
print(a1) #[[10 20 30 ] [40 50 60] [70 80 90]]
a2=np.concatenate((a1,b.reshape(3,1)),axis=1) #축을 1로 
print(a2) #[[10 20 30 70] [40 50 60 80 ] [70 80 90 90]]


load_data=np.loadtxt('./data.csv',delimiter=',',dtype=np.float32) #콤마를 기준으로 불러오겠다.
print(load_data) #data.csv에 저장했던 data들이 출력.
x_data=load_data[:,0:-1] #열은 마지막열 전까지 출력됨.
y_data=load_data[:,-1]  #마지막 열만찍힘
print(x_data,x_data.ndim,x_data.shape)  #ndim: 몇차원인지
print(y_data,y_data.ndim,y_data.shape)

#random
r1=np.random.rand(3)    #3개의 랜덤값 vector
r2=np.random.rand(1,3)  #3개의 랜덤값 (1행3열)행렬
r3=np.random.rand(3,1)  #3행1열
print(r1,r1.shape)  #[0.26209884 0.79606674 0.47134299] (3,)
print(r2,r2.shape)  #[[0.29762314 0.77340798 0.28882766]] (1, 3)
print(r3,r3.shape)  #[[0.21026463][0.02601043][0.85216123]] (3, 1)

x=np.array([2,4,6,8])
print(np.sum(x))  #더하기 20
print(np.exp(x))  #자연상수 e를 x제곱한것 e=2.71.. [ 7.3890561  54.59815003  403.42879349 2980.95798704]
print(np.log(x))  #로그값 [0.69314718 1.38629436 1.79175947 2.07944154]
print(np.max(x))  #최댓값 8
print(np.min(x))  #최솟값 2
print(np.argmax(x))   #arg:인덱스를 리턴. 최댓값의 인덱스는 3
print(np.argmin(x))   #0

a=np.ones([3,3])  #3,3인 1로 채워진 행렬 
print(a)          #[[1. 1. 1.][1. 1. 1.][1. 1. 1.]]
b=np.zeros([2,4])
print(b)        #[[0. 0. 0. 0.][0. 0. 0. 0.]]

x=np.array([[2,4,6],[1,2,3],[0,5,8]])
print(np.max(x,axis=0))   #[2 5 8] 열비교해서 가장 큰 것
print(np.min(x,axis=0))   #[0 2 3]
print(np.argmax(x,axis=1)) #[2 2 2]
print(np.argmin(x,axis=1)) #[0 0 0]

