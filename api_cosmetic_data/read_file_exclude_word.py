from openpyxl import load_workbook

def exclude_word_list():
  # 셀 값이 함수 및 수식일 경우 data_only=Ture로 해줘야 수식이 아닌 결과값만 받음
  load_wb = load_workbook("./cosmetic_data_files/화장품 제외 리스트.xlsx", data_only=True)
  load_ws = load_wb['Sheet1'] #시트 이름으로 불러오기

  columns = load_ws['A:L'] # 열 범위 지정
  #print(columns)

  all_values = [] # 화장품 제외 단어를 담을 리스트

  for column in columns:
    column = list(column) # 행을 지정하기 위해서 리스트 타입으로 형변환
    # print(column)
    for cell in column[1:]: # 첫번째 행은 제외하고 범위 지정
      value = cell.value # 각 셀의 값을 가져옴
      if value != None:
        all_values.append(value)
        #print(value)

  #print(all_values)
  load_wb.close() # 파일 닫기
  return all_values
