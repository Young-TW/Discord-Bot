import discord
from discord.ext import commands,tasks
import requests
# import json
import nhentaiCrawer
import nhentaiEmbed

# with open('setting.json', mode='r',encoding='utf8') as jfile:
    # jdata = json.load(jfile)

intents = discord.Intents.all()
bot=commands.Bot(command_prefix="[",intents=intents)

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
        urls = []
            
        if number!=None:
            #爬蟲
            #從內容頁面
            urls,url = nhentaiCrawer.crawler(number,page)
            print(urls,url)

            page = 0
            #輸出訊息
            print("輸出訊息")
            embed = discord.Embed
            nhentaiEmbed.Embedinit()
            embed.set_image(url=urls[0])
            #增加表情符號
            message=await ctx.send(embed=embed)
            for i in ["◀","▶"]:
                await message.add_reaction(i)
            #檢查表情符號(函式)
            print("檢查表情符號")
            def check(reaction, user):
                return user == ctx.author and reaction.message == message
            #檢查表情符號(迴圈)
            while 1 :
                print("檢查表情符號(迴圈)")
                if(page + 1 > len(urls) - 1):
                    print("已結束")
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
                embed=discord.Embed(color=0x009dff,title="Nhentai Viewer",url=url)
                embed.set_footer(text="By Young#0001")
                embed.set_image(url=urls[page])
                await message.edit(embed=embed)
        else:
            await ctx.send(f"Please input number")

##################################################################################################
# bot.run(jdata['TestBotTOKEN'])

bot.run("Nzg2OTg2OTU0NDc4NTgzODU4.X9OYtw.oqe0V_ICdc5tn61nQTyaB2eMqqE")