import discord
from discord.ext import commands,tasks
from discord import Guild, guild
import random
import copy
import requests
import bs4

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
    if number!=None:
        text = f"https://nhentai.net/g/{number}/"
        #爬蟲
        hentai = requests.get(text)
        data = bs4.BeautifulSoup(hentai.text, "lxml").select("#thumbnail-container img")
        urls = [i["src"] for i in data if not i["src"].startswith("data")]
        url = urls[0]
        #輸出訊息
        #embed=discord.Embed(color=0x009dff,title="Nhentai Viewer",url=(urls[page]))
        embed=discord.Embed(color=0x009dff,title="Nhentai Viewer",url=url)
        embed.set_footer(text=" By Young#0001")
        #embed.set_image(url=urls[page])
        embed.set_image(url=url)
        message=await ctx.send(embed=embed)
        for i in ["◀","▶"]:
            await message.add_reaction(i)
        #檢查表情符號(函式)
        def check(reaction, user):
            return user == ctx.author and reaction.message == message
        #翻頁
        '''
        def userinput(self):
            page={"◀":self.left,"▶":self.right}
        def left(self):
            return page-1
        def right(self):
            return page+1
        '''
        #檢查表情符號(迴圈)
        print (f"{url[:-6]}{page+1}t.jpg")#print以確認頁數
        while 1 :
            reaction, user = await bot.wait_for("reaction_add",timeout=60.0,check=check)
            if reaction ==  "▶":
                page+=1
            elif reaction == "◀":
                page-=1
            await message.remove_reaction(reaction,user)
            #userinput(str(reaction))

            #embed=discord.Embed(color=0x009dff,title="Nhentai Viewer",url=(urls[page]))
            embed=discord.Embed(color=0x009dff,title="Nhentai Viewer",url=f"{url[:-6]}{page+1}t.jpg")
            embed.set_footer(text="By Young#0001")
            #embed.set_image(url=urls[page])
            embed.set_image(url=f"{url[:-6]}{page+1}t.jpg")
            print (f"{url[:-6]}{page+1}t.jpg")
            await message.edit(embed=embed)
    else:
        await ctx.send(f"請輸入參數")
##################################################################################################
'''
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
        res = requests.get(text)
        content = res.content.decode()
        print (content)
'''
#text = f"https://nhentai.to/g/{number}/{page}/"
'''
@commands.command()
async def nv(ctx:commands.Context):
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
        embed=discord.Embed(title="Nhentai Viewer",description=f"```\n{text}\n```")
        await message.edit(embed=embed)
'''
'''
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
res = requests.get("https://nhentai.to")
content = res.content.decode()

page = 1
number = 150449
hentai = requests.get("https://nhentai.to/g/"+"{number}/")
data = bs4.BeautifulSoup(hentai.text, "lxml").select("#thumbnail-container img")
urls = [i["src"] for i in data if not i["src"].startswith("data")]

print(urls)
'''

bot.run('Nzg2OTg2OTU0NDc4NTgzODU4.X9OYtw.qUcAwXfdLTFkGG9J2HXhc3JKn-8')