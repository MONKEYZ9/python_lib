page_form = """
1. 상품 구매
2. 자유 게시판
3. 종료
"""

def page_rendering():
  print(page_form)

  service_choice = input("선택 : ")

  if service_choice == '1':
    return 'product_page'

  elif service_choice == '2':
    return 'freeboard_page'

  else:
    return 'exit'