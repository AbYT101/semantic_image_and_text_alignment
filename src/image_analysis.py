from autogen import Agent
from PIL import Image
import pytesseract
import cv2
import numpy as np
import torch
from sklearn.cluster import KMeans
from collections import Counter


class ImageAnalysisAgent(Agent):
    def __init__(self):
        super().__init__()
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5x')  # Upgraded model

    def object_identification(self, image: Image.Image):
        img_np = np.array(image)
        results = self.model(img_np)
        objects = results.pandas().xyxy[0].to_dict(orient="records")
        return objects

    def color_identification(self, image: Image.Image, num_colors: int = 5):
        image = np.array(image)

        # Ensure the image has three color channels
        if len(image.shape) == 2 or image.shape[2] == 1:  # Grayscale image
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
        elif image.shape[2] == 4:  # Image with alpha channel
            image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)

        # Flatten the image to shape (num_pixels, 3)
        image = image.reshape((image.shape[0] * image.shape[1], 3))

        # Use KMeans to find the dominant colors
        clt = KMeans(n_clusters=num_colors)
        clt.fit(image)

        # Get the colors and their frequency
        hist = self._centroid_histogram(clt)
        colors = clt.cluster_centers_

        # Convert to a list of RGB tuples
        color_info = []
        for (percent, color) in zip(hist, colors):
            color_info.append({
                'color': color.astype(int).tolist(),
                'percentage': percent
            })

        return color_info

    def _centroid_histogram(self, clt):
        # Create a histogram based on the number of pixels assigned to each cluster
        num_labels = np.arange(0, len(np.unique(clt.labels_)) + 1)
        (hist, _) = np.histogram(clt.labels_, bins=num_labels)

        # Normalize the histogram, so that it sums to one
        hist = hist.astype("float")
        hist /= hist.sum()

        return hist

    def position_extraction(self, image: Image.Image):
        img_np = np.array(image)
        results = self.model(img_np)
        bboxes = results.xyxy[0].numpy()
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
