from LoginNJoin import member_Login
from LoginNJoin import member_Join
from myModule.member import Commerce6_product



def homepage_Go():
    # 로그인이 성공했을때
    login_comment, login_id, login_pw = member_Login()
    if login_comment == 'login_complete':
        # 게시판이나 상품 페이지로 f가면 되고
        product_progress = Commerce6_product(login_id, login_pw)
        comment, book_name, book_price = product_progress.product_infomation_resule()
        return comment, book_name, book_price, login_id
    else:
        # 회원가입이 진행
        join_comment, join_id, join_pw  = member_Join()
        if join_comment == "join_guest_complete":
            product_progress = Commerce6_product(join_id, join_pw)
            comment, book_name, book_price = product_progress.product_infomation_resule()
            return comment, book_name, book_price, join_id

