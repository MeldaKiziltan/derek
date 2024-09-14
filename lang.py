import os
import cohere
import numpy as np

from dotenv import load_dotenv
load_dotenv()

API_KEY = os.environ.get("COHERE_API_KEY")
co = cohere.Client(API_KEY)

def generate_sassy_response(input_number):
    # Define a prompt template with placeholders for the input number and tone
    # prompt_template = "Generate a sassy response for the input number {}. The tone should be more sassy as the number increases."
    prompt_template = "Pretend you are M-O from the movie WALL-E, except your name is actually DEREK. You are a very sassy and tempermental cleaning robot. All the dirt is considered a contaminant aboard your space ship. Give an appropriate response for the input number of dirt {}. The tone should be more sassy, angry, and sarcastic as the number increases."

    # Generate a prompt by filling in the placeholders
    prompt = prompt_template.format(input_number)

    response = co.generate(
        model='command-nightly',  # You can choose the appropriate model
        prompt=prompt,
        max_tokens=100,  # Adjusts the length of the response
        temperature=0.7,  # Adjust the temperature for creativity and :sparkles: Spice :sparkles:
    )

    # Return the generated text response
    return response.generations[0].text

input_number = 3
response = generate_sassy_response(input_number)
print(response)

