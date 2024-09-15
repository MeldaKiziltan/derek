
import json
import base64
import requests
import asyncio
from src.sentiment import generate_face
from viam.robot.client import RobotClient
from viam.components.board import Board
from viam.components.motor import Motor
from viam.components.base import Base
from viam.components.camera import Camera
from viam.components.encoder import Encoder
import pyttsx3
import os
import cohere
from dotenv import load_dotenv

load_dotenv()


API_KEY = os.getenv("COHERE_API_KEY")
co = cohere.Client(API_KEY)


def generate_sassy_response(input_number, wall_e):
    if wall_e:
        prompt_template = "Scream and yell at Wall-E. His existence angers you."
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




async def connect():
    opts = RobotClient.Options.with_api_key(
        api_key='sp9ruf8fvultpqw2xu5rahwpvdgn8wid',
        api_key_id='d2122058-f9f0-43b7-a984-c2995d433493'
    )
    return await RobotClient.at_address('my-rasp-pi-main.oebs8wmwbh.viam.cloud', opts)




async def viam_update():
    machine = await connect()

    # Declaration of all components
    # local
    local = Board.from_robot(machine, "local")

    # right
    right = Motor.from_robot(machine, "right")

    # left
    left = Motor.from_robot(machine, "left")

    # viam_base
    viam_base = Base.from_robot(machine, "viam_base")

    # Renc
    renc = Encoder.from_robot(machine, "Renc")

    # Lenc
    lenc = Encoder.from_robot(machine, "Lenc")

    # cam
    cam = Camera.from_robot(machine, "cam")
    
    engine = pyttsx3.init()
    engine.setProperty('rate', 200)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # For some reason, changing it to 1 gives a french female voice
    engine.setProperty('volume', 5)
    engine.startLoop()

    while True:
        # get the camera image and perform image analysis on it
        cam_return_value = await cam.get_image()
        data = cam_return_value.data
        byte_data = data
        # Convert bytes to Base64
        base64_data = base64.b64encode(byte_data).decode('utf-8')
        url = 'https://api.joseph.ma/walle/process_base64'
        x = requests.post(url, json = {'base64_string':base64_data})
        camera_readings = json.loads(x.text)
        print(camera_readings)
        dirt_counter = camera_readings['redSquares']
        if camera_readings['legoWalle'] == 'True' or camera_readings['paperWalle'] == 'True':
            rant = generate_sassy_response(0, True)
            engine.say(rant, "WallE_rant")
        # send camera readings for sentiment AI

        if dirt_counter > 3:
            rant = generate_sassy_response(dirt_counter, False)
            engine.say(rant, "Dirt_rant")
            right_go = asyncio.create_task(right.go_for(60,-8))
            left_go = asyncio.create_task(left.go_for(60, -8))
            _ = await right_go
            _ = await left_go
        await asyncio.sleep(2)

    # Closes the machine after reading
    await machine.close()


if __name__ == '__main__':
    asyncio.run(viam_update())

