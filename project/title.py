from tkinter import *
import working  # Import the next stage
def show_main_area(root, title):
    title_selection_frame.pack_forget()  # Remove title selection frame
    working.show_main_area(root, title)  # Call main working area

def show_title_selection(root):
    global title_selection_frame
    title_selection_frame = Frame(root, bg="black")
    title_selection_frame.pack(fill="both", expand=True)

    # Title Selection Design
    title_label = Label(title_selection_frame, text="Enter Notepad Title", font=("Arial", 20, "bold"), bg="black", fg="white")
    title_label.pack(pady=20,padx=100)

    title_entry = Entry(title_selection_frame, font=("Arial", 14), width=40)
    title_entry.pack(pady=10)

    next_button = Button(title_selection_frame, text="Next", font=("Arial", 12), bg="white", fg="black", 
                         command=lambda: show_main_area(root, title_entry.get()))
    next_button.pack(pady=20)
