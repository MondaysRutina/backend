# Python3 샘플 코드 #
#-*-coding:utf-8-*-
import requests
import json

url = 'http://apis.data.go.kr/1471000/FtnltCosmRptPrdlstInfoService/getRptPrdlstInq'
params ={'serviceKey' : 'RzZpuK2Y2fzMk+xUlOR6G0NaRPOkBX9LSniKx170jnDBpg1/rlcT13RgMpS5JYCAlHt03aQGLYk70mRB8d5aZg==', 'pageNo' : '1', 'numOfRows' : '1', 'type' : 'json', 'item_seq' : '', 'item_name' : '', 'cosmetic_report_seq' : '' }

response = requests.get(url, params=params)
re_decode = response.content.decode('utf-8')
re_dict = json.loads(re_decode) # dict 타입이 된다.
#print(re_dict)

re_body = re_dict.get('body')
#print(re_body)

pageNo = re_body.get('pageNo') # int 타입
#print(pageNo, end = ' ')
totalCount = re_body.get('totalCount')# int 타입, 데이터 수: 211850
#print(totalCount, end = ' ')
numOfRows = re_body.get('numOfRows')# int 타입
#print(numOfRows, end = ' ')
items = re_body.get('items') # 리스트 타입임, 리스트 타입 안에 numOfRows 개수 만큼 딕셔너리 타입으로 들어가 있다.
#print(items)

item_name = "" # str  타입
item_ph = "" # str  타입, 이건 넣을건지 안넣을 건지 물어보기
item_list = [] # 정리한 데이터를 넣을 list

for x in items:
  empty_list = []
  empty_list.append(pageNo)
  item_name = x['ITEM_NAME']
  empty_list.append(item_name)
  item_ph = x['ITEM_PH'] # ph 넣을건지 물어보기  
  empty_list.append(item_ph)
  
  date_seq = x['COSMETIC_REPORT_SEQ']
  date_seq = list(date_seq)
  
  num_date= ''
  for x in date_seq[0:4]:
    num_date += x
  num_date = int(num_date) # int
  if num_date > 2010:    
    print('up 2010')
  else:
    print('under 2010')
  
  item_list.append(empty_list)

#print(item_name, end = ' ')
#print(item_ph)
print(item_list)