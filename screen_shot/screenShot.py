import pyautogui
import time


def screenshot():
    name = time.time()
    name = f"C:/Users/COONG SANH/Downloads/{name}.png"
    img = pyautogui.screenshot()
    img.save(name)
    img.show()


screenshot()
