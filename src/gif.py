import pygame
from PIL import Image, ImageSequence
from pathlib import Path
from guizero import App, Picture

def display_gif(gif_path):
    app = App(width=1100, height=700)
    picture = Picture(app, image=gif_path, width=1100, height=700)
    app.display

def choose_gif(input_number, wall_e):
    if wall_e:
        return "./M-O_face_assets/GIFS/wall-e_mad.gif"
    elif input_number == 0:
        return "./M-O_face_assets/GIFS/blinking_gif.gif"
    else:
        return "./M-O_face_assets/GIFS/angry_dirt_gif.gif"
