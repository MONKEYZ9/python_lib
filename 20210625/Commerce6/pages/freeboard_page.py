import os
import time
import pandas as pd
from texttable import Texttable
from modules import freeboard

page_form = """
글 읽기(r) / 글 작성(c) / 돌아가기(b) / 종료(q)
"""

content_form = """
글 수정(u) / 글 삭제(x) / 돌아가기(b)
"""

def borad_content_rendering(content_df):
  os.system('cls')
  single_bord = Texttable()
  single_bord.set_deco(Texttable.HEADER)
  title = content_df['title'].values[0]
  content = content_df['content'].values[0]
  single_bord.add_rows([["제목 : ", title],["내용 : ", content]])
  print(single_bord.draw())
  print(content_form)
  
  service_choice = input("선택 : ")
  if service_choice == 'u':
    update_title = input("제목 : ")
    update_content = input("내용 : ")
    freeboard.update_content(content_df['number'].values[0], update_title, update_content)
    return 'update'
  elif service_choice == 'x':
    freeboard.delete_content(content_df['number'].values[0])
    return 'delete'
  else:
    return 'back'

def page_rendering():
  display_df = freeboard.get_display_df()
  freeboard_table_colums = ["번호", "제목", "생성 날짜"]
  freeboard_table_rows = display_df.values.tolist()

  freeboard_table_rows.insert(0, freeboard_table_colums)
  
  freeboard_table = Texttable()
  freeboard_table.add_rows(freeboard_table_rows)
  print(freeboard_table.draw())
  
  print(page_form)

  service_choice = input("선택 : ")

  if service_choice == 'r':
    select_index = int(input("글 번호 : "))
    
    while True:
      select_df = freeboard.read_content(select_index)
      if select_df.size == 0:
        print("선택하신 번호의 글이 없습니다.")
        time.sleep(1)
        break
      response = borad_content_rendering(select_df)

      if response == 'update':
        continue
      break
    
    return 'freeboard_page'

  elif service_choice == 'c':
    create_title = input("제목 : ")
    create_content = input("내용 : ")
    freeboard.create_content(create_title, create_content)
    return 'freeboard_page'
  
  elif service_choice == 'b':
    return 'index_page'

  elif service_choice == 'q':
    return 'exit'
  else:
    return 'index_page'