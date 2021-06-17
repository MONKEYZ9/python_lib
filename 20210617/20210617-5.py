# -*- coding: utf-8 -*-

# LV5 : 메모장에 새로운 텍스트를 확인하고, 추가할 수 있는 함수 제작

# 결과 
# 기존 텍스트 :  ['2019년에도 한반도를 둘러싼 가장 중요한 외교안보 화두는 북한의 비핵화입니다', ' 극적인 반전의 해였던 2018년에 만들어 낸 전반적인 기조가 큰 변화 없이 이어질 것이라는 전망이 많습니다', ' 좀 더 구체적으로 말하면 핵이나 미사일 도발이 재개될 가능성 보다는 지루한 협상과정이 이어질 가능성이 높아 보입니다', ' 조심스런 낙관의 근거는 김정은 위원장의 신년사와 그에 대한 트럼프의 화답입니다', ' 가장 중요한 변수는 2차 북-미 정상회담이 언제 열리느냐에 달려 있을 것 같습니다', ' 폼페이오 국무장관과 김영철 부위원장 간에 구축된 고위급 협상라인이 사실상 개점 휴업상태이고, 실무채널인 비건-최선희 라인은 아예 가동조차 되지 않고 있습니다', ' 김정은은 신년사에서 다시 한번 트럼프 대통령에게 러브콜을 보냈고, 트럼프도 “만남을 고대하고 있다”고 했습니다', ' 하지만 두 정상의 만남에 대한 기대감은 지난해 6월 1차 정상회담 때에 비해 급속히 떨어져 있는 상황입니다', '● 여전한 친서외교 극과 극일 것 같은 두 사람의 ‘케미’가 괜찮다는 것은 익히 알려진 사실입니다', ' 그 중심에는 두 사람 간에 오간 친서가 있습니다', ' 김정은 위원장이 보내서 공개된 것만 6통이구요, 트럼프 대통령은 3통의 편지를 보낸 것으로 확인됐습니다', ' 물론 지난해 6월 정상회담을 취소하겠다는 내용이 담겼던 트럼프 대통령의 공식 서한은 제외합니다', '트럼프 대통령은 대한민국 정부와 성공적인 회담을 이뤄냈습니다', '트럼프는 미국 대통령이다', '트럼프는 미국 대통령이다트럼프는 대통령이다', '트럼프는 한국을 좋아한다', '한국정부와 미국정부', '']
# 추가할 텍스트 입력 : 한반도는 행복합니다.
# 기존 텍스트 :  ['2019년에도 한반도를 둘러싼 가장 중요한 외교안보 화두는 북한의 비핵화입니다', ' 극적인 반전의 해였던 2018년에 만들어 낸 전반적인 기조가 큰 변화 없이 이어질 것이라는 전망이 많습니다', ' 좀 더 구체적으로 말하면 핵이나 미사일 도발이 재개될 가능성 보다는 지루한 협상과정이 이어질 가능성이 높아 보입니다', ' 조심스런 낙관의 근거는 김정은 위원장의 신년사와 그에 대한 트럼프의 화답입니다', ' 가장 중요한 변수는 2차 북-미 정상회담이 언제 열리느냐에 달려 있을 것 같습니다', ' 폼페이오 국무장관과 김영철 부위원장 간에 구축된 고위급 협상라인이 사실상 개점 휴업상태이고, 실무채널인 비건-최선희 라인은 아예 가동조차 되지 않고 있습니다', ' 김정은은 신년사에서 다시 한번 트럼프 대통령에게 러브콜을 보냈고, 트럼프도 “만남을 고대하고 있다”고 했습니다', ' 하지만 두 정상의 만남에 대한 기대감은 지난해 6월 1차 정상회담 때에 비해 급속히 떨어져 있는 상황입니다', '● 여전한 친서외교 극과 극일 것 같은 두 사람의 ‘케미’가 괜찮다는 것은 익히 알려진 사실입니다', ' 그 중심에는 두 사람 간에 오간 친서가 있습니다', ' 김정은 위원장이 보내서 공개된 것만 6통이구요, 트럼프 대통령은 3통의 편지를 보낸 것으로 확인됐습니다', ' 물론 지난해 6월 정상회담을 취소하겠다는 내용이 담겼던 트럼프 대통령의 공식 서한은 제외합니다', '트럼프 대통령은 대한민국 정부와 성공적인 회담을 이뤄냈습니다', '트럼프는 미국 대통령이다', '트럼프는 미국 대통령이다트럼프는 대통령이다', '트럼프는 한국을 좋아한다', '한국정부와 미국정부', '한반도는 행복합니다', '']

# with open("C://Users\mingzzang\Desktop\step5.txt", "r", encoding="UTF-8") as f:
#     line = f.readline()
#     print(line)
#     word = line + ' ' + input()
#     f.write(word)

#     # with open("C://Users\mingzzang\Desktop\step5.txt", "w", encoding="UTF-8") as f:
#     #     word = line + ' ' +input()
#     #     f.write(word)
    
# with open("C://Users\mingzzang\Desktop\step5.txt", "r", encoding="UTF-8") as f:
#     line = f.readline()
    # print(line)

    # 한번에 읽고 쓸 수 있는게 있다. 이걸 확인하고 블로그에 남기도록 하자
# Character	Meaning
# 'r'	open for reading (default)
# 'w'	open for writing, truncating the file first
# 'x'	create a new file and open it for writing
# 'a'	open for writing, appending to the end of the file if it exists
# 'b'	binary mode
# 't'	text mode (default)
# '+'	open a disk file for updating (reading and writing)
# 'U'	universal newline mode (deprecated)
# The default mode is 'rt' (open for reading text). 
# For binary random access, the mode 'w+b' opens and truncates the file to 0 bytes, 
# while 'r+b' opens the file without truncation. The 'x' mode implies 'w' and raises an FileExistsError if the file already exists.

# 고객이 고를 수 있게
num = int(input('기존 텍스트 확인 시, 1 또는 새로운 텍스트 추가 시, 2 입력 : '))

def add_funtion(num):
    if num == 1:
        with open("C://Users\mingzzang\Desktop\step5.txt", "r", encoding="UTF-8") as f:
            text = f.readline()
            print(text)
    elif num == 2:
        with open("C://Users\mingzzang\Desktop\step5.txt", "r+", encoding="UTF-8") as f:
            line = f.readline()
            text = line + ' ' + input()
            f.write(text)
            with open("C://Users\mingzzang\Desktop\step5.txt", "r", encoding="UTF-8") as f:
                line = f.readline()
                print(line)
add_funtion(num)