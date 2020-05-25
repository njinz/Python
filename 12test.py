import pandas
from sklearn import svm,metrics
from sklearn.model_selection import train_test_split
# Iris-setosa  -> 0
# Iris-versicolor  -> 1
# Iris-virginica   -> 2로 변환

#SepalLength,SepalWidth,PetalLength,PetalWidth,Name
csv=pandas.read_csv("iris.csv")
data=csv[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]   
label=csv["Name"]   #답으로 'Name'이 출력되게끔
#학습시킬 데이터를 train_data
#테스트할 데이터를 test_data

train_data,test_data,train_label,test_label=train_test_split(data,label)
print(train_data)

# print(data)         #입력데이터
# print(label)        #출력데이터

clf=svm.SVC()
clf.fit(data,label)
pre=clf.predict(test_data)

ac_score=metrics.accuracy_score(test_label,pre)
result=clf.predict([[5.8,4.0,1.2,0.2],[4.8,3.4,1.5,0.2],[6.7,3.1,4.4,1.4]])
print(result)

#결과
#80            5.5         2.4         3.8        1.1
# 21           5.1         3.7          1.5         0.4
# 130          7.4         2.8          6.1         1.9
# 13           4.3         3.0          1.1         0.1
# 98           5.1         2.5          3.0         1.1
# ..           ...         ...          ...         ...
# 31           5.4         3.4          1.5         0.4
# 124          6.7         3.3          5.7         2.1
# 37           4.9         3.1          1.5         0.1
# 44           5.1         3.8          1.9         0.4
# 111          6.4         2.7          5.3         1.9

# [112 rows x 4 columns]
# [0 0 1]