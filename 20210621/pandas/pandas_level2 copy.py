import pandas as pd
import numpy as np

# 임신	포도당	혈압	피부 두께	인슐린	BMI	당뇨계열 병	나이
# 0	6	148	72	35	0	33.6	0.627	50
# 내껄 넣어주고 


df = pd.read_csv('C:/Users/mingzzang/Desktop/PART17-20210621T020629Z-001/PART17/dataset/diabetes.csv', encoding='EUCKR')

# my_Info = list(input().split(', '))
# # 이상민, 0, 117, 100, 60, 45, 26, 0.3221, 35
# print(my_Info)
# # 없는 결과값을 넣어야 해
# your_info_list = my_Info + [None]
# print(my_Info)

# # 내꺼 넣어야지
# # list_series = pd.Series(data_list, index=["라면", "김치", "떡볶이", "마라탕", "볶음밥", "짬뽕"])
# # append로 하면 된다. 그냥 리스트에 추가하듯이 하면 되네
# # 내껄 넣고 싶으면 이렇게 해야함
# # df = df.append(my_Info, index)
# # new_row = pd.Series(data={'name':'Geo', 'physics':87, 'chemistry':92}, name='x')
# # #append row to the dataframe
# # df_marks = df_marks.append(new_row, ignore_index=False)
# df_names = df.columns.to_list()
# print(df_names)
# df_rows = len(df)
# print(df_rows)
# # print(len(my_Info[1:]))
# new_row = pd.Series(data=your_info_list[1:], index=df_names, name=df_rows)
# df_marks = df.append(new_row, ignore_index=False)

# # 내꺼 넣은 걸 결과 값 None을 없애고
# # # Nan을 없애주고
# # 일단 Nan값이 몇개인지 확인해보자
# print(df_marks.isnull().sum()) # 결과에 하나 있는거 보이네 이거를 중앙값으로 대체해주자
# df_marks['결과'].fillna( df_marks['결과'].median(axis=0), inplace=True )
# # df_marks

# # 중복된 것을 없애주는 작업을 하자
# drop_duplicate_df = df_marks.drop_duplicates()
# df = drop_duplicate_df

# print(drop_duplicate_df[df_names[0]]) 임신 값을 다 가져왔네

# 사분위 값을 가져와야 하잖아
# quantile(0.25) => 25% 로 생각하면서 작고 크고로 4분위값을 나타낼 수 있을거 같아
# print(drop_duplicate_df[df_names[0]].quantile(0.25))
# df_rows = len(df)
# df_cols = len(df.columns)
# df_names = df.columns.to_list()
# df = drop_duplicate_df
# medical_certificate = []
# print(type(int(my_Info[1])))
# # print(df[df_names[1]].quantile(0.25))

# medical_certificate = []

# for i in range( df_cols-1 ) :
#     if your_info_list[i+1] <= df[df_names[i]].quantile(0.25) : 
#         medical_certificate.append( "{}님의 {}항목의 경우, 전체 조사 인원 25% 이하에 속하고 있습니다.".format(your_info_list[0], df_names[i]) )
#     elif your_info_list[i+1] > df[df_names[i]].quantile(0.25) and your_info_list[i+1] <= df[df_names[i]].quantile(0.50) : 
#       medical_certificate.append( "{}님의 {}항목의 경우, 전체 조사 인원 25% 초과 50% 이하에 속하고 있습니다.".format(your_info_list[0], df_names[i]) )
#     elif your_info_list[i+1] > df[df_names[i]].quantile(0.50) and your_info_list[i+1] <= df[df_names[i]].quantile(0.75) : 
#       medical_certificate.append( "{}님의 {}항목의 경우, 전체 조사 인원 50% 초과 75% 이하에 속하고 있습니다.".format(your_info_list[0], df_names[i]) )
#     elif your_info_list[i+1] > df[df_names[i]].quantile(0.75) and your_info_list[i+1] <= df[df_names[i]].quantile(1) : 
#       medical_certificate.append( "{}님의 {}항목의 경우, 전체 조사 인원 75% 초과 100% 이하에 속하고 있습니다.".format(your_info_list[0], df_names[i]) )
#     else :
#       medical_certificate.append( "{}님의 {}항목의 경우, 4분위 수에서 확인되지 않을 정도로 낮거나 높습니다.".format(your_info_list[0], df_names[i]) )


