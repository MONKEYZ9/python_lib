# LV1 : 데이터셋에 빈 값이 존재합니다. 
# 확률적인 분포(백분율) 을 기반으로 데이터셋을 새롭게 생성하세요!
import numpy as np
# np_texts = ['A', 'B', 'C', 'D', 'E']
# np_choice = np.random.choice(np_texts, 7, p=[0.1, 0, 0.3, 0.6, 0])
# print(np_choice)

# 자 데이터셋에 빈 값을 존재하게끔 만들어 보자
def make_dataSet():
    data_list = []
    percent_list = []
    # 데이터 리스트에 값을 에펜드 해주자(5가지로 해주자)
    # 몇 개의 데이터로 할건지 정하자
    menu_num = int(input('오늘 저녁 메뉴 몇개 설정할까? : '))
    for i in range(menu_num):
        data = input("오늘의 저녁 메뉴는 뭐로 먹고 싶어? : {}순위 ".format(i+1))
        data_list.append(data)
        percent = float(input("적어주신 메뉴의 확률을 적어주세요(총합은 1입니다.) : "))
        percent_list.append(percent)
    data_num = int(input('몇개의 데이터를 뽑아서 볼껴? : '))
    # print(data_list)
    # p로 확률 정해줄때 합이 1이 되어야 해
    return np.random.choice(data_list, data_num, p=percent_list)
print(make_dataSet())

# 확률 정해주고 
# 랜덤하게 그걸 뽑아내주는


# 좋아하는 음식을 입력해주세요 (1순위) : 라면
# 좋아하는 음식을 입력해주세요 (2순위) : 돈가스
# 좋아하는 음식을 입력해주세요 (3순위) : 김밥
# array(['라면', '라면', '돈가스', '라면', '돈가스', '돈가스', '돈가스'], dtype='<U3')
