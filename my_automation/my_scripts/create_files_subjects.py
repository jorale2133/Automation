###Create Files

import os as system
import tkinter as tk
from tkinter import filedialog

# Create a GUI window
root = tk.Tk()
root.withdraw()  # Hide the root window
# Ask the user to select a directory
directory = filedialog.askdirectory(title="Select a directory to create files")
if not directory:
    print("No directory selected. Exiting.")
    exit()
# List of directories to create
files = ['Notas', 'Tareas', 'Libros', 'Recursos']

for file in files:
    file_path = system.path.join(directory, file)
    if not system.path.exists(file_path):
        system.mkdir(file_path)
        print(f"Directory '{file}' created.")
    else:
        print(f"Directory '{file}' already exists.")