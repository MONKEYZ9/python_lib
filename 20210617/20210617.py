
# LV1 : txt / 텍스트 파일을 불러와주세요.
# step1.txt

# 결과 
# 2019년에도 한반도를 둘러싼 가장 중요한 외교안보 화두는 북한의 비핵화입니다. 극적인 반전의 해였던 2018년에 만들어 낸 전반적인 기조가 큰 변화 없이 이어질 것이라는 전망이 많습니다. 좀 더 구체적으로 말하면 핵이나 미사일 도발이 재개될 가능성 보다는 지루한 협상과정이 이어질 가능성이 높아 보입니다. 조심스런 낙관의 근거는 김정은 위원장의 신년사와 그에 대한 트럼프의 화답입니다. 가장 중요한 변수는 2차 북-미 정상회담이 언제 열리느냐에 달려 있을 것 같습니다. 폼페이오 국무장관과 김영철 부위원장 간에 구축된 고위급 협상라인이 사실상 개점 휴업상태이고, 실무채널인 비건-최선희 라인은 아예 가동조차 되지 않고 있습니다. 김정은은 신년사에서 다시 한번 트럼프 대통령에게 러브콜을 보냈고, 트럼프도 “만남을 고대하고 있다”고 했습니다. 하지만 두 정상의 만남에 대한 기대감은 지난해 6월 1차 정상회담 때에 비해 급속히 떨어져 있는 상황입니다.● 여전한 친서외교 극과 극일 것 같은 두 사람의 ‘케미’가 괜찮다는 것은 익히 알려진 사실입니다. 그 중심에는 두 사람 간에 오간 친서가 있습니다. 김정은 위원장이 보내서 공개된 것만 6통이구요, 트럼프 대통령은 3통의 편지를 보낸 것으로 확인됐습니다. 물론 지난해 6월 정상회담을 취소하겠다는 내용이 담겼던 트럼프 대통령의 공식 서한은 제외합니다.트럼프 대통령은 대한민국 정부와 성공적인 회담을 이뤄냈습니다.트럼프는 미국 대통령이다.트럼프는 미국 대통령이다트럼프는 대통령이다.트럼프는 한국을 좋아한다.한국정부와 미국정부.


# with open("C://Users\mingzzang\Desktop\step1.txt", "r", encoding="UTF-8") as f:
#     line = f.readline()
#     print(line)

# with를 가지고 해보자
# 이걸 정리할 필요가 있을 거 같아


# ------------------------------------------------------------------------
# 강사님 필기
# 파일 읽기 쓰기를 정리한다고 함
text_file = open('C://Users\mingzzang\Desktop\step1.txt', 'r', encoding='utf-8')
# r은 그냥 읽어오는 거
# w는 쓰는거 포맷하고 다시 쓰는 상태를 말하고
# a는 append와 같은거 이거는 추가하는거야 
# 5번에서 w를 쓰지 않고 a를 사용했으면 되네

# 파일을 불러오려면 이럭헤 해야 하해
text_read = text_file.read()
print(text_read)
text_file.close()

# 이걸 줄여서 쓸 수 있는게
# with open('C://Users\mingzzang\Desktop\step1.txt', 'r') as f_read:
#     print(f_read)
# with open('C://Users\mingzzang\Desktop\step1.txt', 'w') as f_write:
#     print(f_write)
# with open('C://Users\mingzzang\Desktop\step1.txt', 'a') as f_append:
#     print(f_append)
# with open('C://Users\mingzzang\Desktop\step1.txt', 'a+') as f_append:
#     print(f_append)

    # r+ 는 읽고 쓰기
    # a+ 는 뭐라고?
    # w+ 는 

    # rw 읽고 쓰기
    # ar 도 있어
#     # 이런 형식이 있으니까 오늘 확인해서 정리하자
# with open('C://Users\mingzzang\Desktop\step1.txt', 'r+') as file_n:
#     print(file_n.read())