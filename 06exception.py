#예외처리
def calc(data):
    sum=0
    try:                                #try: finally: 는 무조건 실행되는 부분. 예외발생시 except
        sum=data[0]+data[1]+data[2]
        if sum<0:
            raise Exception("sum error")  #except 의 Exception 부분으로 감. sum<0일시 강제로 예외발생시킴.

    except IndexError as err:    #indexerror일경우 이 부분이 실행되고 finally: 부분 실행됨.
        print(str(err))
    except Exception as err:     #모든 예외일경우 이 부분이 실행되고 finally:부분 실행됨.
        print(str(err))

    finally:
        print(sum)

calc([1,2])         #에러: list index out of range  0  (인덱스 3개여야 하는데 예외발생함)
calc([1,2,3])       #6

calc([-1,-2,-3])    #sum error -6


# WITH 구문 : 파일을 사용자 임의대로 열고 닫게 해줌. (java using과 유사)

f=open("파일명","w")            #with 안쓴 구문
f.write("Asdf")
f.close

with open("파일명") as f:       #with 쓴 구문 (따로 close 불필요)
    f.write("Asdf")


