import pyautogui
from PIL import Image,ImageGrab
import time
def hit(key):
    pyautogui.keyDown(key)
    return
def iscol(data):
    for i in range(220, 250):
        for j in range(420, 450):
            if data[i, j] in range(70,200):
                hit('up')
                return
    for i in range(170, 230):
        for j in range(300, 380):
            if data[i, j] in range(70,200):
                hit('down')
                return
    return



def takeScreenshot():
    image= ImageGrab.grab()
    image.show()
    return image
if __name__=="__main__":
    time.sleep(3)
    while True:
        image=ImageGrab.grab().convert('L')
        data=image.load()
        iscol(data)





