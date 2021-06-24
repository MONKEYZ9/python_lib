from myModule.controller import MemberController
from myModule.controller import ProductController
from myModule.controller import EmailController

id, pw = MemberController.progress_member()
nickname, customer_pay, book_name, book_price, customer_email = ProductController.progress_product(id, pw)
EmailController.mailToCustomer(nickname, customer_pay, book_name, book_price, customer_email)