import pandas as pd
import numpy as np

# print( "--CSV 불러오기 + 판다스 시리즈 선언-------------" )
# csv = pd.read_csv('C:/Users/mingzzang/Desktop/PART17-20210621T020629Z-001/PART17/dataset/Historical Product Demand.csv', index_col = 0, squeeze = True) 
# # 구문 분석된 데이터에 열이 하나만 포함되어 있으면 영상 시리즈를 반환합니다.

# # 파일을 불러올때 어떤 형식의 파일을 불러오는건 상관없이 부를 수 있어
# # csv = pd.read_pickle 데이터 압축한거 불러올때
# # csv = pd.read_excel 엑셀 불러올때

# series = pd.Series( csv )
# # 시리즈는 보통 키 옆에 벨류가 있어 그런걸 잘 할 수 있다는 거야
# print( series )
# print( "-----------------------------------------" )
# # Product_Code
# # Product_0993     100
# # Product_0979     500
# # Product_0979     500
# # Product_0979     500
# # Product_0979     500
# #                 ...
# # Product_0021    1500
# # Product_0033    1000
# # Product_0033    1000
# # Product_0021    1000
# # Product_0033    1500
# # Name: Order_Demand, Length: 12738, dtype: int64
# # -----------------------------------------

# # 시리즈는 워드클라우드 단어 수 셀때 많이 씀

# # 시리즈를 뜯어보자
# print( "----------------시리즈 데이터 삽입(리스트) -------------------------" )
# data_list = [3000, 40000, 5000, 7000, 10000, 10000]
# list_series = pd.Series(data_list, index=["라면", "김치", "떡볶이", "마라탕", "볶음밥", "짬뽕"])
# print(list_series)
# print( "-----------------시리즈 데이터 처리(리스트) -------------------------" )
# print( list_series[[3]] ) # 슬라이싱 한거야 세번째꺼만 찍어올리는 거야
# print( "-----------------------------------------" )
# print( list_series[[0, 1, 2]] )
# print( "-----------------------------------------" )
# # 조금 다르네 
# print( list_series[0:3] )
# # 텍스트 인덱스 값으로 자를 수 있다.
# print( list_series["라면":"볶음밥"] )
# print( "-----------------------------------------" )
# print( list_series.index )
# print( list_series.values )
# print( "-----------------------------------------" )
# print( "----------------시리즈 데이터 삽입(튜플) -------------------------" )
# data_tuple = (3000, 40000, 5000, 7000, 10000, 10000)
# tuple_series = pd.Series(data_tuple, index = ["라면", "김치", "떡볶이", "마라탕", "볶음밥", "짬뽕"])
# print(tuple_series)
# print( "-----------------시리즈 데이터 처리(튜플) -------------------------" )
# print( tuple_series[[3]] ) # 슬라이싱 한거야 세번째꺼만 찍어올리는 거야
# print( "-----------------------------------------" )
# print( tuple_series[[0, 1, 2]] )
# print( "-----------------------------------------" )
# # 조금 다르네 
# print( tuple_series[0:3] )
# # 텍스트 인덱스 값으로 자를 수 있다.
# print( tuple_series["라면":"볶음밥"] )
# print( "-----------------------------------------" )
# print( tuple_series.index )
# print( tuple_series.values )
# print( "-----------------------------------------" )
# print( "-----------------시리즈 데이터 처리(dict) -------------------------" )
# # 인덱스만 지정해주면 돼 이미 값은 있으니까
# print( tuple_series )
# print( "-----------------------------------------" )
# data_dic = {"라면" : 3000, "김치" : 40000}
# dict_series = pd.Series( data_dic ) #dict은 바로 집어넣을 수 있다는 것
# print( tuple_series )
# print( "-----------------------------------------" )
# # --------------------------------------------------------------------------------------------
# print( "--데이터프레임 데이터 삽입 --------------------" )
# # 행, 열, 2차원 이상의 데이터
# tuple_data = ((6, 148, 72), (1, 85, 66))
# print( pd.DataFrame(tuple_data, columns=["임신", "포도당", "혈압"]) )



