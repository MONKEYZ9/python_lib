from modules import product, mail

def page_rendering(user_id, user_nickname):
  user_product = product.Commerce6_product(user_id, user_nickname)
  book_name, book_price = user_product.product_infomation_resule()
  customer_pay, customer_email = user_product.make_change(book_name, book_price)
  mail.Commerce6_productMail(user_nickname, customer_pay, book_name, book_price, customer_email).send_mail()
  return 'index_page'