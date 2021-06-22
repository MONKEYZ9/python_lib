# LV2 : 로또 번호 생성기
# 이건 0부터 45 에서 6개를 중복없이 빼내면 돼
import numpy as np
# print( "--넘파이 난수 생성/처리 기능 활용하기------------" )
# # 정수형 배열 생성 randint 0부터 45까지 6개를 뽑는거야
# # 로또 만들기
# np_randint = np.random.randint(0, 45, size=6)
# print( np_randint ) # 정수형 배열 생성
# # [31 27 33  1  8 30]

# unique를 가지고 나온 데이터 종류별 하나씩 가져오는 거야
# 순정값만 뺀다고 생각하면 돼
# print( np.unique(np_choice) )



# np_randint = np.random.randint(0, 45, size=6)
# print( np_randint )

def set_lottoNumber():
    # 뽑아냈는데 중복이 있을 수 있으니까
    # print(unique_lottoNumber)
    while True:
        first_lottoNumber = np.random.randint(1, 45, size=6)
        unique_lottoNumber = np.unique(first_lottoNumber)
        if len(unique_lottoNumber) == 6:
            return unique_lottoNumber
        else:
            # 만약 안되면 다시 해야지 continue해서 
            continue
        
print(set_lottoNumber())

# 로또번호 생성완료 : [20  4 16 16  1 25 17]