# ------------------------------------ 위 아래로 주석 풀어서 사용할 것-----------------------------------------
df = pd.read_csv('C:/Users/mingzzang/Desktop/PART17-20210621T020629Z-001/PART17/dataset/diabetes.csv', encoding='EUCKR')
# ------------------------------------ 위 아래로 주석 풀어서 사용할 것-----------------------------------------


# print( type(df) )

# print( "-----------------------------------------" )
# print(df) #데이터 프레임을 찍어보는거

# print( df["혈압"] ) # 원하는 열을 하나 뽑아보고
# # 0      72
# # 1      66
# # 2      64
# # 3      66
# # 4      40
# #        ..
# # 763    76
# # 764    70
# # 765    72
# # 766    60
# # 767    70
# # Name: 혈압, Length: 768, dtype: int64
# print('--------------------------------')
# print( df.인슐린 ) # 이렇게도 가능하다
# # 0        0
# # 1        0
# # 2        0
# # 3       94
# # 4      168
# #       ...
# # 763    180
# # 764      0
# # 765    112
# # 766      0
# # 767      0
# # Name: 인슐린, Length: 768, dtype: int64
# print('--------------------------------')
# print(df.BMI)
# print('--------------------------------')
# print( df[["혈압", "인슐린", "BMI"]]) #이런식으로 내가 원하는대로 나눌 수 있어
# # 나중에 데이터 셋을 나눠야 하는 경우가 올때 독립변수랑 종속변수를 나눌때 사용할 수 있게 돼
# #  혈압  인슐린   BMI
# # 0    72    0  33.6
# # 1    66    0  26.6
# # 2    64    0  23.3
# # 3    66   94  28.1
# # 4    40  168  43.1
# # ..   ..  ...   ...
# # 763  76  180  32.9
# # 764  70    0  36.8
# # 765  72  112  26.2
# # 766  60    0  30.1
# # 767  70    0  30.4

# # [768 rows x 3 columns]
# print('--------------------------------')
# print('--------------------------------')
# # loc과 iloc의 차이?
# # # loc은 label을 이용해서 값을 선택
# # iloc은 integer position(정수형 위치 index)를 이요하여 값을 선택
print(df.loc[0:5])
#    임신  포도당  혈압  피부 두께  인슐린   BMI  당뇨계열 병  나이  결과
# 0   6  148  72     35    0  33.6   0.627  50   1
# 1   1   85  66     29    0  26.6   0.351  31   0
# 2   8  183  64      0    0  23.3   0.672  32   1
# 3   1   89  66     23   94  28.1   0.167  21   0
# 4   0  137  40     35  168  43.1   2.288  33   1
# 5   5  116  74      0    0  25.6   0.201  30   0
print('--------------------------------')
print('--------------------------------')
print('--------------------------------')
print(df.iloc[0:5]) # 0, 5 니까 0이랑 5가 찍히는 걸 볼 수 있어
# --------------------------------
#    임신  포도당  혈압  피부 두께  인슐린   BMI  당뇨계열 병  나이  결과
# 0   6  148  72     35    0  33.6   0.627  50   1
# 1   1   85  66     29    0  26.6   0.351  31   0
# 2   8  183  64      0    0  23.3   0.672  32   1
# 3   1   89  66     23   94  28.1   0.167  21   0
# 4   0  137  40     35  168  43.1   2.288  33   1
print(df.iloc[[0, 5]]) # 0, 5 니까 0이랑 5가 찍히는 걸 볼 수 있어
#    임신  포도당  혈압  피부 두께  인슐린   BMI  당뇨계열 병  나이  결과
# 0   6  148  72     35    0  33.6   0.627  50   1
# 5   5  116  74      0    0  25.6   0.201  30   0

# print('--------------------------------')
# print('--------------------------------')
# print('--------------------------------')

# print(df.set_index("결과")) #인덱스를 뭐로 잡냐가 달라진다는 거야
# print(df.set_index("BMI")) #인덱스를 뭐로 잡냐가 달라진다는 거야

# print('--------------------------------')
# print('--------------------------------')
# print('--------------------------------')

# print(df.loc[[0], ["임신", "혈압", "인슐린", "나이", "결과"]])
# # loc[인뎃스], [열, 열... ]
# # 임신	혈압	인슐린	나이	결과
# # 0	6	72	0	50	1
# # 0번째 환자의  임신 혈압 인슐린 나이 결과 어떤지 보고 싶은거야

