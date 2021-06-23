from myModule.member import Commerce6_login
from myModule.member import Commerce6_product
def member_LoginNJoin():
    login_progress = Commerce6_login()
    login_comment, login_id, login_pw = login_progress.login_doit()
    if login_comment == 'login_complete':
        # 게시판이나 상품 페이지로 가면 되고
        product_progress = Commerce6_product(login_id, login_pw)
        comment, book_name, book_price = product_progress.product_infomation_resule()
        return(comment)
    else:
        print('login_fail')
        # 회원가입
        login_progress = Commerce6_login()
        join_comment, join_id, join_pw  = login_progress.join_guest()
        if join_comment == "join_guest_complete":
            product_progress = Commerce6_product(join_id, join_pw)
            comment, book_name, book_price = product_progress.product_infomation_resule()
            return comment, book_name, book_price
        else:
            member_LoginNJoin()

comment = []
comment.append(member_LoginNJoin())
print(comment)