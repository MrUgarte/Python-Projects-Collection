# Mouse Position Capture Program

This program allows you to capture the current position of the cursor on your screen. It is especially useful for automations and scripts that require precise coordinates.

## Description

The program displays the real-time position of the cursor on the screen. By pressing `Ctrl + Shift + Left`, it captures and displays the last recorded position. You can exit the program by pressing the `ESC` key.

## Usage Instructions

1. Clone or download this repository.
2. Make sure you have Python installed on your machine.
3. Install the required libraries by running the following command in the terminal:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the program with the following command:

    ```bash
    python capture_mouse_position.py
    ```

5. Once running, the terminal will display the cursor coordinates in real-time. Use the following key combinations:
   - **`Ctrl + Shift + Left`**: Captures and displays the current cursor position.
   - **`ESC`**: Exits the program.

## Requirements

- Python 3.x
- Libraries specified in `requirements.txt`

## Libraries Used

- **pyautogui**: To retrieve the cursor's position.
- **keyboard**: To capture keystrokes and assign specific actions.

---

## Example Output
When you run the program, the terminal will display something similar to:

Program to capture mouse position Press Ctrl+Shift+left to capture mouse position Press ESC to exit
X: 500 Y: 300... Last position: X: 500 Y: 300
You have left the program...

