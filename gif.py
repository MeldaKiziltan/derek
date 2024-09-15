import pygame
from PIL import Image, ImageSequence
from pathlib import Path

def display_gif(gif_path, change_gif_event, default_gif_path):
    pygame.init()
    
    def load_frames(gif_path):
        """Helper function to load frames from a GIF file."""
        try:
            gif = Image.open(gif_path)
        except IOError:
            print(f"Error: Unable to open file '{gif_path}'")
            return [], []
        
        frames = []
        durations = []
        for frame in ImageSequence.Iterator(gif):
            pygame_image = pygame.image.fromstring(
                frame.convert("RGBA").tobytes(), frame.size, "RGBA")
            frames.append(pygame_image)
            durations.append(frame.info.get('duration', 100))  # Default to 100ms if not specified
        return frames, durations

    # Load the initial GIF
    frames, durations = load_frames(gif_path)
    if not frames:
        return

    # Get the screen's display resolution
    display_info = pygame.display.Info()
    screen_width, screen_height = display_info.current_w, display_info.current_h

    # Get the GIF's frame size
    gif_width, gif_height = frames[0].get_size()

    # Ensure the window size fits the screen resolution if the GIF is too large
    window_width = min(gif_width, screen_width)
    window_height = min(gif_height, screen_height)

    # Create the display window based on the GIF or screen size
    screen = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
    pygame.display.set_caption(Path(gif_path).stem)

    clock = pygame.time.Clock()
    current_frame = 0
    time_elapsed = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # If the event is triggered, switch to the default GIF
        if change_gif_event.is_set():
            frames, durations = load_frames(default_gif_path)
            change_gif_event.clear()  # Reset the event after switching GIFs

        # Clear the screen with a black background
        screen.fill((0, 0, 0))

        # Center the GIF frame on the window
        frame_rect = frames[current_frame].get_rect(center=(window_width//2, window_height//2))
        screen.blit(frames[current_frame], frame_rect.topleft)

        pygame.display.flip()

        time_elapsed += clock.tick()
        if time_elapsed >= durations[current_frame]:
            time_elapsed = 0
            current_frame = (current_frame + 1) % len(frames)

def choose_gif(input_number, wall_e):
    if wall_e:
        return "M-O_face_assets/GIFS/wall-e_mad.gif"
    elif input_number == 0:
        return "M-O_face_assets/GIFS/blinking_gif.gif"
    else:
        return "M-O_face_assets/GIFS/angry_dirt_gif.gif"
