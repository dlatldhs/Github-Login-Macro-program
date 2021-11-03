import pyautogui
import time
screenWidth, screenHeight = pyautogui.size()
print('{0}, {1}'.format(screenWidth, screenHeight))
mouseX, mouseY = pyautogui.position()
print('{0}, {1}'.format(mouseX, mouseY))
p_list = pyautogui.locateAllOnScreen("C:\\Users\\SW2126\\Desktop\\source.png")
p_list = list(p_list)
print(p_list)
p_center = pyautogui.center(p_list[0])
pyautogui.click(p_center)