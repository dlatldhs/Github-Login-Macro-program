from pynput.keyboard import Key, Controller

bit=int(input("비트수를 입력해주세요:"))

keyboard = Controller()

# Press and release space
keyboard.press(Key.space)
keyboard.release(Key.space)