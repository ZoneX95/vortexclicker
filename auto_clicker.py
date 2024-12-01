import pyautogui
import os
import time
import threading
import tkinter as tk
import keyboard

# Define the folder where the script and images are located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Paths to the images
img1_path = os.path.join(script_dir, 'img1.png')
img2_path = os.path.join(script_dir, 'img2.png')

# Global variable to control the script status
running = False

# Function to click on an image and report success or failure
def click_image(image_path, confidence=0.8):
    try:
        location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
        if location:
            pyautogui.click(location)
            print(f"Success: Clicked on {os.path.basename(image_path)}")
        else:
            print(f"Failure: Image {os.path.basename(image_path)} not found on screen.")
    except pyautogui.ImageNotFoundException:
        print(f"Error: Image {os.path.basename(image_path)} could not be located.")

# Function to run the clicker script
def run_clicker():
    global running
    while running:
        click_image(img1_path)
        time.sleep(1)  # Short delay between clicks
        click_image(img2_path)
        time.sleep(3)  # Wait 3 seconds before repeating the loop

# Function to start the clicker script
def start_clicker():
    global running
    if not running:
        running = True
        status_label.config(text="Status: ACTIVE", fg="green")
        threading.Thread(target=run_clicker).start()

# Function to stop the clicker script
def stop_clicker():
    global running
    if running:
        running = False
        status_label.config(text="Status: DISABLED", fg="red")

# Function to handle key press events
def on_key_press(event):
    if event.name == 'esc':
        stop_clicker()

# Listen for the Esc key press globally
keyboard.on_press(on_key_press)

# Create the GUI
root = tk.Tk()
root.title("Auto Clicker")
root.geometry("500x300")  # Set initial window size
root.resizable(True, True)  # Allow window resizing

# Create a frame for the buttons and status
frame = tk.Frame(root)
frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

start_button = tk.Button(frame, text="Start", command=start_clicker, font=("Helvetica", 14), width=15)
start_button.pack(pady=10)

stop_button = tk.Button(frame, text="Stop", command=stop_clicker, font=("Helvetica", 14), width=15)
stop_button.pack(pady=10)

status_label = tk.Label(frame, text="Status: DISABLED", fg="red", font=("Helvetica", 14))
status_label.pack(pady=10)

# Instructions label
instructions_label = tk.Label(frame, text="Press Esc to stop the script", font=("Helvetica", 12))
instructions_label.pack(pady=10)

root.mainloop()
