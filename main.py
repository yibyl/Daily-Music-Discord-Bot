import os
import discord
import asyncio
import random
from discord.ext import commands
from discord.utils import get

Token = ("")
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    if message.author.id == 238752815055372290:
        await message.delete()
        dm = await message.author.create_dm()
        await message.channel.send("no speak " + message.author.name)

    await bot.process_commands(message)

bot.run(Token)

