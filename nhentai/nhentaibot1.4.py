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
Error404 = False
@bot.command()
async def n(ctx,number=None,page=0):
    c = ctx.channel.is_nsfw()
    if c == False:
        await ctx.send("This is not NSFW channel")
    else:
        if number!=None:
################################################################
            #爬蟲
            #從內容頁面
            #翻頁時爬下一張
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'}
            p = 1

            #定義爬蟲函式
            def Check404(r):#判斷網頁是否結束
                if "404" in r:
                    PageEnd()
                    return True
                else:
                    return False

            #輸入頁數 取得頁面連結
            def GetLink(p):
                print(f"GetLink p={p}")
                url = f"https://nhentai.net/g/{number}/{p}/"
                return url
            #url = Getlink(page)

            #輸入頁面連結 取得網頁回應
            def Crawler(url):
                print(f"Crawler url={url}")
                r = requests.get(url,headers=headers)
                return r
            #r = Crawler(Getlink(p))

            #輸入網頁回應 取得圖片連結
            def FindImgUrl(r):
                if Check404(r)==1:
                    PageEnd()

                print(f"FindImgUrl r={r}")
                Burl = BeautifulSoup(r.text, 'html.parser')
                img_tags = Burl.find_all('img')
                print(img_tags)
                img_tags  = BeautifulSoup(r.text, 'html.parser').find_all('img')
                print(img_tags)
                for tag in img_tags:
                    imgUrl = tag.get('src')
                print(f"imgUrl: {imgUrl}")
                #imgUrl.rfind('.')
                return imgUrl
            #imgUrl = FindImgUrl(Crawler(GetLink(p)))

            #輸入圖片連結 建立embed
            def CreateEmbed(imgUrl):
                embed=discord.Embed(color=0x009dff,title="Nhentai Viewer",url=imgUrl)
                embed.set_footer(text="By Young#0001")
                embed.set_image(url=imgUrl)
                return embed

            #檢查表情符號
            def check(reaction, user):
                return user == ctx.author and reaction.message == message

            #超出最後一頁時呼叫
            def PageEnd():
                embed=discord.Embed(color=0x009dff,title="Nhentai Viewer",description="The end.")
                embed.set_footer(text="By Young#0001")
            

            embed = CreateEmbed(FindImgUrl(Crawler(GetLink(p))))
            #輸入embed 傳送embed
            message = await ctx.send(embed=embed)

            #新增翻頁用表情符號
            for i in ["◀","▶"]:
                await message.add_reaction(i)
            

            while 1:
                reaction, user = await bot.wait_for("reaction_add",timeout=60.0,check=check)
                if Error404 == True:
                    PageEnd()
                    break
                else:
                    if str(reaction) ==  "▶":
                        page = page+1
                    elif str(reaction) == "◀":
                        page = page-1
                    await message.remove_reaction(reaction,user)

                    c = Crawler(page)
                    imgUrl = FindImgUrl(c)
                    Check404(c)
                    CreateEmbed(imgUrl)
                    await message.edit(embed=embed)#輸入embed 編輯已傳送embed
            '''
            def dcSend():
                reaction, user = await bot.wait_for("reaction_add",timeout=60.0,check=check)
                if Error404 == True:
                    embed=discord.Embed(color=0x009dff,title="Nhentai Viewer",description="The end.")
                    embed.set_footer(text="By Young#0001")
                    await message.edit(embed=embed)
                if str(reaction) ==  "▶":
                    crawler(page+1)
                elif str(reaction) == "◀":
                    crawler(page-1)
                await message.remove_reaction(reaction,user)
                embed=discord.Embed(color=0x009dff,title="Nhentai Viewer",url=url)
                embed.set_footer(text="By Young#0001")
                embed.set_image(url=url)
                await message.edit(embed=embed)
            '''
        else:
            await ctx.send(f"Please input number")

##################################################################################################
bot.run(jdata['TestBotTOKEN'])