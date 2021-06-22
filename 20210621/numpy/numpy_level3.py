# LV3 : 데이터셋의 정보를 손쉽게 찾아주는 메소드를 제작합니다.
# # 이거 정리하고 기억하기
# print( "--넘파이 계산/통계 기능 활용하기------------" )
# print( np_data_reshape )
# print( np_data_reshape.sum() )
# print( np_data_reshape.max() )
# print( np_data_reshape.min() )
# print( np_data_reshape.mean() ) #평균
# print( np_data_reshape.std() ) #표준편차

# 데이터 합계, 최대값, 최소값, 평균, 표준편차를 뽑아내고
# 데이터를 셔플링해서
# 셔플링한 데이터를 어느 정도 슬라이스 해서
# 다시 그 작업을 반복한다.

# 먼저, 데이터를 읽어오자
from sys import path_hooks
import numpy as np

# 'C:/Users/mingzzang/Desktop/PART12-20210621T000404Z-001/PART12/dataset/wine.csv'
def make_dataSet(path):
    wine_data = np.loadtxt(path, delimiter=",", dtype=np.float32)
    # print( wine_data )
    # 읽어온 와인 데이터를 정리해보자
    # 만약 고정산도를 구하고 싶으면 뒤집어야 해
    wine_data_transform = wine_data.T
    print('와인 고정산도를 보면 {}'.format(wine_data_transform[0]))
    print('와인 고정 산도의 합계는 {}'.format(wine_data_transform[0].sum()))
    print('와인 고정 산도의 최대값은 {}'.format(wine_data_transform[0].max()))
    print('와인 고정 산도의 최소값은 {}'.format(wine_data_transform[0].min()))
    print('와인 고정 산도의 평균값은 {}'.format(wine_data_transform[0].mean()))
    print('와인 고정 산도의 표준편차는 {}'.format(wine_data_transform[0].std()))


    print('그럼 나눠서 가보자')


    while True:
        q = int(input('진행하려면 1을, 중단하려면 2를 눌러주세요 : '))
        if q == 1:
            index_slicing = int(input('데이터 범위를 입력해주세요 : '))
            print('와인 고정산도를 보면 {}'.format(wine_data_transform[0][0:index_slicing]))
            print('와인 고정 산도의 합계는 {}'.format(wine_data_transform[0][0:index_slicing].sum()))
            print('와인 고정 산도의 최대값은 {}'.format(wine_data_transform[0][0:index_slicing].max()))
            print('와인 고정 산도의 최소값은 {}'.format(wine_data_transform[0][0:index_slicing].min()))
            print('와인 고정 산도의 평균값은 {}'.format(wine_data_transform[0][0:index_slicing].mean()))
            print('와인 고정 산도의 표준편차는 {}'.format(wine_data_transform[0][0:index_slicing].std()))
            break
        elif q == 2:
            print('데이터 산출 과정을 중단합니다.')
            break
        else:
            print('진행하려면 1을, 중단하려면 2를 누르셔야 합니다.')
            continue


path_input = input('읽어올 파일의 경로를 넣어주세요 : ')
make_dataSet(path_input)