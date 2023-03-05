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
