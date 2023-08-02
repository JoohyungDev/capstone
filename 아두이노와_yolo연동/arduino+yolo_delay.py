import cv2
import serial
from ultralytics import YOLO


def capture_frame(every_n_seconds):
    # 아두이노와 연결
    arduino = serial.Serial('COM7', 9600)

    # YOLO v5 모델 불러오기
    model = YOLO("best.pt")
    model.conf = 0.5

    # 웹캠 사용
    # cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture("test.mp4")

    # 프레임 속성 설정
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(fps * every_n_seconds)

    # 프레임 카운터 초기화
    frame_count = 0

    while True:
        # 프레임 읽기
        ret, frame = cap.read()

        if not ret:
            break

        # 특정 초마다 프레임 처리
        if frame_count % frame_interval == 0:
            # YOLO v5로 물체 감지
            results = model(frame)

            for box in results[0].boxes:
                cls = box.cls
                conf = box.conf
                if cls == 1:
                    print('class:', cls)
                    arduino.write(b'1')
                else:
                    print('class:', cls)
                    arduino.write(b'2')

        # 프레임 카운터 증가
        frame_count += 1

        # 인식 결과 시각화
        annotated_frame = results[0].plot()
        cv2.imshow("YOLOv5 Inference", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 해제
    cap.release()
    cv2.destroyAllWindows()
    arduino.close()


# 5초마다 프레임을 인식하기 위해 함수 호출
capture_frame(1)
