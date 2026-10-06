# YOLO Object Detection using YOLOv8

## 📌 Project Overview

This project implements **real-time object detection using YOLOv8 and OpenCV**.

The application captures video frames from a webcam and uses a pre-trained **YOLOv8 Medium (`yolov8m.pt`)** model to detect objects in real time. Detected objects are displayed with bounding boxes and labels. 

## 🎯 Objectives

- Perform real-time object detection using a webcam
- Use YOLOv8 for object detection
- Display detected objects with bounding boxes
- Apply a confidence threshold to improve detection reliability
- Gain practical experience with computer vision and deep learning

## 🛠️ Technologies Used

- **Python**
- **YOLOv8**
- **Ultralytics**
- **OpenCV**
- **Computer Vision**
- **Deep Learning**

## 📂 Project Files

```text
YOLO-Object-Detection/
│
├── yolo_camera.py
├── yolov8m.pt
└── README.md
```

### `yolo_camera.py`

The Python script:

1. Loads the YOLOv8 Medium model.
2. Opens the computer webcam.
3. Captures video frames continuously.
4. Performs object detection on each frame.
5. Draws bounding boxes around detected objects.
6. Displays the processed video.
7. Allows the user to press **`q`** to stop the application.  

## 🔄 Project Workflow

```text
Webcam
   ↓
Capture Video Frame
   ↓
YOLOv8 Model
   ↓
Object Detection
   ↓
Confidence Filtering
   ↓
Bounding Box & Labels
   ↓
Display Real-Time Detection
```

## ⚙️ Detection Configuration

The project uses the **YOLOv8 Medium** model:

```python
model = YOLO("yolov8m.pt")
```

A confidence threshold of **0.7** is used for object detection:

```python
results = model(frame, conf=0.7)
```

This means detections with lower confidence are filtered out. 

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/keerthanaragupathy03/YOLO-Object-Detection.git
```

### 2. Navigate to the project folder

```bash
cd YOLO-Object-Detection
```

### 3. Install the required libraries

```bash
pip install ultralytics opencv-python
```

## ▶️ How to Run

Make sure your webcam is connected and available.

Run:

```bash
python yolo_camera.py
```

The webcam window will open and YOLO will begin detecting objects in real time.

To stop the application, press:

```text
q
```

## 📊 Output

The application displays:

- Real-time webcam video
- Detected objects
- Bounding boxes
- Object labels
- Detection results based on the confidence threshold

## 📚 Key Learning Outcomes

Through this project, I gained practical experience in:

- Real-time Object Detection
- YOLOv8
- Computer Vision
- OpenCV
- Deep Learning
- Python
- Webcam-based Video Processing
- Model Inference

## 🔮 Future Enhancements

Possible improvements include:

- Adding object-specific alerts
- Integrating a web interface
- Adding object counting
- Saving detection results
- Adding detection statistics
- Supporting image and video file input
- Improving the user interface

## 👩‍💻 Author

**Keerthana Raghupathy**

Computer Science and Engineering Student

GitHub: **keerthanaragupathy03**

---

⭐ If you find this project useful, feel free to star the repository.
