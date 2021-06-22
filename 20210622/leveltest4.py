# Q4 파이썬 Pre 내용을 활용한 전기 고지서 프로그램 만들기
from myModule.sixclass import Six_Class 

electric_bill = Six_Class("박선호", 44, "여성", "010-3233-1133", 332, "sangmingsang@likelion.org")
# print(electric_bill.age_gender())
# print(electric_bill.send_mail())
# print(electric_bill.kWh_email())
electric_bill.send_mail()