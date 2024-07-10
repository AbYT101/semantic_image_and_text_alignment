from autogen import Agent
from PIL import Image
import pytesseract
import cv2
import numpy as np
import torch

class ImageAnalysisAgent(Agent):
    def __init__(self):
        super().__init__()
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
    def object_identification(self, image: Image.Image):
        # Use a pre-trained YOLO model for object detection
        # Convert PIL image to numpy array
        img_np = np.array(image)
        # Perform object detection
        results = self.model(img_np)
        # Extract detection results
        objects = results.pandas().xyxy[0].to_dict(orient="records")
        return objects

    def color_identification(self, image: Image.Image):
        image = np.array(image)
        avg_color_per_row = np.average(image, axis=0)
        avg_color = np.average(avg_color_per_row, axis=0)
        return avg_color

    def position_extraction(self, image: Image.Image):
        # Convert PIL image to numpy array
        img_np = np.array(image)
        # Perform object detection
        results = self.model(img_np)
        # Extract bounding boxes
        bboxes = results.xyxy[0].numpy()
        # Extract positions
        positions = []
        for bbox in bboxes:
            x_min, y_min, x_max, y_max, confidence, class_id = bbox[:6]
            positions.append({
                'class_id': int(class_id),
                'confidence': float(confidence),
                'x_min': float(x_min),
                'y_min': float(y_min),
                'x_max': float(x_max),
                'y_max': float(y_max),
                'width': float(x_max - x_min),
                'height': float(y_max - y_min)
            })
        return positions

    def character_recognition(self, image: Image.Image):
        return pytesseract.image_to_string(image)

# Instantiate the agent
image_agent = ImageAnalysisAgent()
