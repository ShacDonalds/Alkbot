# -*- coding: utf-8 -*-
"""
Created on Fri May 15 17:31:42 2020

@author: PC didi
"""

import pyautogui
from time import sleep
import random
import cv2
import numpy as np
from PIL import ImageGrab
import os

pyautogui.FAILSAFE=False
screenWidth, screenHeight = pyautogui.size()


#####################################################################################################################   first queue

def StartAlkbot():
    pyautogui.moveTo(441, 201, duration = 0.75)
    pyautogui.click()
    pyautogui.moveTo(468, 263, duration = 1)
    pyautogui.click()
    pyautogui.moveTo(802, 715, duration = 0.5)
    pyautogui.click()
    pyautogui.moveTo(860, 848, duration = 0.5)
    pyautogui.click()
    sleep(2)
    pyautogui.click()
    return Accept()

#####################################################################################################################   match accept + chamselect






def Accept():
    t = 0
    if pyautogui.locateOnScreen('In queue.png', confidence = 0.9) == None :
        if pyautogui.locateOnScreen('In champselect.png', confidence = 0.9) == None:
            return replay()
        else :
            return Champselect()
    while  pyautogui.locateOnScreen('In champselect.png', confidence = 0.9) == None:
        pyautogui.click(955, 720)
        if t > 15 and t % 6 == 0:
            if pyautogui.locateOnScreen('In champselect.png', confidence = 0.9) == None:
                if pyautogui.locateOnScreen('Match found.png', confidence = 0.9) == None:
                    if pyautogui.locateOnScreen('In queue.png', confidence = 0.95) == None :
                        return replay()
        sleep(1.5) 
        t += 1.5
    return Champselect()
        
def Champselect():
    pyautogui.moveTo(468, 835, duration = 0.2)
    pyautogui.click()
    pyautogui.write('jgl', interval = 0.08)
    pyautogui.press(['enter'])
    pyautogui.moveTo(1140, 260, duration = 0.2)
    pyautogui.click()
    pyautogui.write('garen', interval = 0.3)
    sleep(0.75)
    pyautogui.moveTo(700, 320, duration = 0.3)
    pyautogui.click()
    sleep(0.75)
    pyautogui.moveTo(955, 770, duration = 0.3)
    pyautogui.click()
    pyautogui.moveTo(468, 835, duration = 0.2)
    pyautogui.click()
    pyautogui.write("i lag btw", interval = 0.04)
    pyautogui.press(['enter'])
    if pyautogui.locateOnScreen('In champselect.png', confidence = 0.95) != None :
        pyautogui.click(1231, 265)
        sleep(1)
        X=[701, 809, 908, 1017, 1113, 1214]
        for x in X:
            pyautogui.moveTo(x, 333, duration = 0.5)
            pyautogui.click()
        sleep(0.75)
        pyautogui.moveTo(955, 770, duration = 0.3)
        pyautogui.click()
    return WaitforStart()



##################################################################################################################### in game


def WaitforStart():
    t=0
    while  pyautogui.locateOnScreen('Start.png', confidence = 0.9) == None and pyautogui.locateOnScreen('MINIMAP2.png', confidence = 0.9) == None and pyautogui.locateOnScreen('MINIMAP1.png', confidence = 0.9) == None:
        sleep(0.5)
        t += 0.5
        if t > 95:
            pyautogui.click(1000, 800)
            click()
            if pyautogui.getActiveWindowTitle() != "League of Legends (TM) Client":
                return replay()
    return PlaytheGame()
            
    
def PlaytheGame():       
    pyautogui.click(1000, 800)
    click()
    s = 0
    shop(s)
    s += 1
    pyautogui.moveTo(1616, 1029, duration = 0.3)
    click()
    learnE()
    sleep(55)
    i = 0
    while pyautogui.getActiveWindowTitle() == "League of Legends (TM) Client":
        if i % 5 == 0:
            red()
        elif i % 5 == 1:
            blue()
        elif i % 5 == 2:
            wolves()
        elif i % 5 == 3:
            grump()
        elif i % 5 == 4:
            chickens()   
        if i == 0 or i==1:
            learnA()
        if i == 2 or i == 7 or i == 12 or i == 16 or i == 25 or i == 35 or i == 45 or i == 55 or i == 70:
            shop(s)
            s += 1
        if i == 3 or i == 4:
            learnZ()
        if i > 4:
            learnE()
            learnA()
            learnZ()
        i += 1 
        if i == 22 or i == 27 or i == 37 or i == 47 or i == 57 or i == 67:
            Drake()
    return Honor()


##################################################################################################################### externals
    
def click():
    pyautogui.mouseDown()
    sleep(0.23)
    pyautogui.mouseUp()

def rightclick():
    pyautogui.mouseDown(button = 'right')
    sleep(0.23)
    pyautogui.mouseUp(button = 'right')
    
