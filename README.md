# 🛣️ Road Damage Object Detection

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)]()
[![Ultralytics](https://img.shields.io/badge/Ultralytics-YOLO-orange)]()
[![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-red)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)]()

Road Damage Object Detection is a Computer Vision project built with **Ultralytics YOLO** for detecting different types of road damage from images.

This repository contains the source code, notebooks, and Gradio interface, while the trained model weights and dataset are hosted separately on Hugging Face.

---

# 🚀 Features

- Road Damage Detection using YOLO
- Supports YOLOv8, YOLOv10 and YOLO11
- Modern Gradio User Interface
- Fast inference
- Easy deployment
- Clean project structure

---

# 📂 Project Structure

```text
Road-Damage-Object-Detection
│
├── notebooks/
│
├── __pycache__/
│
├── UI.py
│
├── README.md
│
├── .gitignore
│
├── yolov8n.pt
├── yolov10n.pt
├── yolo11n.pt
├── yolo26n.pt
│
└── requirements.txt
```

---

# 📊 Model Performance

| Model | mAP50 | mAP50-95 | Precision | Recall | Size | FPS |
|--------|-------|----------|-----------|--------|------|------|
| 🥇 YOLOv8n | **0.3936** | **0.2299** | 0.5835 | **0.3952** | 23.36 MB | 269.97 |
| ⚖️ YOLOv10n | 0.3694 | 0.2173 | **0.5849** | 0.3527 | 5.49 MB | 253.44 |
| ⚡ YOLO11n | 0.3344 | 0.1905 | 0.5093 | 0.3504 | **5.22 MB** | **272.88** |

---

# 📥 Download Trained Weights

The trained models are hosted on Hugging Face.

👉 **Model Repository**

https://huggingface.co/nsr51324/Road_Damage_Object_Detection

Available checkpoints

- YOLOv8 Best
- YOLOv10 Best
- YOLO11 Best

---

# 📁 Dataset

The dataset used for training is available on Hugging Face.

👉 Dataset Repository

https://huggingface.co/datasets/nsr51324/Road_Damage

Original Roboflow Dataset

https://universe.roboflow.com/trafficsignssafeway/road-damage-l1ju7

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/nsr51324/Road-Damage-Object-Detection.git

cd Road-Damage-Object-Detection
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🖥️ Run the Application

Launch the Gradio interface

```bash
python UI.py
```

Open your browser

```
http://127.0.0.1:7860
```

---

# 💻 Technologies

- Python
- Ultralytics YOLO
- PyTorch
- OpenCV
- NumPy
- Gradio

---

# 📈 Training

All models were trained using the Ultralytics framework.

Configuration

- Image Size: 640×640
- Batch Size: 16
- Epochs: 50
- Early Stopping Enabled

---

# 📌 Repository Links

### GitHub

https://github.com/nsr51324/Road-Damage-Object-Detection

### Hugging Face Model

https://huggingface.co/nsr51324/Road_Damage_Object_Detection

### Hugging Face Dataset

https://huggingface.co/datasets/nsr51324/Road_Damage

---

# 👨‍💻 Author

**Nasr Mohamed**

AI Engineer

GitHub:
https://github.com/nsr51324

Hugging Face:
https://huggingface.co/nsr51324

---

⭐ If you like this project, don't forget to give it a Star.
