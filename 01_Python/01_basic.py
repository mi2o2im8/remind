print("안냥")


# 문자열의 여러 유용한 기능함수들
message= " python ReVies, Python  "
print(message.strip())
print(message) #원본 붋변
print(message.strip().lower())
print(message.replace('python', '파이썬'))
print("사과,바나나,우냐냐우냐".split(',')) #응답결과는 리스트
print("Py" in message)
print(len(message)) #글자수
print()

# 3. 제어문(조건, 반복)
# 점수에 따른 학점 





# ---
for n in range(1,6): #1~5까지 반복
    if n==3:
        continue
    print(n)

count=0

# 4. (중요) 리스트[], 튜플(), 딕셔너리{key:value}, Set{}, 컴프리헨션
fruits= ["사과","우사기","토벌해용"] #순서대로 저장. 수정 가능. 중복데이터 허용
print(fruits)
fruits.append("포도")
print(fruits)
fruits[1]= "하치와레"
print(fruits)

point= (10,20) #튜플 - 요소 수정 불가
print(point, point[0], point[1])
#point.append() ##존재하지 않는 기능
# point[0]=100 #error

student= {"name":"sam","score":80} #key:value pair
print(student)
student['score']= 90
print(student['score'], student.get('nam','없음'))

# 중복 데이터를 허용하지 않는 Set 타입
unique_fruits= set(fruits) #list ==> set 타입으로 변경
print(unique_fruits) #순서는 보장 안됨. 중복 허용 안함.

# 리스트 컴프리헨션 (새로운 리스트 생성)
# 1~5에 제곱값을 저장하는 리스트 생성
squars= [ n**2 for n in range(1,6) ] #n*2 등등 다양하게
print(squars)

passing= [n for n in [65,90,73,82] if n>=80] #시험 패스 조건 통과점수들
print(passing)
print()

# 5. 함수, lambda
def greet(person, greeting='우냐냐우냐 야~하~~~~~!~!!~!~!!~~~!~!~!~!~!'):
    return f"{greeting}, {person}님!"

print(greet('우사기'))
print(greet('하치와레','우냐?'))

def average(numbers):
    return sum(numbers) / len(numbers) #총합/개수 = 평균 (sum, len 내장(표준)함수)
print("평균:", average([80,90,75]))


# 제곱해주는 기능 함수
# def square(x):
#     return x*x

square= lambda x: x*x
print(square(5))
#내장함수 중에서 자주 사용
print('정렬:', sorted([3,1,5,2]))
print(min(3,1,5), max(3,1,5))

#6. 파일 입출력 기능함수
# 현재 파일이 있는 폴더에 결과 txt 문서를 저장
from pathlib import Path
BASE_DIR= Path(__file__).resolve().parent # ../././ 이런 상대경로대신 절대 경로로 난옴 / 현재 실행되고 있는 파일의 폴더의 문서를 열겠다.
# C:\Users\mbc\Desktop\mbca\MBCA\00 심화학습 전 리마인드 수업
file_path= BASE_DIR / "aaa.txt"

file= open(file_path, "w",encoding="utf-8")
file.write('파이썬 복습\n파일 입출력 예제\n')
file.close()

with open(file_path, "r", encoding="utf-8") as file:
    print('파일 내용:', file.read())  # 들여쓰기 시 클로즈가 자동으로 됨

# 예외처리 (예외가 발생해도 다운되지 않도록..)
try:
    number= int("80")
    print(number+10)
except ValueError as error:
    print("예외발생:", error)
finally:
    print("예외여부와 상관없이 무조건 실행")



