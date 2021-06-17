from openpyxl import Workbook
import openpyxl


id = input()
pw = input()

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



from csv import reader as r
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
                print("로그인 성공")
                break
            else:
                print("비번 틀림")
                break
    else:
        print('회원가입 이력이 없습니다.')    