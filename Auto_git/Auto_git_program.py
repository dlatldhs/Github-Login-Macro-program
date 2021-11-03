from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui as pagx
import pyautogui
import time

name = input("What is your git name??:")
email = input("What is your git email??:")
pwd = input("What is your git password??:")

#======실험=====실시간 마우스 좌표 구하기====== 나중에 필요할 때만 쓰는거
'''
while True:
    print("Current Mouse Position:",pyautogui.position())
    time.sleep(1)
'''
#========================================================================
driver = webdriver.Chrome('C:\\Users\\SW2126\\Desktop\\Python\\projects\\Macro_programs\\Auto_git\\chromedriver_win32\\chromedriver.exe')
url = 'https://github.com/login'


driver.get(url) # url open
driver.maximize_window() # 창 크게 만들기
action = ActionChains(driver)
time.sleep(3)
#id 부분
pyautogui.click(808,421)
pyautogui.typewrite(email, interval=0.1)
#password 부분
pyautogui.click(938,464)
#login 하기 부분
pyautogui.typewrite(pwd, interval=0.1)
pyautogui.click(938,581)
