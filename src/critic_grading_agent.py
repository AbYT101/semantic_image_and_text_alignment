from autogen import Agent
from PIL import Image
import numpy as np
import os
from image_analysis import image_agent
from text_analysis import text_agent
from openai_image_analysis import openai_image_agent

class CriticGradingAgent(Agent):
    def __init__(self, image_agent, text_agent):
        super().__init__()
        self.image_agent = image_agent
        self.text_agent = text_agent

    def analyze_asset(self, image: Image.Image, text: str):
        image_analysis = {
            'objects': self.image_agent.object_identification(image),
            'colors': self.image_agent.color_identification(image),
            'positions': self.image_agent.position_extraction(image),
            'text': self.image_agent.character_recognition(image)
        }

        text_analysis = {
            'summary': self.text_agent.text_summarization(text),
            'key_phrases': self.text_agent.key_phrase_identification(text),
            'narrative': self.text_agent.narrative_understanding(text)
        }

        return {
            'image_analysis': image_analysis,
            'text_analysis': text_analysis
        }

# Instantiate the critic/grading agent
critic_grading_agent = CriticGradingAgent(openai_image_agent, text_agent)

assets_dir = 'data/assets/images'
image_files = [os.path.join(assets_dir, f) for f in os.listdir(assets_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]
images = [Image.open(file) for file in image_files]

# Example usage
image = images[1]
text = "Simple advertisement for inspiring travel."
analysis = critic_grading_agent.analyze_asset(image, text)
print(analysis)
