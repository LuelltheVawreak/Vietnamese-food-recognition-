import os
from sklearn.metrics import classification_report
from PIL import Image
import numpy as np
from ultralytics import YOLO

#check list
print(os.listdir('dataset_raw/Images/Validate'))

model = YOLO('yolov8n-cls.pt')

model.train(
    data='dataset_raw/Images/Train',  # vì trong này đã có Train/Validate rồi
    epochs=15,
    imgsz=112,
    batch=64,
    name='vietnamese_food_yolov8'
)


# Load pretrain model
model = YOLO('runs/classify/vietnamese_food_yolov8/weights/best.pt')

#Folder have validation/test (ImageFolder PyTorch:each layer is 1 folder)
val_dir = 'dataset_raw/Images/Validate'  # correct ur folder

class_names = sorted(os.listdir(val_dir))  

# Mapping classnam to index
class_to_idx = {name: idx for idx, name in enumerate(class_names)}

# save pred label and char
y_true = []
y_pred = []


for class_name in class_names:
    class_idx = class_to_idx[class_name]
    class_folder = os.path.join(val_dir, class_name)

    for image_name in os.listdir(class_folder):
        image_path = os.path.join(class_folder, image_name)

        # pred
        results = model.predict(image_path, verbose=False)[0]
        pred_idx = int(results.probs.top1)

        y_true.append(class_idx)
        y_pred.append(pred_idx)

# In classification report

print("== Classification Report ==")
print(classification_report(y_true, y_pred, target_names=class_names))
