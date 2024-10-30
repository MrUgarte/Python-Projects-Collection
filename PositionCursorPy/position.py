import pyautogui
import time
import keyboard

print("Program to capture mouse position")
print("Press Ctrl+Shift+left to capture mouse position")
print("Press ESC to exit")
print("----------------------------------------------------------")

try:
    while True:
        x, y = pyautogui.position()
        positionStr = f"X: {x} Y: {y}"
        print(positionStr, end="...\r")
      

        if keyboard.is_pressed("ctrl") and keyboard.is_pressed("shift") and keyboard.is_pressed("left"):
            print("Last position: ", positionStr)
            time.sleep(0.5)
           
        
        if keyboard.is_pressed("esc"):
            print("----------------------------------------------------------")
            print("You have left the program...")
            break
        
except KeyboardInterrupt:
    print("")
