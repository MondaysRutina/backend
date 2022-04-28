# Python3 샘플 코드 #
# -*-coding:utf-8-*-
import requests
import json
from api_data_count import get_page_count

url = 'http://apis.data.go.kr/1471000/FtnltCosmRptPrdlstInfoService/getRptPrdlstInq'
params = {'serviceKey': 'RzZpuK2Y2fzMk+xUlOR6G0NaRPOkBX9LSniKx170jnDBpg1/rlcT13RgMpS5JYCAlHt03aQGLYk70mRB8d5aZg==',
          'pageNo': '1', 'numOfRows': '100', 'type': 'json', 'item_seq': '', 'item_name': '', 'cosmetic_report_seq': ''}

item_list = []  # items에서 추출한 데이터를 넣을 list
pass_data_count = 0  # 한 페이지에서 통과한 데이터의 수
total_pass_data_count = 0  # 2017년 이후 등록 + 스킨케어 분류 통과한 데이터의 수
total_delete_data_count = 0  # 전체 페이지에서 총 삭제된 데이터의 수

exclude_word = ['선크림', '썬크림', '선로션', '썬로션', '선스프레이', '썬스프레이', '선블록', '썬블록', '선스틱', '썬스틱', '선쿠션', '썬쿠션', '선팩트', '썬팩트',
                '에스피에프', '파운데이션']


def page_run(page_num):
    for num in range(page_num):
        page_num = str(num + 1)
        params['pageNo'] = page_num  # 페이지 숫자 설정
        # print(params)
        analyze_response(params)


def analyze_response(params):
    response = requests.get(url, params=params)
    re_decode = response.content.decode('utf-8')  # 바이트 타입으로 넘어온 데이터를 utf-8 형식으로 바꿔 문자열로 나타냄
    re_dict = json.loads(re_decode)  # dict 타입이 된다.
    # print(re_dict)

    re_body = re_dict.get('body')  # re_body 는 dict 타입
    # print(re_body)

    pageNo = re_body.get('pageNo')  # int 타입
    # print(pageNo, end = ' ')
    # totalCount = re_body.get('totalCount')# int 타입, 데이터 수: 211850
    # print(totalCount, end = ' ')
    # numOfRows = re_body.get('numOfRows')# int 타입
    # print(numOfRows, end = ' ')
    items = re_body.get('items')  # 리스트 타입임, 리스트 타입 안에 numOfRows 개수 만큼 딕셔너리 타입으로 들어가 있다.
    # print(items)

    global total_delete_data_count, total_pass_data_count, pass_data_count
    for x in items:
        check_data_report_date(x, pageNo)  # 2017년 이후에 등록된 데이터인지 확인
    print('페이지 번호 : ', pageNo, ' , 통과한 데이터 수 : ', pass_data_count, ', 삭제된 데이터 수 : ', 100 - pass_data_count)

    total_delete_data_count += (100 - pass_data_count)
    total_pass_data_count += pass_data_count
    pass_data_count = 0


def check_data_report_date(item, pageNo):  # 2017년 이후에 등록된 데이터인지 확인
    date_seq = item['COSMETIC_REPORT_SEQ']
    date_seq = list(date_seq)  # list 타입으로 변경

    num_date = ''
    for x in date_seq[0:4]:
        num_date += x
    num_date = int(num_date)  # 문자를 int으로 바꿔서 넣어줌

    if num_date >= 2017:
        check_data_word(item, pageNo)


def check_data_word(item, pageNo):  # 제품명으로 스킨케어 제품만 분류하는 작업
    empty_list = []
    empty_list.append(pageNo)
    item_name = item['ITEM_NAME']

    # item_name 이 exclude_word의 모든 항목과 일치하지 않으면 넣어라
    for word in exclude_word:
        if word in item_name:
            print('제품명:', item_name, ', 포함 단어:', word)
            break
        else:
            if exclude_word[-1] == word:
                empty_list.append(item_name)

                item_ph = item['ITEM_PH']  # str 타입으로 출력됨
                # print(item_ph)
                if item_ph is None:  # ph 입력값이 없는 경우 검사
                    empty_list.append(-1)
                else:
                    empty_list.append(item_ph)

                item_list.append(empty_list)
                global pass_data_count
                pass_data_count += 1


# 전체 데이터 수 / 100 으로  전체 페이지를 알아내서 그 페이지 값으로 page_run 함수 돌리는 코드 만들기
api_page_count = get_page_count()
print('검색해야할 페이지 수 : ', api_page_count)
# page_run(api_page_count)

if __name__ == "__main__":
    page_run(1060)
    # print(item_list)
    print('총 삭제된 항목의 수 = ', total_delete_data_count)
    print('총 통과된 항목의 수 = ', total_pass_data_count)


# 제품명에서 스킨, 토너 단어 찾아서 화장품 종류 항목 만들기
