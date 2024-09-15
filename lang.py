import os
import cohere
from dotenv import load_dotenv
# Load .env file and get API key
load_dotenv()
API_KEY = os.getenv("COHERE_API_KEY")
co = cohere.Client(API_KEY)



def generate_sassy_response(input_number, wall_e):
    if wall_e:
        prompt_template = "Scream and yell at Wall-E to die"
    else:
        prompt_template = (
            "Pretend you are M-O from the movie WALL-E, except your name is DEREK. "
            "You are a very sassy and temperamental cleaning robot. "
            "Give an appropriate response for the input number of dirt {}. "
            "The tone should be more sassy, sarcastic, and angry as the number increases. "
            "The closer the number is to zero though, the calmer you are. "
        )
    prompt = prompt_template.format(input_number)

    response = co.generate(
        model='command-nightly',
        prompt=prompt,
        max_tokens=75,
        temperature=0.7,
    )

    return response.generations[0].text
