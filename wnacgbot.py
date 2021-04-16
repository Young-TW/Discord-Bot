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
async def w(ctx,number=None,page=0):
    if number!=None:
        text = f"https://www.wnacg.org/photos-slide-aid-{number}.html/"
        #爬蟲
        hentai = requests.get(text)
        data = bs4.BeautifulSoup(hentai.text, "lxml").select("#thumbnail-container img")
        urls = [i["src"] for i in data if not i["src"].startswith("data")]
        #輸出訊息
        embed=discord.Embed(color=0x009dff,title="Wnacg Viewer",url=urls[0])
        embed.set_footer(text=" By Young#0001")
        embed.set_image(url=urls[0])
        message=await ctx.send(embed=embed)
        for i in ["◀","▶"]:
            await message.add_reaction(i)
        #檢查表情符號(函式)
        def check(reaction, user):
            return user == ctx.author and reaction.message == message
        #檢查表情符號(迴圈)
        while 1 :
            if(page + 1 > len(urls) - 1): break
            reaction, user = await bot.wait_for("reaction_add",timeout=60.0,check=check)
            if str(reaction) ==  "▶":
                page+=1
            elif str(reaction) == "◀":
                page-=1
            await message.remove_reaction(reaction,user)

            embed=discord.Embed(color=0x009dff,title="Wnacg Viewer",url=f"{urls[page]}")
            embed.set_footer(text="By Young#0001")
            embed.set_image(url=f"{urls[page]}")
            print (f"{urls[page]}")
            await message.edit(embed=embed)
    else:
        await ctx.send(f"請輸入參數")
##################################################################################################
bot.run('Nzg2OTg2OTU0NDc4NTgzODU4.X9OYtw.9MJdNf_WwI5P67Vgc9meepVYQkg')