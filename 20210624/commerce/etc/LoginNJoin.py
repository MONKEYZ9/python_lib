from myModule.member import Commerce6_login
from myModule.member import Commerce6_product

def member_Login():
    login_progress = Commerce6_login()
    login_comment, login_id, login_pw = login_progress.login_doit()
    return login_comment, login_id, login_pw

def member_Join():
    print('login_fail')
    # 회원가입
    login_progress = Commerce6_login()
    join_comment, join_id, join_pw  = login_progress.join_guest()
    return join_comment, join_id, join_pw

