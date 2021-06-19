# 여러개의 변수 한번에 할당
a, b, c, d = 1, 2, 3, 4
print(a, b, c, d)

# 주의점: 변수할당할 때 함수명은 피할것 ex) print = 10 print의 함수로서의 기능이 날아가고 10이라는 데이터가 할당되어버림
print("----자료형----")
#자료형 : 파이썬에서 활용하는 모든 데이터의 형태
# 숫자자료형 : 정수(int), 실수(float)
# // :  나눈몫 , % : 나눈 나머지, ** : 거듭제곱
# 문자열(string) : '' or ""
print("hello " + "world!")

print("----Bool----")
# Bool(True / False)
print(type(True), ",", type(False))
print(int(True), ",", int(False))

print("----set----")
# 집합(Set) : data의 중복을 허용하지 않음
print({1, 2, "hahaha", 1, 2, 1})    

print("----tuple----")
# 튜플(Tuple) : 자료의 수정이 불가능
a = (1, 2, 3)
print((1, 2, 3, "haha", a))


print("----list----")
# 리스트(List) : 각 원소에 위치번호가 매겨져있다(index), 여러 자료형이 함께 들어가도 됨
# 인덱싱(indexing) :  인덱스로 원소를 불러오는 것
# 슬라이싱(Slicing) : 인덱스로 여러 원소를 불러오는 것
# 
ls = [10, 20, 30, 40, 50]
print(ls[0], ls[1])
print(ls[-1])
print(ls[ :-1])

ls[4] = ls[0] * 7
print(ls[0])

print(ls[1:3])
print(ls[1: ])
print(ls[ :3])

ls[1:3] = [2, 3]
print(ls)

print("----list 연산----")
# + : list 데이터 합침
# .append() : 새로운 원소를 리스트 맨 뒤에 추가
# .pop() : 리스트의 맨 뒤의 원소를 하나 제고하고 제거한 원소를 반환
# .remove() : 입력한 이름에 해당되는 원소를 제거

ls2 = [1, 2, 3, 4, 5]
print(ls + ls2)

ls.append(100)
print(ls)
ls.append("안녕")
print(ls)
ls.pop()
print(ls)
ls.pop(5)
print(ls)
ls.remove(70)
print(ls)

print("----인덱싱----")
# 인덱싱이 되는 자료형들 :  문자열, 튜플

hi = "안녕하세요"
print(hi[0])
print(hi[1: ])

tp = (1, 2, 3, 4)
print(tp[0])
print(tp[1: ])

# tp[0] = tp[0]*10
# print(tp)   튜플은 데이터 수정 불가


print("----Dictionary----")
# 딕셔너리(Dictionary) : key 값과 value 값의 쌍으로 구성된 자료형
# value 자리에는 어떤 자료형을 가져와도 무관함(단, key 값의 경우 조심 > 튜플이나 리스트형태는 X)
# key값과 value 값을 통해 자료에 접근
# 인덱스가 없음 = 인덱싱이 불가능
dic = {"토끼반" : ["지형", "현택", "지윤", "인석"], "거북이반" : ("지현", "승미", "채영", "희정")}
print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())

# 새로운 자료추가
dic["민들레반"] = ["선영"]
print(dic)

# 기존 자료 제거
del dic["민들레반"]
print(dic)

print("----if----")
# 조건문
a = 10
if a > 5:
    print("와 5보다 크네?")
if a == 3:
    print("a는 3입니다")

# elif는 위의 조건문이 불일치할때만 구동, 일치하면 조건문 멈춤
# else는 위의 조건문에 모두 위배될 때 구동
b = 20
if b > 30:
    print("b는 30보다 큽니다")
elif b > 15:
    print("b는 15보다 큽니다")
elif b > 10:
    print("b는 10보다 큽니다")
else:
    print("b는 11보다 작습니다")

print("----for----")
# 반복문
ls = [10, 20, 30, 40, 50]
for i in ls:
    print(i)
print("***")

for i in range(10):
    print(i)
print("***")

for i in range(3, 11):
    print(i)
print("***")

ls = []
for i in range(0, 101, 10):
    ls.append(i)
print(ls)
print('***')

ls = [i for i in range(1, 11)]
print(ls)
print('***')

ls = [i*10+1 for i in range(1, 11)]
print(ls)


print("----라이브러리 설치/불러오기----")
# 라이브러리 : 데이터분석, 시각화 등 파이썬 언어로 여러 기능들을 수행할 수 있는 도구들을 모아 둔 것
# 설치 : Terminal 창 / cmd 창 / anaconda prompt 창 -> pip install '설치할 라이브러리명'
# 불러오기 : import pandas
import pandas
print(pandas.DataFrame({"hi" : [1, 2, 3]}))