# print('--------------------------------')
# print('--------------------------------')
# print('--------------------------------')

# print(df.loc[[0, 5, 415, 600], ["나이"]])
# # 0, 5, 415, 600번째 환자들의 나이를 알고 싶을때

# print('--------------------------------')
# print('--------------------------------')
# print('--------------------------------')

# df.loc[0] = [6, 148, 72, 35, 0, 33.6, 0.627, 55, 1]
# # 새롭게 만든 데이터를 0번째에 넣었어
# # head, tail 등등 있어
# print(df.head(3)) #위에서 3가지만 가져오겠다
# #    임신  포도당  혈압  피부 두께  인슐린   BMI  당뇨계열 병  나이  결과
# # 0   6  148  72     35    0  33.6   0.627  55   1
# # 1   1   85  66     29    0  26.6   0.351  31   0
# # 2   8  183  64      0    0  23.3   0.672  32   1
# print(df.tail(3))
# #      임신  포도당  혈압  피부 두께  인슐린   BMI  당뇨계열 병  나이  결과
# # 765   5  121  72     23  112  26.2   0.245  30   0
# # 766   1  126  60      0    0  30.1   0.349  47   1
# # 767   1   93  70     31    0  30.4   0.315  23   0
# print('--------------------------------')
# print('--------------------------------')
# print('--------------------------------')

# 나이로 정렬을 했고 ascending = False하게 되면 내림차순으로 높은 숫자부터 나오게 돼
# print('나이로 내림차순 하기')
sort_df = df.sort_values('나이', ascending=False) # 내림차순
# print(sort_df)
# #      임신  포도당  혈압  피부 두께  인슐린   BMI  당뇨계열 병  나이  결과
# # 459   9  134  74     33   60  25.9   0.460  81   0
# # 453   2  119   0      0    0  19.6   0.832  72   0
# # 666   4  145  82     18    0  32.5   0.235  70   1
# # 684   5  136  82      0    0   0.0   0.640  69   0
# # 123   5  132  80      0    0  26.8   0.186  69   0
# # ..   ..  ...  ..    ...  ...   ...     ...  ..  ..
# # 240   1   91  64     24    0  29.2   0.192  21   0
# # 136   0  100  70     26   50  30.8   0.597  21   0
# # 382   1  109  60      8  182  25.4   0.947  21   0
# # 392   1  131  64     14  415  23.7   0.389  21   0
# # 271   2  108  62     32   56  25.2   0.128  21   0

# print('나이로 오름차순 하기')
# sort_df = df.sort_values('나이', ascending=True) # 오름차순
# # print(sort_df)
# print('--------------------------------')
# print('--------------------------------')
# print('--------------------------------')

# drop으로 임신이랑 포도당
# axis=1 ==========================================>>>>>>>?
# axis=1은 세로로 그래프를 적용하겠다는거야
# 만약 drop을 하고 싶은데 4행과 19행을 없애고 싶어?
# drop_sort_df = sort_df.drop([4, 19], axis=0)

drop_sort_df = sort_df.drop(['임신', '포도당'], axis=1)
print(drop_sort_df)
# 이러면 임신과 포도당을 날리는 거야

print('--------------------------------')
print('--------------------------------')
print('--------------------------------')


# 값을 내보낼때
df.to_json('C:/Users/mingzzang/Desktop/indian_diabetes.json')
# vscode 파일 정렬은 ctrl + k + f를 눌러 주면 된다.

# json을 읽어올때
json_df = pd.read_json('C:/Users/mingzzang/Desktop/indian_diabetes.json')
print('json 읽어올거임')
# ------------------------------------ 아래로 주석 풀어서 JSON 형식 가져오는거 확인해라-------------------------
# print(json_df)

