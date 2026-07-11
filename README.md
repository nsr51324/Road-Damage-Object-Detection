# 🛣️ Road Damage Object Detection

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)]()
[![Ultralytics](https://img.shields.io/badge/Ultralytics-YOLO-orange)]()
[![PyTorch](https://img.shields.io/badge/PyTorch-2.x-red)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)]()

A computer vision project for **Road Damage Detection** using three generations of the YOLO family (**YOLOv8, YOLOv10, and YOLO11**) trained and evaluated on the same dataset to compare accuracy, speed, and model size.

---

# 📌 Features

- Detect multiple types of road damage.
- Compare YOLOv8, YOLOv10, and YOLO11.
- Benchmark accuracy, precision, recall, FPS, and model size.
- Gradio Web Interface.
- Ready-to-use trained weights.
- Easy deployment on local machine or Hugging Face Spaces.

---

# 📊 Benchmark Results

| Model | mAP50 | mAP50-95 | Precision | Recall | Model Size | FPS |
|--------|-------|----------|-----------|--------|------------|------|
| 🥇 YOLOv8n | **0.3936** | **0.2299** | 0.5835 | **0.3952** | 23.36 MB | 269.97 |
| ⚖️ YOLOv10n | 0.3694 | 0.2173 | **0.5849** | 0.3527 | 5.49 MB | 253.44 |
| ⚡ YOLO11n | 0.3344 | 0.1905 | 0.5093 | 0.3504 | **5.22 MB** | **272.88** |

---

# 📂 Project Structure

```text
Road_Damage_Object_Detection/
│
├── runs/
│   ├── detect/
│   │   ├── yolov8_road/
│   │   │   └── weights/
│   │   │       └── best.pt
│   │   │
│   │   ├── yolov10_road/
│   │   │   └── weights/
│   │   │       └── best.pt
│   │   │
│   │   └── yolov11_road/
│   │       └── weights/
│   │           └── best.pt
│
├── UI.py
├── Road_Damage.ipynb
├── requirements.txt
└── README.md
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/YourUsername/Road_Damage_Object_Detection.git

cd Road_Damage_Object_Detection
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 📥 Model Weights

The trained checkpoints are included in

```text
runs/detect/
```

Available models

```
runs/detect/yolov8_road/weights/best.pt

runs/detect/yolov10_road/weights/best.pt

runs/detect/yolov11_road/weights/best.pt
```

Load any model

```python
from ultralytics import YOLO

model = YOLO("runs/detect/yolov8_road/weights/best.pt")

results = model("road.jpg")

results[0].show()
```

---

# 🖥️ Gradio Interface

Run

```bash
python UI.py
```

Then open

```
http://127.0.0.1:7860
```

Features

- Upload Image
- Detect Road Damage
- Confidence Score
- Object Count
- Annotated Image

---

# 📁 Dataset

The project was trained on a Road Damage Dataset exported in YOLO format from Roboflow.

The dataset contains **7 road damage classes**.

---

# 🏋️ Training Configuration

- Framework: Ultralytics YOLO
- Image Size: 640 × 640
- Batch Size: 16
- Epochs: 50
- Optimizer: Default Ultralytics
- Early Stopping Enabled

---

# 📈 Validation

Validation metrics were generated using

```python
model.val()
```

Metrics include

- Precision
- Recall
- mAP50
- mAP50-95
- PR Curve
- Confusion Matrix
- FPS

---

# 💻 Technologies

- Python
- Ultralytics
- PyTorch
- OpenCV
- Gradio
- NumPy

---

# ⚠️ Limitations

This project is intended for research and benchmarking purposes.

Performance depends on the quality and diversity of the training dataset. Additional data and larger YOLO models can significantly improve detection accuracy.

---

# 👨‍💻 Author

**Nasr Mohamed**

AI Engineer

GitHub:
https://github.com/YourUsername

Hugging Face:
https://huggingface.co/nsr51324

LinkedIn:
https://linkedin.com/in/YourLinkedIn

---

# ⭐ If you found this project useful, consider giving it a star.
