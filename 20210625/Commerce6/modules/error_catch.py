class ErrorDetect():

  def error_alert(error_type):
    if error_type == 'ValueError':
      return '키를 잘못 입력하셨습니다. 다시 입력하세요'

    elif error_type == 'RangeError':
      return '유효 범위 번호만 골라 주세요'

    elif error_type == 'IdOverlapped':
      return '이미 사용중인 아이디입니다. 다시 입력하세요'

    elif error_type == 'EmptyValue':
      return '입력값이 없습니다. 다시 입력하세요'
