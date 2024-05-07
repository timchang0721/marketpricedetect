import pyautogui
import pydirectinput
import pyperclip
import time
import re
from PIL import Image 
import pytesseract
import openpyxl
from openpyxl.styles import Font 
import os
import mysql.connector
from datetime import datetime
def key(word):
    pydirectinput.keyDown(word)
    pydirectinput.keyUp(word)
def word(word):
    abc= word
    pyperclip.copy(abc)
    pyautogui.hotkey('enter')
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('v')
    pyautogui.keyUp('v')
    pyautogui.keyUp('ctrl')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('enter')
    abc=""
def searchitem(item):
    print (item)
    pydirectinput.click(241,90)
    time.sleep(0.5)
    pyautogui.press('backspace',15,0.1)
    time.sleep(0.5)
    word(item)
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    time.sleep(0.5)
def checkprice():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    im = pyautogui.screenshot(region=(726,220, 150,20))
    im.save('123.png')
    img = Image.open("123.png")
    text = pytesseract.image_to_string(img, lang='eng')
    text.split('\n')
    ans = text.split('\n')[0].replace(",","")
    ans = ans.split('\n')[0].replace(".","")
    ans = re.sub(r'\D', '', ans)
    print(ans)
    return ans
def readtext():
    text =[]
    f = open('items.txt', 'r',encoding="utf-8")
    for line in f:
        ans = line.replace("\n","")
        text.append(ans)
    return text
def uploaddate(item,price,date):
    con = mysql.connector.connect(user= 'tim',password='hacj4932', host ='114.34.51.115', database = 'wordpress')
    cursor = con.cursor()
    sql = " INSERT INTO item(name, price,date) VALUES(%s,%s,%s)"
    val = (item, price ,date)
    cursor.execute(sql, val)
    con.commit()
    sql = " SELECT * FROM item"
    cursor.execute(sql)
    for row in cursor :
        print(row)
    cursor.close()
    con.close()
if __name__ == '__main__':
    uploaddate("123",11,datetime.now())
    # while(1):
    #     items = []
    #     items = readtext()
    #     for item in items:
    #         searchitem(item)
    #         uploaddate(item,checkprice(),datetime.now())
    #         time.sleep(6)
    #     time.sleep(3600)

        
        
        
        
    
    