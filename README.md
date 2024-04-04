<h1> Automation with PyAutoGUI </h1>

note: user can force pyautogui to stop running by moving the mouse to a corner of the screen

### Install PyAutoGUI
<code> pip3 install pyautogui </code> 

### Making a square with pyautogui 
<code>import pyautogui</code>

### Move mouse by iterating 100 times (can change how any amount)
```
for i in range(100): 
    pyautogui.moveTo(100, 100, duration = 0.25)
    pyautogui.moveTo(200, 100, duration = 0.25)
    pyautogui.moveTo(200, 200, duration = 0.25)
    pyautogui.moveTo(100, 200, duration = 0.25)
    
```
