from ultralytics import YOLO
import cv2

# Load YOLO model (medium for better accuracy)
model = YOLO("yolov8m.pt")

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot open webcam")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Cannot read frame")
        break

    # Run object detection with confidence threshold
    results = model(frame, conf=0.7)

    # Draw bounding boxes
    annotated_frame = results[0].plot()

    cv2.imshow("YOLO Object Detection", annotated_frame)

    # Press 'q' to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()