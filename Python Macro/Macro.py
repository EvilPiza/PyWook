import PyWook as pyw
import pyautogui as pag
from time import sleep

def Macro():
    ROBLOX_START_UP()

#   Rest of Macro code can go here


def ROBLOX_START_UP():

    pyw.message("Opening Roblox...", "light blue")

    pag.press("winleft")

    sleep(2)

    pag.write("opera gx")     # Browser Name

    pag.press("enter")

    sleep(5)

    pag.leftClick(960, 50, 1)

    pag.write("https://www.roblox.com/share?code=a0962317a9359743aef5161a2a3ea217&type=Server")           # Roblox Link

    sleep(1)

    pag.press("enter")

    sleep(5)

    pyw.message("Roblox Opened!", "purple")

    sleep(8)

while __name__ == "__main__":
    Macro()
    __name__ = "Macro"

while pyw.end_macro:
    exit()
