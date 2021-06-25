import os
from modules.error_catch import ErrorDetect as err
from pages import login_page, product_page, index_page, freeboard_page

service_page = 'login_page'
user_info = None

while True:
  os.system('cls')
  if service_page == 'login_page':
    service_page, user_info = login_page.page_rendering()
    continue

  elif service_page == 'login_page_rangeError':
    print(err.error_alert('RangeError'))
    service_page, user_info = login_page.page_rendering()
    continue

  elif service_page == 'login_page_valueError':
    print(err.error_alert('ValueError'))
    service_page, user_info = login_page.page_rendering()
    continue

  elif service_page == 'index_page':
    service_page = index_page.page_rendering()
    continue

  elif service_page == 'product_page':
    service_page = product_page.page_rendering(user_info.id, user_info.nickname)
    continue
  
  elif service_page == 'freeboard_page':
    service_page = freeboard_page.page_rendering()
    continue
  
  else:
    break