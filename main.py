import numpy as nm
import pytesseract
import cv2
from PIL import ImageGrab
import config
import discord
from discord.ext.commands import Bot
from discord.ext import tasks
import urllib.request
import urllib.error
import json
import tkinter as tk
import re
from helper_functions import parse_name, parse_notif_from_tesseract


class DiscordClient(discord.Client):
    async def on_ready(self):
        print('DISCORD:')
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        # clear all the messages in the soundboard channel
        print('------')
        self.image_to_string.start()

    @discord.ext.tasks.loop(seconds=2.5)
    async def image_to_string(self):

        pytesseract.pytesseract.tesseract_cmd = config.TESSERACT_PATH
        # get the bounding box dimensions for image grab based off of screen dimensions
        root = tk.Tk()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        y_offset = 300
        x1 = screen_width / 2 - 500
        y1 = screen_height / 2 - 25 + y_offset
        x2 = screen_width / 2 + 500
        y2 = screen_height / 2 + 25 + y_offset
        # capture the section of the screen where notifications appear
        cap = ImageGrab.grab(bbox=(x1, y1, x2, y2))

        # Converted the image to monochrome for it to be easily
        # read by the OCR and obtained the output String.
        tesstr = pytesseract.image_to_string(
            cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY),
            lang='eng')
        #notif_str = parse_notif_from_tesseract(tesstr)
        notif_str= tesstr
        if 'you' in notif_str.lower():
            print(notif_str)
            cap.save(fp=('C:\\Users\\Ben\\Desktop\\misc ideas and notes\\pics'+str(self.i)+'.png'))
            await self.lookup_enemy(notif_str)

    async def lookup_enemy(self, name):
        names = parse_name(name)
        users = get_users(names)
        try:
            for user in users['data']:
                clip = create_clip(user['id'])
                await self.get_channel(config.DISCORD_CHANNEL).send(clip['data']['edit_url'])
        except Exception as e:
            print('Error: ', e)


def get_users(users):
    try:
        url = f"https://api.twitch.tv/helix/users?"
        heading = {
            "Client-ID": config.TWITCH_CLIENT_ID,
            "Authorization":("Bearer "+config.TOKEN)
        }
        for user in users:
            url += "login="+user+"&"

        req = urllib.request.Request(url, headers=heading)
        response = urllib.request.urlopen(req)
        output = json.loads(response.read())
        return output
    except Exception as e:
        print( 'gettwitchapi' , e )
        return e


def create_clip(broadcast_id):
    try:
        url = f"https://api.twitch.tv/helix/clips?broadcaster_id="+broadcast_id
        heading = {
            "Client-ID": config.TWITCH_CLIENT_ID,
            "Authorization":("Bearer "+config.OAUTH_TOKEN)
        }
        req = urllib.request.Request(url, headers=heading, method='POST')
        response = urllib.request.urlopen(req)
        output = json.loads(response.read())
        return output
    except Exception as e:
        print( 'gettwitchapi' , e )
        return e


discord_bot = DiscordClient()
discord_bot.run(config.DISCORD_TOKEN)

