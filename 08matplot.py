import matplotlib.pyplot as plt
import numpy as np 

#matplotlib : 자동으로 분포도그래프 그려주는 라이브러리
x_data=np.random.rand(100)
y_data=np.random.rand(100)

# plt.title('scatter plot')
# plt.grid()
# plt.scatter(x_data,y_data,color='b',marker='o')
# plt.show()

#line그래프 그려보자
#주의. x,y 범위 갯수가 같아야 함. 서로 맵핑되기 때문에
x_data=[x for x in range(-5,5)] #-5와 5사이의 숫자를 반복하여 넣는다.
y_data=[y*y for y in range(-5,5)] #0과 25와 사이의 숫자를 반복하여 넣는다.

#좌표를 넣어도 가능
x_data=[-3,-2,-1,0,1,2,3] 
y_data=[3,2,1,10,11,12,13]

plt.xlabel('needs') #x축 이름
plt.ylabel('supply')
plt.title('line graph')
plt.grid()
plt.plot(x_data,y_data,color='r')
plt.show()


