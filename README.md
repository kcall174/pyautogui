<h1> Automation with PyAutoGUI </h1>

note: user can force pyautogui to stop running by moving the mouse to a corner of the screen

### Install PyAutoGUI
<code> pip3 install pyautogui </code> 

### Import pyautogui
<code>import pyautogui</code>

### Move mouse in a square - here we iterate 100 times (user can change amount)
```
for i in range(100): 
    pyautogui.moveTo(100, 100, duration = 0.25)
    pyautogui.moveTo(200, 100, duration = 0.25)
    pyautogui.moveTo(200, 200, duration = 0.25)
    pyautogui.moveTo(100, 200, duration = 0.25)
    
```
