# PyWook
# Made By Christian Fillmore

import asyncio
import discord
from discord import Webhook
import aiohttp
import pyscreeze as pys
from PIL import Image
from inspect import getframeinfo, stack
from colorama import Fore, Style
from tkinter import Tk as tk
import pyautogui as pag


################################
# WEBHOOK GUI
################################

class Webhook_Gui:

    def __init__(self):
        self.screen = tk()
        self.screen.geometry("450x400")
        self.screen.title("Py-Macro Start")
        self.mainframe = tk.Frame(self.screen, background="gray")
        self.mainframe.pack(fill="both", expand=True)

        self.text = tk.Label(self.mainframe, text="Py-Macro", background='gray', font=('Brass Mono', 30))
        self.text.grid(row=0, column=0, padx=140, pady=25)

        self.little_text = tk.Label(self.mainframe, text="Paste your webhook url below", background='gray', font=('Brass Mono', 15)) 
        self.little_text.grid(row=1, column=0)

        self.text_box = tk.Entry(self.mainframe)
        self.text_box.grid(row=2, column=0, pady=15, sticky="NWES")

        self.ok_button = tk.Button(self.mainframe, text="OK", command=self.OK_BUTTON)
        self.ok_button.grid(row=3, column=0, pady=5)

        self.screen.mainloop()

    def OK_BUTTON(self):
        self.screen.quit()
        self.webhook_url = self.text_box.get()
        return str(self.webhook_url)


################################
# VARIABLES
################################

default_webhook_url = ""

discord_bot_token = ""

show_time = True

webhook_username = "Py-Macro"

custom_webhook_user = True

image_path = ""

user_id = 0

webhook_gui = False

custom_gui = False

default_embed_color = (55, 103, 246)

file_name = ""

current_task = ""

# You can replace 'default_embed_color' with words/presets:
presets = ("red", "blue", "green", "light red", "light blue", "light green", "dark red", "dark blue", "dark green", "white", "black", "magenta", "cyan", "yellow", "orange", "purple")


################################
# PyWook Class
################################

