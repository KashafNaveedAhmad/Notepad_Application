from tkinter import *
from PIL import Image, ImageTk
import working  # Import the next stage to show the working area

# Function to show the main working area
def show_main_area(root, title):
    # Hide the title selection frame
    title_selection_frame.pack_forget()  
    # Call the show_main_area function from working.py and pass the root and title
    working.show_main_area(root, title)

# Function to show the title selection screen
def show_title_selection(root):
    global title_selection_frame
    title_selection_frame = Frame(root, bg="black")
    title_selection_frame.pack(fill="both", expand=True)

    # Load and display the image
    image = Image.open("Notepad_Application\project\\3.webp")  # Replace with your image path
    image = image.resize((450, 300))  # Resize the image to fit the screen width
    photo = ImageTk.PhotoImage(image)
    image_label = Label(title_selection_frame, image=photo, bg="black")
    image_label.photo = photo  # Keep a reference to avoid garbage collection
    image_label.pack(pady=10)  # Add padding between image and other elements

    # Title Selection Design
    title_label = Label(title_selection_frame, text="Enter Notepad Title", font=("Arial", 20, "bold"), bg="black", fg="white")
    title_label.pack(pady=20, padx=100)

    # Entry for title input
    title_entry = Entry(title_selection_frame, font=("Arial", 14), width=40)
    title_entry.pack(pady=10)

    # Button to proceed to the next screen (working area)
    next_button = Button(title_selection_frame, text="Next", font=("Arial", 12), bg="white", fg="black", 
                         command=lambda: show_main_area(root, title_entry.get()))  # Pass the entered title
    next_button.pack(pady=20)

# Example root window (this can be handled in your main script)
if __name__ == "__main__":
    root = Tk()
    root.geometry("550x620")
    root.title("Notepad Title Selection")

    show_title_selection(root)  # Show the title selection screen

    root.mainloop()