# # 판다스 통계
# print( json_df.mean() )
# print( "-----------------------------------------" )
# print( json_df.median() ) #중앙값
# print( "-----------------------------------------" )
# print( json_df.max() )
# print( "-----------------------------------------" )
# print( json_df.min() )
# print( "-----------------------------------------" )
# print( json_df.std() ) #표준편차
# print( "-----------------------------------------" )
# print( json_df.corr() ) # 48:10초 쯤에 있을 수 있어
# # 상관관계 표를 보여주는거야
# # 인과관계는 99 ~100 프로 원인되었다고 볼 수 있어
# # 관계에 대한걸 이야기하는데 2번째 녹음 51초까지 다시 들어봐라
# print( "-----------------------------------------" )
# print( json_df.info() )
# # 값을 맞춰주고 행값을 전부다 정확하게 맞춰줘야 한다는 거야
# # 지금은 결집체가 없어서?
# # 그래서 768로 나와
# # 케글이나 이런거 하게 되면 결집체가 있는게 있어?
# # 공모전같은거 하게 되면 있어
# # 결집체가 많으면 열을 제거해야 할 필요가 있다는 거야
# # 데이터 타입도 확인 할 수 있어
# # int와 float 형태 다양하게 확인 할 수 있다.

# # <class 'pandas.core.frame.DataFrame'>
# # Int64Index: 768 entries, 0 to 767
# # Data columns (total 9 columns):
# #  #   Column  Non-Null Count  Dtype
# # ---  ------  --------------  -----
# #  0   임신      768 non-null    int64
# #  1   포도당     768 non-null    int64
# #  2   혈압      768 non-null    int64
# #  3   피부 두께   768 non-null    int64
# #  4   인슐린     768 non-null    int64
# #  5   BMI     768 non-null    float64
# #  6   당뇨계열 병  768 non-null    float64
# #  7   나이      768 non-null    int64
# #  8   결과      768 non-null    int64
# # dtypes: float64(2), int64(7)
# # memory usage: 60.0 KB
# # None
# print( "-----------------------------------------" )
# print( json_df.describe() )
# # 이거 하나면 다 해결 가능해 
# # 사분위값을 볼 수 있어
# # 사분위값을 보통 언제 쓰냐면
# # 전국 아파트 매매가를 비교해서 저렴이냐 비싼거냐를 볼 수 있어
# # -----------------------------------------
# #                임신         포도당          혈압       피부 두께         인슐린         BMI      당뇨계열 병          나이          결과
# # count  768.000000  768.000000  768.000000  768.000000  768.000000  768.000000  768.000000  768.000000  768.000000
# # mean     3.845052  120.894531   69.105469   20.536458   79.799479   31.992578    0.471876   33.247396    0.348958
# # std      3.369578   31.972618   19.355807   15.952218  115.244002    7.884160    0.331329   11.770901    0.476951
# # min      0.000000    0.000000    0.000000    0.000000    0.000000    0.000000    0.078000   21.000000    0.000000
# # 25%      1.000000   99.000000   62.000000    0.000000    0.000000   27.300000    0.243750   24.000000    0.000000
# # 50%      3.000000  117.000000   72.000000   23.000000   30.500000   32.000000    0.372500   29.000000    0.000000
# # 75%      6.000000  140.250000   80.000000   32.000000  127.250000   36.600000    0.626250   41.000000    1.000000
# # max     17.000000  199.000000  122.000000   99.000000  846.000000   67.100000    2.420000   81.000000    1.000000
# print( "-----------------------------------------" )
# print('--------------------------------')   
# print('--------------------------------')

# # BMI가 32가 나온 사람이 몇명일까 라는 걸 찾고 싶을때 하는거야
# # print(json_df['BMI'].value_counts(dropna=False))
# # dropna는 결집체를 없애는 거래
# # -----------------------------------------
# # 32.0    13
# # 31.2    12
# # 31.6    12
# # 0.0     11
# # 33.3    10
# #         ..
# # 19.3     1
# # 49.3     1
# # 19.4     1
# # 20.0     1
# # 40.1     1
# # Name: BMI, Length: 248, dtype: int64
# ------------------------------------ 위로로 주석 풀어서 JSON 형식 가져와서 확인하는 걸 다시 확인해라-------------------------

json_df.loc[0] = [6, 148, 72, 35, 0, 33.6, 0.627, None, 1]
# 지금 결집체를 만들었어
# null값을 넣었자나
print(json_df['BMI'].value_counts(dropna=False))
print(json_df.isnull().sum())
# null값이 몇개인지 알려주는 거야

