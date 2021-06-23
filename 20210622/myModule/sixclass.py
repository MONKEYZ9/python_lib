# Class Descriptions
# Name / Age / Gender / Phone Numbers / kWh

import smtplib
from email.mime.text import MIMEText

class Six_Class :

  def __init__(self, name, age, gender, phone, kWh, email) :
    self.name = name
    self.age = age
    self.gender = gender
    self.phone = phone
    self.kWh = kWh
    self.email = email

  def name_age(self) :
    return "안녕하세요, {}({}세) 고객님. 스마트 전기 고지서를 보내드립니다.".format(self.name, self.age)

  def age_gender(self) :
    return "{}세 / {} 이신 고객님의 전기 사용량({}kWh)은 비슷한 연령대 고객님들보다 높습니다.".format(self.age, self.gender, self.kWh)

  def gender_phone(self) :
    return "{} 고객님 연락하신 휴대번호 {} 로 스마트 이체를 강제로 신청해 드리겠습니다.".format(self.name, self.phone)

  def kWh_email(self) :
    kWb_based_fare = 0
    ct = ''

    # 기본 요금 계산
    if self.kWh <= 100 :
      kWb_based_fare += 390
    elif self.kWh >= 101 and self.kWh <= 200 :
      kWb_based_fare += 850
    elif self.kWh >= 201 and self.kWh <= 300 :
      kWb_based_fare += 1500
    elif self.kWh >= 301 and self.kWh <= 400 :
      kWb_based_fare += 3590
    elif self.kWh >= 401 and self.kWh <= 500 :
      kWb_based_fare += 6750
    elif self.kWh > 500 :
      kWb_based_fare += 11980

    # 전력량 요금
    if self.kWh <= 50 :
      kWb_based_fare += self.kWh * 34.5
      self.kWh = 0
    else :
      kWb_based_fare += 50 * 34.5
      self.kWh -= 50

    if self.kWh <= 50 :
      kWb_based_fare += self.kWh * 81.7
      self.kWh = 0
    else :
      kWb_based_fare += 50 * 81.7
      self.kWh -= 50

    if self.kWh <= 100 :
      kWb_based_fare += self.kWh * 122.9
      self.kWh = 0
    else :
      kWb_based_fare += 100 * 122.9
      self.kWh -= 100

    if self.kWh <= 100 :
      kWb_based_fare += self.kWh * 177.7
      self.kWh = 0
    else :
      kWb_based_fare += 100 * 177.7
      self.kWh -= 100

    if self.kWh <= 100 :
      kWb_based_fare += self.kWh * 308
      self.kWh = 0
    else :
      kWb_based_fare += 100 * 308
      self.kWh -= 100

    if self.kWh <= 100 :
      kWb_based_fare += self.kWh * 405.7
      self.kWh = 0
    else :
      kWb_based_fare += 100 * 405.7
      self.kWh -= 100

    kWb_based_fare += self.kWh * 639.4
    
    self.kWh -= self.kWh

    auto_dc = (kWb_based_fare - ( kWb_based_fare * 0.3223 / 1.0323 )) * 0.01
    VAT = (kWb_based_fare - ( kWb_based_fare * 0.3223 / 1.0323 ) - auto_dc) * 0.1

    result_cost = kWb_based_fare + VAT - auto_dc
  
    return "{} 고객님 금월 우리 계좌로 이체 해주셔야 하는 금액은 {} 원입니다. 안내시면 고발합니다.".format(self.name, format(int(result_cost), ",") )

  def send_mail(self) : 

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()

    s.login(self.email, 'nqgkhcchbzamgkxe')

    txt = "{}\n{}\n{}\n{}".format(self.name_age(), self.age_gender(), self.gender_phone(), self.kWh_email())
    msg = MIMEText(txt)
    msg['Subject'] = '[광주인공지능] 스마트 전기고지서'
  
    s.sendmail(self.email, "sangmin3285@gmail.com", msg.as_string()) # 보내는 이메일 / 받는 이메일
    s.quit()