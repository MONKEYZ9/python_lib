import pandas as pd
import numpy as np
import os
import bisect


# 상품을 장르별로도 검색해볼 수는 없을까요?
# 단순히 구매하기 말고, csv 파일을 DB 처럼 활용하는 방법으로 장바구니도 구현할 수 있을것 같습니다.
class Commerce6_product :
  def __init__(self, id, pw) :
    self.id = id
    self.pw = pw
    self.product_df = pd.read_csv("C:/Users/mingzzang/Desktop/bestsellers with categories.csv")
    # self.bag_df = pd.read_csv("C:/Users/mingzzang/Desktop/bag.csv") 하나의 장바구니를 사용하는게 아니라 각자의 장바구니를 만들어주려함
    self.login_df = pd.read_csv("C:/Users/mingzzang/Desktop/idPw.csv")


  def product_infomation_resule(self) :
    # login_df = pd.read_csv("/content/drive/My Drive/lion/Commerce6/login/Commerce6_login.csv")
    # login_df = pd.read_csv("C:/Users/mingzzang/Desktop/idPw.csv")

    # product_df = pd.read_csv("C:/Users/mingzzang/Desktop/bestsellers with categories.csv")
    product_df = self.product_df
    # 전체 책 고르는거
    while True :
      # 콘솔 지우기
      os.system('cls')
      first_customer_choice = int(input("카테고리별로 보려면 (1) / 책을 직접 찾으려면 (아무버튼이나 눌러주세요) : "))
      
      # 카테고리별로 본다면
      if first_customer_choice == 1:

        # 처음 책 목록의 갯수는 20개
        book_countStart = 0
        book_countEnd = 20

        # 카테고리별로 검색했을 시, 결제 및 장바구니
        product_choice_options = int(input("평점높은순(1) / 리뷰많은순(2) / 낮은가격순(3) / 높은가격순(4) / 최신출시순(5) / 장르별(6): "))
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
        elif product_choice_options == 6 :
          product_df = product_df.sort_values(by=['Genre'], axis=0, ascending=False)
        
        # 카테고리 목록을 늘려가면서 보여줘야 하니까
        while True:
          # 콘솔 지우기
          os.system('cls')

          # 데이터의 총 갯수는 502개로 확인
          if book_countStart == 500:
            book_countEnd = 503

          for i in range( book_countStart, book_countEnd ) :
            print( "-------------------------------" )
            print( "-{} 번째 서적번호------------------".format(i+1) )
            print( "-------------------------------" )
            for j in range( len(product_df.columns) ) :
              if j == 4 :
                print( "{} : {} 원".format(product_df.columns.to_list()[j], format(product_df.loc[i][j]*1000, ",") ) )
              else :
                print( "{} : {}".format(product_df.columns.to_list()[j], product_df.loc[i][j]) )
            print( "-------------------------------" )

          # 해당 목록에 맘에 드는 책이 없을때
          next_list = int(input("찾으시는 책이 있으신가요?\r\n(있다면 (1) / 없다면 아무버튼이나 눌러주세요) : "))
          if next_list == 1:
            choice_product_booknumber = int(input("구매하실 서적 번호를 입력 : "))

            print( f"{self.id} 님, 구매 신청하신 서적은 {product_df.loc[choice_product_booknumber-1][0]} 입니다.")
            print( f"가격은 {product_df.loc[choice_product_booknumber][4]*1000} 원입니다.")
            
            # 책 이름과 가격을 변수로
            book_name = product_df.loc[choice_product_booknumber-1][0]
            book_author = product_df.loc[choice_product_booknumber-1][1]
            book_price = product_df.loc[choice_product_booknumber][4]*1000
            book_Year = product_df.loc[choice_product_booknumber-1][5]

            choice_product_bookorder = int(input("바로 구매하시나요?\r\n(바로 구매 (1) / 장바구니에 담기 (아무버튼이나 눌러주세요)) : "))
            if choice_product_bookorder == 1 :
              # 바로 결제하고 구매 진행
              print("결제처리 진행 중")

              # 콘솔 지우기
              os.system('cls')

              # 필요한 값들 리턴해주기
              return book_name, book_price
            else:
              # 장바구니에 담는 작업 진행중
              os.system('cls')
              self.product_packBag(book_name, book_author, book_price, book_Year)
              print("장바구니에 담고 다른 서적을 확인 중")
              break    
          else:
            next_choice = int(input("다음 목록으로 갈까요?\r\n(다음목록 (1) / 책 검색 또는 새로운 카테고리로 보려면 (아무버튼이나 눌러주세요)) : "))
            # 검색할거랑 다음 목록 보여줄걸 하자
            if next_choice == 1:
              book_countStart += 20
              book_countEnd += 20
            else:
              print('책 검색 또는 새로운 카테고리 검색으로 갑니다.')
              break
      else:
        # 검색기능 구현
        print('검색기능')
        comment, book_name = self.product_search()

  #주어진 index를 기반으로 모든 책 검색하는 메소드 아래 검색메소드를 사용하려면 있어야 함
  def search_list(self, df_series, location, info): 
        if location == len(df_series.index):
            return [location]

        result = []
        index_limit= len(df_series.index)

        while True:
            if location > index_limit - 1: #550개이고 index는 0부터 시작하므로, 1을 빼줘야 IndexError 발생 안함!
                return result

            else:
                if df_series[location] == info:
                    result.append(location)
                    location += 1

                else:
                    return result

  #검색 메소드
  def product_search(self): #검색 메소드
      while True:
          try:
              number = int(input('이름 검색 (1) / 작가 검색 (3) / 종료 (3) : '))
              if number == 1: #이름 검색
                  book_series = self.product_df.sort_values(by=['Name'], axis=0, ascending=True, ).reset_index(inplace = False)['Name']
                  book_name = input('책 이름을 검색해주세요 : ')
                  book_location = bisect.bisect_left(book_series, book_name) #무조건 left로 해야 한다(index 초과방지 및 정확성)


                  # *추가해야 하는게 있음 --> book_name말고 book_author, book_price, book_Year 가 필요함
                  # 이정도 있으면 장바구니에 정확하게 넣을 수 있음

                  # if book_name == self.product_df.loc[book_location, 'Name']:
                  if book_name == book_series[book_location]:
                      return(f'찾으시는 {book_name} 책이 존재합니다'), book_name
                      

                      # *1 이름같은 책 목록을 전부 꺼내서 줘야 하는데 이럼 다시 분류해야함
                      # index_list = self.search_list(book_series, book_location, book_name)  #책이 복수 개면 다 출력
                      # if len(self.product_df.iloc[index_list, :]) > 1:
                      #   print(index_list) # 여기서 같은 이름의 책들의 df를 보여주면서 고르라고 해야할 거 같음
                      # print(self.product_df.iloc[index_list, :]) #책 출력

                  else:
                      return (f'{book_name} 책은 존재하지 않습니다.')

              elif number == 2: #작가 검색
                  #기존은 책 이름 기준으로 오름차순 정렬되었기 때문에 author기준으로
                  author_series = self.product_df.sort_values(by=['Author'], axis=0, ascending=True, ).reset_index(inplace = False)['Author']
                  author_name = input('작가를 검색해주세요 : ')
                  author_location = bisect.bisect_left(author_series, author_name)

                  if author_name == author_series[author_location]:
                      return(f'찾으시는 {author_name} 책이 존재합니다')

                      # *2 위와 같은 이유임
                      # index_list = self.search_list(author_series, author_location, author_name)
                      # print(self.product_df.iloc[index_list, :]) #책 출력
                  else:
                      return(f'{author_name} 작가의 존재하지 않습니다.')

              
              elif number == 3: #종료
                  print('검색을 마칩니다.') 

              else:
                  # print(err.error_alert('RangeError')) #int형 중에, 1~4 이내의 숫자만 허용
                  print('다시 입력바랍니다.\r\n이름 검색 (1) / 작가 검색 (3) / 종료 (3) 입니다.')
      
          except : 
              return('ValueError') #int 이외 값 입력되면 ValueError 처리

  # 장바구니를 먼저 만들자
  def bag_make(self):
    product_book_df = pd.DataFrame(columns=['Name', 'Author', 'User', 'Rating', 'Reviews', 'Price', 'Year', 'Genre'])
    product_book_df.to_csv(f'C:/Users/mingzzang/Desktop/bag{self.id}.csv')
 
  # 장바구니에 담자
  def bag_pack(self, book_name, book_author, book_price, book_Year):
    product_df = self.product_df
    product_user_book_df = product_df.loc[(product_df['Name'] == book_name)&(product_df['Author'] == book_author)&(product_df['Price'] == book_price)&(product_df['Year'] == book_Year)]
    # 새로운 df에 적용시켜서 그걸 파일로 만들어야해
    # 위에 만든 장바구니를 받아와서 여기다가 에펜드를 해주면 돼
    product_user_book_df.to_csv(f'C:/Users/mingzzang/Desktop/bag{self.id}.csv', mode='a', header=False)


  # 장바구니 가격 및 품목들 확인하기
    price_hab = sum(product_df['Price'].values)
    book_names = product_df['Name'].values

  # 장바구니에 담은 거 전부 삭제하기
  # 이건 내일
  # 


  # 영수증 뽑기
  # 먼저, 고객이 내는 돈에 대해 이야기하자
  def make_change(self, book_name, book_price):
    login_df = self.login_df
    # login_df = pd.read_csv("C:/Users/mingzzang/Desktop/idPw.csv")
    os.system('cls')
    nickname = login_df.loc[(login_df['id'] == self.id) & (login_df['pw'] == self.pw)]['nickname'].values[0]
    while True:
      customer_pay = int(input(f"{nickname}님께서 구입하시려는 {book_name}의 가격은 {book_price}원입니다.\r\n하실 금액을 적어주세요(단위 원) : "))
      if customer_pay < book_price:
        print(f"{nickname}님께서 지불하시려는 금액이 너무 작습니다.")
      else:
        break
    while True:
      print('------------------------------------------------------------------------------------------')
      customer_email = input(f"{nickname}님께서\r\n지불하신 {customer_pay}원과 {book_name}의 가격 {book_price}원입니다. \r\n 거스름돈은 {customer_pay - book_price}원 입니다. \r\n 영수증은 입력해주신 메일로 보내드리겠습니다. \r\n 이메일을 입력하세요 : ")
      if '@' not in customer_email:
        print(f"{nickname}님의 이메일 형식이 잘못되었습니다.")
        continue
      else:
        break
    print('------------------------------------------------------------------------------------------')
    return nickname, customer_pay, book_name, book_price, customer_email
