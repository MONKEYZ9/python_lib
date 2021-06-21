import numpy as np
from numpy.lib.function_base import delete
# 1차원 배열을 만들거임
print( "--1차원 배열 선언 + 데이터 타입 변경------------" )
array_1d = np.array([8, 2, 2, 5, 9, 10, 13, 3], dtype=float)
print( array_1d )
print( "-----------------------------------------" )


print( "--2차원 배열 선언 + 데이터 타입 변경------------" )
array_2d = np.array([(1,2,3), (4,5,6), (7,8,9)], dtype=float)
print( array_2d )
print( "-----------------------------------------" )


print( "--다차원 배열 선언 + 무작위 값 삽입-------------" )
array_2d_empty = np.empty([3, 3])
# 3 * 3 3개 행 3개 열로 만들어 놓겠다는 거야
print( array_2d_empty )
print( "-----------------------------------------" )
print( "np.zeros() / np.ones()" )
print( "-----------------------------------------" )

print( "--넘파이에서 데이터를 정렬하기------------------" )
print( np.sort(array_1d))
print( "-----------------------------------------" )
print( "-----------------------------------------" )

print( "--넘파이와 넘파이를 결합하기--------------------" )
np_tmp = np.array([3, 8, 10, 5, 9, 99]) #방금 생성한거랑 위에 1차원 배열을 합칠거임
np_concat = np.concatenate([array_1d, np_tmp]) # concatenate 이라는 거로 한다는거야 pandas에도 있음 데이터를 결합할때 쓰임
# 이게 update라고 하는거야
print( np_concat )
print( "-----------------------------------------" )
print( "-----------------------------------------" )
# CRUD에서 돈다는 거야
# create, read, update, delete를 하는거야
# mysql을 위주로 하겠네
print( "--넘파이에서 '99' 값 제거하기------------------" )
np_concat_data_delete = np.delete(np_concat, [-1]) #delete를 불러서 배열을 가져와야 한다는거야
# 그리고 위치를 넣어야 해, -1은 마지막에 있는걸 지우는거야


print( np_concat_data_delete )
print( "-----------------------------------------" )
print( "-----------------------------------------" )