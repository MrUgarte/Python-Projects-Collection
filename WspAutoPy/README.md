# WhatsApp Automated Message Sender

This program allows you to automatically send personalized messages through WhatsApp Web to a list of contacts, with the option to attach an image. It uses data from an Excel file that contains names and phone numbers.

## Description

The program opens WhatsApp Web in a browser, sends a customized message to each contact, attaches an image file, and closes the browser window afterward. This script requires an Excel file (`wsp.xlsx`) with columns for `NAME` and `NUMBER`. **Note:** You need to be logged into WhatsApp Web for this to work, and you may need to adjust click coordinates for your screen.

## Usage Instructions

1. Clone or download this repository.
2. Make sure you have Python installed on your computer.
3. Install the required libraries by running the following command in the terminal:

    ```bash
    pip install -r requirements.txt
    ```

4. Prepare the Excel file (`wsp.xlsx`) with the following columns:
    - **NOMBRE**: Contact name
    - **NUMERO**: Contact phone number (with country code, e.g., +123456789)

5. Run the program with the following command:

    ```bash
    python send_whatsapp_message.py
    ```

## Requirements

- Python 3.x
- Libraries specified in `requirements.txt`

## Libraries Used

- **pandas**: To read and manage contact data from the Excel file.
- **pyautogui**: To automate mouse clicks and typing.
- **time**: To manage delays between actions.
- **webbrowser**: To open WhatsApp Web in the default browser.
- **os**: To close the browser after sending the message.

---

## Important Notes

- **Image Attachment**: The image file is automatically selected based on a predefined path. Make sure the image (`img.png`) is in the current directory or adjust the path in the code.
- **Coordinates**: You might need to update the `pg.click()` coordinates based on your screen's resolution. To get the correct coordinates, you can use a separate mouse position capture tool.

## Example Output

The program will print a message for each contact to confirm the message content:

