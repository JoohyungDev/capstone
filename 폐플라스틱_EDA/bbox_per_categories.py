import json
import numpy as np
from pycocotools.coco import COCO
import cv2
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
# import skimage.io as io
import random
import pandas as pd
import seaborn as sns


# 두 변수는 각자 데이터 경로에 따라 변경 필요
dataset_dir = "./coco/"
train_json_dir = dataset_dir + "coco_1.json"

# COCO json 파일 읽기
with open(train_json_dir, 'r') as f:
    coco_json = json.load(f)

images = coco_json['images']
categories = coco_json['categories']
annotations = coco_json['annotations']
categories_names = ['None', 'PET','PS','PP','PE']

sns.set(rc = {'figure.figsize':(8,5)})
fig, ax1 = plt.subplots()

# 카테고리별 bounding box 개수를 카테고리 이름과 함께 저장
category_to_num_bbox = []
for i, category_name in enumerate(categories_names):
    if i == 0:
        continue  # 'None'은 제외
    num_bbox = sum([ann['category_id'] == i for ann in annotations])
    category_to_num_bbox.append((category_name, num_bbox))

# 카테고리별 bounding box 개수에 따라 내림차순 정렬
category_to_num_bbox = sorted(category_to_num_bbox, key=lambda x: x[1], reverse=True)

# 카테고리 목록과 bounding box 개수를 각각 리스트로 추출
categories_names = [t[0] for t in category_to_num_bbox]
category_to_num_bbox = [t[1] for t in category_to_num_bbox]

# 데이터프레임 생성
df = pd.DataFrame({'Categories': categories_names, 'Number of bounding boxes': category_to_num_bbox})

# 카테고리별 bounding box 개수를 barplot으로 시각화
plot_1 = sns.barplot(x="Number of bounding boxes", y="Categories", data=df, label="Total", ax=ax1, width=0.4)

# ax1의 제목과 막대그래프 수치 표현을 위해 작성
ax1.set_title("Bounding box per categories", fontsize=15)
for i, p in enumerate(plot_1.patches):
    x, y, width, height = p.get_bbox().bounds
    plot_1.text(width*1.01, y+height/2, df['Number of bounding boxes'][i], va='center')

# 하나의 이미지당 box 개수
images_len = len(images)
total_num_bbox = sum(category_to_num_bbox)

# 범례로 텍스트 추가
info_text = f"Total image: {images_len}\nTotal bbox: {total_num_bbox}\nBbox average per image: {total_num_bbox/images_len:.2f}"

# 범례 본인 입맛에 맞게 수정
ax1.legend(handles=[patches.Patch(label=info_text)], loc='lower right')
plt.show()

# # 전체 bbox의 크기만큼 반복, 반복하는 작업은 박스 크기 / 이미지 크기 
# total_box_ratio = []

# for i in range(total_num_bbox):
#     box_ratio = round(annotations[i]['area'] / (2048**2), 10)
#     total_box_ratio.append(box_ratio)


# print('Done')
# print(total_box_ratio)
# print(sum(total_box_ratio))