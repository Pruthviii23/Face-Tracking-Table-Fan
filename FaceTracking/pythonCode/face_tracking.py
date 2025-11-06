import cv2
import serial
import time

# Replace 'COM3' with your Arduino's port
arduino = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)  

# --- INITIALIZE HAAR CASCADE ---
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# --- CAMERA SETUP ---
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Frame width
cap.set(4, 480)  # Frame height

# --- INITIAL SERVO ANGLES ---
x_angle = 90
y_angle = 90

# --- CONTROL PARAMETERS ---
Kp = 0.1  
frame_center_x = 320
frame_center_y = 240

print("System starting... Press 'q' to exit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip frame to correct mirror effect
    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    if len(faces) > 0:
        # Get the largest detected face
        (x, y, w, h) = max(faces, key=lambda f: f[2] * f[3])
        face_center_x = x + w // 2
        face_center_y = y + h // 2

        # Draw tracking rectangle and face center
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.circle(frame, (face_center_x, face_center_y), 5, (0, 255, 0), -1)

        # Compute error between frame center and face center
        error_x = frame_center_x - face_center_x
        error_y = frame_center_y - face_center_y

        # Update servo angles proportionally
        x_angle += Kp * error_x
        y_angle -= Kp * error_y  # Invert Y-axis

        # Clamp angles to 0–180 range
        x_angle = max(0, min(180, x_angle))
        y_angle = max(0, min(180, y_angle))

        # Send data to Arduino
        command = f"{int(x_angle)},{int(y_angle)}\n"
        arduino.write(command.encode('utf-8'))

        # Display tracking data on screen
        cv2.putText(frame, f"X:{int(x_angle)} Y:{int(y_angle)}", (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

    cv2.imshow("Face Tracking", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
arduino.close()
cv2.destroyAllWindows()