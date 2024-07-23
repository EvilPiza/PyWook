# Made By Christian Fillmore

import time
from datetime import datetime
import random
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

if webhook_url == "":
    start_setup = Start_Setup()
    webhook_url = start_setup.OK_BUTTON()

async def Text(url, message, embed_color):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(url, session = session)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        message = f"[{current_time}] {message}"
        embed = discord.Embed(title=message, color=discord.Color.from_rgb(embed_color[0], embed_color[1], embed_color[2]))
        await webhook.send(embed=embed, username = "Py-Macro")

async def Image_(url):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(url, session = session)
        file = discord.File(fp="screenshots/Screenshot.png")
        await webhook.send(file=file, username="Py-Macro")

def start(_type="MESSAGE", message="Error Message Missing!", url=webhook_url, embed_color=(0,0,0)): 
    if _type == "MESSAGE":
        loop = asyncio.new_event_loop()
        loop.run_until_complete(Text(url, message, embed_color))
        loop.close()
    
    elif _type == "IMAGE":
        loop = asyncio.new_event_loop()
        loop.run_until_complete(Image_(url))
        loop.close()

ok = pys.screenshot("screenshots/Screenshot.png")


################################
# MACRO
################################

start("MESSAGE", "Starting Macro!", webhook_url, (52, 97, 235))
start("IMAGE", "", webhook_url, ())
