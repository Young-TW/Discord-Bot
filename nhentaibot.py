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
async def n(ctx,channel,number=None,page=0):
    channel = n.channel
    c = channel.is_nsfw(channel)
    if c == 1:
        if number!=None:
            #爬蟲
            #從內容頁面
            '''
            page = 1
            while 1:
                text = f"https://nhentai.net/g/{number}/{page}/"
                hentai = requests.get(text)
                data = bs4.BeautifulSoup(hentai.text, "lxml").select("#image-container img")#這行不確定
                urls[page] = None#這邊爬蟲不會寫
                if urls[page] == None:
                    break
                #if not i["src"].startswith("data")
                page += 1
                #img class=fit-horizontal
                #section id=image-container
            '''
            #從預覽頁面
            text = f"https://nhentai.net/g/{number}/"
            hentai = requests.get(text)
            data = bs4.BeautifulSoup(hentai.text, "lxml").select("#thumbnail-container img")
            urls = [i["src"] for i in data if not i["src"].startswith("data")]
            #輸出訊息
            embed=discord.Embed(color=0x009dff,title="Nhentai Viewer",url=text)
            embed.set_footer(text="By Young#0001")
            embed.set_image(url=urls[0])
            message=await ctx.send(embed=embed)
            for i in ["◀","▶"]:
                await message.add_reaction(i)
            #檢查表情符號(函式)
            def check(reaction, user):
                return user == ctx.author and reaction.message == message
            #檢查表情符號(迴圈)
            while 1 :
                if(page + 1 > len(urls) - 1):
                    embed=discord.Embed(color=0x009dff,title="Nhentai Viewer",description="The end.")
                    embed.set_footer(text="By Young#0001")
                    await message.edit(embed=embed)
                    break
                reaction, user = await bot.wait_for("reaction_add",timeout=60.0,check=check)
                if str(reaction) ==  "▶":
                    page+=1
                elif str(reaction) == "◀":
                    page-=1
                await message.remove_reaction(reaction,user)
                embed=discord.Embed(color=0x009dff,title="Nhentai Viewer",url=text)
                embed.set_footer(text="By Young#0001")
                embed.set_image(url=urls[page])
                await message.edit(embed=embed)
        else:
            await ctx.send(f"Please input number")   
    else:
        ctx.send("This is not NSFW channel")
##################################################################################################
bot.run(jdata['TestBotTOKEN'])