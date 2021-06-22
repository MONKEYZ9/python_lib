# LV2 : 데이터를 분석해서 나의 결과와 비교해주는 함수를 만들어주세요.

# 임신	포도당	혈압	피부 두께	인슐린	BMI	당뇨계열 병	나이
# 0	6	148	72	35	0	33.6	0.627	50

# Attributes:
#     [성명, 임신횟수, 포도당 수치, 혈압 수치, 피부두께, 인슐린, BMI, 당뇨계열 합병증 위험도, 나이](list) : 원하는 퍼센트를 정수형태로 삽입해주세요. (50, 10, 90)

#   Example:
#     ["나호용", 0, 117, 100, 60, 45, 26, 0.3221, 35]

#   Result:
#     ['나호용님의 임신항목의 경우, 전체 조사 인원 25% 이하에 속하고 있습니다.',
#     '나호용님의 포도당항목의 경우, 전체 조사 인원 25% 초과 50% 이하에 속하고 있습니다.',
#     '나호용님의 혈압항목의 경우, 전체 조사 인원 75% 초과 100% 이하에 속하고 있습니다.',
#     '나호용님의 피부 두께항목의 경우, 전체 조사 인원 75% 초과 100% 이하에 속하고 있습니다.',
#     '나호용님의 인슐린항목의 경우, 전체 조사 인원 50% 초과 75% 이하에 속하고 있습니다.',
#     '나호용님의 BMI항목의 경우, 전체 조사 인원 25% 이하에 속하고 있습니다.',
#     '나호용님의 당뇨계열 병항목의 경우, 전체 조사 인원 25% 초과 50% 이하에 속하고 있습니다.',
#     '나호용님의 나이항목의 경우, 전체 조사 인원 50% 초과 75% 이하에 속하고 있습니다.'] (list)

#   Todo:
#     * 데이터의 공백(NaN)과 중복을 제거할 수 있는 기능을 추가해주세요.
# 이상민, 0, 117, 100, 60, 45, 26, 0.3221, 35

import pandas as pd

my_Info = list(input().split(', '))
# print(type(my_Info)) <class 'list'>
json_df = pd.read_json('C:/Users/mingzzang/Desktop/indian_diabetes.json')
print('json 읽어올거임')
print(json_df)

# 임신 뭐시기 뭐시기를 하나의 배열에 넣어서 숫자로 불러올수 있게
df_names = json_df.columns.to_list()
print(len(df_names))
# 행을 번호로 불러와보자
df_rows = len(json_df)
print(len(my_Info[1:])) # 결과 값이 없어서 지금 배열 갯수가 안맞아 결과 값으로 하나 넣어줘야 겠다
# json_df['나이'].fillna( json_df['나이'].median(axis=0), inplace=True )
json_df['결과'].fillna( json_df['결과'].median(axis=0), inplace=True )

# 내껄 넣어주고
# 아직 내껄 안넣었네 ㅋㅋㅋㅋ
# json_df_addInfo = pd.Series(my_Info[1:], index=df_names)
# print(my_Info[1:])
# list_series = pd.Series(data_list, index=["라면", "김치", "떡볶이", "마라탕", "볶음밥", "짬뽕"])

# # Nan을 없애주고
# for i in range(len(df_names)):
#     json_df_addInfo.dropna(subset=[df_names[i]], how='any', axis=0)
# # unique해서 중복된거 없애보자
# drop_df = json_df_addInfo.drop_duplicates()
# # 중복된거 없앴으니까 다시 해야 하지 않을까?
# df_len_rows = len(drop_df)

# # 이렇게 하고 쫙 정리해야지
# # # 판다스 통계
# # print( json_df.mean() )
# # print( "-----------------------------------------" )
# # print( json_df.median() ) #중앙값
# # print( "-----------------------------------------" )
# # print( json_df.max() )
# # print( "-----------------------------------------" )
# # print( json_df.min() )
# # print( "-----------------------------------------" )
# # print( json_df.std() ) #표준편차
# # print( "-----------------------------------------" )
# # print( json_df.corr() ) # 48:10초 쯤에 있을 수 있어
# # print(drop_df[df_drop_names[0]])
# for i in range(len(df_names)):
#     print(drop_df[df_names[i]])
#     print('--------------------------------')

