import cv2
import serial
from ultralytics import YOLO
from collections import deque

# 아두이노와 연결
# arduino = serial.Serial('COM7', 9600)

# YOLO v5 모델 불러오기
model = YOLO("model_619.pt")
model.conf = 0.5

# 웹캠 사용
cap = cv2.VideoCapture(0)

# 객체 정보를 저장하는 큐
object_queue = deque([[],[],[],[],[],[]])
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 크롭 좌 180, 128 (1152)
    frame = frame[:, 128:1100]
    # 웹캠 영상 크기를 640x640로 변환
    frame = cv2.resize(frame, (640, 640))

    # YOLO v5로 물체 감지
    results = model(frame)

    # results를 frame에 표현하기
    annotated_frame = results[0].plot()

    # annotated_frame 시각화
    cv2.imshow("YOLOv5 Inference", annotated_frame)

    temp = []
    for box in results[0].boxes:
        cls = box.cls
        conf = box.conf
        if conf >= 0.8:
            temp.append(model.names[int(cls)])
    
    object_queue.append(temp)
    object_queue.popleft()
    print(object_queue)
    # if 'Plastic' in object_queue[1]:
    #     print('Plastic 밀기')
    #     arduino.write(b'1')

    # if 'Can' in object_queue[1]:
    #     print('Can 밀기')
    #     arduino.write(b'2')

    # if 'Paper' in object_queue[1]:
    #     print('Paper 밀기')
    #     arduino.write(b'3')

    # if 'Styrofoam' in object_queue[1]:
    #     print('Styrofoam 밀기')
    #     arduino.write(b'4')

    # if 'Glass' in object_queue[1]:
    #     print('Glass 밀기')
    #     arduino.write(b'5')
        
    # if 'General Trash' in object_queue[1]:
    #     print('General Trash 밀기')
    #     arduino.write(b'6')

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
# arduino.close()