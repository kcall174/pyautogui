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

### Adding Single Mouse Clicks
```
import pyautogui
import threading
import datetime

screenSize= pyautogui.size() # get screensize
 
def moveMouse(): 
    pyautogui.moveTo95, screenSize[1], duration = 1
    
def clickMouse():
    pyautogui.click()
    main()
    
def main():
    hour = datetime.datetime.now().hour
    if hour == 17 or hour == 12:
        print('end of dat reached')
        quit()
        
    else: 
        threading.Timer(5.0, moveMouse).start()
        threading.Timer(10.0, clickMouse).start()
        
main()
```

