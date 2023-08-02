import os
import json
import pandas as pd
from pandas import json_normalize


path = "./01.데이터/2.Validation/라벨링데이터"

# 모든 결과가 저장될 빈 데이터프레임 생성
result = pd.DataFrame(pd.DataFrame(columns=['width', 'height', 'id', 'file_name', 'id', 'image_id', 'category_id', 'metainfo_id', 'bbox', 'ignore', 'iscrowd', 'area']))

for (path, dir, files) in os.walk(path):
    for file_name in files:
        ext = os.path.splitext(file_name)[-1]
        if ext == '.json':
            with open(path + '/' + file_name, 'rt', encoding='UTF-8') as f:
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
            for i in range(result_temp.shape[0]):
                result_temp.fillna(method='ffill', inplace=True)
            result = pd.concat([result, result_temp], ignore_index=True)

print(result)

# 정제된 데이터를 csv로 뽑아보아요
# result.to_csv('../Waste_Plastics_result.csv', index=False)