import smtplib
from email.mime.text import MIMEText

class Commerce6_productMail :

  def __init__(self, nickname, customer_pay, book_name, book_price, email) :
    self.nickname = nickname
    self.customer_pay = customer_pay
    self.book_name = book_name
    self.book_price = book_price
    self.email = email

  def name_receipt(self) :
    return f"안녕하세요, {self.nickname} 고객님. 스마트 영수증 보내드립니다."

  def book_Info(self) :
    return " {} 고객님께서 구입하신 책은 {}입니다.".format(self.nickname, self.book_name)

  def book_receipt(self):
    change = self.customer_pay-self.book_price
    return "지불하신 금액 : {}\n {}의 가격은 {} \n 거스름돈 {} 입니다. ".format(self.customer_pay, self.book_name, self.book_price, change)

  def send_mail(self) :
    try :
      s = smtplib.SMTP('smtp.gmail.com', 587)
      s.starttls()

      s.login('sangmingsang@likelion.org', 'nqgkhcchbzamgkxe')

      txt = "{}\n{}\n{}\n 감사합니다 \n 광주인공지능 올림".format(self.name_receipt(), self.book_Info(), self.book_receipt())
      msg = MIMEText(txt)
      msg['Subject'] = '[광주인공지능] 스마트 영수증'
    
      s.sendmail(self.email, self.email, msg.as_string()) # 보내는 이메일 / 받는 이메일
      s.quit()
      print('{}로 스마트 영수증을 발송했습니다.'.format(self.email))
    except:
      print('{}메일 발송하는데에 오류가 발생했습니다.'.format(self.email))
