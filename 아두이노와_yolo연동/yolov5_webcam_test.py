from ultralytics import YOLO

model = YOLO("model_619.pt")

# results = model.predict(source="test.mp4", conf=0.5, show=True)
results = model.predict(source=0, conf=0.5, show=True) # 웹캠 사이즈 = 384x512