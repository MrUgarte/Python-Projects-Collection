import pandas as pd
import pyautogui as pg
import time
import webbrowser as web
import os 

# Program to send messages by wsp web, including an image to be selected by route
# To get the coordinates for pg you can use my position capture program
# Do you need a xlsx file with the names and numbers of the contacts and the image
def send_message_whatsapp(number, msj):
    url = f"https://web.whatsapp.com/send?phone={number}&text={msj}"
    web.open(url)
    time.sleep(8)
    pg.click(1103, 1339) # Icon +
    time.sleep(3)
    pg.click(1135, 1121) # Select image section 
    time.sleep(3)
    pg.write("img.png") # Select image by automatic write, you must have recently opened the image section in wsp web, otherwise you will have to search by route.
    pg.press('enter')
    time.sleep(3)
    pg.click(2041, 1315) # Send msg
    time.sleep(5)
    os.system("taskkill /im chrome.exe /f") # This is to close the current browser window

# Read excel file and obtain number and name, A:B is the range of the columns
df = pd.read_excel('wsp.xlsx', usecols='A:B')

# Iterate through the dataframe
for key, row in df.iterrows():
    # Name of columns
    name = row['NOMBRE']
    number = row['NUMERO']
    msj = f"""Hi {name}, I'm marco and I'm writing from my automated python script"""
    print(msj)
    send_message_whatsapp(number, msj)
