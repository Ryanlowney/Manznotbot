import tkinter as tk
from tkinter import ttk

import pyautogui,time,random, win32api,win32con, win32com.client

from PIL import Image
import pytesseract, csv, urllib.request, urllib.parse, requests, json, ast
from bs4 import BeautifulSoup
#from urllib.request import urlopen



shell = win32com.client.Dispatch("WScript.Shell")
# Globals
xSlot=680
ySlot=465
xSlot2=682
ySlot2=483
xSlot3=720
ySlot3=480
#class Item:
ItemList ={'FireBattleStaff' :{'ItemNumber':1393,'ItemCurrentPrice': 0,'ItemBuyLimit' : 1000,'ItemHighAlchPrice':9300,'ItemMerchSellSpeed':0,'ItemMerchMargin':0 },
'WaterBattleStaff': {'ItemNumber':1395,'ItemCurrentPrice': 0,'ItemBuyLimit' : 1000,'ItemHighAlchPrice':9300,'ItemMerchSellSpeed':0,'ItemMerchMargin':0 }, 
'AirBattleStaff':{'ItemNumber':1397,'ItemCurrentPrice': 0,'ItemBuyLimit' : 1000,'ItemHighAlchPrice':9300,'ItemMerchSellSpeed':0,'ItemMerchMargin':0 },
'EarthBattleStaff':{'ItemNumber':1399,'ItemCurrentPrice': 0,'ItemBuyLimit' : 1000,'ItemHighAlchPrice':9300,'ItemMerchSellSpeed':0,'ItemMerchMargin':0 },
'MysticFireBattleStaff':{'ItemNumber':1401,'ItemCurrentPrice': 0,'ItemBuyLimit' : 1000,'ItemHighAlchPrice':25500,'ItemMerchSellSpeed':0,'ItemMerchMargin':0 },
'MysticWaterBattleStaff':{'ItemNumber':1403,'ItemCurrentPrice': 0,'ItemBuyLimit' : 1000,'ItemHighAlchPrice':25500,'ItemMerchSellSpeed':0,'ItemMerchMargin':0 },
'MysticAirBattleStaff':{'ItemNumber':1405,'ItemCurrentPrice': 0,'ItemBuyLimit' : 1000,'ItemHighAlchPrice':25500,'ItemMerchSellSpeed':0,'ItemMerchMargin':0 },
'MysticEarthBattleStaff':{'ItemNumber':1407,'ItemCurrentPrice': 0,'ItemBuyLimit' : 1000,'ItemHighAlchPrice':25500,'ItemMerchSellSpeed':0,'ItemMerchMargin':0 },
'RuneMace':{'ItemNumber':1432,'ItemCurrentPrice': 0,'ItemBuyLimit' : 100,'ItemHighAlchPrice':8640,'ItemMerchSellSpeed':0,'ItemMerchMargin':0 },
'RunePlateSkirt':{'ItemNumber':13488,'ItemCurrentPrice': 0,'ItemBuyLimit' : 100,'ItemHighAlchPrice':38400,'ItemMerchSellSpeed':0,'ItemMerchMargin':0 },
'RunePlateLegs':{'ItemNumber':13487,'ItemCurrentPrice': 0,'ItemBuyLimit' : 100,'ItemHighAlchPrice':38400,'ItemMerchSellSpeed':0,'ItemMerchMargin':0 },
'RuneFullHelm':{'ItemNumber':13495,'ItemCurrentPrice': 0,'ItemBuyLimit' : 100,'ItemHighAlchPrice':21120,'ItemMerchSellSpeed':0,'ItemMerchMargin':0 },
'RuneHelm':{'ItemNumber':13783,'ItemCurrentPrice': 0,'ItemBuyLimit' : 100,'ItemHighAlchPrice':11520,'ItemMerchSellSpeed':0,'ItemMerchMargin':0 },
'RuneKiteShield':{'ItemNumber':13507,'ItemCurrentPrice': 0,'ItemBuyLimit' : 100,'ItemHighAlchPrice':32640,'ItemMerchSellSpeed':0,'ItemMerchMargin':0 },
'RuneSqShield':{'ItemNumber':13787,'ItemCurrentPrice': 0,'ItemBuyLimit' : 100,'ItemHighAlchPrice':23040,'ItemMerchSellSpeed':0,'ItemMerchMargin':0 },
'RuneCrossBow':{'ItemNumber':13530,'ItemCurrentPrice': 0,'ItemBuyLimit' : 100,'ItemHighAlchPrice':9720,'ItemMerchSellSpeed':0,'ItemMerchMargin':0 },
'RuneSword':{'ItemNumber':1289,'ItemCurrentPrice': 0,'ItemBuyLimit' : 100,'ItemHighAlchPrice':12480,'ItemMerchSellSpeed':0,'ItemMerchMargin':0 },
'Rune2hSword':{'ItemNumber':13778,'ItemCurrentPrice': 0,'ItemBuyLimit' : 100,'ItemHighAlchPrice':38400,'ItemMerchSellSpeed':0,'ItemMerchMargin':0 },
'RuneHalbard':{'ItemNumber':3202,'ItemCurrentPrice': 0,'ItemBuyLimit' : 100,'ItemHighAlchPrice':76800,'ItemMerchSellSpeed':0,'ItemMerchMargin':0 },
'RuneChainBody':{'ItemNumber':13781,'ItemCurrentPrice': 0,'ItemBuyLimit' : 100,'ItemHighAlchPrice':30000,'ItemMerchSellSpeed':0,'ItemMerchMargin':0 },
'RunePlateBody':{'ItemNumber':13482,'ItemCurrentPrice': 0,'ItemBuyLimit' : 100,'ItemHighAlchPrice':39000,'ItemMerchSellSpeed':0,'ItemMerchMargin':0 },
'RuneBoots':{'ItemNumber':13782,'ItemCurrentPrice': 0,'ItemBuyLimit' : 100,'ItemHighAlchPrice':75000,'ItemMerchSellSpeed':0,'ItemMerchMargin':0 },
'BlackDhideBody':{'ItemNumber':2503,'ItemCurrentPrice': 0,'ItemBuyLimit' : 5000,'ItemHighAlchPrice':8088,'ItemMerchSellSpeed':0,'ItemMerchMargin':0 },
'RedDhideBody':{'ItemNumber':2501,'ItemCurrentPrice': 0,'ItemBuyLimit' : 5000,'ItemHighAlchPrice':6738,'ItemMerchSellSpeed':0,'ItemMerchMargin':0 },
'BlueDhideBody':{'ItemNumber':2499,'ItemCurrentPrice': 0,'ItemBuyLimit' : 5000,'ItemHighAlchPrice':5616,'ItemMerchSellSpeed':0,'ItemMerchMargin':0 },

'NatureRune':{'ItemNumber':561,'ItemCurrentPrice': 0,'ItemBuyLimit' : 100,'ItemHighAlchPrice':0,'ItemMerchSellSpeed':0,'ItemMerchMargin':0 },
}

