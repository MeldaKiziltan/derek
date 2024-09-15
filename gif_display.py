import sys
from tkinter import Tk, Label, messagebox
from PIL import Image, ImageTk

def display_gif(file_path, width, height):
    # Create the main window
    root = Tk()
    root.title("GIF Display")

    try:
        # Open the GIF file
        img = Image.open(file_path)
    except IOError:
        messagebox.showerror("Error", f"Unable to open file: {file_path}")
        root.destroy()
        return

    # Create a PhotoImage object
    photo = ImageTk.PhotoImage(img)
    
    # Create a label to display the image
    label = Label(root)
    label.pack()

    def update_image(frame):
        img.seek(frame)
        # Resize the image to fit the given dimensions
        resized_frame = img.copy().resize((width, height), Image.Resampling.LANCZOS)
        photo.paste(resized_frame)
        label.config(image=photo)
        root.after(50, update_image, (frame + 1) % img.n_frames)

    # Start the animation
    root.after(0, update_image, 0)

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    # if len(sys.argv) != 4:
    #     print("Usage: python script.py <gif_file_path> <width> <height>")
    #     sys.exit(1)
    
    # file_path = sys.argv[1]
    # width = int(sys.argv[2])
    # height = int(sys.argv[3])
    
    display_gif("M-O_face_assets/GIFS/angry_dirt_gif.gif", 800, 480)