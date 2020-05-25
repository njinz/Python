from sklearn import svm,metrics
# clf=svm.SVC()                             #인공지능 실행객체 생성 후 변수에 저장.
# clf.fit(입력데이터,출력데이터)              #데이터 세팅: 매개변수 2개(입력data, 출력 data)
# 질문의 답=clf.predict(질문데이터)           #질문데이터를 매개변수로 넣음.
# print(질문의 답)

clf=svm.SVC()
clf.fit([[0,0],[0,1],[1,0],[1,1]],[0,1,1,1])
result=clf.predict([[0,0],[1,0]])
print(result)                                                #[0 1]
score=metrics.accuracy_score([0,1],result)            #정답률 (답, 정답)
print("정답률:",score)                                 #정답률: 1.0 (100%라는 뜻)
