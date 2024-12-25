from tkinter import *
from PIL import Image, ImageTk  # For displaying images
import title  # Import the next stage

def show_title_selection(root):
    front_frame.pack_forget()  # Remove front page frame
    title.show_title_selection(root)  # Call title selection screen


def show_front_page(root):
    global front_frame
    front_frame = Frame(root, bg="black")
    front_frame.pack(fill="both", expand=True)

    # Front Page Design
    startup_label = Label(front_frame, text="Welcome to Notepad", font=("Arial", 24, "bold"), bg="black", fg="white")
    startup_label.pack(pady=20)

    # Add an image (Ensure you have a valid image file named "notepad_image.png")
    image = Image.open("1.jpg")
    image = image.resize((400, 200))
    photo = ImageTk.PhotoImage(image)
    image_label = Label(front_frame, image=photo, bg="black")
    image_label.photo = photo  # Keep a reference to avoid garbage collection
    image_label.pack(pady=10)

    start_button = Button(front_frame, text="Create New File", font=("Arial", 14), bg="white", fg="black", 
                        command=lambda: show_title_selection(root))
    start_button.pack(pady=20)
