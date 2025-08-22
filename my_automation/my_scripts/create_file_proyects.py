###Create Files

import os as system
import tkinter as tk    
from tkinter import filedialog
import openpyxl

# Create a GUI window
root = tk.Tk()
root.withdraw()  # Hide the root window
# Ask the user to select a directory
directory = filedialog.askdirectory(title="Select a directory to create files")
if not directory:
    print("No directory selected. Exiting.")
    exit()
# List of directories to create
main_files = ['0_managment', '1_docs', '2_implementation', '3_resources', '4_results']
for file in main_files:
    file_path = system.path.join(directory, file)
    if not system.path.exists(file_path):
        system.mkdir(file_path)
        print(f"Directory '{file}' created.")
    else:
        print(f"Directory '{file}' already exists.")
# Cretae subdirectories in '0_managment'
workbook = openpyxl.Workbook()
workbook.save(system.path.join(directory, '0_managment', 'Schedule.xlsx'))# Create an empty Excel file
sub_files = ['ProyectPlan.docx', 'Material and budget.docx', 'Tasks.docx']
sub_directory = system.path.join(directory, '0_managment')
for file in sub_files:
    file_path = system.path.join(sub_directory, file)
    if not system.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write("")  # Create an empty file
        print(f"File '{file}' created in '0_managment'.")
    else:
        print(f"File '{file}' already exists in '0_managment'.")


# Create subdirectories in '1_docs'
sub_files_docs = ['Report.docx', 'Documentation.docx']
sub_directory_docs = system.path.join(directory, '1_docs')  
for file in sub_files_docs:
    file_path = system.path.join(sub_directory_docs, file)
    if not system.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write("")  # Create an empty file
        print(f"File '{file}' created in '1_docs'.")
    else:
        print(f"File '{file}' already exists in '1_docs'.")
# Create subdirectories in '2_implementations'
sub_files_impl = ['Software', 'Hardware', 'Simulations']
sub_directory_impl = system.path.join(directory, '2_implementation')
for file in sub_files_impl: 
    file_path = system.path.join(sub_directory_impl, file)
    if not system.path.exists(file_path):
        system.mkdir(file_path)
        print(f"Directory '{file}' created in '2_implementation'.")
    else:
        print(f"Directory '{file}' already exists in '2_implementation'.")
# Create subdirectories in '3_resources'
sub_files_res = ['Images', 'Diagrams', 'Data', 'References Materials']
sub_directory_res = system.path.join(directory, '3_resources')
for file in sub_files_res:
    file_path = system.path.join(sub_directory_res, file)
    if not system.path.exists(file_path):
        system.mkdir(file_path)
        print(f"Directory '{file}' created in '3_resources'.")
    else:
        print(f"Directory '{file}' already exists in '3_resources'.")
# Create subdirectories in '4_results'
sub_files_resu = ['Results', 'Analysis', 'Conclusions']
sub_directory_resu = system.path.join(directory, '4_results')
for file in sub_files_resu:
    file_path = system.path.join(sub_directory_resu, file)
    if not system.path.exists(file_path):
        system.mkdir(file_path)
        print(f"Directory '{file}' created in '4_results'.")
    else:
        print(f"Directory '{file}' already exists in '4_results'.")
# End of the script
print("All directories and files have been created successfully.")