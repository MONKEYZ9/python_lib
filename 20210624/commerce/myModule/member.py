import pandas as pd
import numpy as np

class Commerce6_member :
  # 로그인 진행하고
  def login_member(self) :
    login_df = pd.read_csv("C:/Users/mingzzang/Desktop/idPw.csv")
    inputId = input('Enter Your Information [id] : ')
    inputPw = input('Enter Your Information [pw] : ')
    # Check Login
    if len(login_df.loc[(login_df['id'] == inputId) & (login_df['pw'] == str(inputPw))]) == 1 :
      return 'login_complete', inputId, inputPw
    else :
      return 'login_fail', None, None

  # 회원가입 진행하고
  def join_guest(self) :
    login_df = pd.read_csv("C:/Users/mingzzang/Desktop/idPw.csv")
    
    info_table = ['id',	'pw',	'nickname',	'location']

    while True:
      return_table = []
      for i in range( 4 ) : # id	pw	nickname	location
        return_table.append( input("Enter Your Information [{}] : ".format(info_table[i])) )

      return_table_df = pd.DataFrame( np.array(return_table).reshape(1, -1), columns=info_table )

      if return_table[0] in login_df['id'].values:
        print('{}는 중복된 아이디입니다.'.format(return_table[0]))
        continue

      else:
        login_df = login_df.append(return_table_df)
        login_df.to_csv("C:/Users/mingzzang/Desktop/idPw.csv", index = False)
        break

    return 'join_guest_complete', return_table[0], return_table[1]

  # 로그인 또는 회원가입을 했을때
  def homepage_Go(self):
    
    # 로그인 진행
    comment, id, pw = self.login_member()
    if comment == 'login_complete':
        return id, pw

    # 로그인 실패시
    elif comment == 'login_fail':
        print('로그인에 실패했습니다.')
        # 회원가입이 진행
        comment, id, pw = self.join_guest()
        if comment == "join_guest_complete":
            return id, pw
