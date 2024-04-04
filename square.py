# Making a square with pyautogui 
import pyautogui

# Move mouse by iterating 100 times (can change how any amount)
for i in range(100): 
    pyautogui.moveTo(100, 100, duration = 0.25)
    pyautogui.moveTo(200, 100, duration = 0.25)
    pyautogui.moveTo(200, 200, duration = 0.25)
    pyautogui.moveTo(100, 200, duration = 0.25)
    
 
