import json

# Custom JSON 파일 읽어오기
with open('coco/coco_1.json', 'r') as f:
    custom_data = json.load(f)

# COCO 형식으로 변환
coco_data = {
    "info": {
        "description": "coco"
    },
    "images": [],
    "annotations": [],
    "license": "https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100",
    "categories": [{"id": 1, "name": "PET", "supercategory": "PET"},
    {"id": 2, "name": "PS", "supercategory": "PS"},
    {"id": 3, "name": "PP", "supercategory": "PP"},
    {"id": 4, "name": "PE", "supercategory": "PE"}]
}

# print(custom_data['images'][0]['width'])

for image in custom_data['images']:
        coco_image = {
            "id": image['id'],
            "width": image["width"],
            "height": image["height"],
            "file_name": image["file_name"],
            # 중복 없도록
        }
        coco_data["images"].append(coco_image)

    

for annotation in custom_data['annotations']:
    coco_annotation = {
        "id": annotation["id"], 
        "image_id": annotation["image id"],
        "category_id": annotation["category_id"],
        "segmentatinon": ["polygon"],
        "bbox": annotation["bbox"],  
        "iscrowd": annotation["iscrowd"],
        "area": annotation["area"]
        }
    coco_data["annotations"].append(coco_annotation)
    
    
#COCO 형식으로 저장
with open('coco2.json', 'w') as f:
    json.dump(coco_data, f)