def useE():
    pyautogui.moveTo(916, 970, duration = 0.3)
    click()


def openshop():
    pyautogui.moveTo(1119, 1022, duration = 0.3)
    click()
    
def learnE():
    pyautogui.moveTo(917, 938, duration = 0.3)
    click()
    
def back():
    pyautogui.moveTo(1171, 1003, duration = 0.3)
    click()
    sleep(9)

def useHeal():
    pyautogui.moveTo(1002, 964, duration = 0.15)
    click()
    pyautogui.moveTo(734, 979, duration = 0.15)
    click()
    
def useA():
    pyautogui.moveTo(836, 974, duration = 0.15)
    click()
    
def learnA():
    pyautogui.moveTo(836, 938, duration = 0.15)
    click()
    
def useSmite():
    pyautogui.moveTo(1032, 960, duration = 0.5)
    click()
    
def learnZ():
    pyautogui.moveTo(879, 929, duration = 0.15)
    click()
    
def useZ():
    pyautogui.moveTo(879, 974, duration = 0.15)
    click()
    
##################################################################################################################### buy at cycle i

def shop(i):
    if i > 4:
        i=4
    L=[242, 388, 492, 639, 756]
    X=[271, 345, 411, 468, 535]
    openshop()
    for x in X:
        pyautogui.moveTo(x, L[i], duration = 0.75)
        rightclick()
    openshop()
	
##################################################################################################################### Clear camps functions
    
def red():
    pyautogui.moveTo(1787, 965, duration = 0.5)
    rightclick()
    sleep(27)    
    pyautogui.moveTo(1082, 394, duration = 0.3)
    rightclick()
    for k in range(2):
        useE()
        useA()
        useZ()
        useSmite()
        pyautogui.moveTo(959, 404, duration = 0.3)
        click()     
        sleep(11)
    back()

def blue():
    pyautogui.moveTo(1721, 890, duration = 0.5)
    rightclick()
    sleep(27)    
    pyautogui.moveTo(1207, 764, duration = 0.3)
    rightclick()
    for k in range(2):
        useA()
        useE()
        useZ()
        useHeal()
        sleep(11)
    back()
    
def wolves():
    pyautogui.moveTo(1726, 925, duration = 0.5)
    rightclick()
    sleep(27)    
    pyautogui.moveTo(947, 392, duration = 0.3)
    rightclick()
    for k in range(2):
        useE()
        useA()
        useZ()        
        sleep(11)
    back()


def grump():
    pyautogui.moveTo(1709, 891, duration = 0.5)
    rightclick()
    sleep(27)    
    pyautogui.moveTo(566, 432, duration = 0.3)
    rightclick()
    for k in range(2):
        useE()
        useA()
        useZ()
        useSmite()
        pyautogui.moveTo(768, 506, duration = 0.3)
        click()     
        sleep(11)
    back()


def chickens():
    pyautogui.moveTo(1784, 941, duration = 0.5)
    rightclick()
    sleep(27)    
    pyautogui.moveTo(626, 358, duration = 0.3)
    rightclick()
    for k in range(2):
        useE()
        useA()
        useZ()   
        useHeal()
        sleep(11)
    back()
    
def Drake():
    pyautogui.moveTo(1834, 946, duration = 0.5)
    rightclick()
    sleep(30)    
    pyautogui.moveTo(535, 807, duration = 0.3)
    rightclick()
    sleep(3)
    for k in range(4):
        useE()
        useA()
        useZ()
        useSmite()
        pyautogui.moveTo(757, 612, duration = 0.3)
        click()     
        useHeal()
        sleep(11)
    back()
    
    
##################################################################################################################### replay


def Honor():
    if pyautogui.locateOnScreen('Honor.jpg', confidence = 0.9) != None :
        pyautogui.click(1100, 546)
        sleep(1.5)
    elif pyautogui.locateOnScreen('loading.jpg' , confidence = 0.9) != None :
        sleep(5)
    else :
        return postGame()
    return Honor()

def postGame():
    while pyautogui.locateOnScreen('ok.png', confidence = 0.9)!= None:
        pyautogui.moveTo(953, 841, duration = 0.5)
        pyautogui.click
        click()
        pyautogui.click(953, 841)
        sleep(3)
    if pyautogui.locateOnScreen('play again.png', confidence = 0.9) != None :
        return replay()
    else :
        pyautogui.click(1416, 798)
        click()
        pyautogui.click(978, 860)
        click()
        pyautogui.moveTo(835, 990, duration = 0.1)
        pyautogui.moveTo(857, 777, duration = 1)
        click()
        pyautogui.moveTo(801, 659, duration = 1)
        click()
        if pyautogui.locateOnScreen('play again.png', confidence = 0.9) != None :
            return replay()
        else :
            return postGame()
        
def replay():
    pyautogui.click(860, 848)
    sleep(2.5)
    pyautogui.click(860, 848)
    return Accept()



##################################################################################################################### 

start()






