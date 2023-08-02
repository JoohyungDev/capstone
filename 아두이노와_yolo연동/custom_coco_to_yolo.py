import json
import os

# MS COCO JSON 파일 읽어오기
with open('C:/Users/PJH/Desktop/네이버_쓰레기데이터/batch_01/data.json', 'r') as f:
    coco_data = json.load(f)

# YOLO 형식으로 변환
yolo_data = ""
for image in coco_data["images"]:
    image_filename = image["file_name"]
    image_width = image["width"]
    image_height = image["height"]
    
    for tation in coco_data["annotations"]:
        bbox = tation["bbox"]
        category_id = tation["category_id"]
        category_name = coco_data["categories"][category_id - 1]["name"]
            
        x_center = bbox[0] + bbox[2] / 2
        y_center = bbox[1] + bbox[3] / 2
        width = bbox[2]
        height = bbox[3]
            
        # YOLO 형식으로 변환된 tation 문자열 추가
        yolo_data += f"{category_id - 1} {x_center / image_width:.6f} {y_center / image_height:.6f} {width / image_width:.6f} {height / image_height:.6f}\n"
    
    # YOLO 형식으로 변환된 tation 문자열을 파일로 저장
    annotation_file_path = os.path.join('./yolo/', f"{image_filename.split('.')[0]}.txt")
    with open(annotation_file_path, 'w') as f:
        f.write(yolo_data)
    
    # 다음 이미지에 대한 tation 문자열 초기화
    yolo_data = ""
