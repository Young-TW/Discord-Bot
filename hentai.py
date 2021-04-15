import bs4
import copy
import discord
from discord import Guild, guild#Guild定義在discord底下
from discord.ext import commands,tasks#這裡是discord.ext
import random
import requests


intents = discord.Intents.all()
bot=commands.Bot(command_prefix=".",intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    game = discord.Game("testing")
    await bot.change_presence(status=discord.Status.online, activity=game)
#####################################################################################
'''
@bot.command()
async def n(ctx,number=None,page=0):
    if number!=None:
        text = f"https://nhentai.net/g/{number}/"
        #爬蟲
        hentai = requests.get(text)
        data = bs4.BeautifulSoup(hentai.text, "lxml").select("#thumbnail-container img")
        urls = [i["src"] for i in data if not i["src"].startswith("data")]
        #輸出訊息
        embed=discord.Embed(color=0x009dff,title="Nhentai Viewer",url=(urls[page]))
        embed.set_footer(text=" By Young#0001")
        embed.set_image(url=urls[page])
        message=await ctx.send(embed=embed)
        for i in ["◀","▶","⏹"]:
            await message.add_reaction(i)
        #檢查表情符號
        def check(reaction, user):
            return user == ctx.author and reaction.message == message
        while 1 :
            reaction, user = await bot.wait_for("reaction_add",timeout=60.0,check=check)
            await message.remove_reaction(reaction,user)
            if str(reaction)=="⏹":break
            ww.userinput(str(reaction))
            embed=discord.Embed(color=0x009dff,title="Nhentai Viewer",url=(urls[page]))
            embed.set_footer(text="By Young#0001")
            embed.set_image(url=urls[page])
            await message.edit(embed=embed)
    else:
        await ctx.send(f"請輸入參數")
'''
###################################################################################################

class nv():
    def __init__(self,ctx,number=None,page=0):
        text = f"https://nhentai.net/g/{number}/"
        #爬蟲
        hentai = requests.get(text)
        data = bs4.BeautifulSoup(hentai.text, "lxml").select("#thumbnail-container img")
        urls = [i["src"] for i in data if not i["src"].startswith("data")]
        self.imgprint
    def imgprint(self,ctx):
        #印出圖片
        embed=discord.Embed(color=0x009dff,title="Nhentai Viewer",url=(urls[page]))
        embed.set_footer(text="Young#0001")
        embed.set_image(urls[page])
        message = await ctx.send(embed=embed)
    def p(self):
        page = {"◀":self.left,"▶":self.right}

    def left(self):
        page=page-1
        self.imgprint
        #往前翻頁   page=page-1
    def right(self):
        page=page+1
        self.imgprint
        #往後翻頁   page=page+1

    @commands.command()
    async def nv(self,ctx:commands.Context):
        embed=discord.Embed(color=0x009dff,title="Nhentai Viewer",url=(urls[page]))
        embed.set_footer(text="By Young#0001")
        embed.set_image(urls[page])
        message=await ctx.send(embed=embed)
        for i in ["◀","▶","⏹"]:
            await message.add_reaction(i)
        def check(reaction, user):
            return user == ctx.author and reaction.message == message
        while 1 :
            reaction, user = await self.bot.wait_for("reaction_add",timeout=60.0,check=check)
            await message.remove_reaction(reaction,user)
            if str(reaction)=="⏹":break
            nv.userinput(str(reaction))
            text=nv.imgprint()
            embed=discord.Embed(color=0x009dff,title="Nhentai Viewer",url=(urls[page]))
            embed.set_footer(text="By Young#0001")
            embed.set_image(urls[page])
            await message.edit(embed=embed)

#####################################################################################
    
'''
    def __init__(self,bot):
        self.bot=bot
'''
'''
    def p(self):
        page = {"◀":self.left,"▶":self.right}
'''
'''    
    def left(self):
        page=page-1
        self.imgprint
        #往前翻頁   page=page-1
    def right(self):
        page=page+1
        self.imgprint
        #往後翻頁   page=page+1
'''
'''
class Game(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    @commands.command()
    async def nv(self,ctx:commands.Context):
        embed=discord.Embed(color=0x009dff,title="Nhentai Viewer",url=(urls[page]))
        embed.set_footer(text="By Young#0001")
        embed.set_image(urls[page])
        message=await ctx.send(embed=embed)
        for i in ["◀","▶","⏹"]:
            await message.add_reaction(i)
        def check(reaction, user):
            return user == ctx.author and reaction.message == message
        while 1 :
            reaction, user = await self.bot.wait_for("reaction_add",timeout=60.0,check=check)
            await message.remove_reaction(reaction,user)
            if str(reaction)=="⏹":break
            ww.userinput(str(reaction))
            text,t=ww.imgprint()
            embed=discord.Embed(color=0x009dff,title="Nhentai Viewer",url=(urls[page]))
            embed.set_footer(text="By Young#0001")
            embed.set_image(urls[page])
            await message.edit(embed=embed)
bot.add_cog(Game(bot))
'''

#Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36
#Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36

#requests.get("https://nhentai.net/g/{number}/{page}/")
'''
@bot.command()
async def osumap(self,ctx,number=None):
    if number!=None:
        await ctx.send(f"https://osu.ppy.sh/beatmapsets/{number}#osu/")
    else :
        await ctx.send("請輸入參數")
'''

'''
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
res = requests.get("https://nhentai.to")
content = res.content.decode()
'''

'''
hati = requests.get("https://nhentai.to/g/340551")
data = bs4.BeautifulSoup(hati.text, "lxml").select("#thumbnail-container img")
img_urls = [i["src"] for i in data if not i["src"].startswith("data")]
print(img_urls)
'''

'''
page = 1
number = 150449
hentai = requests.get("https://nhentai.to/g/"+"{number}/")
data = bs4.BeautifulSoup(hentai.text, "lxml").select("#thumbnail-container img")
urls = [i["src"] for i in data if not i["src"].startswith("data")]
#print(urls[page])

#cdn = "https://cdn.dogehls.xyz/galleries/1804195/"+{page}+"t.jpg"

print(urls)
'''



'''
class nv():
    def __init__(self,difficulty):
        
    def userinput(self,x):
        number={"◀":self.left,"▶":self.right}
        page[]()
    def getnhentai(self):
        #放爬蟲
        hati = requests.get("https://nhentai.to/g/{number}/{page}/")
        data = bs4.BeautifulSoup(hati.text, "lxml").select("#thumbnail-container img")
        urls = [i["src"] for i in data if not i["src"].startswith("data")]
        print(urls)
    def imgprint(self):
        #印出圖片
    def left(self):
        page=page-1
        #往前翻頁   page=page-1
    def right(self):
        page=page+1
        #往後翻頁   page=page+1
'''

'''
class Game(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    @commands.command()
    async def nv(self,ctx:commands.Context,level:int=None):
        ww=nv(level)
        text,_=ww.imgprint()
        embed=discord.Embed(title="Nhentai Viewer",description=f"```\n{text}\n```")
        message=await ctx.send(embed=embed)
        for i in ["◀","▶","⏹"]:
            await message.add_reaction(i)
        def check(reaction, user):
            return user == ctx.author and reaction.message == message
        while 1 :
            reaction, user = await self.bot.wait_for("reaction_add",timeout=60.0,check=check)
            await message.remove_reaction(reaction,user)
            if str(reaction)=="⏹":break
            ww.userinput(str(reaction))
            text,t=ww.mapprint()
            embed=discord.Embed(title="Nhentai Viewer",description=f"```\n{text}\n```")
            await message.edit(embed=embed)
            if t :
                await ctx.send("已停止")
                break
bot.add_cog(Game(bot))
'''
#####################################################################################
bot.run('')