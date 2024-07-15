import sys
import os
from src.text_analysis import text_agent
from src.image_analysis import image_agent
from src.critic_grading_agent import CriticGradingAgent
from PIL import Image


def evaluate_image(file, description):
    # Load the knowledge base from the file
    with open('data/design_concepts.txt', 'r') as file:
        knowledge_base = file.read()

    # Instantiate the critic/grading agent
    critic_grading_agent = CriticGradingAgent(image_agent, text_agent, knowledge_base)

    # Example usage
    image = Image.open(file)
    text =  description
    # analysis = critic_grading_agent.analyze_asset(image, text)
    # print(analysis)
    critic = critic_grading_agent.critic_frame(image, text)
    evaluation_result = critic
    return evaluation_result
