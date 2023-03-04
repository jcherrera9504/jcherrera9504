import pyautogui, webbrowser

from time import sleep


webbrowser.open('https://web.whatsapp.com/send?phone+526181554117')

sleep(5) 
pyautogui.press('tab')
sleep(0.2) 
pyautogui.press('tab')
sleep(0.2) 
pyautogui.press('tab')
sleep(0.2)  
pyautogui.press('tab')
sleep(0.2) 
pyautogui.press('tab')
sleep(0.2)              
pyautogui.press('tab')
sleep(0.2)
pyautogui.press('tab')
sleep(0.2)  
pyautogui.press('tab')
sleep(1)  
for i in range(3):
    pyautogui.typewrite('Amor')
    pyautogui.press('enter')