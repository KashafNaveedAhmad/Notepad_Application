from tkinter import *
from PIL import Image, ImageTk  # For displaying images
from tkinter import filedialog  # To open a file dialog
import working 
import title  # Import the working file to show the notepad area

def show_title_selection(root):
    front_frame.pack_forget()  # Remove front page frame
    title.show_title_selection(root)  # Call title selection screen

def open_file_in_working(root):
    """Function to open a file and display its content in the working area."""
    file = filedialog.askopenfile(mode='r', filetypes=[('Text Files', '*.txt')])  # File open dialog
    if file is not None:
        content = file.read()  # Read the content of the file
        filename = file.name.split("/")[-1]  # Extract the file name from the file path
        file.close()
        
        # Remove any existing frames before showing the new content
        for widget in root.winfo_children():
            widget.destroy()  # Clear existing content
            
        # Call working.show_main_area with the content of the file
        working.show_main_area(root, filename, content)  # Pass the file name and content to the working area

def show_front_page(root):
    global front_frame
    front_frame = Frame(root, bg="black")
    front_frame.pack(fill="both", expand=True)

    # Front Page Design
    startup_label = Label(front_frame, text="Welcome to Notepad", font=("Arial", 24, "bold"), bg="black", fg="white")
    startup_label.pack(pady=20)

    # Add an image (Ensure you have a valid image file named "notepad_image.png")
    image = Image.open("project\\2.jpeg")
    image = image.resize((400, 200))
    photo = ImageTk.PhotoImage(image)
    image_label = Label(front_frame, image=photo, bg="black")
    image_label.photo = photo  # Keep a reference to avoid garbage collection
    image_label.pack(pady=10)

    # Button to create a new file
    start_button = Button(front_frame, text="Create New File", font=("Arial", 14), bg="white", fg="black", 
                        command=lambda: show_title_selection(root))
    start_button.pack(pady=20)

    # Button to open an existing file
    open_button = Button(front_frame, text="Open a File", font=("Arial", 14), bg="white", fg="black", 
                         command=lambda: open_file_in_working(root))  # Calls the function to open the file in working.py
    open_button.pack(pady=10)
