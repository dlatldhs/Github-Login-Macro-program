from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui as pagx
import pyautogui
import time
import time as t


#변수 설정
github_id = input("What is your git id??:")
github_pwd = input("What is your git password??:")
driver = webdriver.Chrome('C:\\Users\\SW2126\\Desktop\\Python\\projects\\Macro_programs\\Auto_git\\chromedriver_win32\\chromedriver.exe')
url = 'https://google.com/'



#url open & start!--
driver.get(url) # url open
driver.maximize_window() # 창 크게 만들기

google_search_box = driver.find_element_by_css_selector('.gLFyf.gsfi')

google_search_box.send_keys('github')
google_search_box.send_keys(Keys.ENTER)
driver.find_element_by_css_selector('.LC20lb.DKV0Md').click()
driver.find_element_by_xpath(
    "/html/body/div[1]/header/div/div[2]/div[2]/div[2]/a"
).click()
driver.find_element_by_css_selector('#login_field').send_keys(github_id)
driver.find_element_by_css_selector('#password').send_keys(github_pwd)
driver.find_element_by_xpath(
    '//*[@id="login"]/div[4]/form/div/input[12]'
).click()

'''

old version
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

url = 'https://github.com/'+name
pyautogui.click(375,67)
pyautogui.typewrite(url, interval=0.1)

'''
