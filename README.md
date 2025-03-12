Crowd Management System
📌 Overview
The Crowd Management System is an AI-powered platform that detects the number of people in a camera feed and monitors crowd density in real time. If the count exceeds a predefined limit, the system triggers a warning alert. This helps in maintaining safety and preventing overcrowding in public spaces.

🚀 Features
Real-time people detection using YOLOv3 and OpenCV
Automatic crowd density analysis
Customizable threshold for crowd limit
Visual warning alert when the limit is exceeded
User-friendly interface with a "Manage Crowd" button to open a monitoring window

🛠️ Technologies Used
Python
OpenCV
YOLOv3 (You Only Look Once)
NumPy
Tkinter / PyQt (for UI)

### 🔧 **Installation Steps for Crowd Management System**  

Follow these steps to set up and run the **Crowd Management System** on your machine.  

---

### **1️⃣ Clone the Repository**  
First, download the project by cloning the GitHub repository:  
```bash
git clone https://github.com/yourusername/crowd-management-system.git
cd crowd-management-system
```

---

### **2️⃣ Install Dependencies**  
Make sure you have Python installed (preferably Python 3.7 or later). Then, install the required dependencies:  
```bash
pip install opencv-python numpy
```

---

### **3️⃣ Install YOLOv3**  

#### **Download YOLOv3 Model Files**  
YOLOv3 requires pre-trained weight files to detect objects. Download the necessary files using the following steps:

1. **Download the YOLOv3 weights:**  
   ```bash
   wget https://pjreddie.com/media/files/yolov3.weights
   ```
   Alternatively, you can download it from the official source:  
   [YOLOv3 Weights](https://pjreddie.com/media/files/yolov3.weights)  

2. **Download YOLOv3 Configuration and Class Labels:**  
   ```bash
   wget https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg
   wget https://github.com/pjreddie/darknet/blob/master/data/coco.names
   ```

3. Move the files to your project directory:  
   ```bash
   mv yolov3.weights yolov3.cfg coco.names crowd-management-system/
   ```

---

### **4️⃣ Run the Crowd Management System**  
Once all the files are in place, execute the Python script to start the system:  
```bash
python main.py
```

---

### **5️⃣ How It Works**  
- The system captures frames from the webcam.  
- It processes the images using **YOLOv3** and **OpenCV** to detect people.  
- If the number of detected individuals exceeds the set limit, a **warning alert** is displayed.  
- Press **'Q'** to exit the application.  

---

### ✅ **You’re all set!**  
Now, your **Crowd Management System** is ready to monitor and control crowd density in real-time! 🚀