class PyWook:

    def __init__(self):

        self.default_webhook_url = default_webhook_url

        self.discord_bot_token = discord_bot_token

        self.show_time = show_time

        self.webhook_username = webhook_username

        self.custom_webhook_user = custom_webhook_user

        self.image_path = image_path

        self.user_id = user_id

        self.webhook_gui = webhook_gui

        self.custom_gui = custom_gui

        self.default_embed_color = default_embed_color

        self.file_name = file_name

        self.current_task = current_task

        # You can replace 'default_embed_color' with words/presets:
        self.presets = ("red", "blue", "green", "light red", "light blue", "light green", "dark red", "dark blue", "dark green", "white", "black", "magenta", "cyan", "yellow", "orange", "purple")

    def str_to_int_color(color):
        if isinstance(color, str):
            color = color.lower()
            match color:
                case "red":
                    color = (255, 0, 0)
                case "green":
                    color = (0, 255, 0)
                case "blue":
                    color = (0, 0, 255)
                case "light red":
                    color = (247, 104, 104)
                case "light green":
                    color = (135, 252, 111)
                case "light blue":
                    color = (111, 250, 252)
                case "dark red":
                    color = (133, 0, 0)
                case "dark green":
                    color = (0, 133, 0)
                case "dark blue":
                    color = (0, 0, 133)
                case "white":
                    color = (255, 255, 255)
                case "black":
                    color = (0, 0, 0)
                case "magenta":
                    color = (247, 5, 223)
                case "cyan":
                    color = (247, 5, 223)
                case "yellow":
                    color = (243, 247, 5)
                case "orange":
                    color = (247, 138, 5)
                case "purple":
                    color = (162, 5, 247)
        return color
    
    def debug_stuff(self):

        if self.webhook_username == "":
            self.custom_webhook_user = False

        if self.default_webhook_url == "":
            if self.webhook_gui == True:
                from tkinter import tk
                start_setup = Webhook_Gui()
                self.webhook_url = start_setup.OK_BUTTON()
            else:
                print("Webhook URL is set to null!")
                print("Either manually input your Webhook into 'default_webhook_gui' or set 'webhook_gui' to True!")
                exit()
        else:
            webhook_url = self.default_webhook_url

    async def Text(self, url, message, embed_color, error=False):
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(url, session = session)
            if self.show_time == True:
                from datetime import datetime
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                message = f"[{current_time}]  {message}"
            embed = discord.Embed(title=message, color=discord.Color.from_rgb(embed_color[0], embed_color[1], embed_color[2]))
            if self.custom_webhook_user == True:
                await webhook.send(embed=embed, username=self.webhook_username)
            else:
                await webhook.send(embed=embed)
            if error == True:
                await webhook.send(f"<@{self.user_id}>")

    async def Image_(self, url):
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(url, session = session)
            file = discord.File(fp=self.image_path)
            if self.custom_webhook_user == True:
                await webhook.send(file=file, username=self.webhook_username)
            else:
                await webhook.send(file=file)

    def message(message, embed_color=default_embed_color, url=default_webhook_url, error=False):
        if not isinstance(message, str):
            caller = getframeinfo(stack()[1][0])
            print("File '%s' - Line %d - %s" % (caller.filename, caller.lineno, "Type Error (" + Fore.RED + f"{type(message).__name__}"+ Style.RESET_ALL +" -> " + Fore.GREEN + "str"+ Style.RESET_ALL +")"))
            exit()
        if isinstance(url, str):
            if url[:33] != "https://discord.com/api/webhooks/":
                caller = getframeinfo(stack()[1][0])
                print("File '%s' - Line %d - %s" % (caller.filename, caller.lineno, "Value Error (Invalid Webhook URL)"))
                exit()
        else:
            caller = getframeinfo(stack()[1][0])
            print("File '%s' - Line %d - %s" % (caller.filename, caller.lineno, "Type Error (" + Fore.RED + f"{type(url).__name__}"+ Style.RESET_ALL +" -> " + Fore.GREEN + "str"+ Style.RESET_ALL +")"))
            exit()

        if isinstance(embed_color, str):
            if embed_color not in presets:
                caller = getframeinfo(stack()[1][0])
                print("File '%s' - Line %d - %s" % (caller.filename, caller.lineno, "Value Error (invalid string)"))
                exit()

            embed_color = PyWook.str_to_int_color(embed_color)
        elif isinstance(embed_color, tuple):
            if not len(embed_color) == 3:
                caller = getframeinfo(stack()[1][0])
                print("File '%s' - Line %d - %s" % (caller.filename, caller.lineno, "Value Error (tuple has missing/overflow values)"))
                exit() 
            if not embed_color[0] <= 255 or not embed_color[1] <= 255 or not embed_color[2] <= 255:
                caller = getframeinfo(stack()[1][0])
                print("File '%s' - Line %d - %s" % (caller.filename, caller.lineno, "Value Error (tuple above 255)"))
                exit()
            elif embed_color[0] < 0 or embed_color[1] < 0 or embed_color[2] < 0:
                caller = getframeinfo(stack()[1][0])
                print("File '%s' - Line %d - %s" % (caller.filename, caller.lineno, "Value Error (tuple below 0)"))
                exit()
        else:
            caller = getframeinfo(stack()[1][0])
            print("File '%s' - Line %d - %s" % (caller.filename, caller.lineno, "Type Error (" + Fore.RED + f"{type(embed_color).__name__}"+ Style.RESET_ALL +" -> " + Fore.GREEN + "str/tuple"+ Style.RESET_ALL +")"))
            exit()
        pywook = PyWook()
        loop = asyncio.new_event_loop()
        loop.run_until_complete(pywook.Text(url, message, embed_color, error))
        loop.close()

    def image(url=default_webhook_url):
        if isinstance(url, str):
            if url[:33] != "https://discord.com/api/webhooks/":    
                caller = getframeinfo(stack()[1][0])
                print("File '%s' - Line %d - %s" % (caller.filename, caller.lineno, "Value Error (Invalid Webhook URL)"))
                exit()
        else:
            caller = getframeinfo(stack()[1][0])
            print("File '%s' - Line %d - %s" % (caller.filename, caller.lineno, "Type Error (" + Fore.RED + f"{type(url).__name__}"+ Style.RESET_ALL +" -> " + Fore.GREEN + "str"+ Style.RESET_ALL +")"))
            exit()
        pywook = PyWook()
        pys.screenshot(image_path)
        loop = asyncio.new_event_loop()
        loop.run_until_complete(pywook.Image_(url))
        loop.close()

    def mention_mess(self, text, color=(255, 0, 0)):
        self.message(text, color, self.webhook_url, True)
        self.image()

def END():
    exit()

def ROBLOX_START_UP():
    pyw = PyWook()
    from time import sleep

    pyw.message("Opening Roblox...", 'light blue')

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

    pyw.message("Roblox Opened!", 'purple')

    sleep(8)


################################
# HELP FUNCTION
################################

def help():
    print("""
        ----------------------------------------------------------
          
          SYNTAX:

          - message("text", (rgb values, or a preset in str form), "webhook url variable")

          - image("webhook url variable")

          - mention_mess("text", (rgb values, or a preset in str form))


          IMPORTANT VARIABLES:

          default_webhook_url           < Set this to a webhook url, make sure it's a str

          image_path                    < Set this to a path, ex: "C:/users/John Doe/Desktop/Secret Coding Stash/image.png"

          user_id                       < Set this to a discord user id (should be set to an int, NOT str)

        ----------------------------------------------------------
          """)
