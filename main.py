import threading
from gif import choose_gif, display_gif
from lang import generate_sassy_response
from tts import text_to_robotic_speech

def main():
    # Hardcode for now
    input_number = 6  # Number of detected dirt objects
    wall_e = True  # Change this to True if Wall-E is detected

    # Emotional response
    response = generate_sassy_response(input_number, wall_e)
    print(response)

    # Prepare for concurrent tasks
    change_gif_event = threading.Event()  # Event to signal GIF change

    # GIF path setup
    gif_path = choose_gif(input_number, wall_e)
    default_gif_path = "M-O_face_assets/GIFS/blinking_gif.gif"

    # Start the GIF in a separate thread
    gif_thread = threading.Thread(target=display_gif, args=(gif_path, change_gif_event, default_gif_path))
    gif_thread.start()

    # Start the speech in another thread
    speech_thread = threading.Thread(target=text_to_robotic_speech, args=(response, change_gif_event))
    speech_thread.start()

    # Wait for both threads to finish
    gif_thread.join()
    speech_thread.join()

if __name__ == "__main__":
    main()