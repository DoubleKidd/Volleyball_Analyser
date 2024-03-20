from ultralytics import YOLO

model = YOLO('yolov8x')

result = model.predict('/Users/BenKidd/Desktop/Volleyball_Data/Videos_in_MP4/pexels-pavel.mp4', save=True)
print(result)
print('boxes: ')
for box in result[0].boxes:
    print(box)

# don't forget to clear the prediction cache