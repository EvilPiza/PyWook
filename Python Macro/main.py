# Made By Christian Fillmore

import time as t
import random as r
import pyautogui as pag
import asyncio
import discord
from discord import Webhook
import aiohttp
import tkinter as tk
import pyscreeze as pys
from PIL import Image

webhook_url = ""


################################
# START GUI
################################

class Start_Setup:

    def __init__(self):
        self.screen = tk.Tk()
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
# WEBHOOK
################################

default_message = "Uh Oh!"

async def Program(url, message, _type):
    if _type == "MESSAGE":
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(url, session = session)
            embed = discord.Embed(title=message)
            await webhook.send(embed=embed, username = "Py-Macro")

    elif _type == "IMAGE":
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(url, session = session)
            _Image = discord.File(fp="screenshots/Screenshot.png")
            await webhook.send(file=_Image, username = "Py-Macro")        

def start(_type="MESSAGE", message=default_message, url=webhook_url):
    loop = asyncio.new_event_loop()
    loop.run_until_complete(Program(url, message, _type))
    loop.close()

if webhook_url == "":
    start_setup = Start_Setup()
    webhook_url = start_setup.OK_BUTTON()
    print(webhook_url)


ok = pys.screenshot("screenshots/Screenshot.png")

################################
# MACRO
################################