print('--------------------------------')
print('--------------------------------')   
print('--------------------------------')

# 열 중에서, 100개 넘으면 열 제거하기
print(json_df.dropna(axis=1, thresh=100))
# null값이 100개보다 많으면 날리겠다는거야
# 근데 그런게 없으니까 그대로 있을거야
# 바로 아래 BMI에 NaN이 있어

#      임신  포도당  혈압  피부 두께  인슐린   BMI  당뇨계열 병    나이  결과
# 0     6  148  72     35    0  33.6   0.627   NaN   1
# 1     1   85  66     29    0  26.6   0.351  31.0   0
# 2     8  183  64      0    0  23.3   0.672  32.0   1
# 3     1   89  66     23   94  28.1   0.167  21.0   0
# 4     0  137  40     35  168  43.1   2.288  33.0   1
# ..   ..  ...  ..    ...  ...   ...     ...   ...  ..
# 763  10  101  76     48  180  32.9   0.171  63.0   0
# 764   2  122  70     27    0  36.8   0.340  27.0   0
# 765   5  121  72     23  112  26.2   0.245  30.0   0
# 766   1  126  60      0    0  30.1   0.349  47.0   1
# 767   1   93  70     31    0  30.4   0.315  23.0   0

print('--------------------------------')
print('--------------------------------')
print('--------------------------------')

# 나이에서 NaN 이 있는 경우 데이터 제거
print(json_df.dropna(subset=['나이'], how='any', axis=0))
#      임신  포도당  혈압  피부 두께  인슐린   BMI  당뇨계열 병    나이  결과
# 1     1   85  66     29    0  26.6   0.351  31.0   0
# 2     8  183  64      0    0  23.3   0.672  32.0   1
# 3     1   89  66     23   94  28.1   0.167  21.0   0
# 4     0  137  40     35  168  43.1   2.288  33.0   1
# 5     5  116  74      0    0  25.6   0.201  30.0   0
# ..   ..  ...  ..    ...  ...   ...     ...   ...  ..
# 763  10  101  76     48  180  32.9   0.171  63.0   0
# 764   2  122  70     27    0  36.8   0.340  27.0   0
# 765   5  121  72     23  112  26.2   0.245  30.0   0
# 766   1  126  60      0    0  30.1   0.349  47.0   1
# 767   1   93  70     31    0  30.4   0.315  23.0   0

# [767 rows x 9 columns] !!!!!!!!!!!!!!!!!!!!!!!!!!여길 봐야해 널값이 껴있는 행을 날렸어 [768 rows x 9 columns] 이거였었어

print('--------------------------------')
print('--------------------------------')
print('--------------------------------')

# 나이에서 NaN 이 있는 경우 데이터 제거
json_df.loc[0] = [6, 148, 72, 35, 0, 33.6, 0.627, None, 1]
print(json_df)
#      임신  포도당  혈압  피부 두께  인슐린   BMI  당뇨계열 병    나이  결과
# 0     6  148  72     35    0  33.6   0.627   NaN   1
# 1     1   85  66     29    0  26.6   0.351  31.0   0
# 2     8  183  64      0    0  23.3   0.672  32.0   1
# 3     1   89  66     23   94  28.1   0.167  21.0   0
# 4     0  137  40     35  168  43.1   2.288  33.0   1
# ..   ..  ...  ..    ...  ...   ...     ...   ...  ..
# 763  10  101  76     48  180  32.9   0.171  63.0   0
# 764   2  122  70     27    0  36.8   0.340  27.0   0
# 765   5  121  72     23  112  26.2   0.245  30.0   0
# 766   1  126  60      0    0  30.1   0.349  47.0   1
# 767   1   93  70     31    0  30.4   0.315  23.0   0

# [768 rows x 9 columns]


json_df['나이'].fillna( json_df['나이'].median(axis=0), inplace=True )
# 위에 None값을 중앙값으로 채울거야
# inplace는 채운다는 거같아
# axis가 뭐야?

