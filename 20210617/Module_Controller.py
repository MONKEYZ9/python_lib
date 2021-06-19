# 1. txt / csv / xlsx 데이터 리드 하기
# 값을 가져와서, 아이디, 패스워드를 입력을 하는데 가져온거랑 내가 지금 쓰는거랑 비교하는 거야
# 맞으면 '로그인 완료 처리' 나오게끔

# 읽고 쓰고 하는거로 바꾸자
# 회원가입도 만들수 있으면 만들어라.
# append로 할 수 있다.

# while문으로 조건을 맞춰서 계속 돌게끔
# 이거를 반복하게끔 

# 이름 , 키, 몸무게를 입력하면 모듈에 맞게 돌아가게끔
# 모듈로 할 수 있게끔


from myModule import module as myModule

print( "[인사말생성기] : {}".format(myModule.인사말생성기("이상민", 38)) )
print( "[BMI계산기!] : {}".format(myModule.BMI측정기("이상민", 74, 178)) )
print( "[실평수계산기] : {}".format(myModule.실평수계산기("이상민", 55.07)) )

id_input = input()
pw_input = input()
print("[txt 로그인 성공여부] : {}".format(myModule.loginCheck_txt_version(id_input, pw_input)))
print("[xlsx 로그인 성공여부] : {}".format(myModule.loginCheck_xlsx_version(id_input, pw_input)))
print("[csv 로그인 성공여부] : {}".format(myModule.loginCheck_csv_version(id_input, pw_input)))

print("[txt 가입 성공여부] : {}".format(myModule.join()))
