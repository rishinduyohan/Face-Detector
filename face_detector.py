import cv2
import time

# Load Haar Cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Start webcam
capture = cv2.VideoCapture(0)

#for FPS calculate
prev_time = 0

while True:
    c_rec, d_img = capture.read()
    if not c_rec:
        break  # exit if camera not working

    # Convert to grayscale
    gray = cv2.cvtColor(d_img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    face = face_cascade.detectMultiScale(gray, 1.3, 6)

    # Change rectangle color (red if >3 faces, green if <=3)
    color = (0, 255, 0) if len(face) <= 3 else (0, 0, 255)

    # Draw rectangles
    for (x1, y1, w1, h1) in face:
        cv2.rectangle(d_img, (x1, y1), (x1+w1, y1+h1), color, 2)

    #Display time
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    cv2.putText(d_img, timestamp, (10, d_img.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,
                0.6, (200, 200, 200), 2, cv2.LINE_AA)

    #FPS calculate
    currentTime = time.time()
    fps = 1 / (currentTime - prev_time) if prev_time else 0
    prev_time = currentTime

    cv2.putText(d_img, f"FPS: {int(fps)}", (d_img.shape[1] - 120, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2, cv2.LINE_AA)

    # Show image
    cv2.imshow('img', d_img)

    # Exit on 'q' key
    h = cv2.waitKey(40) & 0xff
    if h == ord('q'):
        break

# Release resources
capture.release()
cv2.destroyAllWindows()