# LV2 : 데이터를 분석해서 나의 결과와 비교해주는 함수를 만들어주세요.

# 임신	포도당	혈압	피부 두께	인슐린	BMI	당뇨계열 병	나이
# 0	6	148	72	35	0	33.6	0.627	50
def customize_analzy(df, info_list) :

    df_rows = len(df)
    df_cols = len(df.columns)
    df_names = df.columns.to_list()

    # print( df )

    medical_certificate = []

    print( "fdsdfsdsffdsdfsdfsdfsdfs", df[df_names[1]].quantile(0.25) )
    print( "fdsdfsdsffdsdfsdfsdfsdfs", df[df_names[1]].quantile(0.50) )
    print( "fdsdfsdsffdsdfsdfsdfsdfs", df[df_names[1]].quantile(0.75) )
    print( "fdsdfsdsffdsdfsdfsdfsdfs", df[df_names[1]].quantile(1) )
    # for i in range( 9 ) :

#     try :
#         # print(  df[df_names[i]].describe() )
#          print(  type(df[df_names[i]][0]) )

        
#     except :
#         print( "dfdfdfs" )

# #   for i in range( df_cols-1 ) :
# #     if info_list[i+1] <= df[df_names[i]].quantile(0.25) : 
# #       medical_certificate.append( "{}님의 {}항목의 경우, 전체 조사 인원 25% 이하에 속하고 있습니다.".format(info_list[0], df_names[i]) )
# #     elif info_list[i+1] > df[df_names[i]].quantile(0.25) and info_list[i+1] <= df[df_names[i]].quantile(0.50) : 
# #       medical_certificate.append( "{}님의 {}항목의 경우, 전체 조사 인원 25% 초과 50% 이하에 속하고 있습니다.".format(info_list[0], df_names[i]) )
# #     elif info_list[i+1] > df[df_names[i]].quantile(0.50) and info_list[i+1] <= df[df_names[i]].quantile(0.75) : 
# #       medical_certificate.append( "{}님의 {}항목의 경우, 전체 조사 인원 50% 초과 75% 이하에 속하고 있습니다.".format(info_list[0], df_names[i]) )
# #     elif info_list[i+1] > df[df_names[i]].quantile(0.75) and info_list[i+1] <= df[df_names[i]].quantile(1) : 
# #       medical_certificate.append( "{}님의 {}항목의 경우, 전체 조사 인원 75% 초과 100% 이하에 속하고 있습니다.".format(info_list[0], df_names[i]) )
# #     else :
# #       medical_certificate.append( "{}님의 {}항목의 경우, 4분위 수에서 확인되지 않을 정도로 낮거나 높습니다.".format(info_list[0], df_names[i]) )

#     return medical_certificate  
# lists = ['이상민', 0, 117, 100, 60, 45, 26, 0.3221, 35]

    # print( customize_analzy(df, ["박수아", 2, 117, 100, 60, 45, 19, 0.3493, 24]))
# df = pd.read_csv('C:/Users/mingzzang/Desktop/PART17-20210621T020629Z-001/PART17/dataset/diabetes.csv', encoding='EUCKR')
print(customize_analzy(df, ["박수아", 2, 117, 100, 60, 45, 19, 0.3493, 24]))




# print(type(df[df_names[1]].quantile(0.25, numeric_only=True)))
# if int(my_Info[1]) <= df[df_names[1]].quantile(0.25):
#     print('asdasd')
# else:
#     print('fdsfdsf')