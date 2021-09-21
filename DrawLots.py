'''
import discord
from discord.ext import commands,tasks
import copy
import bs4
import json
from bs4 import BeautifulSoup

with open('setting.json', mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.all()
bot=commands.Bot(command_prefix=".",intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    game = discord.Game("Testing")
    await bot.change_presence(status=discord.Status.idle, activity=game)
'''
##################################################################################################
import random

count = int(1)
a = []
while 1:
    a = a + input("")
    if a[count] == "0":
        break
    count += 1

print(a)

##################################################################################################
#bot.run(jdata['TestBotTOKEN'])

# 不會寫 哭哭
# 未完成