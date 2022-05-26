import requests
import json
from api_data_count import get_page_count
from check_cosmetic_category import check_data_cosmetic_category
from read_file_exclude_word import exclude_word_list
from make_file_cosmetic_data import make_file

url = 'http://apis.data.go.kr/1471000/FtnltCosmRptPrdlstInfoService/getRptPrdlstInq'
params = {'serviceKey': 'RzZpuK2Y2fzMk+xUlOR6G0NaRPOkBX9LSniKx170jnDBpg1/rlcT13RgMpS5JYCAlHt03aQGLYk70mRB8d5aZg==',
          'pageNo': '1', 'numOfRows': '100', 'type': 'json', 'item_seq': '', 'item_name': '', 'cosmetic_report_seq': ''}

item_list = []  # items에서 추출한 데이터를 넣을 list
pass_data_count = 0  # 한 페이지에서 통과한 데이터의 수
total_pass_data_count = 0  # 2017년 이후 등록된 데이터인지 확인 -> 스킨케어 분류 통과한 데이터의 수
total_delete_data_count = 0  # 전체 페이지에서 총 삭제된 데이터의 수

exclude_word = exclude_word_list()
# print(exclude_word)


def page_run(page_num):
    for num in range(page_num):
        page_num = str(num + 1)
        params['pageNo'] = page_num  # 페이지 숫자 설정
        # print(params)
        analyze_response(params)


def analyze_response(params):  # api를 통해 넘어오는 데이터를 분석함
    response = requests.get(url, params=params)
    re_decode = response.content.decode('utf-8')  # 바이트 타입으로 넘어온 데이터를 utf-8 형식으로 바꿔 문자열로 나타냄
    re_dict = json.loads(re_decode)  # dict 타입이 된다.

    re_body = re_dict.get('body')  # re_body 는 dict 타입

    pageNo = re_body.get('pageNo')  # int 타입
    # totalCount = re_body.get('totalCount')# int 타입
    # numOfRows = re_body.get('numOfRows')# int 타입
    items = re_body.get('items')  # 리스트 타입임, 리스트 타입 안에 numOfRows 개수 만큼 딕셔너리 타입으로 들어가 있다.

    global total_delete_data_count, total_pass_data_count, pass_data_count
    for x in items:
        check_data_report_date(x, pageNo)  # 2017년 이후에 등록된 데이터인지 확인
    print('페이지 번호 : ', pageNo, ' , 통과한 데이터 수 : ', pass_data_count, ', 삭제된 데이터 수 : ', 100 - pass_data_count)

    total_delete_data_count += (100 - pass_data_count) # 삭제된 데이터 수를 누적함
    total_pass_data_count += pass_data_count # 통과한 데이터 수를 투적함
    pass_data_count = 0 # 한 페이지에서 통과한 데이터 수를 다시 0으로 초기화 함


def check_data_report_date(item, pageNo):  # 2017년 이후에 등록된 데이터인지 확인하는 작업
    date_seq = item['COSMETIC_REPORT_SEQ']  # 2008000229 형태로 출력됨
    date_seq = list(date_seq)  # 문자를 자르기 위해 list 타입으로 변경

    num_date = ''  # 화장품이 보고된 연도를 담을 변수
    for x in date_seq[0:4]:
        num_date += x  # 2008000229 에서 앞에 4자리만 잘라 붙여서 보고 연도인 2008이 되도록 함
    num_date = int(num_date)  # 문자를 int으로 바꿔서 넣어줌

    if num_date >= 2017:
        check_data_word(item, pageNo)


def check_data_word(item, pageNo):  # 제품명으로 스킨케어 제품만 분류하는 작업
    empty_list = []
    # empty_list.append(pageNo)
    item_name = item['ITEM_NAME']

    # item_name 이 exclude_word의 모든 항목과 일치하지 않으면 넣어라
    for word in exclude_word:
        if word in item_name:
            #print('제품명:', item_name, ', 포함 단어:', word)
            break
        else:
            if exclude_word[-1] == word:
                category = check_data_cosmetic_category(item_name)  # 화장품 종류 분류
                empty_list.append(category) # 화장품 종류 넣기

                empty_list.append(item_name)  # 화장품 이름 넣기

                item_ph = item['ITEM_PH']  # str 타입으로 출력됨
                # print(item_ph)
                if item_ph is None:  # ph 입력값이 없는 경우 검사
                    empty_list.append(-1)
                else:
                    empty_list.append(item_ph)  # api에서 넘어오는 ph 입력값으로는 숫자 또는 '해당사항없음' 두 경우가 있음

                item_list.append(empty_list)
                global pass_data_count
                pass_data_count += 1 # 통과한 데이터 수에 1 추가


if __name__ == "__main__":
    api_page_count = get_page_count()  # (전체 데이터 수 / 100)으로 전체 페이지 수를 알아냄
    print('검색해야할 페이지 수 : ', api_page_count)

    page_run(api_page_count) # 전체 페이지 수 만큰 프로그램 실행함
    # page_run(1060) # 1060 페이지까지 프로그램 실행함

    # print(item_list) # ['스킨', '스킨푸드유자수분씨비타아이마스크', '6.0']
    make_file(item_list)  # 분류한 데이터를 엑셀 파일에 쓰기

    print('총 삭제된 항목의 수 = ', total_delete_data_count)
    print('총 통과된 항목의 수 = ', total_pass_data_count)

