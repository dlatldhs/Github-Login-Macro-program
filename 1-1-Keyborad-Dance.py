from pynput.keyboard import Key, Controller
import time

def press_spacebar(delay=0):#spacebar 눌러주는 걸 그냥 함수로 만듬
    # Press and release space
    keyboard.press(Key.space)
    keyboard.release(Key.space)

    if delay > 0:
        time.sleep(delay)

bit=0.54

keyboard = Controller()
print("Dance-Start(after 10 seconds")
time.sleep(10)

#얼불춤 시작 3 초 기다리는거
press_spacebar()
time.sleep(2.8)
#--------------------------
for i in range(9):
    press_spacebar()
    time.sleep(bit)
print('[*] Done!')