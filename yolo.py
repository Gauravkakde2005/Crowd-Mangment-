import os
import urllib.request

# Define URLs for the YOLO files
yolo_urls = {
    "yolov3.cfg": "https://github.com/pjreddie/darknet/raw/master/cfg/yolov3.cfg",
    "yolov3.weights": "https://pjreddie.com/media/files/yolov3.weights",
    "coco.names": "https://github.com/pjreddie/darknet/raw/master/data/coco.names"
}

# Define directory to save files
save_dir = "yolo_files"
os.makedirs(save_dir, exist_ok=True)

# Download files
for filename, url in yolo_urls.items():
    save_path = os.path.join(save_dir, filename)
    if not os.path.exists(save_path):
        print(f"Downloading {filename}...")
        urllib.request.urlretrieve(url, save_path)
        print(f"Saved {filename} to {save_path}")
    else:
        print(f"{filename} already exists, skipping download.")

print("All YOLO files are ready!")