def AssignVariables():

	item1 = input("Alch item 1 amount: ")

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
#def ItemGeFethcLoop():

def ItemGeFetch(ItemID):
	ItemRequest = requests.get('http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item='+ItemID)
	ItemRequest = ItemRequest.content
	ItemRequest = json.loads(ItemRequest)
	#print(ItemRequest)
	#print(ItemRequest.text)
	'''
	ItemRequest = str(ItemRequest)
	ItemRequest = ItemRequest.split("item")
	ItemRequest = ItemRequest[2:]
	ItemRequest = ItemRequest[:-1]
	ast.literal_eval(ItemRequest)
	'''
	'''
	things to look for 
	"name":"Logs"
	"price":400},"today" - maybe today then chars before
	-or start at current and parse 
	current":{"trend":"neutral","price":400},"today":{"trend":"negative","price":"- 12"},
	"members":"false","day30":{"trend":"positive","change":"+26.0%"},
	"day90":{"trend":"positive","change":"+33.0%"}
	,"day180":{"trend":"positive","change":"+2.0%"}}}

	'''
	## replace for efficiency 
	#dict1 = ItemRequest.json()	
	#dict = ItemRequest.json()
	#print(dict.get("today"))

	ItemRequestPrice = ItemRequest["item"]["current"]
	ItemRequest30 = ItemRequest["item"]["day30"]
	ItemRequest90 = ItemRequest["item"]["day90"]
	ItemRequest180 = ItemRequest["item"]["day180"]

	ItemReturn = ItemRequestPrice+ "/" + ItemRequest30+ "/" + ItemRequest90+ "/" + ItemRequest180
	print(ItemReturn)
	return ItemReturn

	'''temRequest = ItemRequest.read().decode('utf-8')
	print(ItemRequest['current'])
	ItemRequest = str(ItemRequest).split("current")
	ItemRequest = ItemRequest.replace("trend","")
	ItemRequest = ItemRequest.replace("price","")
	ItemRequest = ItemRequest.replace("change","")
	ItemRequest = ItemRequest.replace(":","")
	'''
	#print(ItemRequest.text)

	#http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item=ItemID
	#Battlestaff 1391
	'''
	fire battlestaff  1393 Limit 1000 High Alch 9300
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
	Plateskirt 13488
	full helm 13495    Limit 100 High Alch 21120
	KiteShield 13507   Limit 100 High Alch 32640
	Cross Bow  13530   Limit 100 High Alch 9720
	Sword 1377 		   Limit 100 High Alch 12480
	2h Sword 13778	   Limit 100 High Alch 38400
	Halbard 13778	   Limit 100 High Alch 76800
	Mace 13780 		   Limit 100 High Alch 8640
	Chainbody 13781	   Limit 100 High Alch 30000
	Boots 13782		   Limit xxx High Alch 7500
	Helm  13783		   Limit 100 High Alch 11520
	Shield 13787	   Limit 100 High Alch

	~~~~ Granite ~~~~
	Helm 13784		Limit 10	High Alch 2760 
	Body 13785		Limit 10 	High Alch 48000
	Legs 13786		Limit 10    High Alch 39600
	Shield  13788   Limit 10 	High Alch 33600




	~~~~ Dragon ~~~~
	mace 1434 Limit 10 High Alch 30000
	helm 13495 Limit 10 High Alch 60000
	~~~~ Barrows ~~~~
	4708 - 4759
	~~~~ LOGS ~~~~
	logs 1511
	magic 1513
	yew 1515
	maple 1517
	willow 1519
	oak 1521
	~~~ Gems ~~~
	1601-1633

	~~~~ Leather ~~~~
	Green Dragon Leather 1745

	Black DragonHide 1747
	Red 			 1749
	Blue		     1751	
	Green			 1753

	black dhide body 2503
	red   dhide body 2501
	blue  dhide body 2499
	
	Magic ShieldBow 13527 Limit 5000 High Alch 1536



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
AlcingLoop(475,0)
def ComplileDictionary():
	print("compile dict running")
	pullData = open(r"D:\PythonStuff\AppData\ItemList2.txt","r")
	
	NewDictList = []
	LinesOfText = pullData.readlines()
	#LinesOfText2 = pullData.read()
	#print(LinesOfText)
	
	po = 0
	pe = 0
	TextLength =len(LinesOfText)
	print("list len",TextLength)
	while (po < TextLength-1):
		NewDictString = ''
		print(po)
		NewDictString = LinesOfText[po]
		#print(NewDictString)
		print("a",po)
		print(NewDictString)
		print("b")
		ListGarbage1=NewDictString.split(",")
		# 'FireBattleStaff' :{'ItemNumber':1393,'ItemCurrentPrice': 0,'ItemBuyLimit' : 1000,'ItemHighAlchPrice':9300,'ItemMerchSellSpeed':0,'ItemMerchMargin':0 }
		NewDictList.append("'" + ListGarbage1[0] + "'" + ":" + "{" + "'ItemNumber'" + ":" + ListGarbage1[1] + "," + "'ItemCurrentPrice': 0,'ItemBuyLimit' : 1000,'ItemHighAlchPrice':9300,'ItemMerchSellSpeed':0,'ItemMerchMargin':0" + "},")
		
		#LinesOfText = pullData.readlines()
		po +=1
	NewFile = open("D:\PythonStuff\AppData\DictionaryItems.txt", "w+")
	while (pe < po ):
		print(pe,po)
		print (NewDictList[pe])
		NewFile.write(NewDictList[pe])
		print("2")
		pe +=1
	NewFile.close()
	pullData.close()

'''ItemGeFetch('1511')
xSlotI,xSlotO=ReassingMouseSpots()
if(xSlotI==0):
	print("Carry On")
