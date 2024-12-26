from tkinter import *
import front  # Import the front pagemodule, QKY ACESS

# Initialize the root window
root = Tk()
root.geometry("550x620")
root.title("Notepad")
root.config(bg="black")
root.resizable(False, False)# RESIZE HELP

# Create a root frame to hold the pages
root_frame = Frame(root)
root_frame.pack(fill="both", expand=True)

# Show the front page
front.show_front_page(root_frame)

# Main loop
root.mainloop()