from tkinter import *
from tkinter import filedialog, messagebox
import front
import subprocess
import sys
import title
import theme

def apply_theme(widget, theme_dict):
    """Apply theme to a widget."""
    widget.config(bg=theme_dict["bg"], fg=theme_dict["fg"])

def toggle_theme():
    """Toggle between light and dark themes."""
    global current_theme
    if current_theme == theme.LIGHT_THEME:
     current_theme = theme.DARK_THEME
    elif current_theme == theme.DARK_THEME:
        current_theme = theme.SLATE_GREY_THEME
    elif current_theme == theme.SLATE_GREY_THEME:
        current_theme = theme.STEEL_BLUE_2_THEME
    elif current_theme == theme.STEEL_BLUE_2_THEME:
        current_theme = theme.DARK_ORCHID_4_THEME
    elif current_theme == theme.DARK_ORCHID_4_THEME:
        current_theme = theme.HOT_PINK_THEME
    else:
        current_theme = theme.LIGHT_THEME
    
    refresh_ui()

def refresh_ui():
    """Refresh the UI to apply the new theme."""
    for widget in main_frame.winfo_children():
        apply_theme(widget, current_theme)
        
def save_file(entry):
    """Save the content of the text area to a file."""
    open_file = filedialog.asksaveasfile(mode='w', defaultextension='.txt')  # File save dialog
    if open_file is None:
        return
    text = str(entry.get(1.0, END))
    open_file.write(text)
    open_file.close()

def open_file(entry):
    """Open a file and display its content in the text area."""
    file = filedialog.askopenfile(mode='r', filetypes=[('Text Files', '*.txt')])  # File open dialog
    if file is not None:
        content = file.read()
        entry.delete(1.0, END)  # Clear existing content
        entry.insert(INSERT, content)

def show_main_area(root_frame, title, content=""):
    """Display the main working area of the notepad with title and content."""
    global main_frame
    main_frame = Frame(root_frame, bg="black")
    main_frame.pack(fill="both", expand=True)

    # Main Area Design
    heading = Label(main_frame, text=title, font=("Arial", 14, "bold"), bg="black", fg="white")
    heading.pack(pady=5)  # Reduced padding for compact design

    entry = Text(main_frame, height=32, width=72, wrap=WORD, bg="white", fg="black")
    entry.pack(pady=5)  # Adjusted padding for balance

    # Insert content if provided
    if content:
        entry.insert(1.0, content)

    # Buttons for file actions
    save_button = Button(main_frame, text="Save File", bg="white", fg="black", 
                         command=lambda: save_file(entry))
    save_button.pack(side=LEFT, padx=10, pady=10)

    open_button = Button(main_frame, text="Open File", bg="white", fg="black", 
                         command=lambda: open_file(entry))
    open_button.pack(side=LEFT, padx=10, pady=10)

    new = Button(main_frame, text="Another Doc", bg="white", fg="black", 
                         command=lambda:subprocess.run(["python", "Notepad_Application\project\main.py"]) ) # Placeholder for navigation
    new.pack(side=LEFT, padx=10, pady=10)

    exit_button = Button(main_frame, text="Exit", bg="white", fg="black", 
                         command=root_frame.quit)  # This will quit the entire app
    exit_button.pack(side=RIGHT, padx=10, pady=10)

    apply_theme(open_button, current_theme)

    theme_toggle_button = Button(main_frame, text="Toggle Theme", command=toggle_theme)
    theme_toggle_button.pack(side=RIGHT, padx=10, pady=10)
    apply_theme(theme_toggle_button, current_theme)

# Set initial theme to LIGHT_THEME
current_theme = theme.LIGHT_THEME
if __name__ == "__main__":
    root = Tk()
    root.geometry("550x620")
    root.title("Notepad")
    
    # Show title selection initially
    title.show_title_selection(root)
    
    root.mainloop()