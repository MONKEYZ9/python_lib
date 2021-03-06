# -*- coding: utf-8 -*-
import openpyxl

"""모듈 만들기 (모듈 설계 코드)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12D6vWZj2osT4wxbeW-s3euSyqIqjvp3E
"""

# LV1 : 직접 원하는 모듈을 생성하기
# def __init__(self, name, age, kg, cm, area ) :
#   self.name = name
#   self.age = age
#   self.kg = kg
#   self.cm = cm
#   self.area = area

def 인사말생성기( name, age ) : 
  if age > 40 :
    return "안녕하세요, {}고객님! 중년의 힘을 보여주세요.".format( name )
  elif age >= 20 and age <= 39 :
    return "안녕하세요, {}고객님! 청년의 힘을 보여주세요.".format( name )
  elif age >= 0 and age <= 19 :
    return "안녕하세요, {}고객님! 청소년의 힘을 보여주세요.".format( name )

def BMI측정기( name, kg, cm ) :
  bmi = round( kg / pow( cm, 2 ) * 10000 )

  if bmi < 20 :
    return "{}고객님께서는 저체중 이시군요!".format( name )
  elif bmi >= 20 and bmi <= 24 :
    return "{}고객님께서는 정상 이시군요!".format( name )
  elif bmi >= 25 and bmi <= 29 :
    return "{}고객님께서는 과체중 이시군요!".format( name )
  elif bmi >= 30 :
    return "{}고객님께서는 비만 이시군요!".format( name )

def 실평수계산기( name, area ) :
  return "{}고객님께서 알아보신 장소의 실제 평수는 {}평 입니다!".format( name, round( area / 3.3 ) )

# 인사말( "나호용", 27 )
# BMI측정기("나호용", 85, 175)
# 실평수계산기( "나호용", 46.02 )


# 1. txt / csv / xlsx 데이터 리드 하기
# 값을 가져와서, 아이디, 패스워드를 입력을 하는데 가져온거랑 내가 지금 쓰는거랑 비교하는 거야
# 맞으면 '로그인 완료 처리' 나오게끔

def loginCheck_txt_version(id, pw):
  with open('C://Users\mingzzang\Desktop\idPw.txt') as idPw_file:
    line = idPw_file.readlines()
    for i in line:
        # 아이디가 있는지 찾고
        if id in i:
            # 그 배열안에 비번도 맞는지 확인하자
            if pw in i:
                return("로그인 성공")
                
            else:
                return("비번 틀림")
                
    else:
        return('회원가입 이력이 없습니다.')

def loginCheck_xlsx_version(id, pw):
  with open('C://Users\mingzzang\Desktop\idPw.xlsx', encoding='utf-8') as idPw_file:
    file_check = openpyxl.load_workbook(idPw_file.name)
    fileSheet_check = file_check.active
    # print(fileSheet_check) 시트 이름 나왔고
    idPwArr = []
    for row in fileSheet_check.rows:
        # print(row)
#         (<Cell 'Sheet1'.A1>, <Cell 'Sheet1'.B1>)
        # (<Cell 'Sheet1'.A2>, <Cell 'Sheet1'.B2>)
        # print(row[0].value)
        arr = []
        arr.append(row[0].value)
        arr.append(row[1].value)
        idPwArr.append(arr)
        # print(idPwArr)
    # 아이디가 있는지 찾고
    for i in range(len(idPwArr)):
        if id in idPwArr[i]:
            # 그 배열안에 비번도 맞는지 확인하자
            if pw in idPwArr[i]:
                return("로그인 성공")
            else:
                return("비번 틀림")
    else:
        return('회원가입 이력이 없습니다.')


from csv import reader as r
def loginCheck_csv_version(id, pw):
  with open('C://Users\mingzzang\Desktop\idPw.csv', 'r') as csv_file:
    csv_reader = r(csv_file)
    idPwArr = []
    for i in csv_reader:
        idPwArr.append(i)
    # 아이디가 있는지 찾고
    for i in range(len(idPwArr)):
        if id in idPwArr[i]:
            # 그 배열안에 비번도 맞는지 확인하자
            if pw in idPwArr[i]:
                return("로그인 성공")
            else:
                return("비번 틀림")
    else:
        return('회원가입 이력이 없습니다.')



# 회원가입 이력이 없다면 그렇게 되면 회원가입을 하러 가야 해
# 그럼 이 사람이 다시 입력을 해 아이디가 기존에 있는지 확인 먼저 해야해

def join_input():
    id = input()
    pw = input()
    return id, pw

def join_check(id, pw):
    with open("C://Users\mingzzang\Desktop\join.txt", 'r+') as join_file:
        arr = []
        while True:
            line = join_file.readline()
            if not line:
                break
            arr.append((line.strip().split()))
            # 만약 생각해보자
            # 내가 찾는 아이디가 있으면 쓰면 안되잖아
            # 그럼 어펜드로 해야 하자나 그럼 read하고 write를 하게 되면 다 지워지잖아.
            # 일단 그럼 해보고 바꾸자
        if id == '중단' or pw == '중단':
            print( '회원가입을 중단하였습니다.')
        else:
            # 이전에 가입이 없다면 바로 가입시켜야지
            if len(arr) == 0:
                # 가입해보자
                with open("C://Users\mingzzang\Desktop\join.txt", 'a') as join_file:
                    join_file.write(id + ' ')
                    join_file.write(pw +'\n')
                    return('가입완료')
            # 누군가 가입했고 가입을 진행하려면 아이디가 중복되는지 확인해야지

            # 지금 아이디가 중복되는걸 하나하나 하려니까 빡세
            # 그럼 아이디만 따로 빼서 배열로 묶자 그리고 아디가 그 배열에 있는지 확인하면 되잖아
            idArr = []
            for i in range(len(arr)):
                idArr.append(arr[i][0])
            if id in idArr:
                print('중복된 아이디입니다.')
                print('가입을 중단하시려면 중단을 두번 입력해주세요')
                id, pw = join_input()
                join_check(id, pw)
            # 아닌 경우에는 가입 ㄱㄱ
            else:
                with open("C://Users\mingzzang\Desktop\join.txt", 'a') as join_file:
                    join_file.write(id + ' ')
                    join_file.write(pw + '\n')
                    return('가입완료')


def join():
        # 있어서 나온 경우
        # 다시 idpw 받아서 다시 찾아야지
        # 그럼 할때 마다 있으면 또 하고 또하고 해야 하잖아 이걸 반복문으로 할지 아님 재귀함수로 할지 정해야 하네
    id, pw = join_input()
    result = join_check(id, pw)
    if result == None:
        return('회원가입 실패')
    else:
        return(result)







# 읽고 쓰고 하는거로 바꾸자
# 회원가입도 만들수 있으면 만들어라.
# append로 할 수 있다.

# while문으로 조건을 맞춰서 계속 돌게끔
# 이거를 반복하게끔 

# 이름 , 키, 몸무게를 입력하면 모듈에 맞게 돌아가게끔
# 모듈로 할 수 있게끔