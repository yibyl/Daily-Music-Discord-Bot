<<<<<<< Updated upstream
import os
import discord
import asyncio
import random
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get

load_dotenv()
Token = ("MTA4MTgzOTU1MDU2Mjg0MDYyNg.Gep1HS.wsg09Q7yHOu00IfVvHxfkPy6zau8eqyIzq-MHc")
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


bot.run(Token)
=======
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#cock and balls
>>>>>>> Stashed changes
