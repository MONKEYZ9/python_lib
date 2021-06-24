from myModule.member import Commerce6_member
from myModule.product import Commerce6_product
from myModule.mail import Commerce6_productMail

class MemberController:
    def progress_member():
        member_progress = Commerce6_member()
        id, pw = member_progress.homepage_Go()
        return id, pw

class ProductController:
    def progress_product(id, pw):
        product_progress = Commerce6_product(id, pw)
        book_name, book_price = product_progress.product_infomation_resule()
        nickname, customer_pay, book_name, book_price, customer_email = product_progress.make_change(book_name, book_price)
        return nickname, customer_pay, book_name, book_price, customer_email

class EmailController:
    def mailToCustomer(nickname, customer_pay, book_name, book_price, customer_email):
        mail_customer_progress = Commerce6_productMail(nickname, customer_pay, book_name, book_price, customer_email)
        mail_customer_progress.send_mail()

