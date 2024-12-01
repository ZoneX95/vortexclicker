# Auto Clicker with GUI

This is a simple auto-clicker script with a graphical user interface (GUI) built using Python's `tkinter` and `pyautogui` libraries. The script searches for two images (`img1.png` and `img2.png`) on the screen, clicks them in sequence, and repeats the process. The GUI allows you to start and stop the script and provides a status indicator.

## Features

- Clicks on two specified images (`img1.png` and `img2.png`) in sequence.
- Simple GUI with start and stop buttons.
- Status indicator showing ACTIVE or DISABLED state.
- Global key detection for stopping the script with the ESC key.

## Requirements

- Python 3.13.0
- `pyautogui` library
- `opencv-python` and `opencv-python-headless` libraries
- `tkinter` (usually included with Python)
- `keyboard` library

## Installation

1. Clone this repository or download the script.
2. Install the required Python libraries:
    ```sh
    pip install pyautogui opencv-python opencv-python-headless keyboard
    ```

## Usage

1. Ensure you have `img1.png` and `img2.png` in the same directory as the script.
2. Run the script:
    ```sh
    python auto_clicker.py
    ```
3. A GUI window will open:
    - Click the **Start** button to begin the auto-clicking process.
    - Click the **Stop** button to stop the auto-clicking process.
    - The status will display as ACTIVE or DISABLED.
    - Press **ESC** to stop the script at any time.

