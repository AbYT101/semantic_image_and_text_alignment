import os
from PIL import Image
from image_composing_with_diffusor import ImageComposingAgent
from critic_grading_agent import CriticGradingAgent
from text_analysis import text_agent
from openai_image_analysis import openai_image_agent

class AdGenerationPipeline:
    def __init__(self, composer_agent, critic_agent):
        self.composer_agent = composer_agent
        self.critic_agent = critic_agent

    def generate_ad(self, concept: dict, target_score: int = 75):
        current_score = 0
        iteration = 0
        
        while current_score < target_score:
            iteration += 1
            print(f"Iteration {iteration}: Composing image...")

            # Step 1: Compose the image using the composer agent
            self.composer_agent.compose_image(concept)
            generated_image = self.composer_agent.generated_image
            
            if not generated_image:
                print("Failed to generate an image. Exiting.")
                return

            # Save the generated image for inspection
            generated_image_path = f'generated_ad_iteration_{iteration}.png'
            generated_image.save(generated_image_path)
            print(f"Generated image saved at {generated_image_path}")

            # Step 2: Criticize the generated image using the critic agent
            print("Criticizing the generated image...")
            critic_feedback = self.critic_agent.critic_frame(generated_image, concept["explanation"])

            # Extract the score and suggestions from the critic feedback
            current_score = int(critic_feedback.get("score", 0))
            suggestions = critic_feedback.get("suggestions", [])

            print(f"Critic score: {current_score}%")
            print(f"Suggestions: {suggestions}")

            # If the score is below the target, improve the image
            if current_score < target_score:
                print("Improving the image based on feedback...")
                self.composer_agent.improve_image(critic_feedback["image_analysis"], suggestions)

        print("Target score achieved. Final ad generated.")
        final_image_path = 'final_generated_ad.png'
        self.composer_agent.generated_image.save(final_image_path)
        print(f"Final generated image saved at {final_image_path}")

# if __name__ == "__main__":
    # # Define the concept dictionary
    # concept = {
    #     "concept": "Driven by Passion",
    #     "assets": {
    #         "Background": "background.png",
    #         "Logo": "logo.png",
    #         "Main Character": "main_character.png",
    #         "Secondary Character": "secondary_character.png",
    #         "Interactive Element": "cta.png",
    #     },
    #     "implementation": {
    #         "frame_1": {
    #             "description": "A scene of a Lexus car on a race track with the text 'Passion for Speed'.",
    #             "interaction_type": "Swipe",
    #             "next_frame": "frame_2",
    #             "duration": "3 seconds"
    #         }
    #     },
    #     "explanation": "This concept aligns with Lexus's brand identity of delivering superior quality automobiles."
    # }

    # # Initialize the agents
    # composer_agent = ImageComposingAgent(model_name_or_path="CompVis/stable-diffusion-v1-4")
    # critic_agent = CriticGradingAgent(openai_image_agent, text_agent, 'data/design_concepts.txt')

    # # Create the ad generation pipeline and generate the ad
    # ad_pipeline = AdGenerationPipeline(composer_agent, critic_agent)
    # ad_pipeline.generate_ad(concept)
