import os
import cv2
from concurrent.futures import ThreadPoolExecutor
from Yolov8nDetector import Yolov8nDetector
from SSD import SSDDetector
from FastRCNN import FastRCNNDetector
COCO_LABELS = [
    "person", "bicycle", "car", "motorcycle", "airplane", "bus",
    "train", "truck", "boat", "traffic light", "fire hydrant", "stop sign",
    "parking meter", "bench", "bird", "cat", "dog", "horse", "sheep",
    "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
    "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball",
    "kite", "baseball bat", "baseball glove", "skateboard", "surfboard",
    "tennis racket", "bottle", "wine glass", "cup", "fork", "knife", "spoon",
    "bowl", "banana", "apple", "sandwich", "orange", "broccoli", "carrot",
    "hot dog", "pizza", "donut", "cake", "chair", "couch", "potted plant",
    "bed", "dining table", "toilet", "tv", "laptop", "mouse", "remote",
    "keyboard", "cell phone", "microwave", "oven", "toaster", "sink",
    "refrigerator", "book", "clock", "vase", "scissors", "teddy bear",
    "hair drier", "toothbrush"
]

SIZE_THRESHOLD=100

if __name__ == "__main__":
    # model = FastRCNNDetector()
    model = Yolov8nDetector()
    # model = SSDDetector()
    conf_threshold = 0.5
    input_base_dir = "C:\CARLA_Latest\WindowsNoEditor\output\image"
    map = "Town01_Opt"
    cameras = ["front", "left_1", "right_1"]
    for camera in cameras:
        input_images_directory = os.path.join(input_base_dir, map, "original", camera)
        if not os.path.exists(input_images_directory):
            print(f"Input directory does not exist: {input_images_directory}")
            continue
        for image_file in os.listdir(input_images_directory):
            image_path = os.path.join(input_images_directory, image_file)
            if image_path is None:
                print(f"Could not read image: {image_path}")
                continue
            bboxes = model.predict(image_path)
            index = image_file.split('.')[0]
            model.save_result(
                image_path, bboxes, map, camera, index
            )
            print(f"Processed {image_file} for camera {camera}")
    
    print("All images processed.")