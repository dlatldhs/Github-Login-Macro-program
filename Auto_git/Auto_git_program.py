from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui as pag

Name_or_email = input("What is your git name or email??:")
PWD = input("What is your git password?:")

#초기화
driver = webdriver.Chrome('C:\\Users\\SW2126\\Desktop\\Python\\projects\\Macro_programs\\Auto_git\\chromedriver_win32\\chromedriver.exe')
url = 'https://github.com/'+Name_or_email
driver.get(url) # url open
driver.maximize_window() # 창 크게 만들기
action = ActionChains(driver)