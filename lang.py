# import os
# import cohere
# import numpy as np

# from dotenv import load_dotenv
# load_dotenv()

# API_KEY = os.environ.get("COHERE_API_KEY")
# co = cohere.Client(API_KEY)

# def generate_sassy_response(input_number):
#     # Define a prompt template with placeholders for the input number and tone
#     # prompt_template = "Generate a sassy response for the input number {}. The tone should be more sassy as the number increases."
#     prompt_template = "Pretend you are M-O from the movie WALL-E, except your name is actually DEREK. You are a very sassy and tempermental cleaning robot. All the dirt is considered a contaminant aboard your space ship. Give an appropriate response for the input number of dirt {}. The tone should be more sassy, angry, and sarcastic as the number increases."

#     # Generate a prompt by filling in the placeholders
#     prompt = prompt_template.format(input_number)

#     response = co.generate(
#         model='command-nightly',  # You can choose the appropriate model
#         prompt=prompt,
#         max_tokens=100,  # Adjusts the length of the response
#         temperature=0.7,  # Adjust the temperature for creativity and :sparkles: Spice :sparkles:
#     )

#     # Return the generated text response
#     return response.generations[0].text

# input_number = 3
# response = generate_sassy_response(input_number)
# print(response)

import os
import cohere
import numpy as np
import pygame
from dotenv import load_dotenv

import pygame
from PIL import Image
# Load .env file and get API key
load_dotenv()
API_KEY = os.getenv("COHERE_API_KEY")
co = cohere.Client(API_KEY)

# Initialize Pygame for displaying images or GIFs
pygame.init()
screen = pygame.display.set_mode((800, 480))  # Set this to match your screen resolution


import pygame
import sys
from pathlib import Path
from PIL import Image, ImageSequence

def display_gif(gif_path):
    pygame.init()
    
    try:
        gif = Image.open(gif_path)
    except IOError:
        print(f"Error: Unable to open file '{gif_path}'")
        return

    frames = []
    durations = []
    for frame in ImageSequence.Iterator(gif):
        pygame_image = pygame.image.fromstring(
            frame.convert("RGBA").tobytes(), frame.size, "RGBA")
        frames.append(pygame_image)
        durations.append(frame.info.get('duration', 100))  # Default to 100ms if not specified

    if not frames:
        print(f"Error: No frames found in '{gif_path}'")
        return

    screen = pygame.display.set_mode(frames[0].get_size())
    pygame.display.set_caption(Path(gif_path).stem)
    
    clock = pygame.time.Clock()
    current_frame = 0
    time_elapsed = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.blit(frames[current_frame], (0, 0))
        pygame.display.flip()

        time_elapsed += clock.tick()
        if time_elapsed >= durations[current_frame]:
            time_elapsed = 0
            current_frame = (current_frame + 1) % len(frames)

def generate_sassy_response(input_number, wall_e):
    # Define prompt template based on whether Wall-E is in the picture
    if wall_e:
        prompt_template = (
            "Scream and yell at Wall-E to die"
        )
    else:
        prompt_template = (
            "Pretend you are M-O from the movie WALL-E, except your name is DEREK. "
            "You are a very sassy and temperamental cleaning robot. "
            "Give an appropriate response for the input number of dirt {}. "
            "The tone should be more sassy, sarcastic, and angry as the number increases."
        )

    # Generate the prompt by filling in the input number
    prompt = prompt_template.format(input_number)

    # Use Cohere to generate the sassy response
    response = co.generate(
        model='command-nightly',
        prompt=prompt,
        max_tokens=50,
        temperature=0.7,  # Adjust for creativity and tone
    )

    return response.generations[0].text

def choose_gif(input_number, wall_e):
    """Selects the appropriate GIF based on the input number or Wall-E's presence."""
    if wall_e:
        return "M-O_face_assets/GIFS/wall-e_mad.gif"  # Evil mad
    elif input_number == 0:
        return "M-O_face_assets/GIFS/blinking_gif.gif"  # Chill
    else:
        return "M-O_face_assets/GIFS/angry_dirt_gif.gif"  # MUST CLEAN

# Main logic
if __name__ == "__main__":
    input_number = 3  # Number of detected dirt objects
    wall_e = True  # Change this to True if Wall-E is detected

    # Generate the sassy response
    # response = generate_sassy_response(input_number, wall_e)
    # print(response)

    # Choose and display the appropriate GIF

    gif_path = choose_gif(input_number, wall_e)

    print(gif_path)
    
    display_gif(gif_path)
