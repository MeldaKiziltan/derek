import pyttsx3

def text_to_robotic_speech(response, change_gif_event):
    engine = pyttsx3.init()

    engine.setProperty('rate', 200)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # For some reason, changing it to 1 gives a french female voice
    engine.setProperty('volume', 5)

    # Convert text to speech
    engine.say(response)
    engine.runAndWait()

    # Switch to blinking when talking is done
    change_gif_event.set()