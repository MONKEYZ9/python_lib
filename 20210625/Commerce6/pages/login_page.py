from modules import account
import time
import getpass

page_form = """
1. 로그인
2. 회원가입
3. 종료
"""

def page_rendering():
  print(page_form)

  try:
    service_choice = int(input("선택 : "))

    user_info = account.Commerce_login()

    if service_choice == 1:
      while True:
        user_id = input("아이디 : ")
        user_pw = getpass.getpass("비밀 번호 : ")

        response = user_info.login(user_id, user_pw)
        
        if response == 'complete':
          print(f'\n로그인에 성공하였습니다 {user_info.nickname}님!', end='\n\n')
          time.sleep(0.8)
          return 'index_page', user_info

        elif response == 'IdFailedUser':
          print('아이디가 틀렸습니다.. 다시 입력해주세요', end='\n\n')
        elif response == 'PwFailedUser':
          print('비밀번호가 틀렸습니다.. 다시 입력해주세요', end='\n\n')

    elif service_choice == 2:

      response = user_info.new_account()
      if response == 'complete':
        return 'index_page', user_info

    elif service_choice == 3:
      return 'exit', None
    
    else:
      return 'login_page_rangeError', None

  except ValueError:
    return 'login_page_valueError', None
