import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from src.text_analysis import text_agent
from src.image_analysis import image_agent
from src.openai_image_analysis import openai_image_agent
from src.critic_grading_agent import CriticGradingAgent
from PIL import Image


def evaluate_image(img, imageAnalyzer, description):
    # Load the knowledge base from the file
    with open('data/design_concepts.txt', 'r') as file:
        knowledge_base = file.read()
        
    if(imageAnalyzer == 'YOLO + Tesseract'):
        critic_grading_agent = CriticGradingAgent(image_agent, text_agent, knowledge_base)
    if(imageAnalyzer == 'OpenAI GPT-4o'):
        critic_grading_agent = CriticGradingAgent(image_agent, text_agent, knowledge_base)

    # Instantiate the critic/grading agent

    # Example usage
    image = Image.open(img)
    text =  description
    # analysis = critic_grading_agent.analyze_asset(image, text)
    # print(analysis)
    critic = critic_grading_agent.critic_frame(image, text)
    evaluation_result = critic
    return evaluation_result
