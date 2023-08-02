import cv2
import os

# 이미지 파일들이 저장된 폴더 경로
folder_path = './data/'

# 폴더 내 모든 이미지 파일 이름 가져오기
img_files = os.listdir(folder_path)

# 모든 이미지를 resize 
for file_name in img_files:
    # 이미지 파일 경로를 생성
    file_path = os.path.join(folder_path, file_name)
    
    # 이미지 파일을 불러오기
    img = cv2.imread(file_path)
    
    # 이미지의 높이와 너비를 가져오기
    height, width = img.shape[:2]
    
    # 1/4로 resize
    resized_img = cv2.resize(img, (int(width/4), int(height/4)))
    
    # 결과 이미지를 파일로 저장
    resized_file_path = os.path.join('./resize', file_name)
    cv2.imwrite(resized_file_path, resized_img)
