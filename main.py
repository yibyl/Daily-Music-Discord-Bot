import discord
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from discord.ext import commands
from selenium import webdriver
from bs4 import BeautifulSoup
import random

Token = ("token")
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='$', intents=intents)

url = "https://rateyourmusic.com/charts/"
driver = webdriver.Chrome()
totalalbs = 0
filteredlinks = []
for pages in range(26):
    url = "https://rateyourmusic.com/charts/top/album/2023/" + str(pages + 1) + "/"
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content)
    links = []
    for i in soup.find_all('a'):
        links.append(i.get('href'))

    totalalbs += 40

    for i in links:
        if i == None:
            continue
        temp = i.split('/')
        if len(temp) == 6 and temp[1] == "release" and temp[2] == "album" and temp not in filteredlinks:
            filteredlinks.append(temp)

    filteredlinks = filteredlinks[:totalalbs]
jsonf = {'albums': []}
allsongs = []
for i in filteredlinks:
    url = "https://rateyourmusic.com/release/album/" + i[3] + "/" + i[4] + "/"
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content)
    songs = []
    for a in soup.find_all('li'):
        if '<span class="tracklist_title"><span class="rendered_text">' in str(a):
            temp = str(a).split("\n")[-3].split(">")[2][:-6]
            songs.append(temp)
            allsongs.append(temp)
    jsonf['albums'].append({'artist': i[3], 'album': i[4], 'songs': songs})


async def daily():
    letters = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
    while True:
        done = False
        try:
            while True:
                valid = True
                r1 = random.randint(0, totalalbs - 1)
                artist = jsonf['albums'][r1]['artist']
                r2 = random.randint(0, len(jsonf['albums'][r1]['songs']) - 1)
                song = jsonf['albums'][r1]['songs'][r2]
                acount = 0
                for i in artist:
                    if i == " ":
                        acount += 1;
                        artist = artist.replace(" ", "+", acount)
                scount = 0
                for i in song:
                    if i == " ":
                        scount += 1;
                        song = song.replace(" ", "+", scount)
                for i in artist + song:
                    if i not in letters:
                        vaild = False
                if valid == True:
                    break
            url = "https://www.youtube.com/results?search_query=" + song + "+" + "by" + "+" + artist
            driver.get(url)
            content = driver.page_source
            soup = BeautifulSoup(content)
            vids = []
            for i in soup.find_all(id='video-title'):
                vids.append(i.get('href'))
            text_channel_list = []
            for guild in bot.guilds:
                for channel in guild.text_channels:
                    text_channel_list.append(channel)
            for i in text_channel_list:
                await i.send("https://www.youtube.com/" + vids[1])
                done = True
        except:
            done = False
        if done:
            break


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    scheduler = AsyncIOScheduler()
    scheduler.add_job(daily, CronTrigger(hour="0",minute="0",second="0"))
    scheduler.start()


bot.run(Token)
