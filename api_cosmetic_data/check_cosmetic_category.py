def check_data_cosmetic_category(item_name):
    skin = {'스킨': '스킨', '토너': '스킨'}
    cream = {'크림': '크림', '젤크림': '크림', '수분크림': '크림', '수딩크림': '크림', '보습크림': '크림', '영양크림': '크림', '멀티밤': '크림',
             '모이스처라이저': '크림'}
    essense = {'세럼': '에센스', '에센스': '에센스', '앰플': '에센스', '엠플': '에센스'}
    lotion = {'로션': '로션', '에멀전': '로션', '에멀젼': '로션'}
    allinone = {'올인원': '올인원'}
    eyecare = {'아이크림': '아이케어', '아이세럼': '아이케어', '아이젤크림': '아이케어', '아이에센스': '아이케어', '아이밤': '아이케어'}
    mist = {'미스트': '기타', '스킨미스트': '기타', '페이셜미스트': '기타'}
    faceoil = {'페이스오일': '기타'}
    gel = {'젤': '기타', '수딩젤': '기타'}

    category_list = [lotion, skin, cream, essense, allinone, eyecare, mist, faceoil, gel]

    category = find_category(category_list, item_name)
    if category == None:
        category = ''
    # print('분류한 카테고리 : ', category) # 분류한 카테고리 :  gel / 분류 안되면 None return 됨
    return category


def find_category(list, item_name):
    for dict in list:
        # print(dict) # {'스킨':'skin', '토너':'skin'}
        for key in dict:
            value = key in item_name
            # print(value, ', 제품명:', item_name, ', 포함 단어:', key)
            # True , 제품명: 옹달샘젤 , 포함 단어: 젤
            if value == True:
                return dict[key]


# check_data_cosemtic_category('옹달샘스킨')