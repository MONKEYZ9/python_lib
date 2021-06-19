from openpyxl import Workbook
import openpyxl



# with open('C://Users\mingzzang\Desktop\idPw.txt') as idPw_file:
#     line = idPw_file.readlines()
#     idArr = []
#     pwArr = []
#     for i in line:
#         # print(type(i)) str
#         idpw = i.split()
#         # print(idpw)
#         idArr.append(idpw[0])
#         pwArr.append(idpw[1])
#         # print(idArr)
#         # print(pwArr)
#     if id in idArr:
#         if pw in pwArr:
#             print('로그인된다.')
#         else:
#             print('비번 틀렸다')
#     else:
#         print('가입이력이 없습니다.')
#     # line2 = line[0].split()
#     # if 'sangmin3285' in  line2:
#     #     print('있다')


# text_file = open('C://Users\mingzzang\Desktop\idPw.txt', 'r', encoding='utf-8')
# text_read = text_file.read()
# print(text_read)
# text_file.close()


# ----------------------------------------------
# with open('C://Users\mingzzang\Desktop\idPw.txt') as idPw_file:
#     line = idPw_file.readlines()
#     for i in line:
#         print(i)
#         # 아이디가 있는지 찾고
#         if id in i:
#             # 그 배열안에 비번도 맞는지 확인하자
#             if pw in i:
#                 print("로그인 성공")
#                 break
#             else:
#                 print("비번 틀림")
#                 break
#     else:
#         print('회원가입 이력이 없습니다.')


# with open('C://Users\mingzzang\Desktop\idPw.xlsx', encoding='utf-8') as idPw_file:
#     file_check = openpyxl.load_workbook(idPw_file.name)
#     fileSheet_check = file_check.active
#     # print(fileSheet_check) 시트 이름 나왔고
#     idPwArr = []
#     for row in fileSheet_check.rows:
#         # print(row)
# #         (<Cell 'Sheet1'.A1>, <Cell 'Sheet1'.B1>)
#         # (<Cell 'Sheet1'.A2>, <Cell 'Sheet1'.B2>)
#         print(row[0].value)
#         arr = []
#         arr.append(row[0].value)
#         arr.append(row[1].value)
#         idPwArr.append(arr)
#         print(idPwArr)
#     # 아이디가 있는지 찾고
#     for i in range(len(idPwArr)):
#         if id in idPwArr[i]:
#             # 그 배열안에 비번도 맞는지 확인하자
#             if pw in idPwArr[i]:
#                 print("로그인 성공")
#                 break
#             else:
#                 print("비번 틀림")
#                 break
#     else:
#         print('회원가입 이력이 없습니다.')
    
    #     # 아이디가 있는지 찾고
    #     if id in i:
    #         # 그 배열안에 비번도 맞는지 확인하자
    #         if pw in i:
    #             print("로그인 성공")
    #             break
    #         else:
    #             print("비번 틀림")
    #             break
    # else:
    #     print('회원가입 이력이 없습니다.')



# from csv import reader as r
# with open('C://Users\mingzzang\Desktop\idPw.csv', 'r') as csv_file:
#     csv_reader = r(csv_file)
#     idPwArr = []
#     for i in csv_reader:
#         idPwArr.append(i)
#     # 아이디가 있는지 찾고
#     for i in range(len(idPwArr)):
#         if id in idPwArr[i]:
#             # 그 배열안에 비번도 맞는지 확인하자
#             if pw in idPwArr[i]:
#                 print("로그인 성공")
#                 break
#             else:
#                 print("비번 틀림")
#                 break
#     else:
#         print('회원가입 이력이 없습니다.')    


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
        print('감사합니다')
    else:
        print(result)

join()
# id, pw = join_input()
# print(join_check(id, pw))


# with open("C://Users\mingzzang\Desktop\join.txt", 'a') as join_file:
#     join_file.write(id + ' ')
#     join_file.write(pw + ' \n')
    # 일단 받아오면 적는 것 까지는 했는데
    # 이게 있는지 먼저 확인해야 하는거

