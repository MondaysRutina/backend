import requests
import json


def get_page_count():
    url = 'http://apis.data.go.kr/1471000/FtnltCosmRptPrdlstInfoService/getRptPrdlstInq'
    params = {'serviceKey': 'RzZpuK2Y2fzMk+xUlOR6G0NaRPOkBX9LSniKx170jnDBpg1/rlcT13RgMpS5JYCAlHt03aQGLYk70mRB8d5aZg==',
              'pageNo': '1', 'numOfRows': '1', 'type': 'json'}

    response = requests.get(url, params=params)
    re_decode = response.content.decode('utf-8')
    re_dict = json.loads(re_decode)  # dict 타입이 된다.

    re_body = re_dict.get('body')
    totalCount = re_body.get('totalCount')  # int 타입
    # print('api를 통한 총 화장품 데이터 수 : ', totalCount)

    countPageNo = (totalCount // 100)  # int 타입, 총 검색해야 할 페이지 수
    modPageNo = (totalCount % 100)  # 페이지에 포함되지 않는 남는 데이터 수
    # print('countPageNo : ', countPageNo, ' modPageNo : ', modPageNo)

    if modPageNo > 0:
        return countPageNo + 1  # 남는 데이터 수가 있는 경우
    else:
        return countPageNo





