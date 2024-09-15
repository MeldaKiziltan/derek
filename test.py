from PIL import Image

img = Image.open("M-O_face_assets/mad_7.png")
img_rgba = img.convert("RGBA")
img_rgba.save("output_image.png")