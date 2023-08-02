import os
import glob
import json
import pandas as pd
from pandas import json_normalize

# JSON 파일이 있는 상위 폴더 경로
folder_path = 'C:/Users/PJH/Desktop/pet/'

# 폴더 내부의 모든 JSON 파일 경로 리스트 가져오기(recuresive=True는 하위폴더를 모두 탐색하는 코드)
json_files = glob.glob(os.path.join(folder_path, 'VL_PE_0/*.json'), recursive=False)

# 모든 결과가 저장될 빈 데이터프레임 생성
# result = pd.DataFrame(pd.DataFrame(columns=['width', 'height', 'id', 'file_name', 'image_id', 'category_id','bbox','iscrowd','area']))
result = pd.DataFrame()

# JSON 파일 불러와서 데이터프레임으로 변환하기
for json_file in json_files:
    with open(json_file, 'rt', encoding='UTF-8') as f:
        data = json.load(f)
    data_norm = json_normalize(data)
    # images 선언
    img = data_norm.loc[0]["images"] 
    images = pd.DataFrame(data=img, columns=['width', 'height', 'id', 'file_name']) 
    # annotations 선언
    ant = data_norm.loc[0]["annotations"] 
    annotation = pd.DataFrame(data=ant, columns=['image_id', 'category_id', 'bbox', 'iscrowd', 'area'])
    # 결과
    result_temp = pd.concat([images, annotation], axis=1)
    # NaN을 이전행의 값으로 채워주고 result 데이터프레임 자체를 수정하는 코드
    # for i in range(result_temp.shape[0]):
    result_temp.fillna(method='ffill', inplace=True)
    result = pd.concat([result, result_temp], ignore_index=True)
    
print(result)


#     # annotations 선언
#     ant = data_norm.loc[0]["annotations"] 
#     annotation = pd.DataFrame(data=ant, columns=['id', 'image_id', 'category_id', 'metainfo_id', 'bbox', 'ignore', 'iscrowd', 'area']) 

#     # 결과
#     result = pd.concat([images, annotation], axis = 1, ignore_index=True)

#     # NaN을 이전행의 값으로 채워주고 result 데이터프레임 자체를 수정하는 코드
#     for i in range(result.shape[0]):
#         result.fillna(method='ffill', inplace=True)
    
#     real_result.append(result)
# print(real_result)

# 여러 json 파일 불러와서 테이블 찍어보기!