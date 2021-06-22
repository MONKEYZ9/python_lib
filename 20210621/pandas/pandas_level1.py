import pandas as pd
import numpy as np
from sklearn.utils import shuffle as sf



# def set_dataList():
#     df = pd.read_csv('C:/Users/mingzzang/Desktop/PART17-20210621T020629Z-001/PART17/dataset/diabetes.csv', encoding='EUCKR')
#     df_rows = len(df)
#     df_cols = len(df.columns)
#     df_names = df.columns.to_list()
#     df2 = sf(df)
#     # print(df_rows)
#     # print(df_cols)
#     # print(df_names)
#     percents = int(input())
#     percent = percents / 100
#     # train_x = df[df_names[0:-1]].loc[0:df_rows]
#     train_y = df2[df_names[-1]].loc[0:df_rows * percent]
#     # print(train_x)
#     # print(train_y)
#     return train_y
# print(set_dataList())

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html
#       * 여기서 데이터가 한쪽으로 치우쳐 분류되는 것을 방지하기 위해 데이터 섞는 방법 하나 추가해주세요.
# https://stackoverflow.com/questions/29576430/shuffle-dataframe-rows
# sklearn으로 셔플링 가능

df = pd.read_csv('C:/Users/mingzzang/Desktop/PART17-20210621T020629Z-001/PART17/dataset/diabetes.csv', encoding='EUCKR')
df = sf(df)
print(df)
df_names = df.columns.to_list()
df_rows = len(df)
train_x = df[df_names[0:-1]].iloc[0:df_rows]
# train_x = df[df_names[0:-1]].loc[0:df_rows] 이거로 하게 될 경우 이하로 포함해서 안된다...
# train_x = df[df_names[0:-1]].loc[0:df_rows-1] 이거로 하게 될 경우 된다
# 셔플 된걸 이제 퍼센트로 해서 뽑아 쓰자
percents = int(input('몇 %로 할 것인지 확인해주세요 : '))
percent = percents / 100
train_y = df[df_names[0:-1]].iloc[0:int(df_rows * percent)]
print(train_y)