import tkinter as tk
from tkinter import ttk

import pyautogui,time,random, win32api,win32con, win32com.client

from PIL import Image
import pytesseract, csv, urllib.request


shell = win32com.client.Dispatch("WScript.Shell")
# Globals
xSlot=680
ySlot=465
xSlot2=682
ySlot2=483
xSlot3=720
ySlot3=480


def AssignVariables():

	item1 =input("Alch item 1 amount: ")

	item2 = input("Alch item 2 amount: ")

	return (item1, item2)
def ReassingMouseSpots():
	KeyInput=input("Continue or key?")
	if(KeyInput =='key'):
		keyspot1 = input("Place mouse over the first slot so that it overlaps both the alching slot and your item slot. Then press a key to continue.") 
		Position1Tuple = pyautogui.position()
		keyspot1 = input("Place mouse over the Second slot so that it overlaps both the alching slot and your item slot. Then press a key to continue.") 
		Position2Tuple = pyautogui.position()
	else:
		return(0,4)
	return (Position1Tuple,Position2Tuple)
def ItemGeFetch(ItemID):
	#http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item= ItemID
	#Battlestaff 1391
	'''
	fire battlestaff  1393
	water battlestaff 1395
	air Battlestaff   1397				
	earth Battlestaff 1399
	mystic battle staff 
	fire 1401
	water 1403
	air 1405
	earth 1407
	~~~ rune~~~
	mace 1432

	~~~~ Dragon ~~~~
	mace 1434


	'''
def click(x,y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
# used for drag 
def MovingHoldClick(x,y,durration,x2,y2):
	pyautogui.moveTo(x,y,durration)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
	pyautogui.moveTo(x2,y2,durration)
# used for drop
def MouseUp(x,y):
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
# randomize clicks so bot detecting is harder
def RandomClick(min, max):
	Reandomclick = random.randint(min,max)

	return Reandomclick

def AfkClick(Durration, Position1, Position2 ):
	F = 0
	midPower1 = 430
	midPower2 = 169
	while (F <= Durration) :	
		RandomPositionAFK = RandomClick(1,3)
		RandomTime = RandomClick(1,10)
		click(Position1+RandomPositionAFK,Position2+RandomPositionAFK)
		time.sleep(40+RandomTime)
		F +=1
		print(F)
def ImageRead(Image):

	text = pytesseract.image_to_string(Image, lang = 'eng')

	return (text)


def AlcingLoop(Item1,Item2):
# args that should be taken Item1,Item2,Item3
# alc for mad loot
	RandomPosition1 = RandomClick(2,8)
	RandomPosition2 = RandomClick(3,6)
	#Item2=0 #delete when added to args
	Item3=0
	LoopNum = Item1+Item2+Item3
	print(LoopNum)
	
	S=0
	ItemMoved =0
	while(S <= LoopNum):
		if Item1 > 0:
			#win32api.keybd_event(0x39,0,0,0)
			time.sleep(2)
			#shell.SendKeys('9')  #'9':0x39,
			click(xSlot2-RandomPosition1,ySlot2-RandomPosition2)
			Item1=Item1-1
			print("Item 1 " , Item1)
			#TestClass.after(15,AlcingLoop(Item1) )
			#win32api.keybd_event(0x39,0,win32con.KEYEVENTF_KEYUP ,0)
			time.sleep(1)
			#AlcingLoop(Item1)
			click(xSlot2-RandomPosition1,ySlot2-RandomPosition2)
			#someway to drag the next item from slot 2 to 1
			

		elif (Item1 ==0 and Item2 >0):
			# reassign for randomness 
			RandomPosition1 = RandomClick(1,3)
			RandomPosition2 = RandomClick(2,5)
			time.sleep(2.3)
			if (ItemMoved ==0):
				# move to bag icon and click
				pyautogui.moveTo(835+RandomPosition1,340+RandomPosition1,1)
				click(835+RandomPosition1,340+RandomPosition1)
				# move the item 
				MovingHoldClick(xSlot3,ySlot3,1,xSlot,ySlot2)
				MouseUp(xSlot,ySlot2)
				# open the magic tab
				pyautogui.moveTo(802-RandomPosition1 ,341,.5)
				click(802-RandomPosition1 ,341)
				# click the alch button
				pyautogui.moveTo(xSlot+RandomPosition2,ySlot+RandomPosition1,1)
				click(xSlot-RandomPosition2,ySlot2-RandomPosition1)
				ItemMoved +=1
				print("Item has been moved", ItemMoved)
			click(xSlot-RandomPosition2,ySlot2-RandomPosition1)
			time.sleep(1)
			#TestClass.after(15)
			click(xSlot-RandomPosition2,ySlot2-RandomPosition1)
			Item2-1
			print("Item 2 " , Item2)
		elif (Item2 ==0 and Item3 >0):
			pyautogui.mouseDown()

			pyautogui.click(xSlot2,ySlot2,2)
			pyautogui.click(xSlot,ySlot,2)
			pyautogui.mouseUp()

			click(xSlot+RandomPosition1,ySlot-RandomPosition2)
			Item3-1
			#TestClass.after(15)
			click(xSlot-RandomPosition2,ySlot+RandomPosition1)
		else :
			print("Alcing click loop failure")

		
		S+=1
		print("Loops Done: " , S)
xSlotI,xSlotO=ReassingMouseSpots()
if(xSlotI==0):
	print("Carry On")
else:
	xSlot2,ySlot2=xSlotI
	xSlot3,ySlot3=xSlotO



item1, item2= AssignVariables()
item1 =int(item1)
item2 = int(item2)
AlcingLoop(item1,item2)
#AfkClick(300, 430,169)
#~~~~~~~~~~~~~/Alcing~~~~~~~~~~~~~~~~~~~~~


# python D:\PythonStuff\AutoclickerBasic.py
