import shutil
from openpyxl import Workbook

filepath1 = './cosmetic_data.xlsx'
filepath2 = './use_api_cosmetic_data_최종.xlsx'

def make_file(item_list):
    write_wb = Workbook()
    write_ws = write_wb.active  # Sheet1에다 입력

    for list in item_list:
        # print(list)
        write_ws.append(list)  # 리스트 안에 들어있는 리스트를 god 단위로 엑셀에 씀

    write_wb.save(filepath1)
    write_wb.close()

    # filepath1 로 만든 파일에 데이터는 들어갔지만 다운 받은 파일이 열리지 않아 파일을 복사하여 해결함
    shutil.copy2(filepath1, filepath2)  # copy2를 사용해 메타 정보도 복사함
    print('출력!')