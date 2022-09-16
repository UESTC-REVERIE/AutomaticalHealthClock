from asyncio.windows_events import NULL
import enum
from msilib.schema import Condition
import sys
from tkinter import Button
from turtle import pos
import pyautogui
import keyboard
def checkMyMouse():
    return pyautogui.mouseInfo()
def mostSpriteNow():
    maxLen = 0
    index = 0
    poses = []
    for dex in range(1,13):
        if(pyautogui.locateAllOnScreen('sprite/'+str(dex)+'.png',confidence=0.8)):
            curlist = list(pyautogui.locateAllOnScreen('sprite/'+str(dex)+'.png',confidence=0.8))
        temp = 0
        tempPos=[]
        #计算实际长度
        for i in range(len(curlist)):
            if(i>0 and (abs(curlist[i-1].top-curlist[i].top)>10 or abs(curlist[i-1].left-curlist[i].left)>10)):
                temp+=1
                tempPos.append(curlist[i])
            elif i==0:
                temp+=1
                tempPos.append(curlist[i])
        if temp>maxLen:
            maxLen=temp
            index=dex
            poses=tempPos
    return index
def closeAD():
    if pyautogui.locateOnScreen('sprite/NoThx.png',confidence=0.8)!=None:
            pyautogui.click(pyautogui.locateOnScreen('sprite/NoThx.png',confidence=0.8))
    if pyautogui.locateOnScreen('sprite/replay.png',confidence=0.8)!=None:
        pyautogui.click(pyautogui.locateOnScreen('sprite/replay.png',confidence=0.8))
    if pyautogui.locateOnScreen('sprite/NoShare.png',confidence=0.8)!=None:
        pyautogui.click(pyautogui.locateOnScreen('sprite/NoShare.png',confidence=0.8))
if __name__=='__main__':
    dict={'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'11':0,'12':0}
    while(True):
        closeAD()
        if keyboard.is_pressed('esc'):
            print("out")
            break
        print("OK")
        #找场上数量最多的物品
        cur = mostSpriteNow()
        print(cur)
        lag = 0.7
        while(cur!=0 and pyautogui.locateOnScreen('sprite/'+str(cur)+'.png',confidence=lag)!=None):
            closeAD()
            print(cur)
            pos=pyautogui.locateOnScreen('sprite/'+str(cur)+'.png',confidence=lag)
            #print(pyautogui.locateOnScreen('sprite/'+str(cur)+'.png',confidence=lag))
            if keyboard.is_pressed('esc'):
                print("out")
                break
            pyautogui.locateOnScreen('sprite/'+str(cur)+'.png',confidence=lag)
            pyautogui.click(pos)
            dex = str(cur)
            dict[dex]=0 if dict[dex]>=2 else dict[dex]+1
            print(dict)
            #点击之后位置的判断，防止重复点击
            AfterClick = pyautogui.locateOnScreen('sprite/'+str(cur)+'.png',confidence=lag)
            print(AfterClick)
            if  AfterClick!=None and (abs(AfterClick.left - pos.left)<10 or abs(AfterClick.top - pos.top)<10):
                dict[dex] = 2 if dict[dex] == 0 else dict[dex] - 1
                lag = 0.85
            else:
                lag =  0.7
            #寻找目前最快到3的物体
            temp = 0
            for i in range(2,-1,-1):
                if(temp == 0):
                    for k,v in dict.items():
                        if v == i and pyautogui.locateOnScreen('sprite/'+k+'.png',confidence=lag)!=None:
                            temp = int(k)
                            cur = temp
                            break
                else:break
            
    '''
    for i in range(len(maxlist)):
        pyautogui.PAUSE=1
        if(i>0 and (abs(maxlist[i-1].top-maxlist[i].top)>10 or abs(maxlist[i-1].left-maxlist[i].left)>10)):
            pyautogui.moveTo(maxlist[i])
            print(1)
        elif i==0:
            pyautogui.moveTo(maxlist[i])
            print(2)

    '''

