import cv2
import time
from motion_detection import detect_person
from cloud_upload import upload_to_drive

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame, person_detected = detect_person(frame)
    cv2.imshow("Security Feed", frame)

    if person_detected:
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"person_detected_{timestamp}.jpg"
        cv2.imwrite(filename, frame)
        upload_to_drive(filename)
        print(f"Person detected! Image saved as {filename} and uploaded to Google Drive.")

    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
