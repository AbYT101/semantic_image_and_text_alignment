from autogen import Agent
from PIL import Image
import numpy as np
import os
# from image_analysis import image_agent
from text_analysis import text_agent
from openai_image_analysis import openai_image_agent
from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()


# Set up OpenAI API key
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI()


class CriticGradingAgent(Agent):
    def __init__(self, image_agent, text_agent, knowledge_base):
        super().__init__()
        self.image_agent = image_agent
        self.text_agent = text_agent
        self.knowledge_base = knowledge_base

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
        
    def critic_frame(self, image: Image.Image, text: str):
        analysis = self.analyze_asset(image, text)
        
        # Prepare the input for GPT-4 evaluation
        prompt = (
            f"Using the following knowledge base about design concepts:\n{self.knowledge_base}\n\n"
            f"Evaluate the ad frame with the following analysis:\n\n"
            f"Image Analysis:\nObjects: {analysis['image_analysis']['objects']}\n"
            f"Colors: {analysis['image_analysis']['colors']}\n"
            f"Positions: {analysis['image_analysis']['positions']}\n"
            f"Text in Image: {analysis['image_analysis']['text']}\n\n"
            f"Text Analysis:\nSummary: {analysis['text_analysis']['summary']}\n"
            f"Key Phrases: {analysis['text_analysis']['key_phrases']}\n"
            f"Narrative: {analysis['text_analysis']['narrative']}\n\n"
            f"Suggest improvements and rank the overall layout and design aesthetics in percentage."
        )

        # Use GPT-4 model to evaluate and generate a response
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an expert in design and advertisement analysis."},
                {"role": "user", "content": prompt}
            ]
        )

        suggestions = response.choices[0].message.content

        return suggestions


# Load the knowledge base from the file
# with open('data/design_concepts.txt', 'r') as file:
#     knowledge_base = file.read()

# # Instantiate the critic/grading agent
# critic_grading_agent = CriticGradingAgent(openai_image_agent, text_agent, knowledge_base)

# assets_dir = 'data/assets/images'
# image_files = [os.path.join(assets_dir, f) for f in os.listdir(assets_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]
# images = [Image.open(file) for file in image_files]

# # Example usage
# image = images[1]
# text = "Simple advertisement for inspiring travel."
# # analysis = critic_grading_agent.analyze_asset(image, text)
# # print(analysis)
# critic = critic_grading_agent.critic_frame(image, text)
# print(critic)