import os
import discord
import asyncio
import random
from discord.ext import commands
from discord.utils import get

Token = ("MTA4MTgzOTU1MDU2Mjg0MDYyNg.Gmd3Pb.QyU42JstgsoXdzBoSthsbKe4GV4hW7w_OFerVw")
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


bot.run(Token)

