# 🌬️ Face-Tracking Smart Fan  
> A fan that *literally follows your face* — because moving your head shouldn’t cost you comfort.  

---

## 🧠 What It Does  
This smart fan automatically detects your face and keeps the airflow directed toward you — no remote, no buttons, just pure comfort powered by computer vision and Arduino magic.  

It uses:  
- **OpenCV (Python)** to detect your face 👀  
- **Arduino + Servos** to physically move the fan 🤖  
- **Serial Communication** to keep both brains talking 💬  

---

## ⚙️ What You’ll Need  
### 🧩 Hardware  
- 1 × Arduino Nano (or UNO)  
- 2 × SG90/MG995 Servo Motors (Pan + Tilt)  
- 1 × Small Fan  
- 1 × Camera (Laptop webcam or phone webcam using DroidCam/Iriun)  
- Jumper Wires  
- (Optional) 5V External Power Supply  

### 💻 Software  
- Python 3.7+  
- Arduino IDE  
- Python Libraries:  
  ```bash
  pip install opencv-python pyserial
  ```

---

## 🧵 How It Works  
1. The **camera** captures live video.  
2. OpenCV detects your **face position** in real-time.  
3. The **Python script** calculates where your face is relative to the screen’s center.  
4. The **Arduino** receives movement angles and adjusts two servos to rotate and tilt the fan.  
5. Result: The breeze never leaves your face. 🌬️  

---

## 🔌 Wiring Setup  
Follow this wiring carefully (you can use the diagram below 👇):  
- **Servo X (Pan):**  
  - Signal → D9  
  - VCC → 5V (or external 5V supply)  
  - GND → GND  

- **Servo Y (Tilt):**  
  - Signal → D10  
  - VCC → 5V  
  - GND → GND  

- **Common Ground:** Always connect Arduino GND with external power GND.  

> ⚠️ Tip: If the servos jitter or reset the Arduino, power them from an external 5V adapter.


---

## 💻 Running the Project  

### **Step 1 – Upload Arduino Code**
1. Open the provided Arduino sketch.  
2. Select your port (e.g., COM3).  
3. Upload and open Serial Monitor (optional, to see live angle data).  

### **Step 2 – Run Python Script**
1. Open your terminal in the project folder.  
2. Run:
   ```bash
   python face_tracking.py
   ```
3. Sit back and move your head — your fan will follow you!

---

## 🧩 Project Files  
| File | Description |  
|------|--------------|  
| `face_tracking.py` | Python script for face detection and servo control |  
| `arduino_servo.ino` | Arduino sketch controlling servos |  
| `Wiring.txt` | Wiring diagram |  
| `README.md` | This file |  

---

## 🧠 Behind the Scenes  
- **Algorithm Used:** OpenCV Haar Cascade Classifier for face detection.  
- **Communication:** Serial (Python → Arduino).  
- **Control Logic:** PID-inspired proportional control for smooth servo motion.  

---

## 🚀 Future Enhancements  
- Replace Haar with **YOLOv5 or DNN** for more accurate face tracking.  
- Add **adaptive fan speed** based on distance.  
- Make it **wireless** using an ESP32 or Bluetooth module.  

---

Staying cool should be *automatic*.  
Inspired by curiosity, powered by caffeine ☕ and code 💻.  
