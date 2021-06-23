import pandas as pd
import numpy as np

class Commerce6_login :

  def login_doit(self) :
    login_df = pd.read_csv("C:/Users/mingzzang/Desktop/idPw.csv")
    inputId = input('Enter Your Information [id] : ')
    inputPw = input('Enter Your Information [pw] : ')
    # Check Login
    if len(login_df.loc[(login_df['id'] == inputId) & (login_df['pw'] == str(inputPw))]) == 1 :
      return 'login_complete', inputId, inputPw
    else :
      return 'login_fail', None, None

  def join_guest(self) :
    login_df = pd.read_csv("C:/Users/mingzzang/Desktop/idPw.csv")
    
    info_table = ['id',	'pw',	'nickname',	'location']
    return_table = []

    while True:
      for i in range( 4 ) : # id	pw	nickname	location
        return_table.append( input("Enter Your Information [{}] : ".format(info_table[i])) )

      return_table_df = pd.DataFrame( np.array(return_table).reshape(1, -1), columns=info_table )
      print(return_table)
      print(return_table_df)

      if return_table[0] in login_df['id'].values:
        print('중복된 아이디입니다.')
        continue

      else:
        login_df = login_df.append(return_table_df)
        login_df.to_csv("C:/Users/mingzzang/Desktop/idPw.csv", index = False)
        break

    return 'join_guest_complete', return_table[0], return_table[1]

# 상품을 장르별로도 검색해볼 수는 없을까요?
# 단순히 구매하기 말고, csv 파일을 DB 처럼 활용하는 방법으로 장바구니도 구현할 수 있을것 같습니다.
class Commerce6_product :
  def __init__(self, id, pw) :
    self.id = id
    self.pw = pw

  def product_infomation_resule(self) :
    # login_df = pd.read_csv("/content/drive/My Drive/lion/Commerce6/login/Commerce6_login.csv")
    product_df = pd.read_csv("C:/Users/mingzzang/Desktop/bestsellers with categories.csv")

    while True :
      product_choice_options = int(input("평점높은순(1) / 리뷰많은순(2) / 낮은가격순(3) / 높은가격순(4) / 최신출시순(5): "))
      
      if product_choice_options == 1 :
        product_df = product_df.sort_values(by=['User Rating'], axis=0, ascending=False)
      elif product_choice_options == 2 :
        product_df = product_df.sort_values(by=['Reviews'], axis=0, ascending=False)
      elif product_choice_options == 3 :
        product_df = product_df.sort_values(by=['Price'], axis=0, ascending=True)
      elif product_choice_options == 4 :
        product_df = product_df.sort_values(by=['Price'], axis=0, ascending=False)
      elif product_choice_options == 5 :
        product_df = product_df.sort_values(by=['Year'], axis=0, ascending=False)

      for i in range( 5 ) :
        print( "-------------------------------" )
        print( "-{} 번째 서적번호------------------".format(i+1) )
        print( "-------------------------------" )
        for j in range( len(product_df.columns) ) :
          if j == 4 :
            print( "{} : {} 원".format(product_df.columns.to_list()[j], format(product_df.loc[i][j]*1000, ",") ) )
          else :
            print( "{} : {}".format(product_df.columns.to_list()[j], product_df.loc[i][j]) )
        print( "-------------------------------" )

      choice_product_booknumber = int(input("구매하실 서적 번호를 입력 : "))

      print( f"{self.id} 님, 구매 신청하신 서적은 {product_df.loc[choice_product_booknumber-1][0]} 입니다.")
      print( "가격은 {} 원입니다.".format( product_df.loc[choice_product_booknumber][4]*1000 ) )
      
      choice_product_bookorder = int(input("구매(1) / 비구매(2) : "))

      if choice_product_bookorder == 1 :
        print("결제처리 진행 중")
        break
      elif choice_product_bookorder == 2 :
        print("다른 서적을 확인 중")
        pass
    book_name = product_df.loc[choice_product_booknumber-1][0]
    book_price = product_df.loc[choice_product_booknumber][4]*1000
    return f'{book_name}을(를) {book_price}원의 가격으로 구매하셨습니다.', book_name, book_price