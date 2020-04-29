#numpy : 라이브러리 . 행렬계산에 쓰임.
#기본적으로 array라는 단위로 데이터를 관리하며 이에 대해 연산을 수행. 
#먼저 numpy를 사용하기 위해서는 아래와 같은 코드로 numpy를 import해야 합니다.

import numpy
a=numpy.array([1,2])
print(a,"",type(a))       #[1 2]  <class 'numpy.ndarray'>  list가 아닌 numpy클래스 안의 nd array이다.

import numpy as np        # as로 별명을 추가할수도 있다. 
a=np.array([1,2])
print(a)

from numpy import exp            #exp라는 함수 호출. 
result = exp(1)
print(type(result),"",result)    #<class 'numpy.float64'>  2.718281828459045

from numpy import array
a=array([1,2])
print(a)                         #[1 2]


from numpy import *
a=array([1,2])
print(a)                             #[1 2]
print(exp(1),log(1.5),sqrt(2))       #2.718281828459045 0.4054651081081644 1.4142135623730951

a=[[1,0],[0,1]]
b=[[1,1],[1,1]]
c=a+b
print(c)                            #[[1, 0], [0, 1], [1, 1], [1, 1]]  list형식으로 계산되버림.


#행렬계산을 하고 싶다면 ->  numpy이용
import numpy as np
a=np.array([[1,0],[0,1]])
b=np.array([[1,1],[1,1]])
c=a+b
print(c)                     #[[2 1]
                             #[1 2]] 행렬의 덧셈
c=a*b
print(c)                     #[[1 0]
                             #[0 1]] 행렬의 곱셈

#벡터 - 1차원 배열의 계산
import numpy as np
a=np.array([1,2,3])
b=np.array([4,5,6])
c=a+b                        # 사칙연산 가능  + - * /  
print(c)                     #[5 7 9]

print(a.shape)               #(3,) 열이 3개라는 뜻. 1차원 배열이라 한개만 쓰임. shape: 행과열 모양새 알려줌
print(b.shape)               #(3,)
print(c.shape)               #(3,)

print(a.ndim)                #1  :1차원 배열      ndim:몇차원 배열인지 알려줌.


a=np.array([[1,2,3],[4,5,6]])
b=np.array([[-1,-2,-3],[-4,-5,-6]])
print(a.shape,b.shape)      #(2, 3) (2, 3) 
print(a.ndim,b.ndim)        #2 2

b=b.reshape(3,2)
print(b)           #[[-1 -2][-3,-4][-5,-6]]

#print(a.shape,b.shape)      
#print(a.ndim,b.ndim)

#reshape 후 a,b,연산
import numpy as np
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[-1,-2,-3],[-4,-5,-6]])
b=b.reshape(3,2)
#c=a*b
c=np.dot(a,b)    #np.dot : 곱하기 
print(c.shape)   #(2,2)
print(c)         #[[-22 -28] [-49 -64]]


#broadcast 알아서 값을 채워서 행렬 계산해줌.
c=a+5
print(c)      #[[ 6  7  8] [9,10,11]]
d=[1,2,3]
c=a+d
c=print(c)    #[[2 4 6] [5,7,9]]

#전치행렬 : 원하는 모양으로 행렬모양 바꿔줌.
c=c.T
print(c)
