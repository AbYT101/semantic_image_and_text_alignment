from autogen import Agent
from PIL import Image
import base64
import requests
from io import BytesIO
from dotenv import load_dotenv
import os
load_dotenv()

class ImageAnalysisAgent(Agent):
    def __init__(self, api_key: str):
        super().__init__()
        self.api_key = api_key
        self.model = "gpt-4o" 

    def encode_image(self,image):
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        buffered = BytesIO()
        image.save(buffered, format="JPEG")
        image_data = buffered.getvalue()
        # Encode the byte data in base64 and return as a string
        return base64.b64encode(image_data).decode('utf-8')


    def analyze_image(self, image: Image.Image, question: str):
        base64_image = self.encode_image(image)
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": question
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            "max_tokens": 300
        }
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        return response.json()

    def object_identification(self, image: Image.Image):
        response = self.analyze_image(image, "Identify all elements in this online ad. This includes, but is not limited to, logos, calls to action, frames, images, text, buttons, background patterns, and any other visual or textual components relevant to the advertisement.")       
        # Extracting objects from the response
        objects_str = response['choices'][0]['message']['content']
        objects_list = objects_str.split('\n')[1:]  # Split by newline and skip the first line
        
        return objects_list

    def color_identification(self, image: Image.Image, num_colors: int = 5):
        response = self.analyze_image(image, "Identify and extract the primary colors used in this image. Ensure to capture all dominant colors to maintain visual consistency.")        
        colors = response['choices'][0]['message']['content'].split('\n')[1:num_colors+1]
        return colors

    def position_extraction(self, image: Image.Image):
        response = self.analyze_image(image, "Determine the position of all objects within this image. This includes identifying the coordinates and relative positions of elements to assist in composing ad frames.")
        positions = response['choices'][0]['message']['content'].split('\n')[1:]
        return positions

    def character_recognition(self, image: Image.Image):
        response = self.analyze_image(image, "Use OCR (Optical Character Recognition) techniques to extract all text from this image. Identify and capture all visible textual information, including fonts and styles if possible.")
        text = response['choices'][0]['message']['content'].split('\n')[1]
        return text

# Instantiate the agent
api_key = os.getenv('OPENAI_API_KEY')
openai_image_agent = ImageAnalysisAgent(api_key)
