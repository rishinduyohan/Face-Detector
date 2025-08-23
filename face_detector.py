import cv2

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

    # Draw rectangles
    for (x1, y1, w1, h1) in face:
        cv2.rectangle(d_img, (x1, y1), (x1+w1, y1+h1), (0, 255, 0), 2)

    # Show image
    cv2.imshow('img', d_img)

    # Exit on 'q' key
    h = cv2.waitKey(40) & 0xff
    if h == ord('q'):
        break

# Release resources
b.release()
cv2.destroyAllWindows()
