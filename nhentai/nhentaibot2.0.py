import discord
from discord.ext import commands
import requests
import threading
from bs4 import BeautifulSoup

intents = discord.Intents.all()
bot=commands.Bot(command_prefix=".",intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    game = discord.Game("Testing")
    await bot.change_presence(status=discord.Status.idle, activity=game)

##################################################################################################

urls = []

def crawlerPage(number,page):
    print(f"第{page}圈爬蟲")
    url = f"https://nhentai.net/g/{number}/{page}/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'}
    r = requests.get(url,headers=headers)
    Burl = BeautifulSoup(r.text, 'html.parser')
    img_tags = Burl.find_all('img')
    for tag in img_tags:
        imgUrl = tag.get('src')
    if imgUrl == "https://static.nhentai.net/img/logo.090da3be7b51.svg":
        return False #爬到logo代表已經結束了
    else:
        urls.append(imgUrl)

def crawlerLoop(number):
    threads = [] #宣告一個list用來放多線程
    page = 1
    while 1:
        threads.append(threading.Thread(target = crawlerPage, args=(number,page)))
        if crawlerPageIndex == False:
            break #第30行回傳False代表爬完了就break
        crawlerPageIndex = threads[page].start()
        page += 1

@bot.command()
async def n(ctx,number=None,page=0):
    c = ctx.channel.is_nsfw()
    if c == False:
        await ctx.send("This is not NSFW channel")
    else:
        if number!=None:
            #爬蟲
            #從內容頁面
            crawlerLoop(number)

            page = 1
            #輸出訊息
            print("輸出訊息")
            embed=discord.Embed(color=0x009dff,title="Nhentai Viewer")
            embed.set_footer(text="By Young#0001")
            embed.set_image(url=urls[0])
            message=await ctx.send(embed=embed)
            for i in ["◀","▶"]:
                await message.add_reaction(i)
            #檢查表情符號(函式)
            print("檢查表情符號")
            def check(reaction, user):
                return user == ctx.author and reaction.message == message
            #檢查表情符號(迴圈)
            while 1 :
                if(page > len(urls) - 1):
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
                embed=discord.Embed(color=0x009dff,title="Nhentai Viewer")
                embed.set_footer(text="By Young#0001")
                embed.set_image(url=urls[page])
                await message.edit(embed=embed)
        else:
            await ctx.send(f"Please input number")

##################################################################################################
bot.run('token here')