import pandas as pd
import matplotlib.pyplot as plt


plt.plot([0, 1, 2, 3, 4], [20, 34, 54, 10, 66])
# 키 벨류 형식으로 해서 들어가는거야

plt.title("Welcome matplotlib")
plt.xlabel("index")
plt.ylabel("value")
# plt.show()



df = pd.read_csv('C:/Users/mingzzang/Desktop/20210617/PART17-20210621T020629Z-001/PART17/dataset/commerce.csv', encoding='unicode_escape')
print(df)

print('-------------------------------------------------------')
print('-------------------------------------------------------')
# 날짜를 자르고 봐야 조금 편하다는 거야
df['parse_InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
# 년월일로 쪼개
df['year_InvoiceDate'] = df['parse_InvoiceDate'].dt.year
df['month_InvoiceDate'] = df['parse_InvoiceDate'].dt.month
df['day_InvoiceDate'] = df['parse_InvoiceDate'].dt.day

# 이름을 지정해주고 하면 '혈압' 이딴식으로 부르지 않아도 된다는 말이야
# df_rows = len(df)
# df_cols = len(df.columns)
# df_names = df.columns.to_list()

print(df)

print('-------------------------------------------------------')
print('-------------------------------------------------------')

import numpy as np
import warnings

warnings.filterwarnings(action='ignore')
# 총 5개를 만들거야 nrows=5, ncols=1 5행 1열로 보여준다는거야
figure, ((ax1), (ax2), (ax3), (ax4), (ax5)) = plt.subplots(nrows=5, ncols=1)
# 2행 3열로 하고 싶다면
# figure, ((ax1), (ax2)) ((ax3), (ax4)) ((ax5) (ax6)) = plt.subplots(nrows=2, ncols=3)
figure.set_size_inches(20, 35) #사이즈


# 교안에 안나와있을거임
# 그룹으로 묶는거야 groupby('year_InvoiceDate')
# groupby('year_InvoiceDate').UnitPrice.sum() 연도 옆에 있는 유닛가격을 합산해줬어
year_InvoiceDate_sum = df.groupby('year_InvoiceDate').UnitPrice.sum()
print(year_InvoiceDate_sum)
# 2010    2.605209e+05
# 2011    2.238283e+06
# groupby 된 변수의 키와 벨류를 다 넣어주고 
ax1.plot(year_InvoiceDate_sum.index, year_InvoiceDate_sum.values)
# 그래프를 그리면 항목값을 바꿔주는거야
ax1.set_xticks(np.unique(df["year_InvoiceDate"]))
# 순정값만 뽑아주는거야 그렇게 그림을 구성
plt.show()

# # 이거는 월별로 구분하는거야
# month_InvoiceDate_sum = df.groupby('month_InvoiceDate').UnitPrice.sum()
# # ax2.scatter(month_InvoiceDate_sum.index, month_InvoiceDate_sum.values)
# # autopct='%0.2f%%' 소수점 나타내주는거야
# ax2.pie( month_InvoiceDate_sum.values, labels=month_InvoiceDate_sum.index, autopct='%0.2f%%' )
# ax2.set_xticks(np.unique(df["month_InvoiceDate"]))
# # 파이차트로 보는거야
# # plt.show()

# # 나라로 구분하는거야
# Country_sum = df.groupby('Country').UnitPrice.sum()
# # ax3.pie(Country_sum.values, labels = Country_sum.index, autopct='%0.2f%%')
# ax3.scatter(Country_sum.index, Country_sum.values)
# # 라벨 바꾸려고 하는거야
# ax3.set_xticklabels(np.unique(df["Country"]), rotation=45 )
# # plt.show()

# # 막대 그래프로 찍을건데 
# CustomerID_sum = df.groupby('CustomerID').UnitPrice.sum()
# ax4.bar(CustomerID_sum.index, CustomerID_sum.values)
# # plt.show()

# # 사분위수
# ax5.boxplot(df['UnitPrice'])
# # 금액이 4분위수 안에서 놀아
# # plt.show()

# # --------------------------------------------------------------------------------------
# # 한 그래프에서 여러 선을 보여주기

# # year_InvoiceDate_sum.index, year_InvoiceDate_sum.values
# unique_customerid = np.unique(df['CustomerID'])
# # 유니크를 씀으로 중복을 없애고
# color_sharp = ['r.', 'b.', 'y.', 'm.', 'g.', 'k.', 'c.']
# # 모양을 미리 지정하는걸

# plt.figure(figsize=(15, 10))

# for i in range( 6 ) :
#   plt.plot( df[(df['CustomerID'] == unique_customerid[i])].month_InvoiceDate, alpha=0.7)
#   # plt.plot( df[(df['CustomerID'] == 17850.0)].month_InvoiceDate, 'r.' )
#   # plt.plot( df[(df['CustomerID'] == 12680.0)].month_InvoiceDate, 'b.' )

# plt.legend(unique_customerid[0:6])
# # plt.show()


# # -----------------------------------------------------------------------------------

# plt.figure(figsize=(20,10))
# df.boxplot()
# # boxplot을 정리를 다시 하자!!
# # plt.show()

# # -----------------------------------------------------------------------------

# import seaborn as sns


# sns.jointplot(x="month_InvoiceDate", y="UnitPrice", data=df.loc[0:300])
# #                                                              loc으로 해서 끊어놨는데 안끊으면 뻗어 오래걸려
# # 밑에 제목 달았다.
# plt.suptitle("month_InvoiceDate & UnitPrice Joint Plot", y=1.02)
# # plt.show()

# # -----------------------------------------------------------------------------
# # 페어 플롯은 더 느려
# sns.pairplot(df.loc[0:100])
# plt.title("Ecommerce Data Pair Plot")
# plt.show()

# # -----------------------------------------------------------------------------






