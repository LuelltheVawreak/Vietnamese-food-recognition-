# Vietnamese-food-recognition-

Vietnamese foods recognition  with YOLOv8n-cls finetuned on Vietnamese Foods dataset (kaggle).

This project use Deep Learning to classify and recognize food images, support related apps, webs deploy auto recommendation about diet, portion, dishes or study computer vision.

# Model & Dataset
```
Base model: YOLOv8n-cls (Ultralytics)
Input size: 224x224
Dataset: [!30VN food](https://www.kaggle.com/datasets/quandang/vietnamese-foods)
Classes: 30 Vietnamese dishes
```

# Installation
```
git clone https://github.com/<yourname>/vietnamese-food-recognition.git
cd vietnamese-food-recognition
pip install -r requirements.txt
```

# Run Training

```
python model/yolo.py
```

# Evaluate

```
python model/eval.py
```

# Gradio

```
python model/grad.py
```

This model support Grad-CAM to visualize 
