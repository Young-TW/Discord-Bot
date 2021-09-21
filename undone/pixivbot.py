import discord
from discord.ext import commands,tasks
import random
import copy
import requests
import bs4
import json

with open('setting.json', mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.all()
bot=commands.Bot(command_prefix=".",intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    game = discord.Game("Testing")
    await bot.change_presence(status=discord.Status.idle, activity=game)
##################################################################################################
@bot.command()
async def p(ctx,number=None):
    if "http" in number:
        number = number-31#從前面去除
    else:
        if number!=None:
            text = f"https://www.pixiv.net/artworks/{number}"
            #爬蟲
            page = requests.get(text)
            data = bs4.BeautifulSoup(page.text, "lxml")
            print(data)
            #輸出訊息
            embed=discord.Embed(color=0x009dff,title="Pixiv Viewer",url=text)
            embed.set_footer(text=" By Young#0001")
            embed.set_image(url=data)
            message=await ctx.send(embed=embed)
        else:
            await ctx.send(f"Please input number")   

#https://www.pixiv.net/ajax/illust/{number}/pages?lang=zh_tw
##################################################################################################
bot.run(jdata['TestBotTOKEN'])