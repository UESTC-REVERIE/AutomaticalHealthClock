from ctypes import sizeof
from tkinter import CENTER, LEFT, RIGHT
from turtle import left, right, tilt
import pyautogui
import time
import keyboard
import sys
def whereami():
    print(pyautogui.position())
if __name__=='__main__':
    def clickBySprite(url,warning):
        time_start=time.time()
        while True:
            time_end=time.time()
            pos=pyautogui.locateOnScreen(url)
            if pos!=None:
                pyautogui.click(pos,button='left')
                return
            if time_end-time_start>=30:
                print(warning)#所有print之后切换到记录本中用于查看
                sys.exit()
    clickBySprite('sprite/StartWeChat.png',"Wechat Not Open")
    clickBySprite('sprite/Applets.png',"Network Error")
    clickBySprite('sprite/UESTC.png',"Applet Not Find")
    clickBySprite('sprite/Hub.png',"UESTC Not Open")
    clickBySprite('sprite/target.png',"Target Not Find")
    
    #keyboard.add_hotkey('up',whereami)
    #keyboard.wait('esc')
