import pandas as pd
import numpy as np
import os
import bisect
from csv import writer
from modules import error_catch
from texttable import Texttable


# 상품을 장르별로도 검색해볼 수는 없을까요?
# 단순히 구매하기 말고, csv 파일을 DB 처럼 활용하는 방법으로 장바구니도 구현할 수 있을것 같습니다.
class Commerce6_product :
  def __init__(self, id, nickname) :
    self.id = id
    self.nickname = nickname
    self.product_df = pd.read_csv(r".\database\product\bestsellers with categories.csv")

  # 메인 모듈
  def product_infomation_resule(self) :
    product_df = self.product_df

    # 장바구니 생성
    self.bag_make()

    # 전체 책 고르는거
    while True :
      first_customer_choice = int(input("카테고리별로 보려면 (1) / 책을 직접 찾으려면 (아무버튼이나 눌러주세요) : "))
      
      # 책을 카테고리별 목록으로 본다면
      if first_customer_choice == 1:

        # 처음 책 목록의 갯수는 20개
        book_countStart = 0
        book_countEnd = 10

        # 카테고리별 목록으로 검색
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
        
        # 카테고리별 목록을 늘려가면서 보여줘야 하니까
        while True:
          # 터미널 클리어
          os.system('cls')

          # 데이터의 총 갯수는 502개로 확인
          if book_countStart == 520:
            book_countEnd = 547

          books_list_table = Texttable()
          books_list_table.set_cols_width([4, 50, 10, 5, 8, 8, 4, 11])
          books_list_table.set_cols_dtype(["t", "t", "t", "t", "t", "t", "t", "t"])
          books_list_table_rows = [['No', 'Title', 'Author', 'Rate', 'Reviews', 'Price', 'Year', 'Genre']]
          for i in range( book_countStart, book_countEnd ) :
            book_info = [i+1]
            for j in range( len(product_df.columns) ) :
              if j == 4 :
                book_info.append(f"{format(product_df.loc[i][j]*1000, ',')}원")
              else :
                book_info.append(str(product_df.loc[i][j]))
            books_list_table_rows.append(book_info)
          books_list_table.add_rows(books_list_table_rows)
          print(books_list_table.draw())

          # 해당 목록에 맘에 드는 책이 없을때
          next_list = int(input("찾으시는 책이 있으신가요?\r\n(있다면 (1) / 없다면 아무버튼이나 눌러주세요) : "))
          if next_list == 1:
            choice_product_booknumber = int(input("구매하실 서적 번호를 입력 : "))

            print( f"{self.nickname} 님, 구매 신청하신 서적은 {product_df.loc[choice_product_booknumber-1][0]} 입니다.")
            print( f"가격은 {product_df.loc[choice_product_booknumber][4]*1000} 원입니다.")
            
            book_choice_df = product_df.loc[choice_product_booknumber-1]
            book_name = book_choice_df.to_dict()['Name']
            book_author = book_choice_df.to_dict()['Author']
            book_price = book_choice_df.to_dict()['Price'].item()
            book_Year = book_choice_df.to_dict()['Year'].item()

            choice_product_bookorder = int(input("바로 구매하시나요?\r\n(바로 구매 (1) / 장바구니에 담기 (아무버튼이나 눌러주세요)) : "))
            if choice_product_bookorder == 1 :
              # 바로 결제하고 구매 진행
              print("결제처리 진행 중")

              # 콘솔 지우기
              os.system('cls')

              # 바로 구매시, 필요한 값들 리턴해주기 --> 이메일 부분으로 넘어감
              return book_name, book_price
            else:
              # 터미널 클리어
              os.system('cls')
              # 장바구니에 담기
              self.bag_pack(book_name, book_author, book_price, book_Year)
              # 장바구니에 있는 물품 확인하기
              price_hab, book_names = self.bag_check()
              print(f'{self.nickname}님의 장바구니에 담긴 책 목록은 {book_names} 입니다.')
              print(f'{self.nickname}님의 장바구니에 담긴 책 목록의 총 가격은 {price_hab * 1000}원 입니다.')
              bag_order = int(input("장바구니에 담긴 책 목록을 구매하시겠습니까?\r\n(바로 구매 (1) / 다른 책 목록 검색하기 (아무버튼이나 눌러주세요)) : "))
              if bag_order == 1:
                return book_names, price_hab
              else:
                break
          else:
            next_choice = int(input("다음 목록으로 갈까요?\r\n(다음목록 (1) / 책 검색 또는 새로운 카테고리로 보려면 (아무버튼이나 눌러주세요)) : "))
            # 검색할거랑 다음 목록 보여줄걸 하자
            if next_choice == 1:
              book_countStart += 10
              book_countEnd += 10
            else:
              print('책 검색 또는 새로운 카테고리 검색으로 갑니다.')
              break
      else:
        # 검색기능 구현
        print('검색기능')
        search_df = self.product_search()
        book_name = search_df.values.tolist()[0][0]
        book_author = search_df.values.tolist()[0][1]
        book_price = search_df.values.tolist()[0][2]
        book_Year = search_df.values.tolist()[0][3]

        choice_product_bookorder = int(input("바로 구매하시나요?\r\n(바로 구매 (1) / 장바구니에 담기 (아무버튼이나 눌러주세요)) : "))

        if choice_product_bookorder == 1 :
          # 바로 결제하고 구매 진행
          print("결제처리 진행 중")

          # 콘솔 지우기
          os.system('cls')

          # 바로 구매시, 필요한 값들 리턴해주기 --> 이메일 부분으로 넘어감
          return book_name, book_price

        else:
          # 터미널 클리어
          os.system('cls')
          # 장바구니에 담기
          self.bag_pack(book_name, book_author, book_price, book_Year)
          # 장바구니에 있는 물품 확인하기
          price_hab, book_names = self.bag_check()
          print(f'{self.nickname}님의 장바구니에 담긴 책 목록은 {book_names} 입니다.')
          print(f'{self.nickname}님의 장바구니에 담긴 책 목록의 총 가격은 {price_hab * 1000}원 입니다.')
          bag_order = int(input("장바구니에 담긴 책 목록을 구매하시겠습니까?\r\n(바로 구매 (1) / 다른 책 목록 검색하기 (아무버튼이나 눌러주세요)) : "))
          if bag_order == 1:
            return book_names, price_hab
          else:
            pass

  # 장바구니를 먼저 만들자
  def bag_make(self):
    product_book_df = pd.DataFrame(columns=['Name', 'Author', 'Rating', 'Reviews', 'Price', 'Year', 'Genre'])
    product_book_df.to_csv(f'./database/purchase/bag_{self.id}.csv')
 
  # 장바구니에 담자
  def bag_pack(self, book_name, book_author, book_price, book_Year):

    # 해당 장바구니 파일을 열고 적어주자
    product_df = self.product_df
    product_user_book_df = product_df.loc[(product_df['Name'] == book_name)&(product_df['Author'] == book_author)&(product_df['Price'] == book_price)&(product_df['Year'] == book_Year)]
    user_book = product_user_book_df.values.tolist()
    user_book_list = [0]

    for i in range(7):
      user_book_list.append(user_book[0][i])

    with open(f'./database/purchase/bag_{self.id}.csv', 'a', newline='') as f:
      writer_object = writer(f)
      writer_object.writerow(user_book_list)
      f.close()

  def product_detail_search(self):
        column_dict = { 
                        1 : ['User Rating' , '(0~5점까지)'],
                        2 : ['Reviews' , '(숫자 입력)'], 
                        3 : ['Price' , '($)'],
                        4 : ['Year' , '(연도 입력)'],
                        5 : ['Genre' , '(Fiction or Non Fiction)']
                      }
        choice = list(map(int, input('1) 유저 평점, 2) 리뷰 수, 3) 가격, 4) 연도, 5)장르 (최대 3개까지 고르세요 ex.1 2 3)').split()))
        product_condition = []
        for idx, c in enumerate(choice, start = 1):
            if c in column_dict:
                if c < 5:
                    while True:
                        value = list(map(float, input(f'{idx}) {column_dict[c][0]} {column_dict[c][1]} (~로 범위 지정) : ').split('~')))
                        if len(value) == 2:
                            break
                        print('다시 입력해주세요.') #예외처리
                elif c == 5:
                    while True:
                        value = input(f'{idx}) {column_dict[c][0]} {column_dict[c][1]}: ') #5번 예외처리
                        if value in ['Fiction', 'Non Fiction']:
                            break
                        print('다시 입력해주세요.')
                product_condition.append([column_dict[c][0], value])
        tmp_df = self.product_df
        for i in range(len(product_condition)):
            if product_condition[i][0] == 'Genre':
                tmp_df = tmp_df[tmp_df["Genre"] == f'{product_condition[i][1]}']
            else:
                tmp_df = tmp_df[(tmp_df[f"{product_condition[i][0]}"] >= product_condition[i][1][0]) & (tmp_df[f"{product_condition[i][0]}"] <= product_condition[i][1][1])]
        if len(tmp_df) == 0:
            print('조건에 만족하는 상품이 없습니다...', end='\n\n')
            return  
        print('요청하신 조건에 대한 결과입니다')
        tmp_df = tmp_df.loc[:, ['Name', 'Author', 'Price', 'Year']]
        print(tmp_df, end='\n\n') #최종 출력
        return tmp_df

  #주어진 index를 기반으로 모든 책 검색하는 메소드      
  def search_list(self, df_series, location, info): #주어진 index를 기반으로 모든 책 검색하는 메소드
      index_limit= len(df_series.index) - 1 #550개이고 index는 0부터 시작하므로, 1을 빼줘야 IndexError 발생 안함!
      if location == index_limit:
          return [location]
      result = []
      while True:
          if location > index_limit: 
              return result
          else:
              if df_series[location] == info:
                  result.append(location)
                  location += 1
              else:
                  return result
  #검색 메소드
  def product_search(self): 
      while True:
          try:
              number = int(input('1) 이름 검색 2) 작가 검색 3) 상세 검색 4) 종료 : '))

              if number == 1: #이름 검색
                  book_series = self.product_df.sort_values(by=['Name'], axis=0, ascending=True, ).reset_index(inplace = False)['Name']
                  book_name = input('책 이름을 검색해주세요 : ')
                  book_location = bisect.bisect_left(book_series, book_name) #무조건 left로 해야 한다(index 초과방지 및 정확성)
                  # if book_name == self.product_df.loc[book_location, 'Name']:
                  if book_location < len(book_series) and book_name == book_series[book_location]:
                      print(f'찾으시는 {book_name} 책이 존재합니다')
                      index_list = self.search_list(book_series, book_location, book_name)  #책이 복수 개면 다 출력
                      search_completed = self.product_df.loc[index_list, ['Name', 'Author', 'Price', 'Year']]
                      print(search_completed)
                      return search_completed
                  else:
                      print(f'{book_name} 책은 존재하지 않습니다.', end='\n\n')
              #작가 검색
              elif number == 2:
                  #기존은 책 이름 기준으로 오름차순 정렬되었기 때문에 author기준으로
                  author_df = self.product_df.sort_values(by=['Author'], axis=0, ascending=True, ).reset_index(inplace = False) #author에 대한 새 df필요
                  author_series = author_df['Author']
                  author_name = input('작가를 검색해주세요 : ')
                  author_location = bisect.bisect_left(author_series, author_name)
                  if author_location < len(author_series) and author_name == author_series[author_location]:
                      print(f'찾으시는 {author_name} 작가의 책이 존재합니다')
                      index_list = self.search_list(author_series, author_location, author_name)
                      search_completed = author_df.loc[index_list, ['Name', 'Author', 'Price', 'Year']]
                      print(search_completed)
                      return search_completed
                  else:
                      print(f'{author_name} 작가의 책이 존재하지 않습니다.', end='\n\n')
              elif number == 3:
                  self.product_detail_search()
              elif number == 4: #종료
                  print('검색을 마칩니다.')
                  return False 
              else:
                  print(err.error_alert('RangeError')) #int형 중에, 1~4 이내의 숫자만 허용
          except ValueError: 
              print(err.error_alert('ValueError')) #int 이외 값 입력되면 ValueError 처리

  # 장바구니 가격 및 품목들 확인하기
  def bag_check(self):
    product_user_book_df = pd.read_csv(f'./database/purchase/bag_{self.id}.csv')
    price_hab = sum(product_user_book_df['Price'].values)
    book_names = product_user_book_df['Name'].values
    return price_hab, book_names

  # 영수증 뽑기
  # 먼저, 고객이 내는 돈에 대해 이야기하자
  def make_change(self, book_name, book_price):
    os.system('cls')
    while True:
      customer_pay = int(input(f"{self.nickname}님께서 구입하시려는 {book_name}의 가격은 {book_price * 1000}원입니다.\r\n하실 금액을 적어주세요(단위 원) : "))
      if customer_pay < book_price:
        print(f"{self.nickname}님께서 지불하시려는 금액이 너무 작습니다.")
      else:
        break
    while True:
      print('------------------------------------------------------------------------------------------')
      customer_email = input(f"{self.nickname}님께서\r\n지불하신 {customer_pay}원과 {book_name}의 가격 {book_price * 1000}원입니다. \r\n 거스름돈은 {customer_pay - (book_price*1000)}원 입니다. \r\n 영수증은 입력해주신 메일로 보내드리겠습니다. \r\n 이메일을 입력하세요 : ")
      if '@' not in customer_email:
        print(f"{self.nickname}님의 이메일 형식이 잘못되었습니다.")
        continue
      else:
        break
    print('------------------------------------------------------------------------------------------')
    return customer_pay, customer_email
