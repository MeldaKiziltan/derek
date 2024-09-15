import threading
from src.gif import choose_gif, display_gif
from src.lang import generate_sassy_response
from src.tts import text_to_robotic_speech

def generate_face(wall_e, input_number):

    # Emotional response
    response = generate_sassy_response(input_number, wall_e)
    print(response)

    # Prepare for concurrent tasks
    change_gif_event = threading.Event()  # Event to signal GIF change

    # GIF path setup
    gif_path = choose_gif(input_number, wall_e)
    default_gif_path = "./M-O_face_assets/GIFS/blinking_gif.gif"

    # Start the GIF in a separate thread
    display_gif(gif_path)

    # Start the speech in another thread
    # speech_thread = threading.Thread(target=text_to_robotic_speech, args=(response, change_gif_event))
    # speech_thread.start()

    # Wait for both threads to finish
    # speech_thread.join()