else:
	xSlot2,ySlot2=xSlotI
	xSlot3,ySlot3=xSlotO
item1, item2= AssignVariables()
item1 =int(item1)
item2 = int(item2)
'''	
def MainLoop():
	options = []

	options.append  (" Key: reassigns mouse spots")
	options.append  (" Continue: continues with set mouse spots")
	options.append  (" Itemfetch ")
	options.append  (" Whatcanialch reg/full: runs through a list reg is normal items that are alched, full is a whole item list(it may take a while due to api call limit)")
	options.append  (" Whatcaniprocess : looks at normally processed items to see if any are profitable")
	options.append  (" Exit : exits program, probably doesnt work rn")
	print("_____Hello, Welcome to the Interface!____")
	print("here are some options...")
	Q = 0
	while(Q < len(options)):
		print(options[Q])
		Q+=1
	KeyInput=input("What's your choice?")
	if (KeyInput == "Key"):
		xSlotI,xSlotO = ReassingMouseSpots()
	elif(KeyInput == "Continue"):
		print("carry on")
	elif(KeyInput == "Itemfetch"):
		KeyInput1 = input("  Item name: fetches item info (type item name without spaces all nouns are proper)")
		try:
			ItemQuant = ItemList.get(KeyInput1)
			print(ItemQuant)
			#ItemQuant = ItemList[KeyInput1][ItemBuyLimit]
			ItemQuant = ItemList[KeyInput1]
			print(ItemQuant)
			ItemNum = ItemList[KeyInput1]['ItemNumber']
			print(ItemNum)
			
			#error is here
			Results = ItemGeFetch(ItemNum)
			print(Results)
		except:
			print(KeyInput1)
			print("not a valid item, or something")
		


#ComplileDictionary()
# to do: Convert and Compare UTC time to current GE update
ItemName = 'Rune helm'
ItemRequest5 = requests.get('http://runescape.wikia.com/wiki/Module:Exchange/'+ItemName+'?action=raw')
ItemRequest5 = ItemRequest5.content
# ItemId, price, date, limit
# options: turn return into a dict = to :
ItemRequest5 = str(ItemRequest5)
ItemRequest6 = ItemRequest5
ItemRequest5 = ItemRequest5.replace("=",'" :')
ItemRequest5 = ItemRequest5.replace(",",', " ')
ItemRequest5 = ItemRequest5.replace("{", '{ " ')
ItemRequest5 = ItemRequest5.replace("'", '" ')
ItemRequest5 = ItemRequest5.replace(' ','')
ItemRequest5 = ItemRequest5.replace(':{',':')
ItemRequest5 = ItemRequest5.replace("return", 'ItemRequestDict" =')
ItemRequest5 = ItemRequest5.replace('n','po')
ItemRequest5 = ItemRequest5.replace('\po', "")
ItemRequest5 = ItemRequest5.replace('"date":"','')
ItemRequest5 = ItemRequest5.replace('"lastdate":"','')
ItemRequest5 = ItemRequest5.replace('""','"')
ItemRequest5 = ItemRequest5.replace('(UTC)"','')
ItemRequest5 = ItemRequest5.replace(',"2018','"')

print(type(ItemRequest6))
ItemRequest6 = ItemRequest6.replace("=",'" :')
ItemRequest6 = ItemRequest6.replace(",", "")
ItemRequest6 = ItemRequest6.replace(' ','')
ItemRequest6 = ItemRequest6.split(":")
ItemRequest7 = requests.get('http://runescape.wikia.com/wiki/'+ItemName)
ItemRequest7 = ItemRequest7.content
ItemRequest7 = str(ItemRequest7)
#ItemRequest7 = ItemRequest7.split

#print(ItemRequest7)


print(ItemRequest6[1]) # itemID
print(ItemRequest6[8]) # Name


soup = BeautifulSoup(ItemRequest7, 'html.parser')
HtmlTextBox = soup.find('table',attrs={'class': 'wikitable infobox plainlinks no-parenthesis-style infobox-item'})
HtmlText = HtmlTextBox.text.strip()
#print(HtmlText)
HtmlTextList = HtmlText.split("High alch")
HtmlGarbage = HtmlText.split("Buy limit")
HtmlGarbage2 = HtmlGarbage[1].split("Weight")
HtmlTextList[0] = HtmlGarbage2[0]
HtmlGarbage3 =HtmlTextList[1].split("Low alch")
HtmlTextList[1] = HtmlGarbage3[0]
HtmlTextList[1] = HtmlTextList[1].replace("coins", "")
print(HtmlTextList)
OldFile = open("D:\PythonStuff\AppData\DictionaryItems.txt", "r")
LinesOfText4 = OldFile.read()
LinesOfText3 = []
LinesOfText3 = LinesOfText4
print(LinesOfText3)
#print(LinesOfText3['Cannonball'])

ast.literal_eval(LinesOfText3)
#print(LinesOfText3['Cannonball'])
#ItemRequest6 = ItemRequest6.replace(' ', '')

# remove dates, months have 3-9 chars
#ItemRequest5.splitlines()
#ItemRequest5 = ItemRequest5.replace(" ","")

#ItemRequest = ast.literal_eval(ItemRequest5)
#ItemRequest5 = json.loads(ItemRequest5)
#print(ItemRequest6)
print(type(LinesOfText3))
MainLoop()


AlcingLoop(1000,0)
#AfkClick(300, 430,169)
#~~~~~~~~~~~~~/Alcing~~~~~~~~~~~~~~~~~~~~~
