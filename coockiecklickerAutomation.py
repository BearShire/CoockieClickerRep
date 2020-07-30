# -*- coding: utf-8 -*-
"""
AutoClicker
https://orteil.dashnet.org/cookieclicker/
Created on Tue Apr 28 00:14:51 2020
Updated on Tue Apr 28 13:35:03 2020


@author: Smith
"""

import pyautogui as pag
import webbrowser
import time
import sys
import tkinter as tk, win32api, win32con, pywintypes

x = 2238
y = 497
Dur =  0.0001
distance= 770
CoockieClicks = 100
pag.PAUSE = 0.001
MaxI = 3 
MaxI +=1 #change due to index starts from 0

#Main action
def AutomatedClicking(CoockieClicks):
    
    start_time = time.time()
    TotalCookieClicks = 0
    
    for MainI in range(1,MaxI):
        pag.moveTo(x, y, duration=Dur)
        
        for i in range(0,CoockieClicks):
            try:
                pag.click()
            
            except KeyboardInterrupt():
                sys.exit()
            
        pag.moveTo(3556, 280, duration=Dur)
        for i in range(0,5):
            pag.click()
        distance= 770    
            
        for i in range(0,7):   
            pag.moveTo(3652, distance, duration=Dur)
            for i in range(0,5):
                pag.click()
            
            distance -=  62
            
        TotalCookieClicks += CoockieClicks
        CoockieClicks += round(CoockieClicks*0.02)
        print("CoockieClicks:" + str(CoockieClicks))
        print("Iteration: " + str(MainI) + " of " + str(MaxI-1))
    
    EndTime = round(time.time() - start_time)
    pag.alert(text="Bot ended work!\nTotal clicks: " + str(TotalCookieClicks) + "\nTotal time: " + str(EndTime) + " seconds", title="Work done!" )
    

#Prompt and init
def Prompting(CoockieClicks):
    test = pag.confirm(text='The bot is about to start working.\
                       \nNumber of iterations: ' + str(MaxI-1) + "\
                       \nNumber of initial clicks per iteration:  " + str(CoockieClicks)
                       , title='Please click ok to proceed', buttons=['OK', 'Cancel'])
    if test == "OK":
        print("Bot starting")
        Site = "https://orteil.dashnet.org/cookieclicker/"
        #webbrowser.open_new(Site)
        time.sleep(2)
        
    else:
        print("Bot action canceled")
        sys.exit()    
     
#Text
label = tk.Label(text='Bot is active!', font=('Times New Roman','70'), fg='red', bg='brown')
label.master.overrideredirect(True)
label.master.geometry("+1980+800")
label.master.lift()
label.master.wm_attributes("-topmost", True)
label.master.wm_attributes("-disabled", True)
label.master.wm_attributes("-transparentcolor", "brown")

hWindow = pywintypes.HANDLE(int(label.master.frame(), 16))
# http://msdn.microsoft.com/en-us/library/windows/desktop/ff700543(v=vs.85).aspx
# The WS_EX_TRANSPARENT flag makes events (like mouse clicks) fall through the window.
exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT
win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)

label.after(1 , label.pack())
label.after(1 , Prompting(CoockieClicks))
label.after(1 , AutomatedClicking(CoockieClicks))
label.after(1 , label.master.destroy)
label.mainloop()
    
   