import discord
from discord.ext import commands,tasks
import random
import copy
import requests
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

##################################################################################################

@bot.command()
async def n(ctx,number=None,page=0):
    c = ctx.channel.is_nsfw()
    if c == False:
        await ctx.send("This is not NSFW channel")
    else:
        if number!=None:
            #爬蟲
            #從內容頁面
            page = 0
            url = f"https://nhentai.net/g/{number}/{page+1}/"
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'}
            def crawler(p):
                print(f"爬蟲")
                url = f"https://nhentai.net/g/{number}/{p+1}/"
                r = requests.get(url,headers=headers)
                Burl = BeautifulSoup(r.text, 'html.parser')
                img_tags = Burl.find_all('img')
                for tag in img_tags:
                    imgUrl = tag.get('src')
                print(f"imgUrl: {imgUrl}")
                imgUrl.rfind('.')
                u = imgUrl-3#未完成
                print(u)
                #判斷網頁是否結束
                if "404" in r:
                    pass
            crawler(page)
            #輸出訊息
            print("輸出訊息")
            embed=discord.Embed(color=0x009dff,title="Nhentai Viewer",url=url)
            embed.set_footer(text="By Young#0001")
            embed.set_image(url=url)
            message=await ctx.send(embed=embed)
            for i in ["◀","▶"]:
                await message.add_reaction(i)
            #檢查表情符號(函式)
            print("檢查表情符號")
            def check(reaction, user):
                return user == ctx.author and reaction.message == message
            #檢查表情符號(迴圈)
            while 1 :
                reaction, user = await bot.wait_for("reaction_add",timeout=60.0,check=check)
                if str(reaction) ==  "▶":
                    crawler(page+1)
                elif str(reaction) == "◀":
                    crawler(page-1)
                await message.remove_reaction(reaction,user)
                embed=discord.Embed(color=0x009dff,title="Nhentai Viewer",url=url)
                embed.set_footer(text="By Young#0001")
                embed.set_image(url=url)
                await message.edit(embed=embed)
        else:
            await ctx.send(f"Please input number")

##################################################################################################
bot.run(jdata['TestBotTOKEN'])