print(json_df)
#      임신  포도당  혈압  피부 두께  인슐린   BMI  당뇨계열 병    나이  결과
# 0     6  148  72     35    0  33.6   0.627  29.0   1
# 1     1   85  66     29    0  26.6   0.351  31.0   0
# 2     8  183  64      0    0  23.3   0.672  32.0   1
# 3     1   89  66     23   94  28.1   0.167  21.0   0
# 4     0  137  40     35  168  43.1   2.288  33.0   1
# ..   ..  ...  ..    ...  ...   ...     ...   ...  ..
# 763  10  101  76     48  180  32.9   0.171  63.0   0
# 764   2  122  70     27    0  36.8   0.340  27.0   0
# 765   5  121  72     23  112  26.2   0.245  30.0   0
# 766   1  126  60      0    0  30.1   0.349  47.0   1
# 767   1   93  70     31    0  30.4   0.315  23.0   0

# [768 rows x 9 columns]

print('--------------------------------')
print('--------------------------------')
print('--------------------------------')

json_df.loc[0] = [1, 85, 66, 29, 0, 26.6, 0.351, 31.0, 0]
json_df.loc[1] = [1, 85, 66, 29, 0, 26.6, 0.351, 31.0, 0]
json_df.loc[2] = [1, 85, 66, 29, 0, 26.6, 0.351, 31.0, 0]

# 추천같은 것을 할때
# 사람이 세명이 있을때, 한 사람한테 동일한 것을 배분될 때가 있어
# 상품명이 A, B, C로 나뉘어야 하는데 A A A로 하면 중복되는데
# 중복된 데이터를 제거할때 쓰는 것
print('----------duplicate------')
print(json_df)
drop_df = json_df.drop_duplicates()
# 파일을 빼낼땐 변수 선언을 해서 빼는 것이 좋다
print(drop_df.to_csv)

print('--------------------------------')
print('--------------------------------')
# 런타임 초기화 -> 다시 시작 및 모두 실행
# !sudo apt-get install -y fonts-nanum
# !sudo fc-cache -fv
# !rm -/.

# 주피터에서 할 때 이걸 해야 경고메세지를 무시 할 수 있때
# import warnings
# warnings.filterwarnings(action='ignore')

import missingno as msno
msno.matrix(json_df, figsize=(12,5))

import matplotlib.pyplot as plt
# 외부 IDE로 할 땐 이게 무조건 
# ----------------- 이거는 vscode로는 볼 수 없나?

print('--------------------------------')
print('--------------------------------')
print('--------------------------------')

# 날짜 데이터
commerce_df = pd.read_csv('C:/Users/mingzzang/Desktop/PART17-20210621T020629Z-001/PART17/dataset/commerce.csv', encoding='unicode_escape')
print(commerce_df)

print('--------------------------------')
print('--------------------------------')
print('--------------------------------')

commerce_df['parse_InvoiceDate'] = pd.to_datetime(commerce_df['InvoiceDate'])
# colum을 하나 만들거임 이렇게 해서 만들거임
# 이건 무조건 해보자 
# to_datetime 파이썬 datetime이라고 기본 라이브러리를 가지고 사용해서 InvoiceDate를 쪼개달라고 하고 쪼갠거야
print(commerce_df)

#     InvoiceNo StockCode                          Description  Quantity      InvoiceDate  UnitPrice  CustomerID         Country
# 0         536365    85123A   WHITE HANGING HEART T-LIGHT HOLDER         6   12/1/2010 8:26       2.55     17850.0  United Kingdom
# 1         536365     71053                  WHITE METAL LANTERN         6   12/1/2010 8:26       3.39     17850.0  United Kingdom
# 2         536365    84406B       CREAM CUPID HEARTS COAT HANGER         8   12/1/2010 8:26       2.75     17850.0  United Kingdom
# 3         536365    84029G  KNITTED UNION FLAG HOT WATER BOTTLE         6   12/1/2010 8:26       3.39     17850.0  United Kingdom
# 4         536365    84029E       RED WOOLLY HOTTIE WHITE HEART.         6   12/1/2010 8:26       3.39     17850.0  United Kingdom
# ...          ...       ...                                  ...       ...              ...        ...         ...             ...
# 541904    581587     22613          PACK OF 20 SPACEBOY NAPKINS        12  12/9/2011 12:50       0.85     12680.0          France
# 541905    581587     22899         CHILDREN'S APRON DOLLY GIRL          6  12/9/2011 12:50       2.10     12680.0          France
# 541906    581587     23254        CHILDRENS CUTLERY DOLLY GIRL          4  12/9/2011 12:50       4.15     12680.0          France
# 541907    581587     23255      CHILDRENS CUTLERY CIRCUS PARADE         4  12/9/2011 12:50       4.15     12680.0          France
# 541908    581587     22138        BAKING SET 9 PIECE RETROSPOT          3  12/9/2011 12:50       4.95     12680.0          France

