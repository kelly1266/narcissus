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


class DiscordClient(discord.Client):
    async def on_ready(self):
        print('DISCORD:')
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        # clear all the messages in the soundboard channel
        print('------')
        self.image_to_string.start()

    @tasks.loop(seconds=5)
    async def image_to_string(self):
        pytesseract.pytesseract.tesseract_cmd = config.TESSERACT_PATH
        # TODO: FIND BBOX DIMENSIONS
        cap = ImageGrab.grab(bbox=(400, 500, 1000, 900))

        # Converted the image to monochrome for it to be easily
        # read by the OCR and obtained the output String.
        tesstr = pytesseract.image_to_string(
            cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY),
            lang='eng')
        await self.lookup_enemy(tesstr)

    async def lookup_enemy(self, name):
        names = parse_name(name)
        names = ['mizkif', 'elpadog']


def parse_name(name):
    possible_names = []
    possible_addons = ['tv', 'ttv', '_tv', '_ttv']
    removables = ['you exiled ', 'you assisted in exiling ', 'you disrupted ', '\n', '\x0c']
    # convert to lowercase for easier parsing
    name = name.lower()
    # remove
    for removable in removables:
        name = name.replace(removable, '')
    # add the cleaned up name to the list of possible names
    possible_names.append(name)
    # remove any additional signifiers
    for addon in possible_addons:
        if addon in name:
            possible_names.append(name.replace(addon, ''))
    return possible_names


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
        print(output)
        return output
    except Exception as e:
        print( 'gettwitchapi' , e )
        return e


discord_bot = DiscordClient()
discord_bot.run(config.DISCORD_TOKEN)

