import cv2

# Load Haar Cascade
a = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Start webcam
b = cv2.VideoCapture(0)

#for FPS calculate
prev_time =0;

while True:
    c_rec, d_img = b.read()
    if not c_rec:
        break  # exit if camera not working

    # Convert to grayscale
    e = cv2.cvtColor(d_img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    f = a.detectMultiScale(e, 1.3, 6)

    # Draw rectangles
    for (x1, y1, w1, h1) in f:
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