# [541909 rows x 8 columns]
# --------------------------------
# --------------------------------
# --------------------------------
#        InvoiceNo StockCode                          Description  Quantity  ... UnitPrice  CustomerID         Country   parse_InvoiceDate
# 0         536365    85123A   WHITE HANGING HEART T-LIGHT HOLDER         6  ...      2.55     17850.0  United Kingdom 2010-12-01 08:26:00   
# 1         536365     71053                  WHITE METAL LANTERN         6  ...      3.39     17850.0  United Kingdom 2010-12-01 08:26:00   
# 2         536365    84406B       CREAM CUPID HEARTS COAT HANGER         8  ...      2.75     17850.0  United Kingdom 2010-12-01 08:26:00   
# 3         536365    84029G  KNITTED UNION FLAG HOT WATER BOTTLE         6  ...      3.39     17850.0  United Kingdom 2010-12-01 08:26:00   
# 4         536365    84029E       RED WOOLLY HOTTIE WHITE HEART.         6  ...      3.39     17850.0  United Kingdom 2010-12-01 08:26:00   
# ...          ...       ...                                  ...       ...  ...       ...         ...             ...                 ...   
# 541904    581587     22613          PACK OF 20 SPACEBOY NAPKINS        12  ...      0.85     12680.0          France 2011-12-09 12:50:00   
# 541905    581587     22899         CHILDREN'S APRON DOLLY GIRL          6  ...      2.10     12680.0          France 2011-12-09 12:50:00   
# 541906    581587     23254        CHILDRENS CUTLERY DOLLY GIRL          4  ...      4.15     12680.0          France 2011-12-09 12:50:00   
# 541907    581587     23255      CHILDRENS CUTLERY CIRCUS PARADE         4  ...      4.15     12680.0          France 2011-12-09 12:50:00   
# 541908    581587     22138        BAKING SET 9 PIECE RETROSPOT          3  ...      4.95     12680.0          France 2011-12-09 12:50:00   

# [541909 rows x 9 columns]

# 이렇게 달라진다는거야
print('--------------------------------')
print('--------------------------------')
print('--------------------------------')

# 년월일을 쪼개고 데이터를 어디서 가져올지 정해야 해
# .을 찍는 순간 dt가 나오고 .를 또 찍게 되면 세부적으로 볼 수 있다는 거야
commerce_df['year_InvoiceDate'] = commerce_df['parse_InvoiceDate'].dt.year
commerce_df['month_InvoiceDate'] = commerce_df['parse_InvoiceDate'].dt.month
commerce_df['day_InvoiceDate'] = commerce_df['parse_InvoiceDate'].dt.day
commerce_df['hour_InvoiceDate'] = commerce_df['parse_InvoiceDate'].dt.hour

print( commerce_df['parse_InvoiceDate'].dt.year )
print( commerce_df['parse_InvoiceDate'].dt.month )
print( commerce_df['parse_InvoiceDate'].dt.day )
print(commerce_df['parse_InvoiceDate'].dt.hour)

print(commerce_df)

print('--------------------------------')
print('--------------------------------')
print('--------------------------------')


# 내가 원하는 데이터만 뽑아오는 거야
# 쿼리 작업이랑 같다는 거야
print(commerce_df[ (commerce_df['year_InvoiceDate'] == 2011) & (commerce_df['CustomerID'] == 13313.0) ])
print('--------------------------------')
print('--------------------------------')
print('--------------------------------')
print(commerce_df[ (commerce_df['month_InvoiceDate'] == 1) & (commerce_df['day_InvoiceDate'] == 4) & (commerce_df['CustomerID'] == 13313.0) ])