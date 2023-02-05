import tkinter as tk
import subprocess

# Function to open the first Python file
def open_first_file():
    subprocess.call(["python", "file1.py"])

# Function to open the second Python file
def open_second_file():
    subprocess.call(["python", "file2.py"])

# Create the window
root = tk.Tk()
root.title("Open Files")

# Create the main frame
main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)

# Create the first button
first_button = tk.Button(main_frame, text="Open File 1", command=open_first_file)
first_button.pack()

# Create the second button
second_button = tk.Button(main_frame, text="Open File 2", command=open_second_file)
second_button.pack()

# Start the event loop
root.mainloop()
