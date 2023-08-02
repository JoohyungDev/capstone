import seaborn as sns
import matplotlib.pyplot as plt
import json

# 두 변수는 각자 데이터 경로에 따라 변경 필요
dataset_dir = "./coco/"
train_json_dir = dataset_dir + "coco_1.json"

# COCO json 파일 읽기
with open(train_json_dir, 'r') as f:
    coco_json = json.load(f)

images = coco_json['images']
categories = coco_json['categories']
annotations = coco_json['annotations']
categories_names = ['None','PET','PS','PP','PE', 'None']

sns.set(rc = {'figure.figsize':(8,5)})

fig, ax1 = plt.subplots() # ax1: bounding box 

category_to_area_bbox = [[] for i in range(len(categories_names))]
for annotation in annotations:
    category = annotation['category_id']
    bbox = annotation['bbox']
    area = annotation['area']
    category_to_area_bbox[category].append(area)

# total_to_area_bbox: 카테고리 상관없이 bounding box 면적정보를 리스트형태로 저장한다.
total_to_area_bbox = []
for idx_category in range(1, len(category_to_area_bbox)):
    total_to_area_bbox += category_to_area_bbox[idx_category]

# bounding box 면적 분포를 kdeplot으로 시각화
sns.kdeplot(total_to_area_bbox, label='Object', ax=ax1)

avg = sum(total_to_area_bbox)/len(total_to_area_bbox)

plt.rc('legend', fontsize=15)
ax1.axvline(x=avg, color='r', linestyle='--', label='Average')  # 박스 평균 출력
ax1.set_title("Area distribution of bounding box", fontsize=15)
ax1.legend()
ax1.set_xlabel(f"Area (Average: {avg:.2f})", fontsize=15)
# plt.xlim(0,500)
plt.ylim([0, (1e-5)/0.1])
plt.show()
 
