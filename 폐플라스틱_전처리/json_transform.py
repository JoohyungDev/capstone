import os
import json

# JSON 파일 불러오기
with open('./Waste_Plastics_result.json', 'r') as f:
    data = json.load(f)

# bbox 항목의 각 원소에 0.25를 곱함
for item in data:
    bbox = item['bbox']
    width = item['width']
    height = item['height']
    area = item['area']
    # 이미지 resize 비율만큼 박스 좌표 변환
    bbox_list = json.loads(bbox)
    bbox_list = [round(elem * 0.25, 2) for elem in bbox_list]
    item['bbox'] = bbox_list
    # 이미지 resize 비율만큼 가로, 세로 변환
    width = int(width / 4)
    height = int(height / 4)
    area = int(area / 4)
    # 바꾼 값 저장
    item['width'] = width
    item['height'] = height
    item['area'] = area
    

# 결과 JSON 파일로 저장
with open('./transform.json', 'w') as f:
    json.dump(data, f, indent=4)
