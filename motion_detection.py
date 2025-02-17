import cv2
import numpy as np

def detect_person(frame):
    net = cv2.dnn.readNetFromCaffe("MobileNetSSD_deploy.prototxt", "MobileNetSSD_deploy.caffemodel")
    CLASS_NAMES = {15: "Person"}
    height, width = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward()

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        class_id = int(detections[0, 0, i, 1])

        if confidence > 0.5 and class_id in CLASS_NAMES:
            box = detections[0, 0, i, 3:7] * np.array([width, height, width, height])
            (x, y, x_max, y_max) = box.astype("int")
            label = f"{CLASS_NAMES[class_id]}: {confidence * 100:.2f}%"
            cv2.rectangle(frame, (x, y), (x_max, y_max), (0, 255, 0), 2)
            cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            return frame, True
    return frame, False
